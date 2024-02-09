import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
import pdb

# NO SÉ PORQUÉ, PERO EN POST ME DA ERROR EN POSTMAN
#@csrf_exempt
def listar_usuarios(request):
    pdb.set_trace()
    usuarios = Usuario.objects.all()
    
    #Esta variable usuarios la creamos diciendo que seleccione todos los usuarios ya creados.
    usuarios_datos = [{'id': 'usuario.id', 'nickname': 'usuario.nickname'} for usuario in usuarios]
    return JsonResponse({'usuarios', usuarios_datos})
    #Creamos otra variable llamada usuarios_datos para que solo seleccione la id y el nickname del usuario
    #creo que es más conveniente si al final va a ser una petición GET para por ejemplo saber el ID de
    #algún usuario para editar su contraseña o borrarlo

#EJEMPLO DE COMO HACER LA QUERY EN PYTHON SHELL:

    #from userJSON.models import Usuario
    #usuarios = Usuario.objects.all()
    #for usuario in usuarios:
        #print(f"ID: {usuario.id}, Nickname: {usuario.nickname}")


@csrf_exempt
def crear_usuario(request):
# try:
        #data = json.loads(request.body) 
        #nickname = data.get('nickname')
        #clave = data.get('clave')
#el try de arriba, servía para extraer los datos de una solicitud HTTP.
#en este caso cogía los datos y los almacenaba (el data) después que fuera convertido en un
#objeto de python (json.loads(request.bodu))
    
    try:
        nickname = request.POST.get('nickname')
        clave = request.POST.get('clave')

        Usuario.objects.create(nickname=nickname, clave=clave)
        #Usuario.save() aquí no tiene sentido porqué justo arriba estoy creando (.create) el objeto Usuario
        # en este caso al crear el usuario, es mejor .create que .save ya que .save implicaría que tuviera que
        # crear una variable sin el objects.create y luego guardarlo con el .save()

        return JsonResponse({'mensaje': 'Usuario creado correctamente'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    #el Exception as e define "e" como la Exception, para que en el return (stre(e)... devuelva como string la variable e

    
@csrf_exempt
def editar_clave(request, usuario_id):
    try:
        # creo la variable usuario, para obtener mediante la id el usuario que yo quiera
        usuario = Usuario.objects.get(pk=usuario_id)
        
        # obtengo la nueva clave mediante una solicitud POST, 
        # ESTO NO LO ENTIENDO BIEN. o mejor dicho a mí la lógica me dice que esto debería ir abajo del if.
        nueva_clave = request.POST.get('nueva_clave')
        
        
        if nueva_clave:
            #sin el if, me daba error al intentar editar la contraseña porqué el campo está configurado como not null y así
            #con el if evitamos que si no se introduce una clave nueva se modifique ésta sin ningún valor lo cual me daría problemas
            usuario.clave = nueva_clave
            usuario.save()
            #En este caso si que utilizamos .save() ya que editamos una contraseña que ya estaba creada.


        return JsonResponse({'mensaje': 'Clave actualizada correctamente'})
    except Usuario.DoesNotExist:
        # DoesNotExist: es una excepción específica generada por Django cuando se realiza una consulta utilizando el método get()
        #en un modelo y no se encuentra ningún objeto que coincida con los criterios de la búsqueda.
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)    
    
@csrf_exempt
def listar_todo(request):
    usuarios = Usuario.objects.values()
    return JsonResponse({'usuarios': list(usuarios)})

#borrar usuario he pensado que no hacía falta hacerlo por POST
def borrar_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
        usuario.delete()
        return JsonResponse({'mensaje': 'Usuario eliminado correctamente'})
    except Usuario.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)



