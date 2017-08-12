from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
# Create your models here.


class Image(models.Model):
	posted_by = models.ForeignKey(User, related_name = 'shots')
	photo = models.ImageField(upload_to = '%Y/%m/%d/photos/')
	body = models.TextField(blank = True, help_text = "description(it's optional)")
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'likes', blank = True)


	def __str__(self):
		return "{} posted a new photo".format(self.posted_by)

	class Meta:
		ordering = ['-updated']

class Comment(models.Model):
	post = models.ForeignKey(Image, related_name = 'comments')
	body = models.TextField(help_text = 'Your comment')
	commented_by = models.ForeignKey(User, related_name = 'commented_by')
	created = models.DateTimeField(auto_now_add = True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return "{} commented on {}".format(self.commented_by, self.post)

