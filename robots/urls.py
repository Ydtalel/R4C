from django.urls import path

from .views import generate_report_view

urlpatterns = [
    path('download-report/', generate_report_view, name='download_report'),
]
