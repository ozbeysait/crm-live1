from django.http import HttpResponse
from django.shortcuts import redirect

def UnauthenticatedUser(view_func):
	def WrapperFunc(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request,*args,**kwargs)

	return WrapperFunc


def AllowedUsers(allowed_roles=[]):
	def Decorator(view_func):
		def WrapperFunc(request,*args,**kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request,*args,**kwargs)
			else:
				return HttpResponse('Bu sayfayı görüntülemeye yetkiniz bulunmamaktadır.')
		return WrapperFunc
	return Decorator

def AdminOnly(view_func):
	def WrapperFunction(request,*args,**kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('user-page')

		if group == 'admin' or group == 'personal':
			return view_func(request,*args,**kwargs)
		

	return WrapperFunction