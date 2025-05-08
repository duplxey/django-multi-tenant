from rest_framework import serializers

from tasks.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "key",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]


class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        source="project", queryset=Project.objects.all(), write_only=True
    )

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "project",
            "project_id",
            "is_done",
            "created_at",
            "updated_at",
        ]
