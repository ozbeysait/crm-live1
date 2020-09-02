from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['dateCreated','userName']
		widgets = {
            'maintenanceStartDate': DateInput(),
            'maintenanceEndDate': DateInput()
        }

class ServiceForm(ModelForm):
	class Meta:
		model = Service
		fields = ['serviceName','solutionName','note','serviceDate']
		widgets = {
            'serviceDate': DateInput(),
            'note' : Textarea(attrs={'class': 'input','rows':'5'}),
        }

class TodoForm(ModelForm):
	class Meta:
		model = Todo
		fields = '__all__'
		widgets = {
            'todoDate': DateInput()
        }

class ContactFormu(ModelForm):
	class Meta:
		model = Ticket
		fields = ['name', 'email', 'subject', 'message']
		widgets = {
			'name' : TextInput(attrs={'class': 'input','placeholder':'İsim & Soyisim'}),
			'email' : TextInput(attrs={'class': 'input','placeholder':'Email Adresi',}),
			'message' : Textarea(attrs={'class': 'input','placeholder':'Mesajınız','rows':'5'}),

		}

class TicketUpdateFormu(ModelForm):
	class Meta:
		model = Ticket
		fields = []

class TicketCommentForm(ModelForm):
	class Meta:
		model = TicketComment
		fields = ['comment']
		widgets = {
			'comment' : Textarea(attrs={'class': 'input','value':'qwe','placeholder':'Mesajınız','rows':'4'}),
		}
	def __init__(self, *args, **kwargs):
	    super(TicketCommentForm, self).__init__(*args, **kwargs)
	    self.fields['comment'].label = False


class RateForm(ModelForm):
	class Meta:
		model = Ticket
		fields = ['rate']