from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login

from .forms import UserRegistrationForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("User created !!!")
		else:
			return HttpResponse("User not created")
	else:
		form = UserRegistrationForm()
		return render(request, 'register.html', {"form": form})

def login(request):
	if request.method == 'POST':
		username =request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			form = auth_login(request, user)
			return render(request, 'index.html')
	form = AuthenticationForm()
	return render(request, 'login.html', {'form': form})