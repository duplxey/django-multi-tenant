from django.contrib import admin


class TimeStampedModelAdmin(admin.ModelAdmin):
    """
    Custom model admin class to handle the 'TimeStampedModel'.
    """

    readonly_fields = ["created_at", "updated_at"]
