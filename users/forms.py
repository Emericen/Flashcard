from django import forms
from django.core.exceptions import ValidationError
from .models import User, Invitation
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _
import sys

def validate_invitation_code(value):
	if not Invitation.objects.filter(invitation_code=value).first() == None:
		return value
	else:
		raise ValidationError("抱歉，您的邀请码无效")


class UserCreationForm(forms.ModelForm):
	invitation_code = forms.CharField(
		required=True,
		label='邀请码 (必填)',
		validators=[validate_invitation_code],
		error_messages={
			'required':'请填写来自管理员的邀请码',
			'unique':'该邀请码已被其他用户使用'
		}
	)

	password1 = forms.CharField(
		strip=False,
		widget=forms.PasswordInput,
		label='设置密码 (6-16个字符组成，区分大小写)',
		error_messages={
			'required':'密码不能为空'
		}
	)

	password2 = forms.CharField(
		strip=False,
		widget=forms.PasswordInput,
		label='请再次输入密码',
		error_messages={
			'required':'确认密码不能为空'
		}
	)


	def clean_password1(self):
		password1 = self.cleaned_data.get("password1")
		if len(password1) < 6:
			raise ValidationError("密码长度太短，请至少设置6位密码")
		return password1


	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise ValidationError("二次输入密码必须和原密码相同")
		return password2


	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		invitation = Invitation.objects.get(invitation_code=self.cleaned_data["invitation_code"])
		invitation.is_used = True
		user.first_name, user.last_name = invitation.first_name, invitation.last_name
		if commit:
			user.save()
		return user


	class Meta:
		model = User
		fields = ['invitation_code', 'password1', 'password2']





class UserLoginForm(AuthenticationForm):

	error_messages = {
		'invalid_login': "邀请码或密码错误",
	}

	username = UsernameField(
		widget=forms.TextInput(attrs={'autofocus': True}),
		label='邀请码',
		error_messages={
			'required':'请填写来自管理员的邀请码',
		}
	)

	password = forms.CharField(
		label='密码',
		strip=False,
		widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
		error_messages={
			'required':'密码不能为空',
		}
	)



class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ('invitation_code','password')

	def clean_password(self):
		return self.initial["password"]



class UserAdmin(BaseUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm
	list_display = ('invitation_code', 'first_name', 'last_name', 'is_admin')
	list_filter = ('is_admin',)
	fieldsets = (
		(None, {'fields': ('invitation_code', 'password')}),
		('Personal info', {'fields': ('first_name', 'last_name')}),
		('Permissions', {'fields': ('is_admin',)}),
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



