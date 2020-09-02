import django_filters as filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import *


class CustomerFilter(filters.FilterSet):
	bakimBitis1 = DateFilter(label='Tarihinden Sonra',field_name="maintenanceEndDate", lookup_expr='gte')
	bakimBitis2 = DateFilter(label='Tarihinden Önce',field_name="maintenanceEndDate", lookup_expr='lte')
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['taxNumber','name','person', 'phone',
		'email','city','dateCreated','productKey'
		,'maintenanceEndDate','maintenanceStartDate']


class ServiceFilter(filters.FilterSet):
	servis1 = DateFilter(label='Tarihinden Sonra',field_name="serviceDate", lookup_expr='gte')
	servis2 = DateFilter(label='Tarihinden Önce',field_name="serviceDate", lookup_expr='lte')
	class Meta:
		model = Service
		fields = '__all__'
		exclude = ['user','serviceDate','serviceName','solutionName','note']
	def __init__(self, *args, **kwargs):
		super(ServiceFilter, self).__init__(*args, **kwargs)
		self.filters['serviceCustomer'].label = "Müşteri"

class CustomerServiceFilter(filters.FilterSet):
	servis1 = DateFilter(label='Tarihinden Sonra',field_name="serviceDate", lookup_expr='gte')
	servis2 = DateFilter(label='Tarihinden Önce',field_name="serviceDate", lookup_expr='lte')
	class Meta:
		model = Service
		fields = '__all__'
		exclude = ['serviceCustomer','user','serviceDate','serviceName','solutionName']