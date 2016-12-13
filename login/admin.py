from django.contrib import admin
from .models import puser
# Register your models here.
class UserDetails(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'mobile')
    
class UserModeladmin(admin.ModelAdmin):
	class Meta:
		model = puser

admin.site.register(puser, UserDetails)
