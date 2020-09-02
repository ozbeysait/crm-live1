from django.urls import path
from . import views
from accounts.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/',views.userPage,name="user-page"),
    path('user-services/',views.userServices,name="user-services"),
    path('tickets/',views.tickets,name="tickets"),
    path('new-ticket/',views.newTicket,name="new-ticket"),
    path('rate_ticket/<str:pk>/', views.rateTicket, name="rate_ticket"),

    path('customers/', views.customers, name='customers'),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),
    path('customer_send_message/<str:pk>/', views.customerSendMessage, name="customer_send_message"),

    path('todo/', views.todo, name='todo'),
    path('delete/<list_id>/', views.delete, name="delete"),
    path('cross_off/<list_id>/', views.crossOff, name="cross_off"),
    path('uncross/<list_id>/', views.uncross, name="uncross"),

    path('ticket-to-service/<str:pk>/', views.ticketToService, name="ticket-to-service"),
    path('ticket/<str:pk>/', views.ticket, name="ticket"),
    path('all-ticket/', views.allTicket, name='all-ticket'),
    path('ticket-close/<str:pk>/', views.closeTicket, name='ticket-close'),

    path('services/', views.services, name='services'),
    path('search_service/', views.searchService, name="search_service"),
    path('create_service/', views.createService, name="create_service"),
    path('update_service/<str:pk>/', views.updateService, name="update_service"),
    path('delete_service/<str:pk>/', views.deleteService, name="delete_service"),


]