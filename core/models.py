from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User)
    year = models.CharField(max_length=50, choices=(
    	('2015','2015'), ('2016','2016'), ('2017', '2017'),
    	('2018', '2018'), ('2019', '2019')))
    position = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)