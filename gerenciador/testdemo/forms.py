from django import forms
from .models import ItemDemo

class FormItemAgenda(forms.ModelForm):
	data = forms.DateField(
		widget=forms.DateInput(format='%d/%m/%Y'),
		input_formats=['%d/%m/%Y', '%d/%m/%y'])

class Meta:
	model = ItemDemo
	fields = ('titulo', 'data', 'hora', 'descricao')