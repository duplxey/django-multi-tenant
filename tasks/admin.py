from django.contrib import admin

from core.admin import TimeStampedModelAdmin
from tasks.models import Project, Task


class ProjectAdmin(TimeStampedModelAdmin):
    list_display = ["id", "key", "name", "created_at", "updated_at"]
    list_display_links = ["id", "key", "name"]


class TaskAdmin(TimeStampedModelAdmin):
    list_display = ["id", "name", "project", "is_done", "created_at", "updated_at"]
    list_display_links = ["id", "name"]
    list_filter = ["project", "is_done"]
    search_fields = ["name", "description"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
