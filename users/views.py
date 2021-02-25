from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .forms import UserCreationForm, UserLoginForm


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


def logout(request):
	django_logout(request)
	messages.info(request, f'您已退出登录 要想再用就他妈先登录')
	return redirect('login')


