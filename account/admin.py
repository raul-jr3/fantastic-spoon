from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'last_active']
	list_filter = ['user']

admin.site.register(Profile, ProfileAdmin)