from django.contrib import admin
#from MesaServicios.models import oficinaAmbiente,User
from appMesaDeServicios.models import *

# Register your models here.
admin.site.register(OficinaAmbiente)

admin.site.register(User) 

admin.site.register(Solicitud) 

admin.site.register(Casos) 

admin.site.register(TipoProcedimiento) 

admin.site.register(SolucionCaso) 

admin.site.register(SolucionCasoTipoProcedimientos) 






