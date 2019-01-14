from django import forms

from clients.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('company_name', 'name', 'vat_number', 'address', 'state', 'zipcode', 'city', 'country', 'inv_tpl')
        widgets = {
            'address': forms.Textarea(attrs={'rows':4, 'cols': 15}),
        }

