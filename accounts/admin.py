from django.contrib import admin

# Register your models here.

from .models import *

class ContactFormMessageAdmin(admin.ModelAdmin):
	list_display = ['id','userName','customer','name','email','subject','message','note','status']
	list_filter = ['status']

class CustomerAdmin(admin.ModelAdmin):
	list_display = ['id','name','person','email','productKey','maintenance']
	list_filter = ['maintenance']
	
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['id','serviceCustomer','serviceName','solutionName','note','user','serviceDate']
	list_filter = ['user']	

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['code','title','explanation','productKey','returnNo','portNo']

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Ticket,ContactFormMessageAdmin)
admin.site.register(TicketComment)
admin.site.register(Company,CompanyAdmin)