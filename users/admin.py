from django.contrib import admin
from .models import User, Invitation, Ownership
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm
	list_display = ('invitation_code', 'first_name', 'last_name', 'is_admin')
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('invitation_code', 'password')}),
		('Personal info', {'fields': ('first_name', 'last_name')}),
		('Permissions', {'fields': ('is_admin','is_active', 'is_staff', 'is_superuser')}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('invitation_code', 'first_name', 'last_name', 'password1', 'password2'),
		}),
	)
	search_fields = ('invitation_code',)
	ordering = ('invitation_code',)
	filter_horizontal = ()



admin.site.register(User, UserAdmin)
admin.site.register(Invitation)
admin.site.register(Ownership)
admin.site.unregister(Group)


