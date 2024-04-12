from django import forms
from StoreApp.models import Cliente

class CadrastroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'