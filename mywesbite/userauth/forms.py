from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length=10)
	first_name = forms.CharField(max_length=255)
	last_name = forms.CharField(max_length=255)

	class Meta:
		model = User
		fields = ['username', 'email','phone_no', 'password1', 'password2']