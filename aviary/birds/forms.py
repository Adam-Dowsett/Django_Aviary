from django import forms
from .models import Bird

class NewBirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ["name", "age", "species"]

class EditBirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ["name", "age", "species"]