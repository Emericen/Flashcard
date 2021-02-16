from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm




def home(request):
	if request.user.is_authenticated():
		pass
	else:
		return redirect('login')



def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()		# create new entry in user table
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You can now log in!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})


