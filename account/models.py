from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'profile')
	profile_photo = models.ImageField(upload_to = '%Y/%m/%d/profile_photos', blank = True)
	bio = models.CharField(max_length = 500, blank = True)
	favourite_quote = models.CharField(max_length = 300, blank = True)
	last_active = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "{}".format(self.user)