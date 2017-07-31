from django.conf.urls import url 
from django.contrib.auth import views as auth_views

from . import views 

urlpatterns = [
				#login and logout views
				url(r'^login/$', auth_views.login, name = 'login'),
				url(r'^logout/$', auth_views.logout, name = 'logout'),
				#registration
				url(r'^register/$', views.register, name = 'register'),
				#profile and edit profile
				url(r'^profile/$', views.profile, name = 'profile'),
				url(r'^profile/edit/$', views.edit_profile, name = 'edit'),
				]