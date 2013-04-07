from django.db import models


class Note(models.Model):
	title = models.CharField(max_length=140)
	content = models.TextField(max_length=5000)

	def __unicode__(self):
		return self.title