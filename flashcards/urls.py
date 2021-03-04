from django.urls import path
from .views import HomeView, CollectionView
from django.contrib.auth.decorators import login_required
# from . import views

urlpatterns = [
	# path('flashcard/<int:pk>/front', views.flashcard, name='flashcard'),
	path('', login_required(HomeView.as_view()), name='home'),
    path('home/', login_required(HomeView.as_view()), name='home'),
	path('collection/<int:pk>/', CollectionView.as_view(), name='collection'),
]


