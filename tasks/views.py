from rest_framework.viewsets import ModelViewSet

from tasks.models import Project, Task
from tasks.serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.select_related("project").all()
    serializer_class = TaskSerializer
