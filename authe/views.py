
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from authe.forms import SignUpForm,UserForm, ChangeForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
 
from django.http import HttpResponse
# for email auth
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
#from ity.tokens import account_activation_token

# decorator
from ity.decorators import unathenticated_user


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User



# Create your views here.



@unathenticated_user

def register(request):
	
	"""if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.refresh_from_db()
			user.customer.first_name =form.cleaned_data.get('first_name')
			user.customer.last_name =form.cleaned_data.get('last_name')
			user.customer.email =form.cleaned_data.get('email')

			user.save()
			print(form.email)
			return redirect('authe:login_page')
			

	

"""	
	
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		last_name = request.POST.get('lasname')
		first_name = request.POST.get('fistname')

		print(username)

		if User.objects.filter(username=username).exists():
			#return render(request, 'register.html', {'error_message': 'Username already exists'})
			return HttpResponse('yoto view this page')
		
		# Create a new user
		user = User.objects.create_user(username=username, password=password1, email=email)
		user.first_name = first_name
		user.last_name = last_name
		user.save()

		# Refresh user data from the database
		user.refresh_from_db()

		# Update additional fields
		user.customer.first_name = user.first_name
		user.customer.last_name = user.last_name
		user.customer.email = user.email
		user.customer.save()

		# Redirect to the login page or any other desired page
		return redirect('authe:login_page')  # Replace 'login' with the actual URL name

	# If it's not a POST request, render the sign-up form
	return render(request, 'register.html')






def logout_page(request):
	logout(request)
	return redirect('authe:login_page')


@unathenticated_user

def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('ity:home')
		else:
			messages.info(request, 'username or password is incorrect')
			
	context = {}
	return render(request, 'login.html', context)


# Create your views here.


class ChangePassword2(LoginRequiredMixin, TemplateView):
	def get(self, request, *args, **kwaegs):
		form = ChangeForm(self.request.user)
		context={'form':form}
		return render(request, 'pass.html', context)

	def post(self, request, *args, **kwaegs):
		form =  ChangeForm(request.user, request.POST)
		if form. is_valid():
			user=form.save()
			update_session_auth_hash(request, user)
			return redirect('authe:login_page')
			context={'form':form, 'password_change': True}
			return render(request,'pass.html', context)

		else:
			return render(request, 'pass.html',{'form':form, 'password_change': False})
		