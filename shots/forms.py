from django import forms

from .models import Image, Comment

class PostForm(forms.ModelForm):
	#specify the model and the fields to be used
	class Meta:
		model = Image
		fields = ['photo', 'body']

class CommentForm(forms.ModelForm):
	#specify the model to be used and the fields to be shown
	class Meta:
		model = Comment 
		fields = ['body']