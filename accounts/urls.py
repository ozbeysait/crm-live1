from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),
    path('customer_send_message/<str:pk>/', views.customerSendMessage, name="customer_send_message"),

    path('services/', views.services, name='services'),
    path('create_service/', views.createService, name="create_service"),
    path('update_service/<str:pk>/', views.updateService, name="update_service"),
    path('delete_service/<str:pk>/', views.deleteService, name="delete_service"),

    path('create_new_order/', views.createNewOrder, name="create_new_order"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]