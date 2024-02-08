from django.urls import path
from .views import listar_usuarios, crear_usuario, listar_todo, borrar_usuario

urlpatterns = [
    path('usuarios/', listar_usuarios, name='listar_usuarios'),#GET PERO DEBERÍA SER POST PORQUE SALEN LAS PASS
    
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    
    path('all/', listar_todo, name='listar_todo'),

    path('borrar_usuario/<int:usuario_id>/', borrar_usuario, name='borrar_usuario'),
]
