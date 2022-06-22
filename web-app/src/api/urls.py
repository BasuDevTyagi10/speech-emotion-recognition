from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path('upload', views.upload_file),
]
