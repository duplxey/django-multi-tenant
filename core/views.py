from django.http import JsonResponse


def index_view(request):
    return JsonResponse(
        {
            "name": "django-multi-tenant",
            "description": "A Django project with multi-tenancy support.",
            "version": "1.0.0",
        }
    )
