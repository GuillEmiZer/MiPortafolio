ZETATEC_DATA_BASE

Zeta Tec es un negocio e-commerce de venta por menor de metales no ferroso en línea que desea llevar registro de:
- Productos vendidos.
- Productos Comprados.
- Proveedores.
- clientes.
- pedidos y ventas. 
- Facturas y Notas de crédito. 
- Pagos y medios de pago. 
- Envíos y empresas de encomienda. 
- Cancelaciones y devoluciones.
- Total mensual facturado por jurisdicción(argentina).

* Para esta Base de Datos no se requiere ningún sistema de gestión de stock y tampoco ningún sistema de gestión de empleados. 

* Sí se espera tener información sobre qué se vende, a quiénes se les vende (y en qué momento del año), productos por mayor
comprados a proveedores, datos generales de los envíos para realizar seguimientos (si corresponde), generación de informes
mensuales de ventas para el contador, entre otros detalles que se especifican a continuación:

-----------------------------------------------------------------------------------------------------------------------------
CLIENTES: nombre completo, dni, cuit, dirección, condición frente a IVA. Dichos datos a parte de servir como identificación
del cliente, también sirven para facturación. Considerar que los datos de dni/cuit/direccion/condicion IVA pueden cambiar en
cada compra. 
-----------------------------------------------------------------------------------------------------------------------------
PROVEEDORES: nombre completo, CUIT, teléfono y dirección. 
-----------------------------------------------------------------------------------------------------------------------------
COMPRAS POR MAYOR: fecha de compra, dolar oficial, dolar paralelo, costo logístico, costo producción estimado, producto por
mayor adquirido, unidades, precio unitario en dólares (a cambio oficial, este dato puede no estar dispnible en cada compra), 
precio total del producto adquirido y kilogramos de material.
-----------------------------------------------------------------------------------------------------------------------------
PRODUCTOS: SKU del producto, nombre, formato del material, tipo de material, proveedor y precio. Sobre éste último considerar
que hay al menos tres listas de precios diferentes. 
-----------------------------------------------------------------------------------------------------------------------------
PEDIDOS Y VENTAS: fecha del pedido, fecha del cierre (venta), cliente, plataforma de venta (redes sociales, ecommerce),
jurisdiccion, descuentos generales al pedido/venta en porcentaje(si corresponde), descuento en importes fijos al pedido/venta
(si corresponde), productos vendidos (cantidades y precios) y descuentos en porcentaje y monto fijo por cada producto.
-----------------------------------------------------------------------------------------------------------------------------
PAGOS: Fecha, medio de pago, códigos de operación de plataformas externas (bancos, plataformas eccomerce,etc), monto.
-----------------------------------------------------------------------------------------------------------------------------  
FACTURACIÓN Y NOTAS DE CRÉDITO: numero de facturas y notas de créditos. 
-----------------------------------------------------------------------------------------------------------------------------
ENVIOS: número de seguimiento, empresa de encomienda, número de seguimiento, página web de seguimiento del envío.
-----------------------------------------------------------------------------------------------------------------------------
CANCELACIONES: Las cancelaciones se aplican generalmente a las ventas o a los pedidos. Es importante remarcar o incluir la
factura correspondiente en caso de que se haya emitido puesto que es necesario realizar la nota de crédito correspondiente. 

FIN















