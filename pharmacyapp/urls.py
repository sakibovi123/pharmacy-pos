from django.urls import path
from .views import *
urlpatterns = [
    path("<int:shop_id>/", PharmaHome.as_view(), name="pharma-home"),
]
