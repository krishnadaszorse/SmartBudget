from django.db import models
from .constants import WEEKDAY_CHOICES,COUNTRY_CHOICES,DATE_CHOICES,ACCOUNTING_CHOICES

class AppUser(models.Model):
	name = models.CharField(verbose_name = "Full Name", max_length=50)
	email = models.EmailField(verbose_name = "Email", max_length=50)
	password = models.CharField(verbose_name = "Password", max_length=50)
	phone = models.CharField(verbose_name = "Phone", max_length=50)
	avatar = models.ImageField(verbose_name = "Avatar", max_length=50)
	weekdays = models.CharField(choices=WEEKDAY_CHOICES,verbose_name="Weekdays",max_length=100,null=True)
	country = models.CharField(choices=COUNTRY_CHOICES,verbose_name="Country",max_length=100,null=True)
	month_start_date = models.CharField(choices=DATE_CHOICES,verbose_name="Month start Date",max_length=100,null=True)
	accounting_type = models.CharField(choices=ACCOUNTING_CHOICES,verbose_name="Accounting Type",max_length=100,null=True)
	verification_key = models.CharField(verbose_name = "Verification key", max_length=50)
	key_generated= models.DateTimeField(verbose_name = "Key generated", max_length=50)
	is_verified = models.BooleanField(verbose_name = "Verified", max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name = "App User"
		verbose_name_plural = "App Users"

	def __str__(self):
		pass
