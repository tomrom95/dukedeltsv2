from django.db import models

class Story(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	image = models.ImageField()
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "stories"
