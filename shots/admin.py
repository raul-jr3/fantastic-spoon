from django.contrib import admin

# Register your models here.
from .models import Image 

class ImageAdmin(admin.ModelAdmin):
	list_display = ['posted_by', 'created', 'updated']
	list_filter = ['posted_by', 'updated']

admin.site.register(Image, ImageAdmin)