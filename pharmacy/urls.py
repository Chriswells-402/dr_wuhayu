from django.urls import path
from pharmacy import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('', auth_views.LoginView.as_view(template_name = 'products/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name='logout'),
    #this lists products with buy item button
    path('home/<int:product_id>', views.product_detail, name='product_detail'),
    #this route is for buying a item with a buy item button
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),
    path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
    path('receipt/', views.receipt, name='receipt'),
]