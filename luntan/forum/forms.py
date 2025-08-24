from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, Comment

class UserRegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True)
    student_id = forms.CharField(max_length=20, required=True)
    grade = forms.CharField(max_length=20, required=True)
    school = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'phone', 'student_id', 'grade', 'school', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']