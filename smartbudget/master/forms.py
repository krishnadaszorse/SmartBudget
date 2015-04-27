from django import forms
from registration.models import AppUser
from .models import Category


class CategoryAdminForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['user','name','is_default','is_income','is_archive']

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name','is_default']
		widgets = {
            'name': forms.TextInput(attrs={}),
        }


class SetMonthStartDateForm(forms.ModelForm):
	class Meta:
		model = AppUser
		fields = ['month_start_date']
		widgets = {
            'month_start_date': forms.Select(attrs={}),
        }

class SetWeekDaysForm(forms.ModelForm):
	class Meta:
		model = AppUser
		fields = ['weekdays']
		widgets = {
            'weekdays': forms.Select(attrs={}),
        }

class SetCountryForm(forms.ModelForm):
	class Meta:
		model = AppUser
		fields = ['country']
		widgets = {
            'country': forms.Select(attrs={}),
        }