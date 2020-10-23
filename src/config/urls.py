from django.contrib import admin
from django.urls import include, path

from .views import DashboardView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
]
