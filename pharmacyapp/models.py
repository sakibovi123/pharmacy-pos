from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.

class Shop(models.Model):
    created_at = models.DateField(default=date.today)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255, unique=True)
    shop_address1 = models.TextField(null=True, blank=True)
    shop_address2 = models.TextField(null=True, blank=True)
    shop_contact = models.CharField(max_length=255, null=True)
    shop_bin_no = models.CharField(max_length=255, null=True, blank=True)
    shop_vat = models.CharField(max_length=255, null=True, blank=True)
    mushak_no = models.CharField(max_length=255, null=True, blank=True)
    shop_logo = models.ImageField(upload_to="images/", null=True)
    is_active = models.BooleanField(default=False, null=True)
    vat_amount = models.FloatField(null=True, default=0)
    show_mushak = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.shop_name


class CountryModel(models.Model):
    country_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.country_name


class CityModel(models.Model):
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.city_name




class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255, unique=True)
    tax_id = models.IntegerField(null=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    address = models.TextField(null=True)
    country = models.ForeignKey(CountryModel, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(CityModel, on_delete=models.SET_NULL, null=True)
    zip_code = models.IntegerField(null=True)
    trade_license = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    contact_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)



class MedicineCategory(models.Model):
    med_cat_name = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=False)


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.med_cat_name


class MedicineBrand(models.Model):
    med_brand_name = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    med_brand_logo = models.ImageField(upload_to="images/")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.med_brand_name

    @property
    def imageURL(self):
        try:
            url = self.med_brand_logo.url
        except:
            url = ""
        return url


class MedicinePower(models.Model):
    power_amount = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.power_amount


class Medicine(models.Model):
    med_name = models.CharField(max_length=255)
    med_image = models.ImageField(upload_to="images/")
    med_category = models.ForeignKey(MedicineCategory, on_delete=models.SET_NULL, null=True)
    med_brand = models.ForeignKey(MedicineBrand, on_delete=models.SET_NULL, null=True)
    med_power = models.ForeignKey(MedicinePower, on_delete=models.SET_NULL, null=True)
    med_vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    buying_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    selling_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    is_out_of_stock = models.BooleanField(default=False)
    stock_amount = models.PositiveIntegerField()


    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.med_name
    
    def save(self, *args, **kwargs):
        super(Medicine, self).save(*args, **kwargs)
        if not self.med_image:
            return

    @property
    def get_medicine_by_category(self):
        return Medicine.objects.filter(
            medicinecategory__med_cat_name=self.med_name
        )
        
    @staticmethod
    def get_medicines(ids):
        return Medicine.objects.filter(
            id__in=ids
        )


class MedicineCartItems(models.Model):
    items = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    


class MedicineCheckout(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    medicine_items = models.ManyToManyField(MedicineCartItems)
    discount = models.FloatField(null=True)
    amount_received = models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00)
    change = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ["-id"]
    
    def __str__(self):
        return self.customer_phone