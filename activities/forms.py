from django import forms

from activities.models import Activity, Category

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity 
        fields = '__all__'
        widgets = {
            'department': forms.CheckboxSelectMultiple(),
            #'category': forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="(Select category)"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "-- (Select category) --"
        #self.fields['category'].widget.attrs.update(empty_label="-- (Select category) --") # Does NOT work


