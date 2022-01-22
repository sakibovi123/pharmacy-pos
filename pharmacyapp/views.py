from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import *
from django.views import View
from datetime import datetime, date, timedelta
from django.db.models import Sum, Avg
from django.db.models import Q

# Here we will get pharma homepage
# Cart functions
# Checkout Functions


class PharmaHome(View):
    template_name = "homeView/home.html"
    def get(self, request, shop_id, *args, **kwargs):
        shop_id = get_object_or_404(Shop, pk=shop_id)
        if shop_id.user == request.user:
            med_cart = request.session.get("med_cart")
            med_cats = MedicineCategory.objects.filter(
                shop=shop_id
            )
            meds = Medicine.objects.filter(
                shop=shop_id
            )

            if not med_cart:
                request.session.med_cart = {}
            
            med_cart_products = None

            if med_cart:
                ids = list(request.session.get("med_cart").keys())
                print(f"{ids=}")
                med_cart_products = Medicine.get_medicines(ids)

            args = {
                "med_cats": med_cats,
                "meds": meds,
                "med_cart_products": med_cart_products,
                "shop_id": shop_id,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("warning")

    def post(self, request, shop_id, *args, **kwargs):
        shop_id = get_object_or_404(Shop, pk=shop_id)
        if shop_id.is_active == True:
            med_cart = request.session.get("med_cart")
            remove = request.POST.get("remove")
            med_id = request.POST.get("med_id")

            if med_id is not None:
                if med_cart:
                    quantity = med_cart.get(med_id)
                    if quantity:
                        if remove:
                            med_cart[med_id] = quantity - 1
                        else:
                            med_cart[med_id] = quantity + 1
                    else:
                        med_cart[med_id] = 1
                    if med_cart[med_id] > 1:
                        med_cart.pop(med_id)

                else:
                    med_cart = {}
                    med_cart[med_id] = 1
                request.session["med_cart"] = med_cart
            
                return redirect(f"/")

# Here all will be shown
# Order will be shown by shop
# post method is none for now
# get method will fetch all order by shop owner


class PharmaCartView(View):
    template_name = ""
    def get(self, request, shop_id, *args, **kwargs):
        shop_id = get_object_or_404(Shop, pk=shop_id)
        if shop_id.user == request.user:
            med_cart = request.sessssion.get("med_cart", None)
            if not med_cart:
                request.session.med_cart = {}
            cart_products = None
            if med_cart:
                ids = list(request.session.get('med_cart').keys())
                cart_products = Medicine.get_medicines(ids)
            orders = MedicineCheckout.objects.filter(
                shop=shop_id
            )
            args = {
                "shop_id": shop_id,
                "cart_products": cart_products,
            }
            return render(self.request, self.template_name, args)
        else:
            # return redirect("warning")
            return HttpResponse("You are not the owner of this shop")

    def post(self, request, shop_id, *args, **kwargs):
        pass


def checkout(self, request, shop_id, *args, **kwargs):
    shopId = get_object_or_404(Shop, pk=shop_id)
    med_cart = request.session.get("med_cart", None)
    ids = list(request.session.get('med_cart').keys())
    medicine_items = Medicine.get_medicines(ids)

    if request.method == "POST":
        post_data = request.POST
        customer_name = post_data.get("customer_name")
        customer_phone = post_data.get("customer_phone")
        discount = post_data.get("discount")
        amount_received = post_data.get("amount_received")
        change = post_data.get("change")
        vat_amount = shopId.vat_amount

        med_checkout = MedicineCheckout(
            customer_name=customer_name,
            customer_phon=customer_phone,
            discount=discount,
            amount_received=amount_received,
            change=change,
            shop=shopId.id,
        )
        med_checkout.save()


        total = 0

        for item in medicine_items:
            quantity = med_cart.get(str(item.id))
            total += item.selling_price * quantity
            medicineCartItems = MedicineCartItems(
                items=item,
                quantity=quantity
            )
            # have to minus the amount of product after successfull checkout
            medicineCartItems.save()
            med_checkout.items.add(medicineCartItems)
            

        # if float(discount) > 0:
        #     grand_total = grand_total - (grand_total * Decimal(float(discount) / 100.0))

        med_checkout.total = total
        med_checkout.total = med_checkout.total + (vat_amount / 100)
        med_checkout.save()
        # trash_checkout.total = grand_total


# Here order details view and reciept will be shown
# Print function included
class PharmaReceiptView(View):
    template_name = ""
    def get(self, request, id, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        order_details = get_object_or_404(MedicineCheckout, pk=id)

        if shopId.user == request.user:

            args = {
                "order_details": order_details,
                "shopId": shopId
            }
            return render(request, self.template_name, args)
        else:
            # return redirect()
            return HttpResponse("You are not the owner of this shop")

    def post(self, request, id, shop_id, *args, **kwargs):
        pass

"""
Admin panel classes
Medicine/category/brand/vendor Adding
editing
deleting

"""

class PharmaAdminView(View):
    template_name = "Test/index.html"
    def get(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        shopTitle = shopId.shop_name
        if shopId.user == request.user:
            today_date = date.today()
            per_day__sale = MedicineCheckout.objects.filter(shop=shopId.id, created_at=today_date).aggregate(Sum("total"))
            per_day_sale = per_day__sale.pop("total__sum")
            orders = MedicineCheckout.objects.filter(
                shop=shopId.id
            )
            nots = NotificationModel.objects.filter(
                shop=shopId.id
            )
            ## Profit Per week

            print("date date " + str(today_date))

            # Filtering functionalities
            date_wise_orders = None
            if request.method == "POST":
                from_date = request.POST.get("from_date")
                to_date = request.POST.get("to_date")

                date_wise_orders = MedicineCheckout.objects.filter(
                    Q(created_at__exact=from_date)&Q(created_at__exact=to_date)
                )
            


            args = {
                "shopId": shopId,
                "today_date": today_date,
                "per_day_sale": per_day_sale,
                "shopTitle": shopTitle,
                "orders": orders,
                "nots": nots,
                "date_wise_orders": date_wise_orders,
            }
            # return render(request, "adminpanel/index.html", args)
            return render(request, self.template_name, args)
        else:
            return redirect("warning")

    def post(self, request, *args, **kwargs):
        pass



"""
Selling Session Action
1. Opening Time Action
2. Ending Time Action
"""

def open_selling(request, shop_id):
    shopId = get_object_or_404(Shop, pk=shop_id)
    if shopId.user == request.user:
        if request.method == "POST":
            pass
        args = {}
        return render(request, "", args)
    else:
        return redirect("")

# Medicine insert
# fetch
# put
# Delete
class MedicineOperation(View):
    template_name = "Test/Medicine/medicines.html"
    def get(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            medicines = Medicine.objects.filter(
                shop=shopId.id
            )
            args = {
                "medicines": medicines,
                "shopId": shopId,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("warning")

    def post(self, request, shop_id, med_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        medId = get_object_or_404(Medicine, pk=med_id)
        if shopId.user == request.user and request.method == "POST":
            medId.delete()
            return redirect("")


class MedicineCreateView(View):
    template_name = "Test/Medicine/create-medicine.html"
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {
                "shopId": shopId,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("")

    def post(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            if request.method == "POST":
                post_data = request.POST
                med_name = post_data.get("med_name")
                med_image = request.FILES.get("med_image")
                med_category = post_data.get("med_category")
                med_brand = post_data.get("med_brand")
                med_power = post_data.get("med_power")
                med_vendor = post_data.get("med_vendor")
                buying_price = post_data.get("buying_price")
                selling_price = post_data.get("selling_price")
                is_out_of_stock = post_data.get("is_out_of_stock")
                stock_amount = post_data.get("stock_amount")
                meds_val = Medicine(
                    med_name=med_name,
                    med_image=med_image,
                    med_category=MedicineCategory.objects.get(id=med_category),
                    med_brand=MedicineBrand.objects.get(id=med_brand),
                    med_power=MedicinePower.objects.get(id=med_power),
                    med_vendor=Vendor.objects.get(id=med_vendor),
                    buying_price=buying_price,
                    selling_price=selling_price,
                    is_out_of_stock=is_out_of_stock,
                    stock_amount=stock_amount,
                )
                if len(med_name) > 0 and len(buying_price) > 0 and len(selling_price) > 0:
                    meds_val.save()
                    return redirect("somewhere")

            return redirect("failed")


class MedicineUpdateView(View):
    template_name = "Test/Medicine/update-medicine.html"
    def get(self, request, shop_id, med_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        med_ids = get_object_or_404(Medicine, pk=med_id)

        if shopId.user == request.user and med_ids is not None:
            args = {
                "shopId": shopId,
                "med_ids": med_ids,
            }
            return render(request, self.template_name, args)
        else:
            return redirect()


    def post(self, request, id, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        med_ids = get_object_or_404(Medicine, pk=id)
        if shopId.user == request.user:
            if request.method == "POST":
                med_ids.med_name = request.POST.get("med_name")
                med_ids.med_image = request.FILES.get("med_image")
                med_ids.med_category = request.POST.get("med_category")
                med_ids.med_brand = request.POST.get("med_brand")
                med_ids.med_power = request.POST.get("med_power")
                med_ids.med_vendor = request.POST.get("med_vendor")
                med_ids.buying_price = request.POST.get("buying_price")
                med_ids.selling_price = request.POST.get("selling_price")
                med_ids.is_out_of_stock = request.POST.get("is_out_of_stock")
                med_ids.stock_amount = request.POST.get("stock_amount")

                med_ids.save()
                return redirect("somewhere")
            return redirect("")
        return redirect("")


# Medicine Category Get, Insert, put, Delete

class MedicineCategoryOperation(View):
    template_name = "Test/Category/category.html"
    def get(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            cats = MedicineCategory.objects.filter(
                shop=shopId.id
            )
            args = {
                "shopId": shopId,
                "cats": cats,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("")
    
    def post(self, request, shop_id, cat_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        catId = get_object_or_404(MedicineCategory, pk=cat_id)
        if shopId.user == request.user and request.method == "POST":
            catId.delete()
            return redirect(f"")



class MedicineCategoryCreateView(View):
    template_name = "Test/Category/create-category.html"
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            cats = MedicineCategory.objects.filter(
                shop=shopId.id
            )
            args = {
                "shopId": shopId,
                "cats": cats,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("")

    def post(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            if request.method == "POST":
                post = request.POST
                med_cat_name = post.get("med_cat_name")
                shop = shopId.id
                is_active = post.get("is_active")

                cat_val = MedicineCategory(
                    med_cat_name=med_cat_name,
                    shop=shop,
                    is_active=is_active
                )
                if med_cat_name and shop and is_active:
                    cat_val.save()
                    return redirect("")
            return redirect()
        else:
            return redirect()


class MedicineCategoryUpdateView(View):
    template_name = "Test/Category/update-category.html"
    def get(self, request, shop_id, cat_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        catId = get_object_or_404(MedicineCategory, pk=cat_id)
        if shopId.user == request.user:
            args = {
                "catId": catId,
            }
            return render(request, self.template_name, args)
        else:
            return redirect(f"")

    def post(self, request, shop_id, cat_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        med_obj = get_object_or_404(MedicineCategory, pk=cat_id)
        if shopId.user == request.user:
            if request.method == "POST":
                med_obj.med_cat_name = request.POST.get("med_cat_name")
                med_obj.shop = shopId.id
                med_obj.is_active = request.POST.get("is_active")
                med_obj.save()
            return redirect()
        else:
            return redirect()


"""
Medicine Brand Get, Insert, put, Delete
""" 
class MedicineBrandOperation(View):
    template_name = "Test/Brand/brands.html"
    def get(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            med_brands = MedicineBrand.objects.filter(
                shop=shopId.id
            )
            args = {
                "shopId": shopId,
                "med_brands": med_brands,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("warning")


    def post(self, request, shop_id, brand_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        brand_obj = get_object_or_404(MedicineBrand, pk=brand_id)
        if shopId.user == request.user:
            if request.method == "POST":
                brand_obj.delete()
                return redirect()
        return redirect()


class MedicineBrandCreateView(View):
    template_name = "Test/Brand/create-brand.html"
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {
                "shopId": shopId,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("warning")

    def post(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            if request.method == "POST":
                post = request.POST
                med_brand_name = post.get("med_brand_name")
                shop = shopId.id
                med_brand_logo = request.FILES.get("med_brand_logo")

                if med_brand_name and shop and med_brand_logo:
                    med_brand = MedicineBrand(med_brand_name=med_brand_name, shop=shop, med_brand_logo=med_brand_logo)
                    med_brand.save()
                    return redirect("")
            return redirect()
        else:
            return redirect("")


class MedicineBrandUpdateView(View):
    template_name = "Test/Brand/update-brand.html"
    def get(self, request, shop_id, brand_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        brandId = get_object_or_404(MedicineBrand, pk=brand_id)
        if shopId.user == request.user and brandId is not None:
            args = {
                "brandId": brandId,
                "shopId": shopId,
            }
            return render(request, self.template_name, args)
        else:
            return None

    def post(self, request, shop_id, brand_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        brand_obj = get_object_or_404(MedicineBrand, pk=id)
        if shopId.user == request.user:
            if request.method == "POST":
                brand_obj.med_brand_name = request.POST.get("med_brand_name")
                brand_obj.med_brand_logo = request.FILES.get("med_brand_logo")
                brand_obj.shop = shopId.id
                brand_obj.save()
                return redirect(f"")
            return redirect()
        else:
            return redirect()


#####
"""
medicine vendor operation
"""


class MedicineVendorView(View):
    tempalte_name = "Test/Vendor/vendors.html"
    def get(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            vendors = Vendor.objects.filter(
                shop=shopId.id
            )
            args = {
                "vendors": vendors,
                "shopId": shopId,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("")

    # Deleting vendor
    def post(self, request, shop_id, vendor_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        vendorId = get_object_or_404(Vendor, pk=vendor_id)
        msg = None
        if shopId.user == request.user and request.method == "POST":
            vendorId.delete()
            return redirect(f"")


class MedicineCreateView(View):
    template_name = "Test/Medicine/create-medicine.html"
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        msg = None
        if shopId.user == request.user:
            vendors = Vendor.objects.filter(
                shop=shopId.id
            )
            args = {
                "shopId": shopId,
                "vendors": vendors,
                "msg": msg,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("warning")


    def post(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if request.method == "POST":
                post = request.POST
                vendor_name = post.get("vendor_name")
                tax_id = post.get("tax_id")
                shop = shopId.id
                address = post.get("address")
                country = post.get("country")
                city = post.get("city")
                zip_code = post.get("zip_code")
                trade_license = post.get("trade_license")
                phone_number = post.get("phone_number")
                contact_name = post.get("contact_name")
                email = post.get("email")
                website = post.get("website")
                
                if zip_code == "" and email == "" and website == "":
                    vendor = Vendor(
                        vendor_name=vendor_name,
                        tax_id=tax_id,
                        shop=shop,
                        address=address,
                        country=CountryModel.objects.get(id=country),
                        city=CityModel.objects.get(id=city),
                        trade_license=trade_license,
                        phone_number=phone_number,
                        contact_name=contact_name
                    )

                    vendor.save()
                    return redirect(f"")

                else:
                    vendor = Vendor(
                        vendor_name=vendor_name,
                        tax_id=tax_id,
                        shop=shop,
                        address=address,
                        country=CountryModel.objects.get(id=country),
                        city=CityModel.objects.get(id=city),
                        trade_license=trade_license,
                        phone_number=phone_number,
                        contact_name=contact_name,
                        zip_code=zip_code,
                        email=email,
                        website=website
                    )

                    vendor.save()
                    return redirect(f"")


class MedicineVendorUpdateView(View):
    template_name = "Test/Vendor/update-vendor.html"
    def get(self, request, shop_id, vendor_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        vendorId = get_object_or_404(Vendor, pk=vendor_id)

        if shopId.user == request.user:
            args = {
                "vendorId": vendorId,
            }
            return render(request, self.template_name, args)
        else:
            return render("warning")
    

    def post(self, request, shop_id, vendor_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        vendorId = get_object_or_404(Vendor, pk=vendor_id)

        if request.method == "POST":
            vendorId.vendor_name = request.POST.get("vendor_name")
            vendorId.tax_id = request.POST.get("tax_id")
            vendorId.shop = shopId.id
            vendorId.address = request.POST.get("address")
            vendorId.country = CountryModel.objects.get(id=request.POST.get("country"))
            vendorId.city = CityModel.objects.get(request.POST.get("vendor_name"))
            vendorId.zip_code = request.POST.get("zip_code")
            vendorId.trade_license = request.POST.get("trade_license")
            vendorId.phone_number = request.POST.get("phone_number")
            vendorId.contact_name = request.POST.get("contact_name")
            vendorId.email = request.POST.get("email")
            vendorId.website = request.POST.get("website")

            vendorId.save()
            return redirect(f"")


class OrdersView(View):
    template_name = "Test/Order/orders.html"

    def get(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            orders = MedicineCheckout.objects.filter(shop=shopId.id)
            args = {
                "orders": orders,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("warning")


class OrderDetailsView(View):
    template_name = "Test/Order/order_details.html"

    def get(self, request, shop_id, order_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        orderId = None
        if shopId.user == request.user:
            orderId = get_object_or_404(MedicineCheckout, pk=order_id)
            args = {
                "shopId": shopId,
                "orderId": orderId,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("warning")


class RoleOperationView(View):
    template_name = ""

    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {
                "shopId": shopId,
            }
            return render(request, self.template_name, args)
        else:
            return redirect("login")
    
    # Deleting role
    def post(self, request, shop_id, role_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        roleId = get_object_or_404(Role, pk=role_id)
        if roleId is not None:
            roleId.delete()
            return redirect()
        else:
            return redirect()


"""
Exception Views
"""

class SuccessView(View):
    success_template = "exceptions/success.html"
    def get(self, request):
        return render(request, self.success_template)


class WarningView(View):
    warning_template = "exceptions/warning.html"
    def get(self, request):
        return render(request, self.warning_template)
