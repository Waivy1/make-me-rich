from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


class Amount(models.Model):
    amount = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



