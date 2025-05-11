from django.contrib import admin
from django.core.exceptions import ValidationError
from django_tenants.admin import TenantAdminMixin

from tenants.forms import UserAdminForm
from tenants.models import Domain, Tenant, User


class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ["schema_name", "name", "created_at", "updated_at"]

    def delete_model(self, request, obj):
        # Force delete the tenant
        obj.delete(force_drop=True)


class DomainAdmin(admin.ModelAdmin):
    list_display = ["domain", "tenant", "is_primary", "created_at", "updated_at"]


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
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

    def delete_model(self, request, obj):
        # Cancel the delete if the user owns any tenant
        if obj.id in Tenant.objects.values_list("owner_id", flat=True):
            raise ValidationError("You cannot delete a user that is a tenant owner.")

        # Cancel the delete if the user still belongs to any tenant
        if obj.tenants.count() > 0:
            raise ValidationError("You cannot delete a user that still belongs to a tenant.")

        # Otherwise, delete the user
        obj.delete(force_drop=True)


admin.site.register(Tenant, TenantAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(User, UserAdmin)
