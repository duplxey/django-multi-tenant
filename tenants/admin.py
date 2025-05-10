from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_tenants.admin import TenantAdminMixin

from tenants.models import Tenant, Domain, User


class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ["schema_name", "name", "created_at", "updated_at"]


class DomainAdmin(admin.ModelAdmin):
    list_display = ["domain", "tenant", "is_primary", "created_at", "updated_at"]


admin.site.register(Tenant, TenantAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(User, UserAdmin)
