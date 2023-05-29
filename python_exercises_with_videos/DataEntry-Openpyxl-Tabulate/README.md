
--- VIDEO YOUTUBE---
https://www.youtube.com/watch?v=yMCaeXwh10M&t=59s&ab_channel=GEZ-DB

DESCRIPCIÓN PROGRAMA:

El código proporcionado es un programa que permite ingresar y almacenar información sobre ventas, productos y pagos en un archivo Excel utilizando la librería openpyxl. Aquí tienes una descripción de lo que hace el código paso a paso:

El programa carga un archivo Excel llamado "Libro1.xlsx" utilizando openpyxl.
Verifica si el número de venta base existe en la celda B1 del archivo. Si no existe, solicita al usuario que ingrese el número de venta base y lo guarda en la celda B1.
Define varias constantes y variables para el formato de las celdas y el seguimiento de las ventas, productos y pagos ingresados.
Inicia un bucle while que permite al usuario ingresar varias ventas.
Dentro del bucle, se solicita al usuario que ingrese información sobre la venta, como el número de venta, fecha, plataforma de venta, nombre del comprador, etc. Estos valores se guardan en las celdas correspondientes del archivo Excel.
A continuación, se le pregunta al usuario si desea agregar productos al pedido. Si la respuesta es "SI", se solicita información sobre cada producto, como descripción, precio unitario y cantidad. Estos valores se guardan en las celdas correspondientes del archivo Excel.
Después de ingresar los productos, se le pregunta al usuario sobre el costo de envío, que se guarda en el archivo Excel.
Luego, se le pregunta al usuario si desea ingresar pagos del comprador. Si la respuesta es "SI", se solicita información sobre cada pago, como el monto y los códigos de operación y medio de pago. Estos valores se guardan en las celdas correspondientes del archivo Excel.
Una vez que se han ingresado todos los datos de la venta, se le pregunta al usuario si la venta ha sido facturada, y esta información se guarda en el archivo Excel.
Se guarda el archivo Excel con los datos ingresados.
El bucle vuelve al paso 5 si el usuario desea ingresar otra venta. De lo contrario, el programa finaliza.
En resumen, este código es un programa para ingresar información detallada sobre ventas, productos y pagos en un archivo Excel, lo cual puede ser útil para llevar un registro y realizar seguimiento de las transacciones comerciales.
