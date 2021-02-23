from django.contrib import admin
from .models import User, Invitation
from django.contrib.auth.models import Group
from.forms import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Invitation)
admin.site.unregister(Group)


