from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Flashcard, Collection


@login_required
def home(request):
	return render(request, 'flashcards/home.html', {'Collections':Collection.objects.all()})


@login_required
def flashcard(request):
	pass




# class FlashcardView(DetailView):
# 	model = Flashcard



