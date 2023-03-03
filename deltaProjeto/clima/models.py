from django.db import models

class Localizacao(models.Model):
    estado = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)