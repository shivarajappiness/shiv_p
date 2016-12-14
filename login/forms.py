from django import forms

from .modles import puser

class Puser(forms.ModelForm):
    class Meta:
        model = Puser
        fields = ['name', 'mobile', 'email']



    def clean_email(self):
        email = self.clean_data.get('email')
        if not "gmail" in email:
            raise forms.ValidationError("Please use a valid 'Gmail' address")
        return email