from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import OrderForm, CustomerForm, ServiceForm
from .filters import OrderFilter

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Teslim Edildi').count()
	pending = orders.filter(status='Bekliyor').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
def customers(request):
	customers = Customer.objects.all()

	return render(request, 'accounts/customer_list.html', {'customers':customers})

@login_required(login_url='login')
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
def updateCustomer(request, pk):

	customer = Customer.objects.get(id=pk)
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect('/customers')

	context = {'form':form}
	return render(request, 'accounts/customer_form.html', context)

@login_required(login_url='login')
def createNewOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/create_new_order.html', context)

@login_required(login_url='login')
def createOrder(request, pk):
	customer = Customer.objects.get(id=pk)
	form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/create_order.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)



@login_required(login_url='login')
def services(request):
	services = Service.objects.all()

	return render(request, 'accounts/services.html', {'services':services})

@login_required(login_url='login')
def createService(request):
	form = ServiceForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ServiceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/services')

	context = {'form':form}
	return render(request, 'accounts/service_form.html', context)

@login_required(login_url='login')
def updateService(request, pk):

	service = Service.objects.get(id=pk)
	form = ServiceForm(instance=service)

	if request.method == 'POST':
		form = ServiceForm(request.POST, instance=service)
		if form.is_valid():
			form.save()
			return redirect('/services')

	context = {'form':form}
	return render(request, 'accounts/service_update_form.html', context)

@login_required(login_url='login')
def deleteService(request, pk):
	service = Service.objects.get(id=pk)
	if request.method == "POST":
		service.delete()
		return redirect('/services')

	context = {'item':service}
	return render(request, 'accounts/delete_service.html', context)