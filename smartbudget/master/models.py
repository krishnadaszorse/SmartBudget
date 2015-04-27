from django.db import models
from registration.models import AppUser

class Category(models.Model):
	name = models.CharField(verbose_name = "Category name", max_length=50)
	is_default = models.BooleanField(verbose_name = "Default?",default=False)
	is_income = models.BooleanField(verbose_name = "Income?")
	is_archive = models.BooleanField(verbose_name = "Archived?",default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(AppUser)
	def save(self, *args, **kwargs):
		if self.is_default == True:
			Category.objects.filter(is_income=self.is_income).update(is_default=False)
		super(Category, self).save(*args, **kwargs)
	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"
	def __str__(self):
		return self.name
