from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
	password=forms.CharField(
		label="Password", 
		widget=forms.PasswordInput)
	password2=forms.CharField(
		label="Confirmar Password",
		widget=forms.PasswordInput)

	class Meta:
		model=User
		fields=['username', 'first_name', 'email']

	def clean_password2(self):
		cd=self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Los passwords no coinciden')
		return cd['password2']	

	def clean_first_name(self):
		cd=self.cleaned_data
		if not cd['first_name']:
			raise forms.ValidationError('Tienes que poner tu nombre')
		return cd['first_name'] 	

	