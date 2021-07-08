from django import forms

from posts.models import Post


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)
