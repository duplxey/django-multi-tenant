from django.contrib.auth.models import User
from django.core.management import BaseCommand

from tenants.models import Tenant, Domain


class Command(BaseCommand):
    help = "Creates a public tenant and two demo tenants"

    def handle(self, *args, **kwargs):
        public_tenant = Tenant.objects.create(
            schema_name="public",
            name="Public Tenant",
        )
        public_tenant_domain = Domain.objects.create(
            domain="localhost",
            tenant=public_tenant,
            is_primary=True,
        )
        public_tenant_superuser = User.objects.create_superuser(
            username="admin@localhost",
            email="admin@localhost",
            password="password",
        )

        demo1_tenant = Tenant.objects.create(
            schema_name="demo1",
            name="Demo Tenant 1",
        )
        demo1_tenant_domain = Domain.objects.create(
            domain="demo1.localhost",
            tenant=demo1_tenant,
            is_primary=False,
        )
        demo1_tenant_superuser = User.objects.create_superuser(
            username="admin@demo1.localhost",
            email="admin@demo1.localhost",
            password="password",
        )

        demo2_tenant = Tenant.objects.create(
            schema_name="demo2",
            name="Demo Tenant 2",
        )
        demo2_tenant_domain = Domain.objects.create(
            domain="demo2.localhost",
            tenant=demo2_tenant,
            is_primary=False,
        )
        demo2_tenant_superuser = User.objects.create_superuser(
            username="admin@demo2.localhost",
            email="admin@demo2.localhost",
            password="password",
        )

        self.stdout.write(self.style.SUCCESS(f"Successfully created tenan"))
