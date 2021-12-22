from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # path for pharmacy pos
    path("pharmacy-pos/", include('pharmacyapp.urls')),
]


# path("itna-pharma/", include("pharmacy.urls")),