from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User)
    year = models.CharField(max_length=50, choices=(
    	('2015','2015'), ('2016','2016'), ('2017', '2017'),
    	('2018', '2018'), ('2019', '2019')), blank=True)
    position = models.CharField(max_length=100, blank=True)
    duke_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    home_street = models.CharField(max_length=100, blank=True)
    home_town = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
    	return "%s %s's profile" %(self.user.first_name, self.user.last_name)

class Background(models.Model):
    img = models.ImageField()

    def __unicode__(self):
        return self.img.url.split('/')[-1]
