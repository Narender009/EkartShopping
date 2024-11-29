from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import category
from carts.models import CartItem



from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def store(request, category_slug=None):
    categories = None
    Products = None

    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        Products = Product.objects.filter(category=categories, is_available=True)
        paginator =Paginator(Products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        Product_count = Products.count()
    else:
        Products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator =Paginator(Products, 2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        Product_count = Products.count()



    context = {
      'products' :paged_products,
       'Product_count' : Product_count,
    }
   
    return render(request, 'store/store.html',context)


def Products_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

        
    except Exception as e:
        raise e


    context = {
        'single_product' : single_product,
        'in_cart': in_cart
    }         

    return render(request, 'store/Products_detail.html', context)