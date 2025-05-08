from rest_framework.routers import DefaultRouter

from blog.views import ArticleViewSet

router = DefaultRouter()
router.register("articles", ArticleViewSet)

urlpatterns = router.urls
