from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cow, MilkProduction, HealthRecord, Veterinarian

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ['name', 'breed', 'date_of_birth', 'image']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

class MilkProductionForm(forms.ModelForm):
    class Meta:
        model = MilkProduction
        fields = ['date', 'amount', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
        }

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['date', 'symptoms', 'diagnosis', 'treatment', 'is_urgent']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'symptoms': forms.Textarea(attrs={'rows': 3}),
            'diagnosis': forms.Textarea(attrs={'rows': 3}),
            'treatment': forms.Textarea(attrs={'rows': 3}),
        }

class VeterinarianForm(forms.ModelForm):
    class Meta:
        model = Veterinarian
        fields = '__all__'
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }