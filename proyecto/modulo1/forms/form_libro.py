from django import forms
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField, Select, NumberInput
from modulo1.models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'id',
            'isbn',
            'titulo',
            'autor',
            'publicacion',
            'paginas',
            'precio',
            'id_editorial',
            'id_distribuidora'
        ]

    def __init__(self, *args, **kwargs):
        super(LibroForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })