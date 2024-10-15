from django.db import models

class Usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200)
    senha = models.CharField(max_length=100)

