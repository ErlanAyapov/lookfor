from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("author", "first_name",)

admin.site.register(Article, ArticleAdmin)