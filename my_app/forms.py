from django import forms

from my_app.models import Food


class food_forms(forms.ModelForm):
    class Meta:
        model = Food
        fields = ("__all__")