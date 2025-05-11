import json

from django.core.management import BaseCommand

from core import settings
from tenants.models import Tenant, Domain, User


class Command(BaseCommand):
    help = "Creates a public tenant and two demo tenants"
    tenants_data_file = "tenants/data/tenants.json"

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)

        # Load the tenant data from JSON
        self.tenants_data = []
        with open(self.tenants_data_file, "r") as file:
            self.tenants_data = json.load(file)

    def handle(self, *args, **kwargs):
        self.create_tenants()
        self.stdout.write(self.style.SUCCESS(f"Successfully created the tenants!"))

    def create_tenants(self):
        for tenant_data in self.tenants_data:
            # Create the tenant
            tenant = Tenant(
                id=tenant_data["id"],
                name=tenant_data["name"],
                schema_name=tenant_data["schema_name"],
            )
            tenant.save()

            # Build the full domain name
            domain_str = settings.BASE_DOMAIN
            if tenant_data["subdomain"]:
                domain_str = f"{tenant_data['subdomain']}.{settings.BASE_DOMAIN}"

            # Create the domain
            domain = Domain(
                domain=domain_str,
                is_primary=tenant_data["schema_name"] == settings.PUBLIC_SCHEMA_NAME,
                tenant=tenant,
            )
            domain.save()

            # Create the tenant owner
            user = User.objects.create_superuser(
                username=tenant_data["owner"]["username"],
                email=tenant_data["owner"]["email"],
                password=tenant_data["owner"]["password"],
            )

