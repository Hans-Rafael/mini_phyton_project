===========================================
  SiGePro - Sistema de Gestión de Productos
  Versión: 1.0.0
  Autor: Hans Garcia
  Licencia: MIT
===========================================

DESCRIPCIÓN
-----------
SiGePro es una aplicación de consola desarrollada en Python que permite 
gestionar productos utilizando una base de datos SQLite. 
Está orientada a usuarios que necesitan llevar un control básico de stock 
e inventario, como estudiantes, pequeños comerciantes o para uso personal.

FUNCIONALIDADES
---------------
1. Registrar nuevos productos.
2. Visualizar todos los productos almacenados.
3. Modificar información de un producto mediante su ID.
4. Eliminar productos de la base de datos.
5. Buscar productos por ID, nombre o categoría.
6. Generar reportes de productos con bajo stock.

REQUISITOS DEL SISTEMA
----------------------
- Python 3.7 o superior.
- Sistema operativo: Linux, Windows o macOS.
- Permisos para crear/modificar archivos en el directorio del proyecto.

INSTRUCCIONES DE USO
--------------------
1. Abrir una terminal o consola.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar el archivo principal con el siguiente comando:

   python main.py

ESTRUCTURA DEL PROYECTO
------------------------
- main.py .............. Archivo principal de ejecución.
- mod_backend.py ....... Funciones de lógica, validaciones y acceso a base de datos.
- mod_frontend.py ...... Funciones visuales: menús, tablas, impresión.
- data.db .............. Base de datos SQLite.
- README.txt ........... Este archivo.

RECOMENDACIONES
---------------
- Ingresar solo datos válidos (el sistema valida pero es importante ser preciso).
- No editar directamente la base de datos (data.db) con otros programas.
- Hacer una copia de seguridad de la base de datos periódicamente si contiene datos importantes.

SITIO DEL PROYECTO
------------------
Este proyecto se encuentra alojado en GitHub:

https://github.com/Hans-Rafael/python_tfi

FUTURAS MEJORAS
---------------
- Versión con interfaz gráfica (Tkinter o PyQt).
- Exportación de reportes a PDF o Excel.
- Versión instalable en Windows (.exe).

LICENCIA
--------
Este programa está bajo Licencia MIT. 
Esto significa que podés usarlo, copiarlo, modificarlo y distribuirlo libremente,
siempre que mantengas los créditos al autor original.

===========================================
          Gracias por utilizar SiGePro
===========================================
