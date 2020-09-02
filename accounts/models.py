from django.db import models
from django.utils import timezone
from datetime import datetime,date
from django.contrib.auth.models import User

""" MÜŞTERİ MODELİ """
class Customer(models.Model):
	MAINTENANCE = (
		('Aktif','Aktif'),
		('Pasif','Pasif'),
		)
	STATUS = (
		('Gönderildi','Gönderildi'),
		('Gönderilmedi','Gönderilmedi'),
		)
	userName = models.OneToOneField(User, null=True,blank=True, on_delete= models.CASCADE)
	name = models.CharField(max_length=200, null=True, blank=True)
	person = models.CharField(max_length=200, null=True, blank=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	gsm = models.CharField(max_length=200, null=True, blank=True)
	fax = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	adress = models.CharField(max_length=1000, null=True, blank=True)
	city = models.CharField(max_length=200, null=True, blank=True)
	town = models.CharField(max_length=50, null=True, blank=True)
	productName = models.CharField(max_length=200, null=True, blank=True)
	productKey = models.CharField(max_length=200, null=True, blank=True)
	productClient = models.CharField(max_length=10, null=True, blank=True)
	taxNumber = models.CharField(max_length=200, null=True, blank=True)
	taxAdmin = models.CharField(max_length=200, null=True, blank=True)
	dateCreated = models.DateTimeField(auto_now_add=True, null=True)
	maintenance = models.CharField(max_length=200, null=True, blank=True, choices=MAINTENANCE)
	maintenanceStartDate = models.DateTimeField(null=True, blank=True)
	maintenanceEndDate = models.DateTimeField(null=True, blank=True)
	emailStatus = models.CharField(max_length=200, null=True, blank=True, choices=STATUS)
	
	def __str__(self):
		return self.name


SERVICE_1 = 'Servis 1'
SERVICE_2 = 'Servis 2'
S1_1 = 'Çözüm 1_1'
S1_2 = 'Çözüm 1_2'
S2_1 = 'Çözüm 2_1'
S2_2 = 'Çözüm 2_2'

SERVICE_CHOICES = [
	(SERVICE_1,SERVICE_1),
	(SERVICE_2,SERVICE_2),
]

SOLUTION_CHOICES = [
	(S1_1,S1_1),
	(S1_2,S1_2),
	(S2_1,S2_1),
	(S2_2,S2_2),
]

def get_s1_strings():
	s1_strings = [
		S1_1,
		S1_2
	]
	return s1_strings

def get_s2_strings():
	s2_strings = [
		S2_1,
		S2_2
	]
	return s2_strings

class Service(models.Model):
	ticketNumber = models.CharField(max_length=10, null=True, blank=True)
	serviceCustomer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	serviceName = models.CharField(max_length=1000, null=True, choices=SERVICE_CHOICES)
	solutionName = models.CharField(max_length=1000, null=True, choices=SOLUTION_CHOICES)
	note = models.CharField(max_length=1000, blank=True)
	serviceDate = models.DateTimeField(null=True)
	user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)

	class Meta:
		get_latest_by = 'id'
		ordering = ('serviceCustomer',)

	def __str__(self):
		return self.serviceName


class Todo(models.Model):
	item = models.CharField(max_length=1000,null=True)
	user = models.ForeignKey(User, null=True, on_delete= models.CASCADE)
	todoDate = models.DateTimeField(null=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.item+ ' | ' + str(self.user) + ' | ' + str(self.completed)

class Ticket(models.Model):
	STATUS = (
		('Yeni','Yeni'),
		('Kapalı','Kapalı'),
		)
	SUBJECTS =(
		('Teknik Destek Talebi','Teknik Destek Talebi'),
		('Lisans Talebi','Lisans Talebi'),
		('Ürün Güncelleştirme','Ürün Güncelleştirme'),
		('Yeni Satın Alım Talebi','Yeni Satın Alım Talebi'),
		('Memnuniyetsizlik','Memnuniyetsizlik'),
		('Tavsiye','Tavsiye'),
		('Diğer','Diğer'),
		)
	RATES =(
		('Çok Kötü','Çok Kötü'),
		('Kötü','Kötü'),
		('Orta','Orta'),
		('İyi','İyi'),
		('Çok İyi','Çok İyi'),
		('Mükemmel','Mükemmel'),
		)
	
	userName = models.ForeignKey(User, null=True, on_delete= models.CASCADE)
	customer = models.CharField(max_length=100, null=True)
	name = models.CharField(blank=True, max_length=50)
	email = models.CharField(blank=True, max_length=50)
	subject = models.CharField(max_length=50,choices=SUBJECTS)
	message = models.CharField(blank=True, max_length=255)
	status = models.CharField(max_length=10,choices=STATUS,default='Yeni')
	ip = models.CharField(blank=True, max_length=20)
	note = models.CharField(blank=True, max_length=100)
	createAt = models.DateTimeField(auto_now_add=True)
	updateAt = models.DateTimeField(auto_now=True)
	rate = models.CharField(blank=True,max_length=20,choices=RATES)

	class Meta:
		get_latest_by = 'id'

	def __str__(self):
		return self.name

class TicketComment(models.Model):
	user = models.ForeignKey(User, null=True, on_delete= models.CASCADE)
	ticket = models.ForeignKey(Ticket, null=True, on_delete= models.CASCADE)
	comment = models.TextField(max_length=255)
	createAt = models.DateTimeField(auto_now_add=True)
	updateAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.comment

class Company(models.Model):
	code = models.CharField(max_length=100, null=True, blank=True)
	title = models.CharField(max_length=100, null=True)
	explanation = models.CharField(max_length=100, null=True, blank=True)
	productKey = models.CharField(max_length=100, null=True, blank=True)
	returnNo = models.CharField(max_length=100, null=True, blank=True)
	control1 = models.CharField(max_length=100, null=True, blank=True)
	control2 = models.CharField(max_length=100, null=True, blank=True)
	control3 = models.CharField(max_length=100, null=True, blank=True)
	control4 = models.CharField(max_length=100, null=True, blank=True)
	control5 = models.CharField(max_length=100, null=True, blank=True)
	portNo = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return self.title
