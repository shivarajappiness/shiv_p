from django.contrib import admin
from django import forms
from .models import puser
# Register your models here.
class UserDetails(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'mobile')

class UserModeladmin(admin.ModelAdmin):
	class Meta:
		model = puser


class UserForm(forms.ModelForm):
    class Meta:
        model = puser
        fields = "__all__" 
        def clean(self):
            name = self.cleaned_data.get('name')
            email = self.cleaned_data.get('email')
            mobile = self.cleaned_data.get('mobile')
            # email = self.cleaned_data.get('email')
            mobile = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
            # if start_date > end_date:
            #     raise forms.ValidationError("Dates are fucked up")
            return self.cleaned_data

admin.site.register(puser, UserDetails)
