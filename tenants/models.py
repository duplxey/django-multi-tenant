from django.db import models
from django_tenants.models import DomainMixin
from tenant_users.tenants.models import TenantBase, UserProfile

from core.models import TimeStampedModel


class User(UserProfile):
    pass


class Tenant(TenantBase, TimeStampedModel):
    name = models.CharField(max_length=100)


class Domain(DomainMixin, TimeStampedModel):
    pass
