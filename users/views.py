from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm




def home(request):
	if not request.user.is_authenticated:
		return redirect('register')
	else:
		return render(request, 'users/home.html')



def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()		# create new entry in user table
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You can now log in!')
			return redirect('login')
	else:
		form = UserRegisterForm(initial={'area_code': '+86'})
	return render(request, 'users/register.html', {'form':form})



