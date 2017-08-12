from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Profile 
from shots.models import Image
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm


def profile(request):
	#retrieve all the posts for this particular user
	posts = Image.objects.filter(posted_by = request.user)
	return render(request, 'account/profile.html', {'posts':posts})

def register(request):
	#check the method
	if request.method == 'POST':
		#create a new instance
		form = UserRegisterForm(data = request.POST)
		#check if it is valid
		if form.is_valid():
			new_user = form.save(commit = False)
			#set the new user's password
			new_user.set_password(form.cleaned_data['password'])
			#save the new user
			new_user.save()
			#create a new profile for the registered user
			profile = Profile.objects.create(user = new_user)
			#render it
			return render(request, 'registration/register_done.html', {'new_user':new_user})

	else:
		#give out an empty form
		form = UserRegisterForm()
	return render(request, 'registration/register.html', {'form':form})

@login_required
def edit_profile(request):
	if request.method == 'POST':
		#populate the forms with the given data
		user_form = UserEditForm(data = request.POST, instance = request.user)
		profile_form = ProfileEditForm(data = request.POST, instance = request.user.profile, files = request.FILES)
		#if they are valid, save it
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('account:profile')

	else:
		#give out the data which is already present
		user_form = UserEditForm(instance = request.user)
		profile_form = ProfileEditForm(instance = request.user.profile)
	return render(request, 'account/edit_profile.html', {'user_form':user_form, 'profile_form':profile_form})