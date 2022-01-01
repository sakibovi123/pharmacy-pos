from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import *
from django.views import View


# Here we will get pharma homepage
# Cart functions
# Checkout Functions


class PharmaHome(View):
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
            }
            return render(request, "homeView/pharma-home.html", args)
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


class PharmaOrderView(View):
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
            return render(self.request, "", args)
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
                change=change
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
                medicineCartItems.save()
                MedicineCheckout.items.add(medicineCartItems)

            # if float(discount) > 0:
            #     grand_total = grand_total - (grand_total * Decimal(float(discount) / 100.0))

            med_checkout.total = total
            med_checkout.total = med_checkout.total + (vat_amount / 100)
            med_checkout.save()
            # trash_checkout.total = grand_total


# Here order details view and reciept will be shown
# Print function included
class PharmaReceiptView(View):
    def get(self, request, id, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        order_details = get_object_or_404(MedicineCheckout, pk=id)

        if shopId.user == request.user:

            args = {
                "order_details": order_details,
                "shopId": shopId
            }
            return render()
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
    def get(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render()
        else:
            return redirect("warning")

    def post(self, request, *args, **kwargs):
        pass


# Medicine insert
# fetch
# put
# Delete
class MedicineOperation(View):
    def get(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            medicines = Medicine.objects.filter(
                shop=shopId.id
            )
            args = {
                "medicines": medicines
            }
            return render()
        else:
            return redirect("warning")

    def post(self, request, shop_id, med_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        medId = get_object_or_404(Medicine, pk=med_id)
        if request.method == "POST":
            medId.delete()
            return redirect("")


class MedicineCreateView(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render()
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
    def get(self, request, shop_id, med_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        med_ids = get_object_or_404(Medicine, pk=id)

        if shopId.user == request.user:
            args = {}
            return render()
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
            return render()
        else:
            return redirect("")
    
    def post(self, request, shop_id, cat_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        catId = get_object_or_404(MedicineCategory, pk=cat_id)
        if request.method == "POST":
            catId.delete()
            return redirect(f"")

class MedicineCategoryCreateView(View):
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
            return render()
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
    def get(self, request, shop_id, cat_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        catId = get_object_or_404(MedicineCategory, pk=cat_id)
        if shopId.user == request.user:
            args = {}
            return render()
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
            return render(request, "", args)
        else:
            return redirect("")


    def post(self, request, shop_id, brand_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        brand_obj = get_object_or_404(MedicineBrand, pk=brand_id)
        if shopId.user == request.user:
            if request.method == "POST":
                brand_obj.delete()
                return redirect()
        return redirect()


class MedicineBrandCreateView(View):
    def get(self, request, shop_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            args = {}
            return render()
        else:
            return None

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
    def get(self, request, shop_id, brand_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        brandId = get_object_or_404(MedicineBrand, pk=brand_id)
        if shopId.user == request.user:
            args = {}
            return render()
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
    def get(self, request, shop_id, *args, **kwargs):
        shopId = get_object_or_404(Shop, pk=shop_id)
        if shopId.user == request.user:
            vendors = Vendor.objects.filter(
                shop=shopId.id
            )
            args = {}
            return render(request, "", args)
        else:
            return redirect("")

    # Deleting vendor
    def post(self, request, shop_id, vendor_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        vendorId = get_object_or_404(Vendor, pk=vendor_id)
        if request.method == "POST":
            vendorId.delete()

            return redirect(f"")


class MedicineCreateView(View):
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
            }
            return render(request, "", args)
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
    def get(self, request, shop_id, vendor_id):
        shopId = get_object_or_404(Shop, pk=shop_id)
        vendorId = get_object_or_404(Vendor, pk=vendor_id)

        if shopId.user == request.user:
            args = {}
            return render()
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

