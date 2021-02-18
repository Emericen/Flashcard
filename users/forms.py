from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


AREA_CODE = (
    # ('', '请选择'),
    ('+86', '中国大陆(+86)'),
    ('+1', '美国(+1)'),
)







class UserRegisterForm(UserCreationForm):

	error_messages = {
        'password_mismatch': "请输入相同密码",
    }
	
	area_code = forms.ChoiceField(choices=AREA_CODE)

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



	class Meta:
		model = User
		fields = ['area_code','phone', 'password1']
		labels = {
			'phone': '手机号',
		}
		# help_texts = {
		# 	'phone':'别tm输空号！待会要验证！'
		# }
		# error_message = {
		# 	'username': {
		# 	'max_length': _("This writer's name is too long."),
		# 	},
		# }

		