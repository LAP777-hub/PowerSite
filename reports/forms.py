from django import forms
from .models import IssueReport


class IssueReportForm(forms.ModelForm):
    class Meta:
        model = IssueReport
        fields = ['title', 'issue_type', 'description', 'area_name', 'latitude', 'longitude', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short title'
            }),
            'issue_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe the issue'
            }),
            'area_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masibekela Village, street, landmark'
            }),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }