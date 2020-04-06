from django.db import models
from django.contrib.auth import get_user_model

class Score(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    score = models.IntegerField()
    game_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " " + str(self.game_datetime)