from django.contrib import admin
from .models import AppUser
# from .forms import AppUserAdminForm

class AppUserAdmin(admin.ModelAdmin):
	model = AppUser
	list_display = ('name','email','password','phone','avatar','verification_key','key_generated','is_verified','created_at','updated_at')
	# form = AppUserAdminForm()
admin.site.register(AppUser)
