from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django_tenants.utils import schema_context
from tenant_users.permissions.models import UserTenantPermissions

from tenants.models import User


def verify_import():
    pass


@receiver(m2m_changed, sender=User.tenants.through)
def on_tenant_user_tenants_changed(sender, instance, action, reverse, model, pk_set, **kwargs):
    # Automatically create 'UserTenantPermissions' when user is added to a tenant
    if action == "post_add":
        for tenant_id in pk_set:
            tenant = model.objects.get(pk=tenant_id)
            with schema_context(tenant.schema_name):
                UserTenantPermissions.objects.get_or_create(profile=instance)

    # Automatically delete 'UserTenantPermissions' when user is removed from a tenant
    if action == "post_remove":
        for tenant_id in pk_set:
            tenant = model.objects.get(pk=tenant_id)
            with schema_context(tenant.schema_name):
                UserTenantPermissions.objects.filter(profile=instance).delete()
