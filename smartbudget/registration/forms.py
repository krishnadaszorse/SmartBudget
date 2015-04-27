from django import forms
from .models import AppUser

class AppUserAdminForm(forms.ModelForm):
	class Meta:
		model = AppUser
		fields = ['name','email','password','phone','avatar']