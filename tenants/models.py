from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

from core.models import TimeStampedModel


class Tenant(TenantMixin, TimeStampedModel):
    name = models.CharField(max_length=100)


class Domain(DomainMixin, TimeStampedModel):
    pass
