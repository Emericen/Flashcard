from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Flashcard


@login_required
def home(request):
	return render(request, 'flashcards/home.html')


class FlashcardView(DetailView):
	model = Flashcard



