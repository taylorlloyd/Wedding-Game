from django.db import models

class Player(models.Model):

    TEAMS = (
        ('N', 'Unassigned'),
        ('B', 'Bride'),
        ('G', 'Groom')
    )

    # The token identifying this player
    rfid_token = models.CharField(max_length=16)

    # Display details
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team = models.CharField(max_length=1, choices=TEAMS)

    # Rule details
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    rule = models.IntegerField(default=-1)
    gender = models.CharField(max_length=1, choices=GENDERS)
    adult = models.BooleanField(default=False)
    groom_relative = models.BooleanField(default=False)
    bride_relative = models.BooleanField(default=False)

    def get_rule(self):
        from wgserver.rules import Rules
        return Rules[self.rule]

    # Leaderboard tracking
    flipped = models.IntegerField(default=0)
    groom_conversions = models.IntegerField(default=0)
    bride_conversions = models.IntegerField(default=0)
    interactions = models.IntegerField(default=0)
