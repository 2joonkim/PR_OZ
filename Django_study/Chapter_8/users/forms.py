from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from django.core.exceptions import ValidationError

User = get_user_model()


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ('password1', 'password2')
        for field in class_update_fields:
            if field == 'password1':
                self.fields[field].label = '비밀번호'
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].widget.attrs['placeholder'] = '비밀번호를 입력해주세요.'
            if field == 'password2':
                self.fields[field].label = '비밀번호 확인'
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].widget.attrs['placeholder'] = '비밀번호를 다시 입력해주세요.'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'email', 'password1', 'password2')
        labels = {
            'name': '이름',
            'email': '이메일',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '이름을 입력해주세요.', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com.', 'class': 'form-control'}),
        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = '이메일'
        self.fields['password'].label = '비밀번호'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = '이메일을 입력해주세요.'
        self.fields['password'].widget.attrs['placeholder'] = '비밀번호를 입력해주세요.'
