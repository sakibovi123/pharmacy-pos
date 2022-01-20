from django.urls import path
from .views import *
urlpatterns = [
    # path("<int:shop_id>/", PharmaHome.as_view(), name="pharma-home"),
    path("<int:shop_id>/", PharmaAdminView.as_view(), name="pharma-admin"),
    # Medicine URLS
    path("medicines/<int:shop_id>/", MedicineOperation.as_view(), name="MedicineView"),
    path("create-medicine/<int:shop_id>/", MedicineCreateView.as_view(), name="CreateMedicineView"),
    path("update-medicine/<int:shop_id>/<int:med_id>/", MedicineUpdateView.as_view(), name="MedicineUpdateView"),
    # Medicine Category URLS
    path("category/<int:shop_id>/", MedicineCategoryOperation.as_view(), name="MedicineCategory"),
    path("create-category/<int:shop_id>/", MedicineCategoryCreateView.as_view(), name="CreateCategory"),
    path("update-category/<int:shop_id>/<int:cat_id>/", MedicineCategoryUpdateView.as_view(), name="UpdateCategory"),
    # Medicine brand URLS
    path("brands/<int:shop_id>/", MedicineBrandOperation.as_view(), name="MedicineBrandView"),
    path("create-brand/<int:shop_id>/", MedicineBrandCreateView.as_view(), name="CreateBrandVie"),
    path("update-brand/<int:shop_id>/<int:brand_id>/", MedicineBrandUpdateView.as_view(), name="UpdateBrandView"),
    # Medicine Orders
    path("all-orders/<int:shop_id>/", OrdersView.as_view(), name="OrderView"),
    # Medicine Order Details
    path("order-details/<int:shop_id>/<order_id>/", OrderDetailsView.as_view(), name="OrderDetailsView"),
    ## Cart View URLS
    path("pharma-cart/<int:shop_id>/", PharmaCartView.as_view(), name="cartView"),
    # checkout action url
    path("checkout/<int:shop_id>/", checkout, name="checkout"),

    # Admin panel views
    path("brands/<int:shop_id>", MedicineBrandOperation.as_view(), name="BrandView"),

    ## Exception URLS
    path("success/", SuccessView.as_view, name="success"),
    path("warning/", WarningView.as_view(), name="warning"),
]
