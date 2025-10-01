from django.contrib import admin
from django.urls import path
from .views import AiHomeView

urlpatterns = [
    path("", AiHomeView.as_view(), name="ai"),
]
