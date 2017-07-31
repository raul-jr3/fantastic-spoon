from django.conf.urls import url 


from . import views

urlpatterns = [
				#home
				url(r'^home/$', views.home, name = 'home'),
				#adding new posts
				url(r'^post/$', views.post, name = 'post'),
				#edit 
				url(r'^edit-post/(?P<post_id>[0-9]+)/$', views.edit_post, name = 'edit'),
				#user detail
				url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name = 'user_detail'),
				]