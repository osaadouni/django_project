from django.db import models
from random import randint 
from django.urls import reverse


class ProjectState(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ' '.join((self.name))

class ProjectPhase(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ' '.join((self.name))
     
class Project(models.Model):
    PRICE_TYPES = (
        ('bill', 'Billable'),
        ('non_bill' , 'Non-billable'), 
        ('fixed', 'Fixed price'), 
    )
    PROJECT_STATES = (
        ('active', 'Active'), 
        ('completed', 'Completed'),
        ('aborted', 'Aborted'),
    )

    PROJECT_KINDS = (
        ('single', 'Single'), 
        ('going', 'Ongoing'),
    )
    
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, verbose_name="Who's the client?")
    name = models.CharField(max_length=100, verbose_name="Project Name:")
    description = models.CharField(max_length=100, verbose_name="Short Description:")
    manager = models.ForeignKey('employees.Employee', models.SET_NULL, null=True, verbose_name="Project manager:") 
    price_type = models.CharField(max_length=10, choices=PRICE_TYPES, default='bill', verbose_name="Project Price Type:")
    budgetted_hours = models.FloatField(null=True, blank=True, default=0.0)

    state = models.ForeignKey(ProjectState, models.SET_NULL, null=True, verbose_name="Project state:") 
    phase = models.ForeignKey(ProjectPhase, models.SET_NULL, null=True, verbose_name="Project phase:") 
    kind = models.CharField(max_length=10, choices=PROJECT_KINDS, default='single', verbose_name="Single/Ongoing:") 
    fixed_price_currency = models.CharField(max_length=3, blank=True, default='')
    fixed_price = models.FloatField(default=0)
    fixed_hours = models.CharField(max_length=20, default='')
    client_ref_number = models.CharField(max_length=50, default='', blank=True, verbose_name="Client reference number (CRN):")
    invoice_number = models.CharField(max_length=50, default='', blank=True, verbose_name="Invoice number (IRN):")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return reverse("projects:project-edit", kwargs={'pk': self.pk})

    def clean(self):
        # generate an automatic name field 
        print(f"self.client : {self.client}")
        self.name = '_'.join([self.client.name, str(randint(10000, 99999)), '_'.join(self.description.split())])
        print(f"self.client : {self.client}")
        print(f"self.description :{self.description}")
        print(f"self.name : {self.name}")


    #def save(self, *args, **kwargs):
    #    """
    #    override save 
    #    """
    #    print(f"self.client : {self.client}")
    #    self.name = '_'.join([self.client.name, str(randint(10000, 99999)), self.description])

    #print(f"self.client : {self.client}")
    #    print(f"self.description :{self.description}")
    #    print(f"self.name : {self.name}")
    #     super().save(*args, **kwargs)

