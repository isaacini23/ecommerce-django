from django.shortcuts import render
from ity.forms import *
from ity.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.contrib import messages
from django.core.mail import send_mail
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
# decorator
from ity.decorators import allowed_user


from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart, cartData, guestOrder


#pagination stuff
from django.core.paginator import Paginator

from django.contrib.auth.models import Group, User

# Create your views here.
 # Create your views here.


def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

@login_required(login_url='authe:login_page')
@allowed_user(allowed_roles=' admin ' )
def upload(request):
	
	if request.method == "POST":
		form = ItyForm(data=request.POST, files = request.FILES)
		if form.is_valid():
			form.save()
			obj=form.instance
		return render(request,"upload.html",{"obj":obj})	
	
	else:
		form=ItyForm()
		img=Mono.objects.all()
	return render(request, "upload.html",{'img':img, 'form':form})

def ent(request):
	
	if request.method == "POST":
		form = EntForm(data=request.POST, files = request.FILES)
		if form.is_valid():
			form.save()
			obj=form.instance
		return render(request,"upload.html",{"obj":obj})	
	
	else:
		form=EntForm()
		img=Mono.objects.all()
	return render(request, "upload.html",{'img':img, 'form':form})


def search(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	if request.method == 'POST' :
	
		searched = request.POST.get('b')
		p = request.POST.get('b')
		mono= Mono.objects.all()
		

		products = mono.filter(others__contains=searched) | mono.filter(cloth_type__contains=searched)


		return render(request,'search.html',{ 'searched':searched, 'products':products, 'cartItems':cartItems,})
	else:
		return render(request,'search.html')
"""	if 'b' in request.GET:
		b = request.GET['b'] 3
		products = Mono.objects.filter(others__contains=b)
		return render(request,'search.html',{ 'b':b, 'products':products})
	else:
		return render(request,'search.html')
"""







def tests(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Mono.objects.all()
	entry = Entry.objects.all() 
	

	#pagination setup
	p = Paginator(Mono.objects.all(), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list, 'entry':entry}
	return render(request, 'test.html', context)


# for monogramming
def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Mono.objects.all().filter(cloth_type='monogramming')
	entry = Entry.objects.all() 
	

	#pagination setup
	p = Paginator(Mono.objects.all().filter(cloth_type='monogramming'), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list, 'entry':entry}
	return render(request, 'monogramming.html', context)



def embriod(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Mono.objects.all().filter(cloth_type='embriodry')
	print('saves')

	#pagination setup
	p = Paginator(Mono.objects.all().filter(cloth_type='embriodry'), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list}
	return render(request, 'embrio.html', context)

def dress(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Mono.objects.all().filter(cloth_type='dress')
	print('saves')


	#pagination setup
	p = Paginator(Mono.objects.all().filter(cloth_type='dress'), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list}
	return render(request, 'clothes.html', context)





def blouse (request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	mono= Mono.objects.all()

	products = mono.filter(cloth_type__contains='blouse') | mono.filter(others__contains='blouse')


	

	#pagination setup
	p = Paginator(mono.filter(cloth_type__contains='blouse') and mono.filter(others__contains='blouse'), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list}
	return render(request, 'sub_sites/blouse.html', context)


def skirts(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	mono= Mono.objects.all()


	products = mono.filter(cloth_type__contains='skirt') | mono.filter(others__contains='skirt')


	#pagination setup
	p = Paginator(mono.filter(cloth_type__contains='skirt') | mono.filter(others__contains='skirt'), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list}
	return render(request, 'sub_sites/skirts.html', context)

def shirt(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	mono= Mono.objects.all()


	products = mono.filter(cloth_type__contains='shirt') | mono.filter(others__contains='shirt')


	#pagination setup
	p = Paginator(mono.filter(cloth_type__contains='skirt') | mono.filter(others__contains='skirt'), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list}
	return render(request, 'sub_sites/skirts.html', context)

def custom(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	mono= Mono.objects.all()


	products = mono.filter(cloth_type__contains='customize') | mono.filter(others__contains='customize')

	#pagination setup
	p = Paginator(mono.filter(cloth_type__contains='customize') | mono.filter(others__contains='customize'), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list}
	return render(request, 'sub_sites/custom.html', context)


def gowns(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	mono= Mono.objects.all()


	products = mono.filter(cloth_type__contains='gown') | mono.filter(others__contains='gown')


	
	#pagination setup
	p = Paginator( mono.filter(cloth_type__contains='gown') | mono.filter(others__contains='gown'), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list}
	return render(request, 'sub_sites/custom.html', context)




def accessories(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Mono.objects.all().filter(cloth_type='accessories')

	#pagination setup
	p = Paginator(Mono.objects.all().filter(cloth_type='accessories'), 20)
	page = request.GET.get('page')
	product_list = p.get_page(page)

	context = {'products':products, 'cartItems':cartItems, 'product_list':product_list}
	return render(request, 'access.html', context)




class ArtDetailView(generic.DetailView):
    model = Mono
    template_name = "test.html"





def details(request, link_id):

	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	
	products = Mono.objects.get(id=link_id)
	print(products)
	entries = Entry.objects.filter()



	if request.method == "POST":
		form = EntryForm(data=request.POST, files = request.FILES)
		if form.is_valid():
			form.save()
			obj=form.instance
		return render(request,"test.html",{"obj":obj}, instance=products)	
	
	else:
		form=EntryForm()
		img=Mono.objects.all()
	return render(request, "test.html",{'img':img, 'form':form,'products':products,'entries':entries,'items':items, 'order':order, 'cartItems':cartItems})

			
		
	
	



def cart(request):
	data = cartData(request) 

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)



def updateItem22(request):
	data = json.loads(request.body)
	productId = data['productId']

	
	entry =  data['action']
	action = data['action']
	print('Action:', entry)
	print('Product:', productId)
	


	customer = request.user.customer
	print(customer)
	product = Mono.objects.get(id=productId)
	

	order, created = Order.objects.get_or_create(customer=customer)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product, )

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Mono.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

def contact(request):
	return render(request, 'contact.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        suggestion = request.POST.get('suggest')

        send_mail(
            subject='Suggestion from ' + name, message=suggestion, from_email= email, recipient_list = ['omarfaruk2468@omar.com']
        )

        messages.add_message(request, messages.SUCCESS, 'Thanks For Your Suggestion!')
        return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'contact.html')



def dress_detail(request, pk):
	mono = Mono.objects.get(pk=pk)
	#mono = get_object_or_404(models.Mono, pk=pk)
	return render(request, 'details.html', {'mono':mono})
