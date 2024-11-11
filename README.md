# Trabajo Practico de Laboratorio de la catedra Diseño 3  del año 2024
# Panaderia El Maná

## acciones disponibles segun seccion:
## Proveedores:
### Alta Baja Modificacion de Proveedor, asignando los insumos que suministra
### Creacion, Cancelacion y Recepcion de Pedidos, cambiando el estado: pendiente, cancelado, recibido
### Al recepcionar un pedido, la cantidad de los insumos se agregan al stock actual del insumo correspondiente

## Productos:
### Alta Baja y Modificacion de Productos, incluye modificacion de stock (Se agrega al existente, no suplanta) y modificacion de precio para la venta
### Alta Baja de insumos, pudiendo agregar stock de forma manual

## Ventas:
### Ver productos para la venta separados por categoria y subcategorias. Si no hay stock de producto, no se mostrara.
### Agregar producto al carrito, modificando la cantidad desde la tarjeta del producto y no desde el carrito. Si el producto ya existe en el carrito, 
### se aumenta la cantidad segun este declarado en la tarjeta.
### Quitar un producto del carrito.
### En el carrito, por cada producto se mostrar el subtotal segun la cantidad del producto. No el total del carrito (falta agregar esa funcionalidad usando js)
### Desde el carrito se puede generar el comprobante de venta, seleccionando el tipo de pago, tipo de comprobante y forma de pago, se listan los productos agregados
### al carrito y su subtotal, mas no el total del carrito.

### Al guardar el comprobante, se actualiza el total del comprobante con el valor correspondiente, y se guarda un registro de venta, vinculando el comprobante y el vendedor

## informes:
### se puede visualizar el listado de productos mas vendido y su cantidad (no el precio total)
### se pede visualizar el listado de insumos faltantes, considerado faltante si el stock esta por debajo o igual al punto de pedido
### se puede visualizar el listado de ventas filtrado por fechas (mostrando solo la fecha, el vendedor y el valor total de venta)
### Se puede exprotar en pdf, xlsx y csv cada informe



## Listado de acciones por roles:
## Administrador:
### todo las acciones disponibles

## Gerente:
### todas las acciones disponibles salvo:
#### Baja de producto, Baja de insumo

## Vendedor:
### todas las acciones en ventas
### visualizar informacion de productos, insumos, proveedores.
### Recepcionar pedidos
### no puede visualizar informes
