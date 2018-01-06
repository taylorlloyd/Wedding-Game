import json
from django.http import JsonResponse
from wgserver.models import Player
from wgserver.rules import Rules
import random

SAME_TEAM = "You're on the same team!"
NO_MATCH = " doesn't match your rule"
CHANGED = "Converted "

def getToken(request, name="tag"):
    if request.GET:
        if name in request.GET:
            return request.GET[name]
    return None

def interact(request):
    # Extract all relevant player information
    token1 = getToken(request, "player1")
    token2 = getToken(request, "player2")
    if token1 is None or token2 is None:
        return errorResponse("player1 and player2 are required fields")
    try:
        player1 = Player.objects.get(rfid_token = token1)
        player2 = Player.objects.get(rfid_token = token2)
    except Player.DoesNotExist:
        return errorResponse("No player with that tag exists")

#TODO: Handle non-activated players
#TODO: Handle playing yourself

    # Resolve rules
    p1_fail_reason = player2.first_name + NO_MATCH
    p2_fail_reason = player1.first_name + NO_MATCH

    p1_team = player1.team
    p2_team = player2.team
    flip1 = player2.get_rule().matches(player2, player1)
    flip2 = player1.get_rule().matches(player1, player2)

    # Handle same-team interactions
    if p1_team == p2_team:
        flip1 = False
        flip2 = False
        p1_fail_reason = SAME_TEAM
        p2_fail_reason = SAME_TEAM

    # Update players
    if flip1:
        player1.team = p2_team
        player1.rule = random.randint(0,len(Rules)-1)
        player1.save()
        p2_fail_reason = CHANGED + player1.first_name
    if flip2:
        player2.team = p1_team
        player2.rule = random.randint(0,len(Rules)-1)
        player2.save()
        p1_fail_reason = CHANGED + player2.first_name

    # Send information
    return JsonResponse({
        'status': 'ok',
        'player1_changed': flip1,
        'player1_reason': p1_fail_reason,
        'player1': playerJson(player1),
        'player2_changed': flip2,
        'player2_reason': p2_fail_reason,
        'player2': playerJson(player2),
    })



def activate(request):
    token = getToken(request)
    if token is None:
        return errorResponse("No tag specified")
    try:
        player = Player.objects.get(rfid_token = token)
    except Player.DoesNotExist:
        return errorResponse("No player with that tag exists")

    if player.team == 'N':
        # We need to activate this player
        bride_side = Player.objects.filter(team='B').count()
        groom_side = Player.objects.filter(team='G').count()
        if bride_side < groom_side:
            player.team = 'B'
        else:
            player.team = 'G'
        player.rule = random.randint(0, len(Rules)-1)
        player.save()
    return JsonResponse({'status':'ok', 'player': playerJson(player)})

def status(request):
    token = getToken(request)
    if token is None:
        return errorResponse("No tag specified")
    try:
        player = Player.objects.get(rfid_token = token)
    except Player.DoesNotExist:
        return errorResponse("No player with that tag exists")
    return JsonResponse({'status':'ok', 'player': playerJson(player)})

def ratio(request):
    bride_side = Player.objects.filter(team='B').count()
    groom_side = Player.objects.filter(team='G').count()
    return JsonResponse({'status':'ok', 'bride_side':bride_side, 'groom_side':groom_side})


def errorResponse(errmsg):
    return JsonResponse({'status':'error', 'msg':errmsg})

def playerJson(player):
    if player.team != 'N':
        return {
        'first_name': player.first_name,
        'last_name': player.last_name,
        'tag': player.rfid_token,
        'team': player.get_team_display(),
        'rule_text': player.get_rule().rule_text(),
        }
    else:
        return {
        'first_name': player.first_name,
        'last_name': player.last_name,
        'tag': player.rfid_token,
        'team': player.get_team_display(),
        }
