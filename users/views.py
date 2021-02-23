from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import UserCreationForm, UserLoginForm
import sys


def home(request):
	if not request.user.is_authenticated:
		return redirect('register')
	else:
		return render(request, 'users/home.html')



def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			invitation_code = form.cleaned_data.get('invitation_code')
			messages.success(request, f'您的账号已注册成功！您可以登陆了！')
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form':form})



class Login(LoginView):
	authentication_form = UserLoginForm




