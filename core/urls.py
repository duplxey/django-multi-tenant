"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import ArticleViewSet
from tasks.views import ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register("blog", ArticleViewSet)
router.register("projects", ProjectViewSet)
router.register("tasks", TaskViewSet)


def index_view(request):
    return JsonResponse(
        {
            "name": "django-multi-tenant",
            "description": "A Django project with multi-tenancy support.",
            "version": "1.0.0",
        }
    )


urlpatterns = [
    path("", index_view, name="index"),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
