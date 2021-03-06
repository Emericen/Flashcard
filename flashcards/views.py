from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Knowledge, Flashcard, Collection
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView





class HomeView(ListView):
	model = Collection
	template_name = 'flashcards/home.html'
	context_object_name = 'collections'

	def get_queryset(self):
		return self.request.user.owned_collections.all()





class CollectionView(TemplateView):
	
	template_name = 'flashcards/collection.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_collection = get_object_or_404(Collection, id=self.kwargs.get('pk'))
		context['knowledges'] = Knowledge.objects.filter(collection=current_collection)
		context['flashcards'] = Flashcard.objects.filter(collection=current_collection)
		context['collection'] = current_collection
		return context




