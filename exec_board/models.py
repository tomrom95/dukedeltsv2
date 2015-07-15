from django.db import models

class BoardMember(models.Model):
	position = models.CharField(max_length=50)
	name = models.CharField(max_length=50)	
	year = models.CharField(max_length=50, choices=(
    	('2015','2015'), ('2016','2016'), ('2017', '2017'),
    	('2018', '2018'), ('2019', '2019')))
	email = models.EmailField()
	pic = models.ImageField()

	def __unicode__(self):
		return "%s: %s" %(self.position, self.name)
