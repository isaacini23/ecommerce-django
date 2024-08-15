from django.urls import path, include
from ity import views
from ity.views import *


app_name = 'ity'


urlpatterns = [

path('', views.index, name='home'),
path('about/', views.about, name='about'),
path('upload/', views.upload, name='upload'),
path('cart/', views.cart , name='cart'),
path('monogramming/', views.store , name='store'),
path('embriodry/', views.embriod , name='embriodry'),
path('clothes/', views.dress , name='dress'),
path('accessories/', views.accessories , name='accessories'),
path('checkout/', views.checkout, name="checkout"),
path('blouse/', views.blouse, name="blouse"),
path('skirts/', views.skirts, name="skirts"),
path('custom/', views.custom, name="custom"),
path('gowns/', views.gowns, name="gowns"),
path('store/', views.tests, name="tests"),
path('contact/', views.contact, name="contact"),
path('search/', views.search, name="search"),
path("test/<int:link_id>/", views.details, name="detail"),
path('<pk>/',views.dress_detail, name='dress_detail'),



   
path('update_item/', views.updateItem22, name="update_item"),
path('process_order/', views.processOrder, name="process_order"),


]