from django.shortcuts import render
from store.models import Product

def home(request):
    Products = Product.objects.all().filter(is_available=True)
 

    context = {
        'Products': Products,
      

    }
    return render(request, 'home.html', context)