from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 


class Activity(models.Model):
    # skill levels 
    SKILL_LEVELS = (
        ('', '-- (Select level)--'), 
        ('low', 'Low'), 
        ('high', 'High'), 
        ('inter', 'Intermediate'),
    )
    # company departments 
    #DEPARTMENTS = (('acct', 'Acctounting',), ('tech','Technology',),('markt','Marketing',),('fina', 'Financial',))

    name = models.CharField('activity name:', max_length=50)
    charge_per_hour = models.DecimalField('charge per hour:', 
        max_digits=5, 
        decimal_places=2, 
        blank=True, 
    )
    sold_per_hour = models.DecimalField('sold per hour:',
        max_digits=5, 
        decimal_places=2, 
        blank=True,
    )
    vat = models.DecimalField('vat:',
        max_digits=2, 
        decimal_places=2, 
        blank=True,
    )
    skill_level = models.CharField("skill level:", max_length=10, 
        choices=SKILL_LEVELS, 
        default='', 
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="category")
    #department = models.CharField(max_length=10, choices=DEPARTMENTS, blank=True, null=True)
    department = models.ManyToManyField('departments.Department', blank=True)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return reverse("activities:activity-edit", kwargs={'pk': self.pk})
  
