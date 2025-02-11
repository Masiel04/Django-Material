from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio),
    path('nuevoMaterial/', views.nuevoMaterial, name='nuevoMaterial'),
    path('listadoMaterial/', views.listadoMaterial, name='listadoMaterial'),
    path('guardarMaterial/', views.guardarMaterial, name='guardarMaterial'),
    path('eliminarMaterial/<int:id_material>/', views.eliminarMaterial, name='eliminarMaterial'),  # Eliminar 
    path('editarMaterial/<int:id_material>/', views.editarMaterial, name='editarMaterial'),  # Editar material
    path('procesarEdicionMaterial/', views.procesarEdicionMaterial, name='procesarEdicionMaterial'),

    path('nuevoDistribuidor/', views.nuevoDistribuidor, name='nuevoDistribuidor'),
    path('listadoDistribuidor/', views.listadoDistribuidor, name='listadoDistribuidor'),
    path('guardarDistribuidor/', views.guardarDistribuidor, name='guardarDistribuidor'),
    path('eliminarDistribuidor/<int:id_dist>/', views.eliminarDistribuidor, name='eliminarDistribuidor'),  # Eliminar 
    path('editarDistribuidor/<int:id_dist>/', views.editarDistribuidor, name='editarDistribuidor'),  # Editar distribuidor
    path('procesarEdicionDistribuidor/', views.procesarEdicionDistribuidor, name='procesarEdicionDistribuidor'),
    path('nuevoAlmacen/', views.nuevoAlmacen, name='nuevoAlmacen'),
    path('listadoAlmacen/', views.listadoAlmacen, name='listadoAlmacen'),
    path('guardarAlmacen/', views.guardarAlmacen, name='guardarAlmacen'),
    path('eliminarAlmacen/<int:id_alm>/', views.eliminarAlmacen, name='eliminarAlmacen'),  # Eliminar 
    path('editarAlmacen/<int:id_alm>/', views.editarAlmacen, name='editarAlmacen'),  # Editar almacen
    path('procesarEdicionAlmacen/', views.procesarEdicionAlmacen, name='procesarEdicionAlmacen'),

    path('nuevoPedido/', views.nuevoPedido, name='nuevoPedido'),
    path('listadoPedido/', views.listadoPedido, name='listadoPedido'),
    path('guardarPedido/', views.guardarPedido, name='guardarPedido'),
    path('eliminarPedido/<int:id_pedido>/', views.eliminarPedido, name='eliminarPedido'),  # Eliminar 
    path('editarPedido/<int:id_pedido>/', views.editarPedido, name='editarPedido'),
    path('procesarEdicionPedido/', views.procesarEdicionPedido, name='procesarEdicionPedido'),

 
]