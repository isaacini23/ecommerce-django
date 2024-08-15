from django.http import HttpResponse
from django.shortcuts import redirect


def unathenticated_user(view_func):
	def wrapper_func(request, *args, **kwarg):
		if request.user.is_authenticated:
			return redirect('ity:home')
		else:
			return view_func(request, *args, **kwarg)

	return wrapper_func
	

def allowed_user(allowed_roles=["admin"]):
	def decorator(view_func):
		def wrapper_func(request,*args,**kwarg):
			print(1)# for test
			print(allowed_roles)
			group = None

			if request.user.groups.exists():
				group= request.user.groups.all()[0].name
				print(2) # this for test
				print(group)

			if group in allowed_roles:
				return view_func(request,*args,**kwarg)
			else:
				return HttpResponse('you are not authorized to view this page')
		
		return wrapper_func
	return decorator	
	