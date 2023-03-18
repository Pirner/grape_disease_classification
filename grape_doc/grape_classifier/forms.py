from django import forms

from .models import GrapeClassification


class ClassificationRequestForm(forms.ModelForm):
    # fields = ('description')

    class Meta:
        model = GrapeClassification
        fields = ('description', )

        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control small'})
        }
