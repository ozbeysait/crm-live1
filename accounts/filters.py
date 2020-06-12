import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter

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
	serviceName = CharFilter(label='Şirket Adı',field_name='name', lookup_expr='icontains')
	productKey = CharFilter(label='Ürün Anahtarı',field_name='product_key', lookup_expr='icontains')
	taxNumber = CharFilter(label='Vergi Numarası',field_name='tax_number', lookup_expr='icontains')
	bakimBitis1 = DateFilter(label='Tarihinden Sonra',field_name="bakim_bitis", lookup_expr='gte')
	bakimBitis2 = DateFilter(label='Tarihinden Önce',field_name="bakim_bitis", lookup_expr='lte')
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['tax_number','name','person', 'phone',
		'email','city','date_created','product_key'
		,'bakim_bitis','bakim_baslangic']


class ServiceFilter(django_filters.FilterSet):
	serviceName = CharFilter(label='Servis Adı',field_name='service_name', lookup_expr='icontains')
	solutionName = CharFilter(label='Çözüm Açıklaması',field_name='solution_name', lookup_expr='icontains')
	servis1 = DateFilter(label='Tarihinden Sonra',field_name="service_date", lookup_expr='gte')
	servis2 = DateFilter(label='Tarihinden Önce',field_name="service_date", lookup_expr='lte')
	class Meta:
		model = Service
		fields = '__all__'
		exclude = ['service_name','solution_name','service_date']