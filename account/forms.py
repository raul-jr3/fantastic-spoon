from django import forms 
from django.contrib.auth.models import User 


from .models import Profile

class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User 
		fields = ['username', 'first_name', 'last_name', 'email']

	def clean_password2(self):
		#get the cleaned form data
		cd = self.cleaned_data
		#check if both are equal or not
		if cd['password'] != cd['password2']:
			# if they aren't equal raise an exception else return the cleaned_password
			raise forms.ValidationError("passwords don't match")
		return cd['password']

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio', 'favourite_quote', 'profile_photo']

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User 
		fields = ['username', 'first_name', 'last_name', 'email']