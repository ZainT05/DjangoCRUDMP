from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'course']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
        }

widgets = {
    'first_name': forms.TextInput(attrs={'class': 'form-control'}),
    'last_name': forms.TextInput(attrs={'class': 'form-control'}),
    'email': forms.EmailInput(attrs={'class': 'form-control'}),
    'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    'course': forms.TextInput(attrs={'class': 'form-control'}),
}
