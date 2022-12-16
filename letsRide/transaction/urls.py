from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('requester', views.requesterr),
    path('rider', views.riderr),
    path('profile', views.profile),
]
