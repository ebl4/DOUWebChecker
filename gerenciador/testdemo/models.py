from django.db import models

# Create your models here.

# Class ItemDemo that refers to an Agenda
class ItemDemo(models.Model):
	data = models.DateField()
	hora = models.TimeField()
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	
	def __str__(self):
		return self.descricao;
