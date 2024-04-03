from django.db import models

# Create your models here.
class  cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    email = models.TextField(max_length=100)
    telefone = models.TextField(max_length=20)
    nacionalidade = models.TextField(max_length=50)
    data_nasc = models.TextField()


class passeio(models.Model):
    id = models.AutoField(primary_key=True)
    bairro = models.TextField(max_length=100)
    data_hora = models.TextField(max_length=100)


class post(models.Model):
    id_post = models.AutoField(primary_key=True)
    img = models.TextField()
    txt = models.TextField(max_length=100)
    data_hora_post = models.TextField(max_length=100)

class tour(models.Model):
    id_passeio = models.ForeignKey("passeio", on_delete=models.CASCADE)
    id_cliente = models.ForeignKey("cliente", on_delete=models.CASCADE)

