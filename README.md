# TP PRE-ENTREGA 3

Autor: Lucas De Maio
Nombre: Tercer Pre-Entrega De Maio

Objetivo del TP:
Desarrollo de una Web en Django de una Concesionaria de Autos y Motos
1. Herencia de HTML:
    Todos los forms se encuentran heredados de "base.html"
    
2. Models:
    1-class Auto(models.Model)
    2-class Moto(models.Model)
    3-class Empleado(models.Model)
    4-class Cliente(models.Model)

3.  Formularios para insertar datos:
    1- Se creó un formulario para Cargar nuevos Autos
    2- Se creó un formulario para Cargar nuevas Motos
    3- Se creó un formulario para Cargar nuevos Empleados
    4- Se creó un formulario para Cargar nuevos Clientes

4.  Formularios para busqueda:
    1- Se creó un formulario para Busqueda/filtro de Autos segun su Marca
    2- Se creó un formulario para Busqueda/filtro de Motos segun su Marca

5. Menu de Administracion
    user: admin
    Clave: 1234

6. Como probar:
    1. Ingresar a http://127.0.0.1:8000/aplicacion
    2. Ingresar a "Autos" en la barra de navegacion
    3. Se mostraran todos los autos disponibles
    4. Utilizar el boton "Filtrar autos por Marca" para la busqueda, o el boton "Dar de alta nuevo Auto" para cargar en la base de Datos un nuevo auto.
    5. Dar click en "Inicio" para volver a la pagina principal
    6. Ingresar a "Motos" en la barra de navegacion
    7. Se mostraran todas las motos disponibles
    8. Utilizar el boton "Filtrar motos por Marca" para la busqueda, o el boton "Dar de alta nueva Moto" para cargar en la base de Datos una nueva moto.
    9. Dar click en "Inicio" para volver a la pagina principal
    10. Ingresar a "Empleados" en la barra de navegacion
    11. Se mostraran todos los empleados
    12. Utilizar el boton "Dar de alta nuevo Empleado" para cargar en la base de Datos un nuevo Empleado
    13. Dar click en "Inicio" para volver a la pagina principal
    14. Ingresar a "Clientes" en la barra de navegacion
    15. Se mostraran todos los Clientes
    16. Utilizar el boton "Dar de alta nuevo Cliente" para cargar en la base de Datos un nuevo Cliente
    17. Dar click en "Inicio" para volver a la pagina principal
    18. Ingresar a "Administracion" en la barra de navegacion con user y clave detallado en punto "5. Menu de Administracion"

7.  URLS:
    Inicio: http://127.0.0.1:8000/aplicacion
    Autos: http://127.0.0.1:8000/aplicacion/autos
    Motos: http://127.0.0.1:8000/aplicacion/motos
    Empleados: http://127.0.0.1:8000/aplicacion/empleados
    Clientes: http://127.0.0.1:8000/aplicacion/clientes
    Busqueda de Autos: http://127.0.0.1:8000/aplicacion/buscar_autos
    Dar de alta Auto: http://127.0.0.1:8000/aplicacion/autos_form
    Busqueda de Motos: http://127.0.0.1:8000/aplicacion/buscar_motos
    Dar de alta Moto: http://127.0.0.1:8000/aplicacion/motos_form
    Empleados: http://127.0.0.1:8000/aplicacion/empleados
    Dar de alta Empleado: http://127.0.0.1:8000/aplicacion/empleados_form
    Clientes: http://127.0.0.1:8000/aplicacion/clientes
    Dar de alta Cliente: http://127.0.0.1:8000/aplicacion/clientes_form
    Menu de administracion: http://127.0.0.1:8000/admin/



    




