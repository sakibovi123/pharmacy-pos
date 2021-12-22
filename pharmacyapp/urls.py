from django.urls import path
from .views import *
urlpatterns = [
    path("/", PharmaHome.as_view(), name="pharma-home"),
]
