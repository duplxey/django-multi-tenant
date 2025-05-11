"""
URLs for the 'public' schema.
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import ArticleViewSet
from core.views import index_view

router = DefaultRouter()
router.register("blog", ArticleViewSet)

urlpatterns = [
    path("", index_view, name="index"),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
