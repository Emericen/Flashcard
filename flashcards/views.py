from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Flashcard, Collection
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView





class HomeView(ListView):
	model = Collection
	template_name = 'flashcards/home.html'
	context_object_name = 'collections'

	def get_queryset(self):
		return self.request.user.owned_collections.all()





class CollectionView(ListView):
	model = Flashcard
	template_name = 'flashcards/collection.html'
	context_object_name = 'flashcards'

	def get_queryset(self):
		current_collection = get_object_or_404(Collection, id=self.kwargs.get('pk'))
		return Flashcard.objects.filter(collection=current_collection)




