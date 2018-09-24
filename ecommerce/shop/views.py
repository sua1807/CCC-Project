from django.shortcuts import render
from django.http import HttpResponse
from .models import Catalog
from django.template import loader


def index(request):

    all_catalog = Catalog.objects.all()
    template = loader.get_template(shop/index.html)
    # context={'all_catalog':all.Catalog}
#return render(request,'shop/index.html','all_catalog': all.Catalog)

   # return HttpResponse(template.render(context, request))



def detail(request,Catalog_id):
   return HttpResponse("<h2>Description of the product" + str(Catalog_id) + "</h2)
def add_to_cart(request, Catalog_id)
    cart= request.session.get('cart',{})
    product= Product.objects.get(id= Catalog_id)
    cart[Catalog_id]= product
    request.session['cart']= add_to_cart
    return HttpResponseRedirect(reverse("cart"))

def get_cart(request):
    cart= request.session.get('cart',{})
    return render(request, 'buylist/cart.html', cart)
