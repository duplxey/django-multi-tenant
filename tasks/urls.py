from rest_framework.routers import DefaultRouter

from tasks.views import ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("tasks", TaskViewSet)

urlpatterns = router.urls
