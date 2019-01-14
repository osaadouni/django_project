from django.db import models
from django.urls import reverse
from django.utils import timezone


from django_countries.fields import CountryField 


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    job_title = models.ForeignKey('jobtitles.JobTitle', models.SET_NULL, blank=True, null=True)
    address = models.TextField(blank=True, verbose_name='Address:')
    state = models.CharField(max_length=50, blank=True, verbose_name='State/Province:')
    zipcode = models.CharField(max_length=20, blank=True, verbose_name='Zip/Postal Code:')
    city = models.CharField(max_length=20, blank=True, verbose_name='City/Town:')
    country = CountryField(blank_label='-- (Select country) --', blank=True, default='', verbose_name='Country:')

    is_admin = models.BooleanField(default=False, verbose_name='Admin Role ?')
     
    picture = models.ImageField(upload_to='photos/employees/%Y/%m/%d', verbose_name='Photo:', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #class Meta:
    #    db_table = 'employee'
    
    def __str__(self):
        return ' '.join((self.first_name, self.last_name))
    
    def get_absolute_url(self):
        return reverse('employees:employee-edit', kwargs={'pk': self.pk})

