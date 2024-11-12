# Trabajo Practico de Laboratorio de la catedra Diseño 3  del año 2024
# Panaderia El Maná

## Para tener en cuenta:
### No se toma en cuenta la gestion de permisos desde el administrador de django. En su lugar he creado un archivo llamado decorators.py en donde creo 
### un par de funciones que suplantan parcialmente la gestion de permisos del administrador de django.
### En ambas funciones, primeramente verifica que se acceda tras haber logeado en el sitio, luego comprueba los perfiles (campo de Emplado destinado a
### identificar el rol que cumple), si no cumple el requisito de perfil sera redireccionado al inicio.
### Para el caso del perfil vendedor, en las vistas donde no tiene restricciones solamente se añade el decorador login_required, redireccionando
### a la vista de login en caso de no haber iniciado session.


## acciones disponibles segun seccion:
### Proveedores:
#### Alta Baja Modificacion de Proveedor, asignando los insumos que suministra
#### Creacion, Cancelacion y Recepcion de Pedidos, cambiando el estado: pendiente, cancelado, recibido
#### En cada pedido puede seleccionarse solo un proveedor, de su proveedor se mostraran los insumos que suministra pudiendo seleccionarlos a todos
#### y la cantidad de cada uno
#### Al recepcionar un pedido, se muestran todos los insumos pedidos y su cantidad, puede ingresarse la cantidad recibida que puede diferir de la pedida
#####(nota: en proxima actualizacion, la diferencia de la cantidad debe ser listada automaticamente en el campo observacion)
#### Al recepcionar un pedido, la cantidad de los insumos recibidos se agregan al stock actual del insumo correspondiente

### Productos:
#### Alta Baja y Modificacion de Productos, incluye modificacion de stock (Se agrega al existente, no suplanta) y modificacion de precio para la venta
#### Alta Baja de insumos, pudiendo agregar stock de forma manual

### Ventas:
#### Ver productos para la venta separados por categoria y subcategorias. Si no hay stock de producto, no se mostrara. la cantidad agregada al carrito
#### no puede superar su stock.
#### Agregar producto al carrito, modificando la cantidad desde la tarjeta del producto y no desde el carrito. Si el producto ya existe en el carrito, 
#### se aumenta la cantidad segun este declarado en la card del producto.

#### Quitar un producto del carrito.
#### En el carrito, por cada producto se mostrar el subtotal segun la cantidad del producto.
#### Desde el carrito se puede generar el comprobante de venta, seleccionando el tipo de pago, tipo de comprobante y forma de pago, se listan los productos agregados
#### al carrito con su subtotal, y total del carrito.
#### Al guardar el comprobante se guarda un registro de venta, vinculando el comprobante y el vendedor

### informes:
#### se puede visualizar el listado de productos mas vendido y su cantidad (no el precio total)
#### se pede visualizar el listado de insumos faltantes, considerado faltante si el stock esta por debajo o igual al punto de pedido
#### se puede visualizar el listado de ventas filtrado por fechas (mostrando solo la fecha, el vendedor y el valor total de venta)
#### Se puede exprotar en pdf, xlsx y csv cada informe



## Listado de acciones por roles:
## Administrador:
### todo las acciones disponibles

## Gerente:
### todas las acciones disponibles salvo:
#### Baja de producto, Baja de insumo

## Vendedor:
### todas las acciones en ventas
#### visualizar informacion de productos, insumos, proveedores.
#### Recepcionar pedidos
#### no puede visualizar informes
