"""
URL configuration for the project.

Includes a simple home page and a health-check endpoint so you can verify
the deployment before adding your own apps.
"""

from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import path


def home(request):
    return HttpResponse(
        "<h1>Django on AWS Elastic Beanstalk</h1>"
        "<p>Deployed via GitHub, CodeConnections and CodePipeline.</p>"
    )


def health(request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("", home, name="home"),
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
    # path("", include("your_app.urls")),
]