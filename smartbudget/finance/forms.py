from django import forms
from .models import Transaction

class TransactionAdminForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = ['name','amount','transaction_date','category','note','photo']

class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = ['name','amount','transaction_date','category','note','photo']
		widgets = {
            'name': forms.TextInput(attrs={}),
            'transaction_date': forms.TextInput(attrs={}),
            'note': forms.Textarea(attrs={}),
            'amount': forms.TextInput(attrs={}),
            'category': forms.Select(attrs={}),
 		}