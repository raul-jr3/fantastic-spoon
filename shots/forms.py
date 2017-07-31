from django import forms

from .models import Image

class PostForm(forms.ModelForm):
	#specify the model and the fields to be used
	class Meta:
		model = Image
		fields = ['photo', 'body']

	