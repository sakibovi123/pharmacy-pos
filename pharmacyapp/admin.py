from django.contrib import admin
from .models import *


admin.site.register([
    Shop,
    CountryModel,
    CityModel,
    Vendor,
    MedicineCategory,
    MedicineBrand,
    Medicine,
    MedicinePower,
    MedicineCartItems,
    MedicineCheckout,
    NotificationModel,
    PurchaseModel,
])
