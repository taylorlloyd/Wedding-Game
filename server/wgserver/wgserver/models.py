from django.db import models

class Player(models.Model):

    TEAMS = (
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
    gender = models.CharField(max_length=1, choices=GENDERS)
    adult = models.BooleanField(default=False)
    groom_relative = models.BooleanField(default=False)
    bride_relative = models.BooleanField(default=False)
