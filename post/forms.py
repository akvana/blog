from django import forms
from .models import Post,Comment
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class PostForm(forms.ModelForm):

    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model=Post
        fields=[
            'title',
            'content',
            'image',
]
class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())


    class Meta:
        model=Comment
        fields=[
            'name',
            'content',
]
