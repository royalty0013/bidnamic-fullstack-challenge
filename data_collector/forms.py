from django.forms import ModelForm, widgets
from .models import ClientData
from django.db.models.fields import DateField

class DataCollectorForm(ModelForm):
    class Meta:
        model = ClientData
        exclude = ('user', 'added', 'updated',)

        widgets = {
            'date_of_birth': widgets.NumberInput(attrs={'type': 'date'}),
            'address': widgets.Textarea(attrs={'cols': 3, 'rows': 3}),
         }
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(DataCollectorForm, self).__init__(*args, **kwargs)
    
    def save(self):
        data_collector = super(DataCollectorForm, self).save(commit=False)
        data_collector.user = self.user
        data_collector.save()
        return data_collector
