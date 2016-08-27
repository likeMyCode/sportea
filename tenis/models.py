from django.db import models

from app.models import User

class Tournament (models.Model):
    name = models.CharField(max_length=30)
    organizer = models.ForeignKey(User, to_field='email')
    datetime = models.DateTimeField()
    deadline = models.DateTimeField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    participants_max = models.IntegerField()
    participants_registered = models.IntegerField()
    logo = models.ImageField(upload_to="tournament")
    def __str__ (self):
        return self.name


class Registration (models.Model):
    email = models.ForeignKey(User, to_field='email')
    tournament = models.ForeignKey(Tournament)
    license = models.CharField(max_length=50, unique=True)
    ranking = models.CharField(max_length=50, unique=True)

    def __str__ (self):
        return str(self.email) + ":" + str(self.tournament)


class Match (models.Model):
    tournament = models.ForeignKey(Tournament)
    stage = models.IntegerField()
    player1 = models.ForeignKey(User, to_field='email', related_name='player1')
    player2 = models.ForeignKey(User, to_field='email', related_name='player2')
    p1_vote = models.IntegerField()
    p2_vote = models.IntegerField()

    def __str__ (self):
        return str(self.tournament) + "_" + str(self.player1) + ":" + str(self.player2)