from django.urls import path

from .views import *

urlpatterns = [
    path('', VitexHomeView.as_view(), name="exchanges"),
    ]