from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.utils import timezone
##auto fill , compay, user, timestamp
##so company actually has to fill name, price, stock
@login_required
def index(request):
    products = Product.objects.filter(company=request.user.company)
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        product = form.save(commit=False)
        product.company = request.user.company
        #product.created_by = request.user.name
        product.created_at = timezone.now()
        product.last_updated_at = timezone.now()
        product.save()
        return redirect('index')
    return render(request, 'index.html', {'products': products, 'form': form})
    #else:
    #    return redirect('admin')
    
    #return HttpResponse("Products index page. Add products here via form")