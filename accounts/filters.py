import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_created']

class CustomerFilter(django_filters.FilterSet):
	serviceName = CharFilter(field_name='name', lookup_expr='icontains')
	productKey = CharFilter(field_name='product_key', lookup_expr='icontains')
	taxNumber = CharFilter(field_name='tax_number', lookup_expr='icontains')
	bakimBitis1 = DateFilter(field_name="bakim_bitis", lookup_expr='gte')
	bakimBitis2 = DateFilter(field_name="bakim_bitis", lookup_expr='lte')
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['tax_number','name','person', 'phone',
		'email','city','date_created','product_key'
		,'bakim_bitis','bakim_baslangic']