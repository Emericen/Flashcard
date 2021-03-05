from django.contrib import admin
from .models import Flashcard, Collection, Knowledge

# Register your models here.
admin.site.register(Flashcard)
admin.site.register(Collection)
admin.site.register(Knowledge)


