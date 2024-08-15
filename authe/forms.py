from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

	email = forms.EmailField( help_text='Required. input a valid email address')
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2',)


class UserForm(UserCreationForm):
	first_name = forms.CharField(max_length=200, help_text='First Name')
	last_name = forms.CharField(max_length=200, help_text='First Name')
	email = forms.EmailField( help_text='Required. input a valid email address')
	

	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'last_name','first_name')

 
class ChangeForm(PasswordChangeForm):
	def __init__(self,user, *args,**kwargs):
		self.user=user
		super().__init__(user, *args,**kwargs)
		self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'old password'})
		
		self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New password'})
		
		self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New password'})
		
	def save(self, commit=True):
		password= self.cleaned_data['new_password1']
		self.user.set_password(password)
		if commit:
			self.user.save()
		return self.user

			
	