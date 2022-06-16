# Django
from django.urls import path

# Local
from .views import create_figurine

urlpatterns = [path("create_figurine", create_figurine)]
