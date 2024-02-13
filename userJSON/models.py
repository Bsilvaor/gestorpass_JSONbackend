from django.db import models

class Usuario(models.Model):
    nickname = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)

    #def __str__(self):
        #return self.nickname
    
    #ESTE DEF PODRÍA LLEVARLO A VIEWS?


