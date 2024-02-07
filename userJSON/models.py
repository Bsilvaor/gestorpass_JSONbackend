from django.db import models

class Usuario(models.Model):
    nickname = models.CharField(max_length=255)  # Cambia 'default_nickname' según tus preferencias
    clave = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname


