from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User



class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
	# favoritecolor = forms.CharField(max_length=254, required=True, help_text='100 characters max.', label='Favorite color')
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')