from django import forms

from .models import Employee


class EmployeeModelForm(forms.ModelForm):
    """ Employee model form """
    class Meta:
        model = Employee
        fields = ['name', 'department', 'position', 'started_work',
                  'date_of_birth', 'email', 'github_link']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'started_work': forms.DateInput(),
            'date_of_birth': forms.DateInput(),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'github_link': forms.TextInput(attrs={'class': 'form-control'}),
        }
