from django import forms
from ity.models import *


class ItyForm(forms.ModelForm):
	class Meta:
		model = Mono
		fields = ['name', 'image', 'price', 'cloth_type','others', 'cloth_size', "full_size"]


 
class EntForm(forms.ModelForm):
	class Meta:
		model = Mono
		fields = ['COLOR', 'full_size', 'others']



	
class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['COLOR', 'full_size', ]
		