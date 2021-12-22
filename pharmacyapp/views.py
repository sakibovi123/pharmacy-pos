from django.shortcuts import get_object_or_404, render, redirect
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
            return render(self.request, "home/pharma-home.html", args)
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
            orders = MedicineCheckout.objects.filter(
                shop=shop_id
            )
            args = {
                "shop_id": shop_id,
            }
            return render(self.request, "", args)
        else:
            return redirect("warning")

    def post(self, request, shop_id, *args, **kwargs):
        pass



# Here order details view and reciept will be shown
# Print function included

class PharmaReceiptView(View):
    def get(self, request, id, shop_id, *args, **kwargs):
        pass

    def post(self, request, id, shop_id, *args, **kwargs):
        pass



## Admin panel classes
# Medicine/category/brand/vendor Adding
# editing
# deleting


class PharmaAdminView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass



# Medicine insert
# fetch
# put
# Delete
class MedicineOperation(View):
    def get(self, request, shop_id, *args, **kwargs):
        pass

    def post(self, request, shop_id, *args, **kwargs):
        pass

    def put(self, request, id, shop_id, *args, **kwargs):
        pass

    def delete(self, request, id, shop_id, *args, **kwargs):
        pass



# Medicine Category Get, Insert, put, Delete

class MedicineCategoryOperation(View):
    def get(self, request, shop_id, *args, **kwargs):
        pass
    def post(self, request, shop_id, *args, **kwargs):
        pass
    def put(self, request, shop_id, id, *args, **kwargs):
        pass
    def delete(self, request, shop_id, id, *args, **kwargs):
        pass

# Medicine Brand Get, Insert, put, Delete

class MedicineBrandOperation(View):
    def get_object(self, request, id, *args, **kwargs):
        queryset = MedicineBrand.objects.get(pk=id)
        return queryset

    def get(self, request, shop_id, *args, **kwargs):
        pass

    def post(self, request, shop_id, *args, **kwargs):
        pass

    def put(self, request, shop_id, id, *args, **kwargs):
        pass

    def delete(self, request, shop_id, id, *args, **kwargs):
        pass
