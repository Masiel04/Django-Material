from django.shortcuts import render
from django.shortcuts import  redirect, get_object_or_404
from django.contrib import messages
from .models import Material, Distribuidor, Almacen, Pedido

# Create your views here.
def inicio(request):
    return render (request, 'inicio.html')

def nuevoMaterial(request):
    return render(request, 'nuevoMaterial.html')

def listadoMaterial(request):
    materiales = Material.objects.all()
    return render(request, 'listadoMaterial.html', {'materiales': materiales})

def guardarMaterial(request):
    nombre = request.POST['txt_nombre']
    descripcion = request.POST['txt_descripcion']
    unidad_medida = request.POST['txt_unidad_medida']
    precio_unitario = request.POST['txt_precio_unitario']
    foto_mat = request.FILES.get("foto_mat")

    nuevo_material = Material.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        unidad_medida=unidad_medida,
        precio_unitario=precio_unitario,
        foto_mat=foto_mat
    )
    messages.success(request, "Material guardado con éxito")

    return redirect('/listadoMaterial')

def eliminarMaterial(request, id_material):
    material_eliminar = get_object_or_404(Material, id_material=id_material)
    material_eliminar.delete()
    messages.success(request, "Material Eliminado con éxito")
    return redirect('/listadoMaterial')

def editarMaterial(request, id_material):
    material_editar = get_object_or_404(Material, id_material=id_material)
    return render(request, 'editarMaterial.html', {'material': material_editar})

def procesarEdicionMaterial(request):
    material = get_object_or_404(Material, id_material=request.POST['id_material'])

    print(f"Precio recibido: {request.POST['txt_precio_unitario']}")  # Agregar para depuración

    material.nombre = request.POST['txt_nombre']
    material.descripcion = request.POST['txt_descripcion']
    material.unidad_medida = request.POST['txt_unidad_medida']
    material.precio_unitario = request.POST['txt_precio_unitario']

    if 'foto_mat' in request.FILES:
        material.foto_mat = request.FILES['foto_mat']

    material.save()
    messages.success(request, "Material actualizado con éxito")
    return redirect('/listadoMaterial')

def nuevoDistribuidor(request):
    return render(request, 'nuevoDistribuidor.html')

# Vista para listar los distribuidores
def listadoDistribuidor(request):
    distribuidores = Distribuidor.objects.all()
    return render(request, 'listadoDistribuidor.html', {'distribuidores': distribuidores})

# Vista para guardar un nuevo distribuidor
def guardarDistribuidor(request):
    nombre = request.POST['txt_nombre']
    direccion = request.POST['txt_direccion']
    telefono = request.POST['txt_telefono']
    email = request.POST['txt_email']

    nuevo_distribuidor = Distribuidor.objects.create(
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        email=email
    )
    messages.success(request, "Distribuidor guardado con éxito")

    return redirect('/listadoDistribuidor')

# Vista para eliminar un distribuidor
def eliminarDistribuidor(request, id_dist):
    distribuidor_eliminar = get_object_or_404(Distribuidor, id_dist=id_dist)
    distribuidor_eliminar.delete()
    messages.success(request, "Distribuidor Eliminado con éxito")
    return redirect('/listadoDistribuidor')

# Vista para editar un distribuidor
def editarDistribuidor(request, id_dist):
    distribuidor_editar = get_object_or_404(Distribuidor, id_dist=id_dist)
    return render(request, 'editarDistribuidor.html', {'distribuidor': distribuidor_editar})

# Vista para procesar la edición de un distribuidor
def procesarEdicionDistribuidor(request):
    distribuidor = get_object_or_404(Distribuidor, id_dist=request.POST['id_dist'])

    distribuidor.nombre = request.POST['txt_nombre']
    distribuidor.direccion = request.POST['txt_direccion']
    distribuidor.telefono = request.POST['txt_telefono']
    distribuidor.email = request.POST['txt_email']

    distribuidor.save()
    messages.success(request, "Distribuidor actualizado con éxito")
    return redirect('/listadoDistribuidor')

def nuevoAlmacen(request):
    return render(request, 'nuevoAlmacen.html')

# Vista para listar los almacenes
def listadoAlmacen(request):
    almacenes = Almacen.objects.all()
    return render(request, 'listadoAlmacen.html', {'almacenes': almacenes})

# Vista para guardar un nuevo almacén
def guardarAlmacen(request):
    nombre = request.POST['txt_nombre']
    direccion = request.POST['txt_direccion']
    capacidad = request.POST['txt_capacidad']

    nuevo_almacen = Almacen.objects.create(
        nombre=nombre,
        direccion=direccion,
        capacidad=capacidad
    )
    messages.success(request, "Almacén guardado con éxito")

    return redirect('/listadoAlmacen')

# Vista para eliminar un almacén
def eliminarAlmacen(request, id_alm):
    almacen_eliminar = get_object_or_404(Almacen, id_alm=id_alm)
    almacen_eliminar.delete()
    messages.success(request, "Almacén Eliminado con éxito")
    return redirect('/listadoAlmacen')

# Vista para editar un almacén
def editarAlmacen(request, id_alm):
    almacen_editar = get_object_or_404(Almacen, id_alm=id_alm)
    return render(request, 'editarAlmacen.html', {'almacen': almacen_editar})

# Vista para procesar la edición de un almacén
def procesarEdicionAlmacen(request):
    almacen = get_object_or_404(Almacen, id_alm=request.POST['id_alm'])

    almacen.nombre = request.POST['txt_nombre']
    almacen.direccion = request.POST['txt_direccion']
    almacen.capacidad = request.POST['txt_capacidad']

    almacen.save()
    messages.success(request, "Almacén actualizado con éxito")
    return redirect('/listadoAlmacen')

def nuevoPedido(request):
    materiales = Material.objects.all()
    distribuidores = Distribuidor.objects.all()
    return render(request, 'nuevoPedido.html', {
        'materiales': materiales,
        'distribuidores': distribuidores
    })

def listadoPedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'listadoPedido.html', {'pedidos': pedidos})

def guardarPedido(request):
    material_id = request.POST['material']
    distribuidor_id = request.POST['distribuidor']
    cantidad = request.POST['cantidad']
    estado = request.POST['estado']

    # Obtener los objetos relacionados usando los campos correctos
    material = get_object_or_404(Material, id_material=material_id)  # Cambia 'id' por 'id_material'
    distribuidor = get_object_or_404(Distribuidor, id_dist=distribuidor_id)  # Cambia 'id' por 'id_dist'

    # Crear un nuevo pedido
    nuevo_pedido = Pedido.objects.create(
        material=material,
        distribuidor=distribuidor,
        cantidad=cantidad,
        estado=estado
    )
    messages.success(request, 'Se ha guardado el Pedido')
    return redirect('/listadoPedido')


def eliminarPedido(request, id_pedido):
    pedido = Pedido.objects.get(id_pedido=id_pedido)
    pedido.delete()
    messages.success(request, "Pedido eliminado")
    return redirect('/listadoPedido')

def editarPedido(request, id_pedido):
    # Obtener el pedido que se va a editar
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    
    # Obtener los materiales y distribuidores disponibles
    materiales = Material.objects.all()
    distribuidores = Distribuidor.objects.all()

    return render(request, 'editarPedido.html', {
        'pedido': pedido,
        'materiales': materiales,
        'distribuidores': distribuidores
    })

def procesarEdicionPedido(request):
    # Obtener el pedido que se va a editar por su ID
    pedido = Pedido.objects.get(id_pedido=request.POST['id_pedido'])

    # Actualizar los campos del pedido con los datos del formulario
    pedido.cantidad = request.POST['cantidad']
    pedido.fecha_pedido = request.POST['fecha_pedido']

    # Obtener el material seleccionado y asignarlo al pedido
    id_material = request.POST['material']
    material = get_object_or_404(Material, id_material=id_material)
    pedido.material = material

    # Obtener el distribuidor seleccionado y asignarlo al pedido
    id_distribuidor = request.POST['distribuidor']
    distribuidor = get_object_or_404(Distribuidor, id_dist=id_distribuidor)
    pedido.distribuidor = distribuidor

    # Actualizar el estado del pedido
    pedido.estado = request.POST['estado']

    # Guardar los cambios en el pedido
    pedido.save()

    # Mensaje de éxito y redirigir a la lista de pedidos
    messages.success(request, "Pedido actualizado con éxito")
    return redirect('/listadoPedido')
