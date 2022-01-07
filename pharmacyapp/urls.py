from django.urls import path
from .views import *
urlpatterns = [
    # path("<int:shop_id>/", PharmaHome.as_view(), name="pharma-home"),
    path("<int:shop_id>/", PharmaAdminView.as_view(), name="pharma-admin"),

    ## Cart View URLS
    path("pharma-cart/<int:shop_id>/", PharmaCartView.as_view(), name="cartView"),
    # checkout action url
    path("checkout/<int:shop_id>/", checkout, name="checkout"),

    ## Exception URLS
    path("success/", SuccessView.as_view, name="success"),
    path("warning/", WarningView.as_view(), name="warning"),
]
