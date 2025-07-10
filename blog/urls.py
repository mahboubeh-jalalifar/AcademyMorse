from django.urls import path
from .views import Iran_time
urlpatterns=[
    path("time/", Iran_time)
]