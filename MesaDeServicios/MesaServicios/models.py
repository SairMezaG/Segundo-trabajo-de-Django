from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
TipoOficinaAmbiente = [
    ('Aministrativo','Administrativo'),
    ('Formacion','Formacion')
]


class oficinaAmbiente(models.Model):
    ofiTipo = models.CharField(max_length=15, choices=TipoOficinaAmbiente, db_comment = "tipo")
    ofiNombre = models.CharField(max_length=50, unique= True,  db_comment = "Nombre de la oficina o ambiente")
    fechaHoraCreacion = models.DateTimeField(auto_now_add= True, db_comment ="Fecha y Hora del Registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now= True, db_comment = "Fecha y Hora última actualizacion")
    
    def __str__(self) -> str:
        return self.ofiNombre
    
 




 
TipoUsuario = [
    ('Aministrativo','Administrativo'),
    ('Instructor','Instructor')
    
]  
   
class user(AbstractUser):
    userTipo = models.CharField(max_length=15, choices=TipoUsuario,db_comment="Tipo de Usuario")
    userFoto = models.ImageField(upload_to=f'fotos/', null=True, blank=True, db_comment="Foto del Usuario")
    fechaHoraCreacion = models.DateTimeField(auto_now_add= True, db_comment ="Fecha y Hora del Registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now= True, db_comment = "Fecha y Hora última actualizacion")
      
      
    def __str__(self) -> str:
      return  self.username
  







class solicitud(models.Model):
    solUsuario = models.ForeignKey(user, on_delete=models.PROTECT, de_comment="Hace referencia al empleado que hace la solicitud") 
    solDescripcion = models.TextField(max_length=1000, de_comment="Texto que describe la solicitud del empleado") 
    solOficinaAmbiente = models.ForeignKey(on_delete=models.PROTECT, de_comment="Hace referencia a la oficina o ambiente donde se encuentra el equipo")
    fechaHoraCreacion = models.DateTimeField(auto_now_add= True, db_comment ="Fecha y Hora del Registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now= True, db_comment = "Fecha y Hora última actualizacion")
    
    def __str__(self) -> str:
      return  self.solDescripcion
 
 
 
 
 
 
  
estadosCaso =[
    ('Solicitad', 'Solicitad'),
    ('En Proceso', 'En Preceso'),
    ('Finalizado', 'Finalizado')
]  
  
class casos(models.Model):
    casSolicitud = models.ForeignKey(solicitud, on_delete=models.PROTECT, db_comment = "Hace referencia a la solicitud que genera")
    casCodigo = models.CharField(max_length=10, unique=True, db_comment = "Codigo único del caso")
    casUsuario =  models.ForeignKey(user, on_delete= models.PROTEC, db_comment="Empleado de soperte tecnico asignado al caso")
    fechaHoraActualizacion = models.DateTimeField(auto_now= True, db_comment = "Fecha y Hora última actualizacion")
    
    def __str__(self) -> str:
      return  self.casSolicitud
  





  
class tipoProcedimiento(models.Model):
    tipoNombre = models.CharField(max_length=20, db_comment = "Nombre del tipo de Procedimiento" )
    tipDescripcion= models.TextField(max_length=100, db_comment = "Texto con la descripcion del procedimiento")
    fechaHoraCreacion = models.DateTimeField(auto_now_add= True, db_comment ="Fecha y Hora del Registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now= True, db_comment = "Fecha y Hora última actualizacion") 
    
  




class solucionCaso(models.Model):
    solCaso = models.ForeignKey(casos, on_delete=models.PROTECT, db_comment = "Hace referencia al caso que se soluciona")
    
      
  
  

        
