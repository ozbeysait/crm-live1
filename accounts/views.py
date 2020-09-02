from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import smtplib
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from .filters import CustomerFilter, ServiceFilter, CustomerServiceFilter
from .decorators import UnauthenticatedUser, AllowedUsers, AdminOnly
import json
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd

@UnauthenticatedUser
def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Kullanıcı Adı veya Şifre Hatalı!')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
@AdminOnly
def home(request):
    """
	users = []
	services_count = []
	for i in User.objects.filter(groups__name='personal'):
		users.append(i.get_short_name())
		services_count.append(i.service_set.all().count())

	customers = []
	customers_services = []
	
	service_customers = Service.objects.order_by().values_list('serviceCustomer').distinct()
	
	for i in service_customers:
		cust = Customer.objects.get(id = i[0])
		customers.append(cust.name)
		customers_services.append(cust.service_set.all().count())

	customers = customers[:5]
	customers_services = customers_services[:5]
	df1 = pd.DataFrame({"x":users,"y":services_count})
	new_index = (df1["y"].sort_values(ascending=False)).index.values
	sorted_data1 = df1.reindex(new_index)

	df2 = pd.DataFrame({"x":customers,"y":customers_services})
	new_index2 = (df2["y"].sort_values(ascending=False)).index.values
	sorted_data2 = df2.reindex(new_index2)
	def bar():
		x1 = sorted_data1.x
		y1 = sorted_data1.y

		trace = go.Bar(
			x=x1,
			y = y1,			
			name="2020",
			text="Servis Sayısı",
			marker = dict(color='rgba(52,58,64,0.5)',
				line=dict(color='rgb(0,0,0)',width=1.5))
		)
		layout = dict(
			title='Personel - Servis Grafiği',
			xaxis=dict(title="Personeller"),
			yaxis = dict(title="Servis Sayıları"),

		)

		fig = go.Figure(data=[trace], layout=layout)
		plot_div = plot(fig, output_type='div', include_plotlyjs=False)
		return plot_div

	def bar2():
		x1 = sorted_data2.x
		y1 = sorted_data2.y

		trace = go.Bar(
			x=x1,
			y = y1,			
			name="2020",
			text="Servis Sayısı",
			marker = dict(color='rgba(72,175,112,0.5)',
						line=dict(color='rgb(0,0,0)',width=1.5))
		)
		layout = dict(
			title='En Çok Servis Alan 5 Müşteri',
			xaxis=dict(title="Müşteriler"),
			yaxis = dict(title="Servis Sayıları")
		)

		fig = go.Figure(data=[trace], layout=layout)
		plot_div = plot(fig, output_type='div', include_plotlyjs=False)
		return plot_div
    """
	auth = request.user.groups.all()[0].name

	context = {'customers':customers,'auth':auth}

	return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['customer'])
def userPage(request):
	customer = Customer.objects.get(userName = request.user)
	services = customer.service_set.all()
	serviceCount = services.count()
	auth = request.user.groups.all()[0].name
	context={'customer':customer, 'services':services, 'serviceCount':serviceCount,'auth':auth}

	return render(request,'accounts/user.html',context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['customer'])
def userServices(request):
	customer = Customer.objects.get(userName = request.user)

	services = customer.service_set.all()
	serviceCount = services.count()

	context={'customer':customer, 'services':services, 'serviceCount':serviceCount}
	return render(request,'accounts/user_services.html',context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['customer'])
def tickets(request):
	allTickets = Ticket.objects.all()

	tickets = allTickets.filter(userName = request.user)
	ticketsCount = tickets.count()
	newTickets = tickets.filter(status='Yeni').count()
	closedTickets = tickets.filter(status='Kapalı').count()

	context={'tickets':tickets, 'ticketsCount':ticketsCount,'newTickets':newTickets,'closedTickets':closedTickets}


	return render(request,'accounts/tickets.html',context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['customer'])
def newTicket(request):
	if request.method == 'POST':

		form = ContactFormu(request.POST,initial={'email':'email'})
		if form.is_valid():
			data = Ticket()
			data.name = form.cleaned_data['name']
			data.email = form.cleaned_data['email']
			data.subject = form.cleaned_data['subject']
			data.message = form.cleaned_data['message']
			data.userName = request.user
			data.customer = Customer.objects.get(userName = request.user)
			data.ip = request.META.get('REMOTE_ADDR')
			
			data.save()
			customers = Customer.objects.all()
			customer = customers.filter(userName=request.user)
			customer = list(customer)
			customer=customer[0]

			ticket = Ticket.objects.latest()
			users = User.objects.all()
			mailList=[]
			for i in users:
				if i.is_staff:
					if ticket.subject=="Teknik Destek Talebi":
						if i.username=='nurettin' or i.username=='sait':
							mailList.append(i.email)
					if ticket.subject=="Lisans Talebi":
						if i.username=='nurettin':
							mailList.append(i.email)
					if ticket.subject=="Ürün Güncelleştirme":
						if i.username=='nurettin':
							mailList.append(i.email)
					if ticket.subject=="Yeni Satın Alım Talebi":
						if i.username=='sait':
							mailList.append(i.email)
					if ticket.subject=="Memnuniyetsizlik":
						if i.username=='sait':
							mailList.append(i.email)
					if ticket.subject=="Tavsiye":
						if i.username=='sait':
							mailList.append(i.email)
					if ticket.subject=="Diğer":
						if i.username=='sait':
							mailList.append(i.email)

			print(mailList)
			try:
				context = {'customer':customer,'ticket':ticket}
				template = render_to_string('accounts/email_ticket_template.html',context)
				
				subject, fromEmail, to = 'Pegasoft - Ticket!', settings.EMAIL_HOST_USER, mailList
				msg = EmailMultiAlternatives(subject, template, fromEmail, to)
				msg.content_subtype = "html"
				msg.send()

				messages.success(request,('Ticket başarıyla gönderildi.'))
			except:
				messages.warning(request,('Mail listenizi kontrol edin'))
			return redirect('/tickets')
	form = ContactFormu()
	context = {'form':form}
	return render(request,'accounts/new_ticket.html',context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def allTicket(request):
	tickets = Ticket.objects.all()
	ticketsCount = tickets.count()
	newTickets = tickets.filter(status='Yeni').count()
	closedTickets = tickets.filter(status='Kapalı').count()
	auth = request.user.groups.all()[0].name
	context = {'tickets':tickets,'ticketsCount':ticketsCount,'newTickets':newTickets,'closedTickets':closedTickets,'auth':auth}

	return render(request, 'accounts/tickets_list.html', context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def closeTicket(request,pk):
	ticket = Ticket.objects.get(id=pk)

	Ticket.objects.filter(id=ticket.id).update(status='Kapalı')

	return redirect('/all-ticket')

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal','customer'])
def ticket(request, pk):
	ticket = Ticket.objects.get(id=pk)
	customers = Customer.objects.all()
	customer = customers.filter(name=ticket.customer)
	allComments = TicketComment.objects.all()
	comments = allComments.filter(ticket=ticket)

	print(comments)
	form = TicketCommentForm()
	if request.method == 'POST':

		form = TicketCommentForm(request.POST)
		if form.is_valid():
			data = TicketComment()
			data.user = request.user
			data.ticket = ticket
			data.comment = form.cleaned_data['comment']
						
			data.save()

			auth = request.user.groups.all()[0].name
			if auth == "customer":
				return redirect('/tickets')
			else:
				return redirect('/all-ticket')

	customer = customer[0]
	auth = request.user.groups.all()[0].name
	
	context = {'ticket':ticket,'customer':customer,'auth':auth,'form':form,'comments':comments}
	return render(request, 'accounts/ticket.html',context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['customer'])
def rateTicket(request, pk):

	ticket = Ticket.objects.get(id=pk)
	form = RateForm(instance=ticket)

	if request.method == 'POST':
		form = RateForm(request.POST, instance=ticket)
		if form.is_valid():
			form.save()
			return redirect('/tickets')

	context = {'form':form,'ticket':ticket}
	return render(request, 'accounts/ticket_rate.html', context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def customers(request):
	customers = Customer.objects.all()

	totalCustomers = customers.count()
	active = customers.filter(maintenance='Aktif').count()
	passive = customers.filter(maintenance='Pasif').count()

	myFilter = CustomerFilter(request.GET, queryset=customers)
	customers = myFilter.qs 

	auth = request.user.groups.all()[0].name

	context = {'customers':customers,
	'totalCustomers':totalCustomers, 'myFilter':myFilter,
	'active':active, 'passive':passive,'auth':auth}

	return render(request, 'accounts/customer_list.html', context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def customer(request, pk):
	customer = Customer.objects.get(id=pk)

	services = customer.service_set.all()
	serviceCount = services.count()
	allTickets = Ticket.objects.all()
	tickets = allTickets.filter(customer = customer)
	ticketsCount = tickets.count()

	myFilter = CustomerServiceFilter(request.GET, queryset=services)
	services = myFilter.qs 

	auth = request.user.groups.all()[0].name

	context = {'ticketsCount':ticketsCount,'customer':customer, 'services':services, 'serviceCount':serviceCount,
	'myFilter':myFilter,'auth':auth}
	return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def customerSendMessage(request, pk):
	customer = Customer.objects.get(id=pk)
	template = render_to_string('accounts/email_template.html',{'customer':customer})
	send_mail(
	    'Pegasoft - Ürün Süreniz Dolmak Üzere!',
	    template,
	    settings.EMAIL_HOST_USER,
	    [customer.email],
    	fail_silently=False
	)
	messages.success(request,('Mesaj başarıyla gönderildi.'))

	auth = request.user.groups.all()[0].name
	context = {'customer':customer,'auth':auth}
	return redirect('/customers',context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def updateCustomer(request, pk):

	customer = Customer.objects.get(id=pk)
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect('/customers')

	auth = request.user.groups.all()[0].name
	context = {'form':form,'auth':auth}
	return render(request, 'accounts/customer_form.html', context)


@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def services(request):
	services = Service.objects.all()

	myFilter = ServiceFilter(request.GET, queryset=services)
	services = myFilter.qs
	auth = request.user.groups.all()[0].name
	context = {'services':services,'myFilter':myFilter,'auth':auth}

	return render(request, 'accounts/services.html', context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def searchService(request):
	
	return render(request, 'accounts/service_form0.html')

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def createService(request):
	
	query = request.GET.get('query')
	try:
		selectedCustomer = Customer.objects.get(taxNumber=query)

		if request.method == 'POST':
			form = ServiceForm(request.POST)
			if form.is_valid():
				data = Service()
				data.serviceCustomer = selectedCustomer
				data.serviceName = form.cleaned_data['serviceName']
				data.solutionName = form.cleaned_data['solutionName']
				data.note = form.cleaned_data['note']
				data.serviceDate = form.cleaned_data['serviceDate']
				data.user = request.user
				data.save()
				return redirect('/services')
	except:
		messages.warning(request,('Müşteri Bulunamadı.'))
		return redirect('/search_service')
	s1Strings = get_s1_strings()
	s2Strings = get_s2_strings()

	json_s1Strings = json.dumps(s1Strings)
	json_s2Strings = json.dumps(s2Strings)
	form = ServiceForm()
	auth = request.user.groups.all()[0].name
	context = {'auth':auth,'selectedCustomer':selectedCustomer,'form':form,'json_s1Strings':json_s1Strings,'json_s2Strings':json_s2Strings}
	return render(request, 'accounts/service_form.html', context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def ticketToService(request,pk):
	ticket = Ticket.objects.get(id=pk)
	selectedCustomer = Customer.objects.get(name=ticket.customer)
	selectedTicketNumber = ticket.id

	if request.method == 'POST':
		form = ServiceForm(request.POST)
		if form.is_valid():
			data = Service()
			data.serviceCustomer = selectedCustomer
			data.ticketNumber = selectedTicketNumber
			data.serviceName = form.cleaned_data['serviceName']
			data.solutionName = form.cleaned_data['solutionName']
			data.note = form.cleaned_data['note']
			data.serviceDate = form.cleaned_data['serviceDate']
			data.user = request.user
			data.save()	

			lastService = Service.objects.latest()
			#Ticket.objects.filter(id=ticket.id).update(status='Kapalı')
			Ticket.objects.filter(id=ticket.id).update(note=lastService.note)

			data2 = TicketComment()
			data2.user = request.user
			data2.ticket = ticket
			data2.comment = lastService.note
			data2.save()	
			
			return redirect('/services')


	s1Strings = get_s1_strings()
	s2Strings = get_s2_strings()

	json_s1Strings = json.dumps(s1Strings)
	json_s2Strings = json.dumps(s2Strings)
	form = ServiceForm()
	auth = request.user.groups.all()[0].name
	context = {'auth':auth,'selectedTicketNumber':selectedTicketNumber,'selectedCustomer':selectedCustomer,'form':form,'json_s1Strings':json_s1Strings,'json_s2Strings':json_s2Strings}
	return render(request, 'accounts/ticket_to_service.html', context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def updateService(request, pk):

	service = Service.objects.get(id=pk)
	form = ServiceForm(instance=service)

	if request.method == 'POST':
		form = ServiceForm(request.POST, instance=service)
		if form.is_valid():
			form.save()
			return redirect('/services')

	auth = request.user.groups.all()[0].name
	context = {'service':service,'form':form,'auth':auth}
	return render(request, 'accounts/service_update_form.html', context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def deleteService(request, pk):
	service = Service.objects.get(id=pk)
	if request.method == "POST":
		service.delete()
		return redirect('/services')

	auth = request.user.groups.all()[0].name
	context = {'item':service,'auth':auth}
	return render(request, 'accounts/delete_service.html', context)



@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def todo(request):
	allItems = Todo.objects.all
	form = TodoForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,('Görev başarıyla eklendi.'))
			return redirect('/todo')

	auth = request.user.groups.all()[0].name
	context = {'allItems':allItems,'form':form,'auth':auth}
	return render(request, 'accounts/todo.html',context)

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def delete(request, list_id):
	item = Todo.objects.get(pk=list_id)
	item.delete()
	messages.success(request,('Görev başarıyla silindi.'))
	return redirect('/todo')

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def crossOff(request, list_id):
	item = Todo.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('/todo')

@login_required(login_url='login')
@AllowedUsers(allowed_roles=['admin','personal'])
def uncross(request, list_id):
	item = Todo.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('/todo')