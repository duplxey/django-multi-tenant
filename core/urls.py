"""
URLs for the tenant schemas.
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from blog.views import ArticleViewSet
from core.views import index_view
from tasks.views import ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register("blog", ArticleViewSet)
router.register("projects", ProjectViewSet)
router.register("tasks", TaskViewSet)

urlpatterns = [
    path("", index_view, name="index"),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
