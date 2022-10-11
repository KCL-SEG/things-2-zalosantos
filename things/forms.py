"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing
from django.core.validators import RegexValidator


class ThingForm(forms.ModelForm):



        description=forms.CharField(max_length=120, blank=True ,widget= forms.Textarea())
        quantity=forms.IntegerField(
            validators=[MinValueValidator(0),MaxValueValidator(50)],
            widget= forms.NumberInput
        )
        name=forms.CharField(max_length=35, unique=True)
