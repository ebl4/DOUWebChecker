from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormItemAgenda

from .models import ItemDemo

# Create your views here.

def index(request):
	lista_itens = ItemDemo.objects.all()
	return render(request, "lista.html", {'lista_itens' : lista_itens})

def adiciona(request):
	if request.method == 'POST':
		form = FormItemAgenda(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect("/")

		else:
			form = FormItemAgenda()

		return render(request, "adiciona.html", {'form' : form})