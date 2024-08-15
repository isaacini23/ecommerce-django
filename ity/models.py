from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

COLOR_CHOICES = (
 	('green', 'green'),
 	('red', 'red'),
 	('black', 'black'),
 	('orange', 'orange'),
 	('purple', 'purple'),
 	('white', 'white'),
 	('gold', 'gold'),
 	('indigo', 'indigo'),
 	('brown', 'brown'),
 	('yellow', 'yellow'),
 	('grey', 'grey'),
 	('dark red', 'dark red'),
 	('turquoise', 'turquoise'),
 	('lavender', 'lavender'),
 	('blue','blue'),


)

CLOTH_SIZE = (

	('Xlarge','Xlarge'),
	('large','large'),
	('medium', 'medium'),
	('slimfit', 'slimfit'),

	)

CLOTH_TYPE = (

	('Gown' , 'Gown'),
	('Shirt' , "Shirt"),
	('Monogramming' , "Monogramming"),
	('Dress' , "Dress"),
	('Blouse' , "Blouse"),
	('Gown' , "Gown"),
	('Accessories' , "Accessories"),
	('Trouser' , "Trouser"),	
	('Customize' , "Customize"),
)

# Create your models here.
class Mono(models.Model):
	name = models.CharField(max_length=200)
	cloth_size = models.CharField(max_length= 300, choices=CLOTH_SIZE, null= True, blank= True)
	others =  models.CharField(max_length=200, null=True)
	price = models.FloatField()
	image = models.ImageField(upload_to='images/', null=False, blank=False, default="null")
	cloth_type = models.CharField(max_length=200, choices=CLOTH_TYPE, null=True)
	COLOR = models.CharField( max_length=200, choices=COLOR_CHOICES, null=False)
	full_size =  models.FloatField(null=True, default='0')
	date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	
	def get_absolute_url(self):
		return get_absolute_url("entries",kwargs={'pk': self.pk})






	"""docstring for Entry"""

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, null=True)
	last_name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.user.username
	@receiver(post_save, sender=User)
	def customer_signal(sender, instance, created, **kwargs):
		if created:
			Customer.objects.create(user=instance)
		instance.customer.save()
		


class Entry(models.Model):
	topic = models.OneToOneField(Mono, on_delete=models.SET_NULL, null=True, blank=True)
	COLOR = models.CharField( max_length=200, choices=COLOR_CHOICES , default='red', null=True)
	full_size =  models.CharField(null=True,choices=CLOTH_SIZE, default='',max_length=100,)
	date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	more_info = models.TextField(null=True)
	
	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return self.COLOR[:50] + "..."

	def get_absolute_url(self):
		return get_absolute_url("entries",kwargs={'pk': self.pk})



	


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	entry = models.ForeignKey(Entry, on_delete=models.SET_NULL, null=True, blank=True)

	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			
			shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 






class OrderItem(models.Model):
	product = models.ForeignKey(Mono,  on_delete=models.SET_NULL, null=True, blank=True)
	entry = models.ForeignKey(Entry, on_delete=models.SET_NULL, null=True, blank=True)

	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

