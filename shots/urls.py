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
				#like and dislike and list
				url(r'^like/(?P<post_id>[0-9]+)/$', views.add_like, name = 'like'),
				url(r'^dislike/(?P<post_id>[0-9]+)/$', views.remove_like, name = 'dislike'),
				url(r'^likers-list/(?P<post_id>[0-9]+)/$', views.likers_list, name = 'likers_list'),
				#delete posts
				url(r'^delete-warn/(?P<post_id>[0-9]+)/$', views.delete, name = 'delete-warn'),
				url(r'^delete/(?P<post_id>[0-9]+)/$', views.delete_post, name = 'delete'),
				#comments
				url(r'^comment/(?P<post_id>[0-9]+)/$', views.comment, name = 'comment'),
				#activity
				url(r'^action/$', views.action, name = 'action'),
				]