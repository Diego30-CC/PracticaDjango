from django.urls import path
from . import views
urlpatterns = [
   #path ("home/",views.saludo, name = "vistaPrincipal"),#

   #path("adios/",views.adios),
   
   #path("Thomo/",views.Thomo),#

   path("Principal/", views.PrimVist, name = "vistaPrimaria"),

   path("Secundaria/", views.SegunVist, name = "vistaSecundaria"),

   path("Terciaria/", views.TercerVist, name = "vistaTerciaria"),
]