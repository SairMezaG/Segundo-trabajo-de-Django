from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from appMesaDeServicios.models import *
from random import *
from django.db import Error, transaction

# Create your views here.


def login (request):
    usuario = request.POST["txtUsuario"]
    contraseña = request.POST["txtPassword"]
    user = authenticate(username=usuario, password=contraseña)
    print(user)
    if user is not None:
        auth.login(request, user)
        if user.groups.filter(name="Administrador").exists():
            return redirect("/inicioAdministrador")
        elif user.groups.filter(name="Tecnico").exists():
            return redirect("/inicioTecnico")
        else:
            return redirect("/inicioEmpleado")
        
        
        
def registroSolicitud(request):
    try:
        with transaction.atomic():
            user = request.user
            descripcion = request.POST["txtDescripcion"]
            idOficinaAmbiente = int(["cbOficinaAmbiente"])
            oficinaAmbiente = oficinaAmbiente.objects.get(id=idOficinaAmbiente) 
            solicitud = Solicitud(solUsuario = user, solDescripcion = descripcion, solOficinaAmbiente = oficinaAmbiente)
            solicitud.save()
            consecutivoCaso = randint(1,1000)
            codigoCaso = "REQ" + str(consecutivoCaso).rjust(5,'0')
            userCaso = User.objects.filter(groups__name__in=["Administrador"])
            estado = "Solicitada"
            caso = Casos(casSolicitud= solicitud, casCodigo= codigoCaso, casUsuario=userCaso, casEstado=estado)
            caso.save()
    except Error as error:
        transaction.rollback()
        mensaje = f"{error}"
        
        
def vistaSolicitud(request):
    if request.user.is_authenticated:
        oficinaAmbientes = OficinaAmbiente.objects.all()
        datosSesion = {"user":request.user, "rol": request.user.groups.get().name, "oficinaAmbientes": oficinaAmbientes}
        return render(request, "")
    else:
        mensaje = "Debes iniciar Sesion" 
        return render        
            
     
         
            

def inicioAdministrador (request):
    if request.user.is_authenticated:
        datosSesion = {"user":request.user,
                       "rol":request.user.groups.get().name}
        return render (request, "administrador/inicioAdministrador.html", datosSesion)
    else:
        mensaje ="Debe iniciar Sesion"
        return render (request, "inicio.html", {"mensaje":mensaje})
    
def inicioTecnico(request):
    if request.user.is_authenticated:
        datosSesion = {"user":request.user,
                       "rol":request.user.groups.get().name}
        return render (request, "tecnico/inicioTecnico.html", datosSesion)
    else:
        mensaje ="Debe iniciar Sesion"
        return render (request, "inicio.html", {"mensaje":mensaje})
    
def inicioEmpleado(request):
    if request.user.is_authenticated:
        datosSesion = {"user":request.user,
                       "rol":request.user.groups.get().name}
        return render (request, "empleado/inicioEmpleado.html", datosSesion)
    else:
        mensaje ="Debe iniciar Sesion"
        return render (request, "inicio.html", {"mensaje":mensaje})

def inicio(request):
    return render(request, 'inicio.html')




    




def incicioAdministrador(request):
    if request .user.is_authenticated:
        datosSesion = {"user": request.user, "rol": request.groups.get().name}
        
        return render (request, "administrador/inicioAdministrador.html", datosSesion)
    else:
        mensaje = "Debe primero iniciar Sesion"
        return render(request, "inicio.html",{"mensaje": mensaje})
        
        




    



