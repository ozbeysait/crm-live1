from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms



from .models import Order, Customer, Service


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class ServiceForm(ModelForm):
	class Meta:
		model = Service
		fields = '__all__'
