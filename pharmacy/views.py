from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#this function includes models (product in this case)to be used by the view in terms of getting data and posting them
from .models import Product
#we are going to iclude our filters to be used by the view
from .filters import Product_filter

# Create your views here.
@login_required
def index(request):
    products= Product.objects.all().order_by('-id')
    product_filters = Product_filter(request.GET,queryset=products)
    products= product_filters.qs
    return render(request, 'products/index.html',{'products':products,'product_filters':product_filters})
#this home loadss the index page
@login_required
def home(request):
    products= Product.objects.all().order_by('-id')
    product_filters = Product_filter(request.GET,queryset=products)
    products= product_filters.qs
    return render(request, 'products/home.html',{'products':products,'product_filters':product_filters})
    
    #create a view for product_details
@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'products/product_detail.html', {'product': product})

#create view for issue item

@login_required
def issue_item(request):
    pass

@login_required
def add_to_stock(request):
    pass
