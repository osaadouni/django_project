from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.core.validators import RegexValidator

from .models import TimeReg


class TimeRegForm(forms.ModelForm):
    numeric = RegexValidator(r'^[0-9]+$', 'Only digits are allowed.')
    hour = forms.CharField(max_length=5,
        label='Hour', 
        initial='00', 
        validators=[numeric])
    minute = forms.CharField(max_length=2, label='Min', initial='00', validators=[numeric])
    sec = forms.CharField(max_length=22, label='Sec', initial='00', validators=[numeric])

    class Meta:
        model = TimeReg
        fields = ['client', 'project', 'activity', 'description', 'date', 'bill', 'hour', 'minute', 'sec']
        widgets = {
            'date': DatePickerInput(format='%Y-%m-%d'),
        }
    

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.hour = '14'
        super().__init__(*args, **kwargs)
   
    def save(self):
        print("TimeRegForm()::save()...") 
        obj = super().save(commit=False)

        obj.created_by = self.user

        hour = self.cleaned_data.get("hour")
        minute = self.cleaned_data.get("minute")
        sec = self.cleaned_data.get("sec")
        time = "{}:{}:{}".format(hour, minute, sec)
        print("TimeRegForm()::save()...time = ", time) 
        obj.time = time

        obj.save()
        return obj
