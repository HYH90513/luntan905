from django.contrib import admin
from .models import User, Post, Comment, Like

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'student_id', 'grade', 'school']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']