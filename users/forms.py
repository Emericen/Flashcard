from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


AREA_CODE = (
    # ('', '请选择'),
    ('+86', '中国大陆'),
    ('+1', '美国'),
    # ('+12','乌干达')
    )



class UserRegisterForm(UserCreationForm):

	error_messages = {
		'password_mismatch': "请输入相同密码",
	}
	
	area_code = forms.ChoiceField(
		choices=AREA_CODE, 
		label='区域'
	)

	phone = forms.CharField(
		required=True, 
		label='手机号', 
		error_messages={
		'required':'请填写常用手机号'
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

	class Meta:
		model = User
		fields = ['area_code','phone', 'password1']





# class UserLoginForm(AuthenticationForm):
# 	def __init__(self, *args, **kwargs):
# 		super(UserLoginForm, self).__init__(*args, **kwargs)

# 	area_code = forms.ChoiceField(
# 		choices=AREA_CODE, 
# 		label='区域'
# 	)

# 	phone = forms.CharField(
# 		required=True, 
# 		label='手机号', 
# 		error_messages={
# 			'required':'请填写常用手机号'
# 		}
# 	)





