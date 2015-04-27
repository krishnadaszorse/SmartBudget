from django.db import models
from master.models import Category
from registration.models import AppUser

class Transaction(models.Model):
	name = models.CharField(verbose_name = "Transaction name", max_length=50)
	transaction_date= models.DateTimeField(verbose_name = "Transaction date", max_length=50)
	category = models.ForeignKey(Category,verbose_name = "Category ", max_length=50)
	amount = models.FloatField(verbose_name = "Amount")
	note = models.CharField(verbose_name = "Note", max_length=50)
	photo = models.ImageField(verbose_name = "Photo", max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(AppUser)
	class Meta:
		verbose_name = "Transaction"
		verbose_name_plural = "Transactions"
	def __str__(self):
		return str(self.id)+" "+self.name
    
