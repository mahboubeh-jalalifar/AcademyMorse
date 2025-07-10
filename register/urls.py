from django.urls import path
from .views import show_name
urlpatterns=[
    path("name/", show_name),
]