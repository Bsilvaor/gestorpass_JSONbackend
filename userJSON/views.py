import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
import pdb

# NO SÉ PORQUÉ, PERO EN POST ME DA ERROR EN POSTMAN
#@csrf_exempt
pdb.setrace
def listar_usuarios(request):
    usuarios = Usuario.objects.values()
    return JsonResponse({'usuarios': list(usuarios)})


@csrf_exempt
def crear_usuario(request):
    try:
        data = json.loads(request.body)
        nickname = data.get('nickname')
        clave = data.get('clave')

        Usuario.objects.create(nickname=nickname, clave=clave)
        #Usuario.save() ME DA ERROR.
        
        return JsonResponse({'mensaje': 'Usuario creado correctamente'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def listar_todo(request):
    usuarios = Usuario.objects.values()
    return JsonResponse({'usuarios': list(usuarios)})

def borrar_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
        usuario.delete()
        return JsonResponse({'mensaje': 'Usuario eliminado correctamente'})
    except Usuario.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

