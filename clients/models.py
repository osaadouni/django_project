from django.db import models
from django.urls import reverse
from django.utils import timezone


from django_countries.fields import CountryField 


class Client(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Full Company Name:")
    name = models.CharField(max_length=30, verbose_name="Name (for internal use))")
    vat_number = models.CharField(max_length=100, verbose_name="VAT Number:")
    address = models.TextField(blank=True, verbose_name='Address:')
    state = models.CharField(max_length=50, blank=True, verbose_name='State/Province:')
    zipcode = models.CharField(max_length=20, blank=True, verbose_name='Zip/Postal Code:')
    city = models.CharField(max_length=20, blank=True, verbose_name='City/Town:')
    country = CountryField(blank_label='-- (Select country) --', blank=True, default='', verbose_name='Country:')

    INV_TPL_EUR = 'EUR'
    INV_TPL_US = 'US'
    INV_TPL_OTHER = 'OTHER'
        
    INV_TEMPLATES = (
        (INV_TPL_EUR, 'EUR'),
        (INV_TPL_US, 'US'), 
        (INV_TPL_OTHER, 'OTHER'), 
    ) 
    inv_tpl = models.CharField(
        max_length=5, 
        choices=INV_TEMPLATES, 
        default=INV_TPL_EUR,
        verbose_name="Invoice Template:",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #class Meta:
    #    db_table = 'client'
    
    def __str__(self):
        return ' -  '.join((self.company_name, self.name))
    
    def get_absolute_url(self):
        return reverse('clients:client-edit', kwargs={'pk': self.pk})

