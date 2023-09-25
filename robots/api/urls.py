from django.urls import path
from . import views

urlpatterns = [
    path('create-robot/', views.CreateRobotView.as_view(), name='download_report'),
]
