from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
class login_form(forms.Form):

    user_name=forms.CharField(max_length=10,label='User Name')
    password=forms.CharField(max_length=15,label='Password',widget=forms.PasswordInput)
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    def clean(self):
        user_name=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if user_name and password:
            user=authenticate(user_name=user_name,password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı Adı veya Şifresi Yanlış')
        return super(login_form,self).clean()

class register_form(forms.ModelForm):

    user_name=forms.CharField(max_length=10,label='User Name')
    password1=forms.CharField(max_length=15,label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(max_length=15,label='Password *',widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=[
        'user_name',
        'password1',
        'password2',
        ]
    def clean_passsword2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parolalar eşleşmiyor')
        return password2
