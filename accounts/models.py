from django.db import models
from django.utils import timezone
from datetime import datetime,date

# Create your models here.

class Customer(models.Model):
	BAKIM = (
		('Aktif','Aktif'),
		('Pasif','Pasif'),
		)
	DURUM = (
		('Gönderildi','Gönderildi'),
		('Gönderilmedi','Gönderilmedi'),
		)
	name = models.CharField(max_length=200, null=True)
	person = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	product_key = models.CharField(max_length=200, null=True)
	tax_number = models.CharField(max_length=200, null=True)
	bakim_anlasmasi = models.CharField(max_length=200, null=True, choices=BAKIM)
	bakim_baslangic = models.DateTimeField(null=True)
	bakim_bitis = models.DateTimeField(null=True)
	email_durumu = models.CharField(max_length=200, null=True, choices=DURUM)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Ticari', 'Ticari'),
			('Otomasyon', 'Otomasyon'),
			('Muhasebe', 'Muhasebe'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Bekliyor', 'Bekliyor'),
			('Teslim Edildi', 'Teslim Edildi'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name

class User(models.Model):
	name = models.CharField(max_length=200, null=True)
	soyad = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Service(models.Model):
	service_name = models.CharField(max_length=1000, null=True)
	solution_name = models.CharField(max_length=1000, null=True)
	#date_created = models.DateTimeField(auto_now_add=True, null=True)
	service_date = models.DateTimeField(null=True)
	user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)

	def __str__(self):
		return self.service_name