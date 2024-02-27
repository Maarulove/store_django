from django.urls import path
from . import views

urlpatterns = [
    path("client/", views.create_client, name="client"),
]


