from django import forms
from .models import Event
from tempus_dominus.widgets import DatePicker


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name','description','catrgorie','venue','startTime','endTime','startDate','endDate','participation')
        labels = {
            'name':'',
            'description':'',
            'catrgorie':'Select Catogries',
            'venue':'Select Venue',
            'startTime':'',
            'endTime':'',
            'startDate':'YYYY-MM-DD',
            'endDate':'YYYY-MM-DD',
            'participation':''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name', 'style': 'width: 500px; text-align: center'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Event Description', 'style': 'width: 500px; text-align: center'}),
            'catrgorie': forms.Select(attrs={'class':'form-control', 'style': 'width: 500px; text-align: center'}),
            'venue': forms.Select(attrs={'class':'form-control', 'style': 'width: 500px; text-align: center'}),
            'startTime': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Start Time', 'style': 'width: 500px; text-align: center'}, format='%H:%M'),
            'endTime': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'End Time', 'style': 'width: 500px; text-align: center'}),
            'startDate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Start Date', 'style': 'width: 500px; text-align: center'}),
            'endDate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'End Date', 'style': 'width: 500px; text-align: center'}),
        }