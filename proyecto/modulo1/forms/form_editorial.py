from django import forms
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField, Select, NumberInput
from modulo1.models import Editorial


class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = [
            'id',
            'nombre',
            'direccion',
            'telefono',
            'contacto',
            'web'
        ]

    def __init__(self, *args, **kwargs):
        super(EditorialForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })