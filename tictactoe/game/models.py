from django.db import models


class Player(models.Model):
    email_address = models.EmailField('email address')
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    highest_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user_name


class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    size = models.IntegerField(default=3)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    result = models.BooleanField()

    def __str__(self):
        return str(self.pk)
