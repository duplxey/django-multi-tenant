from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from tenants.models import Domain, Tenant, User


class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ["schema_name", "name", "created_at", "updated_at"]


class DomainAdmin(admin.ModelAdmin):
    list_display = ["domain", "tenant", "is_primary", "created_at", "updated_at"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "is_active"]
    list_display_links = ["id", "email"]
    search_fields = ["email"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "password",
                ],
            },
        ),
        (
            "Administrative",
            {
                "fields": [
                    "tenants",
                    "last_login",
                    "is_active",
                    "is_verified",
                ],
            },
        ),
    ]


admin.site.register(Tenant, TenantAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(User, UserAdmin)
