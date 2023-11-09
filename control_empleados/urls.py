from django.urls import path
from control_empleados.views import listar_empleados

urlpatterns = [
    path('empleados/', listar_empleados),
    path("empleados/", listar_empleados, name="listar_empleados"),

]