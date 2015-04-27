from django.contrib import admin
from .models import Transaction	
# from .forms import TransactionAdminForm

class TransactionAdmin(admin.ModelAdmin):
	model = Transaction
	list_display = ('name','user','transaction_date','category','note','photo')
	list_filter = ('category','transaction_date','created_at','updated_at',)
	# form = TransactionAdminForm()
admin.site.register(Transaction, TransactionAdmin)