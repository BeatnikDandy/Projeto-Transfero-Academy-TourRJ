from django.db import models

# Create your models here.
class  cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    telefone = models.TextField(max_length=20)
    nacionalidade = models.TextField(max_length=50)
    data_nasc = models.TextField()
    interesse = models.IntegerField()


class passeio(models.Model):
    id = models.AutoField(primary_key=True)
    bairro = models.TextField(max_length=100)


