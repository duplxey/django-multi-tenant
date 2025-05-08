from django.contrib import admin

from blog.models import Article
from core.admin import TimeStampedModelAdmin


class ArticleAdmin(TimeStampedModelAdmin):
    list_display = ["id", "title", "created_at", "updated_at"]
    list_display_links = ["id", "title"]
    search_fields = ["title"]


admin.site.register(Article, ArticleAdmin)
