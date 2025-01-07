# ExamenPOO
Examen Programación Orientada a Objetos -  Segundo semestre Ingeniería en informática Inacap.

Desarrollo de Proyecto: Sistema de Reservas de Hoteles
Objetivo:
Desarrollar un proyecto en Python que implemente un sistema de reservas de hoteles utilizando la arquitectura MVC (Model-View-Controller). El proyecto debe organizarse en carpetas y clases que permitan gestionar la información de habitaciones, tipos de habitaciones y hoteles, siguiendo la estructura especificada.
Estructura del Proyecto:
El proyecto debe contener las siguientes carpetas:
1.	Model:
-	Clases que representan las entidades principales del sistema:
	Hotel: Almacena la información de los hoteles.
	TipoHabitacion: Representa los tipos de habitaciones (ej. individual, doble, suite).
	Habitación: Representa las habitaciones disponibles en los hoteles.
2.	View:
-	Contiene la interfaz del usuario, implementada como una consola interactiva que permita gestionar distintas opciones para el usuario.

3.	Controller:
o	Clases responsables de realizar las operaciones sobre la base de datos:
	HotelDAO: Maneja las consultas relacionadas con los hoteles.
	TipoHabitacionDAO: Administra las consultas relacionadas con los tipos de habitaciones.
	HabitacionDAO: Gestiona las consultas relacionadas con las habitaciones.
4.	Database:
-	Conexion: Clase encargada de conectar a una base de datos MySQL.
5.	Services:
-	Clases que ofrecen servicios adicionales:
	CurrencyService: Obtiene el valor del dólar desde una API para calcular los precios de las habitaciones en dólares.
 
Funcionalidades Solicitadas
1.	Listar hoteles con sus habitaciones y tipos:
-	Mostrar todos los hoteles disponibles junto con sus habitaciones y el tipo de cada habitación.
2.	Registrar un nuevo hotel con sus habitaciones y tipos:
-	Permitir agregar un hotel e incluir información sobre las habitaciones y los tipos asociados.
3.	Buscar hotel:
-	Buscar un hotel por su nombre o dirección y listar sus habitaciones.
4.	Agregar una habitación a un hotel existente:
-	Permitir registrar una nueva habitación en un hotel existente, indicando su tipo.
5.	Eliminar una habitación:
-	Eliminar una habitación específica identificada por su número.
6.	Mostrar precios en dólares:
-	Utilizar una clase CurrencyService que consulte una API para obtener el valor del dólar y calcular el precio de las habitaciones en dólares.
Requisitos:
-	Implementar el sistema en Python utilizando MySQL como gestor de base de datos.
-	Seguir el modelo de arquitectura MVC, respetando la separación de responsabilidades.
-	Documentar el código adecuadamente.
-	Implementar un menú interactivo en la consola para realizar las operaciones principales.
-	Aplicar las reglas de negocio correspondientes para que el sistema funcione correctamente a pesar del ingreso de valores incorrectos
-	Manejar excepciones 
-	El script de la base de datos no puede ser modificado.
Entregables:
1.	Código fuente del proyecto organizado en carpetas según la estructura MVC.
 
Evaluación:
-	Correcta implementación de la arquitectura MVC.
-	Funcionamiento del menú interactivo.
-	Conexión y consultas exitosas a la base de datos.
-	Modularidad y claridad del código.
¡Buena suerte con tu proyecto!
