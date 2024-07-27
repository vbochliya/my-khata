
from django import forms
from .models import khata_transactions,given_taken

class khata_transaction_form(forms.ModelForm):
    class Meta:
        model = khata_transactions
        fields = ['datetime', 'name', 'ammount', 'catagory']

class given_taken_form(forms.ModelForm):
    class Meta:
        model = given_taken
        fields = ['datetime', 'name', 'ammount', 'catagory']