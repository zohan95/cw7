from django import forms

from webapp.models import Choice


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['variation']
