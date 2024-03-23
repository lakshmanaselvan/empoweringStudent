from django import forms
from .models import Registration
from .models import StaffRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('name','email','password')
        labels = {
            'name':'',
            'email':'',
            'password':''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'style': 'width: 500px; text-align: center'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'style': 'width: 500px; text-align: center'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'style': 'width: 500px; text-align: center'})
        }

class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = StaffRegistration
        fields = ('name', 'email', 'password')
        labels = {
            'name':'',
            'email':'',
            'password':''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'style': 'width: 500px; text-align: center'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'style': 'width: 500px; text-align: center'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'style': 'width: 500px; text-align: center'})
        }

class studentLoginForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('email', 'password')
        labels = {
            'email':'',
            'password':''
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'style': 'width: 500px; text-align: center'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'style': 'width: 500px; text-align: center'})
        }

class staffLoginForm(forms.ModelForm):
    class Meta:
        model = StaffRegistration
        fields = ('email', 'password')
        labels = {
            'email':'',
            'password':''
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'style': 'width: 500px; text-align: center'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'style': 'width: 500px; text-align: center'})
        }