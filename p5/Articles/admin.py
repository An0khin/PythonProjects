from django.contrib import admin
from .models import *

class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)