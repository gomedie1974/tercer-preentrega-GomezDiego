from django.urls import path
from control_empleados.views import (listar_empleados, cargar_bodega, listar_bodegas,
buscar_bodegas, cargar_empleado, buscar_empleados, eliminar_empleado, eliminar_bodega,
editar_empleado, editar_bodega, EmpleadoListView,EmpleadoCreateView,EmpleadoDeleteView,EmpleadoDetailView,EmpleadoUpdateView, BodegaListView, BodegaCreateView,BodegaDeleteView, BodegaDetailView, BodegaUpdateView
)   

urlpatterns = [
    #URLS de empleados
    #path('empleados/', listar_empleados, name='lista_empleados'),
    #path('alta-empleados/', cargar_empleado, name='cargar_empleado'),
    #path('buscar-empleados/', buscar_empleados, name='buscar_empleados'),
    #<int:id> es el identificador del empleado a borrar
    #path('eliminar-empleados/<int:id>', eliminar_empleado, name='eliminar_empleado'), 
    #path('editar_empleado/<int:id>', editar_empleado, name='editar_empleado'),
    #EMPLEADOS
    path('empleados/', EmpleadoListView.as_view(), name='lista_empleados'),
    path('empleados/<int:pk>', EmpleadoDetailView.as_view(), name='ver_empleados'),
    path('alta-empleados/', EmpleadoCreateView.as_view(), name='cargar_empleado'),
    path('editar_empleado/<int:pk>', EmpleadoUpdateView.as_view(), 
    name='editar_empleado'),
    path('eliminar-empleados/<int:pk>', EmpleadoDeleteView.as_view(), name='eliminar_empleado'), 
 

    #URLS de bodegas
    #path('alta-bodegas/', cargar_bodega, name='cargar_bodega'),
    #path('lista-bodegas/', listar_bodegas, name='listar_bodegas'),
    #path('buscar-bodegas/', buscar_bodegas, name='buscar_bodegas'),
    #path('eliminar_bodega/<int:id>', eliminar_bodega, name='eliminar_bodega'),
    #path('editar_bodega/<int:id>', editar_bodega, name='editar_bodega'),

 
    path('bodegas/', BodegaListView.as_view(), name='listar_bodegas'),
    
    path('bodegas/<int:pk>', BodegaDetailView.as_view(), name='ver_bodegas'),

    path('alta-bodegas/', BodegaCreateView.as_view(), name='cargar_bodega'),
    
    path('editar_bodegas/<int:pk>', BodegaUpdateView.as_view(), 
    name='editar_bodegas'),

    path('eliminar-bodegas/<int:pk>', BodegaDeleteView.as_view(), name='eliminar_bodegas'), 

    
]
