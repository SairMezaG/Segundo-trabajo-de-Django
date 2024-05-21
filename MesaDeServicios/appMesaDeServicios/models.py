from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
TipoOficinaAmbiente = [
    ('Aministrativo','Administrativo'),
    ('Formacion','Formacion')
]


class OficinaAmbiente(models.Model):
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
   
class User(AbstractUser):
    userTipo = models.CharField(max_length=15, choices=TipoUsuario,db_comment="Tipo de Usuario")
    userFoto = models.ImageField(upload_to=f'fotos/', null=True, blank=True, db_comment="Foto del Usuario")
    fechaHoraCreacion = models.DateTimeField(auto_now_add= True, db_comment ="Fecha y Hora del Registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now= True, db_comment = "Fecha y Hora última actualizacion")
      
      
    def __str__(self) -> str:
      return  self.username
  







class Solicitud(models.Model):
    solUsuario = models.ForeignKey(User, on_delete=models.PROTECT, db_comment="Hace referencia al empleado que hace la solicitud") 
    solDescripcion = models.TextField(max_length=1000, db_comment="Texto que describe la solicitud del empleado") 
    solOficinaAmbiente = models.ForeignKey(OficinaAmbiente, on_delete=models.PROTECT, db_comment="Hace referencia a la oficina o ambiente donde se encuentra el equipo")
    fechaHoraCreacion = models.DateTimeField(auto_now_add= True, db_comment ="Fecha y Hora del Registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now= True, db_comment = "Fecha y Hora última actualizacion")
    
    def __str__(self) -> str:
      return  self.solDescripcion
 
 
 
 
 
 
  
estadosCaso =[
    ('Solicitad', 'Solicitad'),
    ('En Proceso', 'En Preceso'),
    ('Finalizado', 'Finalizado')
]  
  
class Casos(models.Model):
    casSolicitud = models.ForeignKey(Solicitud, on_delete=models.PROTECT, db_comment = "Hace referencia a la solicitud que genera")
    casCodigo = models.CharField(max_length=10, unique=True, db_comment = "Codigo único del caso")
    casUsuario =  models.ForeignKey(User, on_delete= models.PROTECT, db_comment="Empleado de soperte tecnico asignado al caso")
    fechaHoraActualizacion = models.DateTimeField(auto_now= True, db_comment = "Fecha y Hora última actualizacion")
    
    def __str__(self) -> str:
      return  self.casSolicitud
  





  
class TipoProcedimiento(models.Model):
    tipoNombre = models.CharField(max_length=20, db_comment = "Nombre del tipo de Procedimiento" )
    tipDescripcion= models.TextField(max_length=100, db_comment = "Texto con la descripcion del procedimiento")
    fechaHoraCreacion = models.DateTimeField(auto_now_add= True, db_comment ="Fecha y Hora del Registro")
    fechaHoraActualizacion = models.DateTimeField(auto_now= True, db_comment = "Fecha y Hora última actualizacion")
    
    def __str__(self) -> str:
      return  self.tipoNombre
   
    
  


tipoSolucion = [
    ('Parcial', 'Parcial'),
    ('Definitiva', 'Definitiva')
]




class SolucionCaso(models.Model):
    solCaso = models.ForeignKey(Casos, on_delete=models.PROTECT,  db_comment="Hace referencia al caso que genera la solución")
                               
    solProcedimiento = models.TextField(max_length=2000, db_comment="Texto del procedimiento realizado en la solución del caso")
                                        
    solTipoSolucion = models.CharField(max_length=20, choices= tipoSolucion, db_comment="Tipo de la solución, si es parcial o definitiva")
                                       
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True,  db_comment="Fecha y hora del registro")
                                            
    fechaHoraActualizacion = models.DateTimeField(auto_now=True, db_comment="Fecha y hora última actualización")
    
    def __str__(self) -> str:
      return  self.solProcedimiento
  
    
    
    


class SolucionCasoTipoProcedimientos(models.Model):
    solSolucionCaso = models.ForeignKey(SolucionCaso, on_delete=models.PROTECT,   db_comment="Hace referencia a la solución del Caso")                                
    solTipoProcedimiento = models.ForeignKey(TipoProcedimiento, on_delete=models.PROTECT,  db_comment="Hace referencia al tipo de procedimiento de la solución")
      
      
    def __str__(self) -> str:
      return  self.solSolucionCaso.solProcedimiento
    
                                            
    
                                                  


    
    
    
    
      
  
  

        
