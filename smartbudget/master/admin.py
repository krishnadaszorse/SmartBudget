from django.contrib import admin
from .models import Category
# from .forms import CategoryAdminForm

class CategoryAdmin(admin.ModelAdmin):
	model = Category
	list_display = ('name','is_default','is_income','is_archive','user','created_at','updated_at')
	list_filter = ('is_default','is_income','is_archive','created_at','updated_at',)
	# form = CategoryAdminForm()
admin.site.register(Category, CategoryAdmin)