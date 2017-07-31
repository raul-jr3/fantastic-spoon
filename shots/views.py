from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 


from .models import Image 
from .forms import PostForm
# Create your views here.
def home(request):
	shots = Image.objects.all()
	return render(request, 'shots/home.html', {'shots':shots})

@login_required
def post(request):
	#check the method
	if request.method == 'POST':
		form = PostForm(data = request.POST, files = request.FILES)

		if form.is_valid():
			#create a new object
			new_post = form.save(commit = False)
			#assign it to the user
			new_post.posted_by = request.user
			#save the object
			new_post.save()
			#redirect the user to the home page
			return redirect('shots:home')
	else:
		#give out an empty form
		form = PostForm()
	return render(request, 'shots/post.html', {'form':form})

@login_required
def edit_post(request, post_id):
	#get the post based on it's id
	post = get_object_or_404(Image, id = post_id)
	#check the method
	if request.method == 'POST':
		#edit the form
		form = PostForm(instance = post, data = request.POST, files = request.FILES)
		#check if it is valid
		if form.is_valid():
			#save the form and redirect the person to the home
			form.save()
			return redirect('shots:home')

	else:
		#give out the form with the previous details
		form = PostForm(instance = post)
	return render(request, 'shots/post.html', {'form':form, 'post':post})

@login_required
def user_detail(request, username):
	#get the user from the User model
	user = get_object_or_404(User, username = username)
	#display it
	return render(request, 'shots/user_detail.html', {'user':user})