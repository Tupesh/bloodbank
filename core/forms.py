from django import forms
from .models import *


class MyForm(forms.ModelForm):
    class Meta:
        model = Donating
        fields = ['donarName', 'age', 'donarBloodGroup', 'gender', 'identity']