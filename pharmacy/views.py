from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#this function includes models (product in this case)to be used by the view in terms of getting data and posting them
from .models import Product, Sale
#we are going to iclude our filters to be used by the view
from .filters import Product_filter
#includinng our models forms included in the models file
from .forms import Addform,Saleform

#handling redirection after the deletion
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
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
def issue_item(request, pk):
    issuedItem= Product.objects.get(id=pk)
    salesForm= Saleform(request.POST)

    if request.method == 'POST':
        if salesForm.is_valid():
            newSale = salesForm.save(commit=False)#commit false makes sure that you enter data once
            newSale.item= issuedItem
            newSale.unitPrice= issuedItem.unitPrice
            newSale.save()
            #to keep track of the stock remaining after sales
            issuedQuantity= int(request.POST['quantity'])
            issuedItem.totalQuantity-=issuedQuantity
            issuedItem.save()
            print(issuedItem.itemName)
            print(request.POST['quantity'])
            print(issuedItem.totalQuantity)

            return redirect('receipt')
    
    return render(request,'products/issue_item.html',{'salesForm':salesForm})

#tis handles the receipt
@login_required
def receipt(request):
    sales= Sale.objects.all().order_by('-id')
    return render (request, 'products/receipt.html',{'sales':sales})


@login_required
def add_to_stock(request, pk):
    issuedItem = Product.objects.get(id = pk)
    form = Addform(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['receivedQuantity'])
            issuedItem.totalQuantity += added_quantity
            issuedItem.save()

            #To add to the remaining stock quantity is reducing
            print(added_quantity)
            print (issuedItem.totalQuantity)
            return redirect('home')

    return render (request, 'products/add_to_stock.html', {'form': form})
    
    #this is going to display all the sales made
    
@login_required
def all_sales(request):
    sales = Sale.objects.all()
    total  = sum([items.ammountReceived for items in sales])
    change = sum([items.getChange() for items in sales])
    net = total - change
    return render(request, 'products/all_sales.html',
     {
     'sales': sales,
     'total': total,
     'change': change,
     'net': net,
      })

def al_sales(request):
    sales = Sale.objects.all()
    total  = sum([items.ammountReceived for items in sales])
    change = sum([items.getChange() for items in sales])
    net = total - change
    return render(request, 'products/all_sales.html',
     {
     'sales': sales,
     'total': total,
     'change': change,
     'net': net,
      })
@login_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request, 'products/receipt_detail.html', {'receipt': receipt})

#deleting
@login_required
def delete_item(request, product_id):
    delete = Product.objects.get(id = product_id)
    delete.delete()
    return HttpResponseRedirect(reverse('home'))


