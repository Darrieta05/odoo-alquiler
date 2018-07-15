# odoo-alquiler
Modulo de alquileres para Odoo

###limitaciones generales:
Lastimosamente la documentación inicial y el tiempo no me fue suficiente para acabar con todos los puntos de la aplicación.

Considero que con la capacitación adecuada y in impulso leve en cuanto a cómo buscar información es posible hacer esta app en aproximadamente 5 o 6 horas íntegras una vez que se tenga la experiencia apropiada.

###Opciones de mejora:

- diseño unico
- integración con sistemas aparte
- manejo de facturas y usuarios
- reporte de alquiler
- envío de correo una vez que se acerca la fecha de pago de alquiler
- manejo de morosos
- lista de alquiler por usuario
- beneficios para usuario
- descuentos
- ofertas en alquileres
- edificios premium




#Secciones del app

##Alquileres

###vista
Contiene los campos de:

- Identificación del documento
- Fecha de modificación
- Fecha de Creación
- Usuario que alquiló

###formulario
Involucra los siguientes elementos:

- usuario que alquila
- monto mensual
- monto de mantenimiento
- fecha de inicio
- decha de fin
- porcentaje de aumento
- lista de los locales asignados al alquiler

####limitaciones
Se intentó involucrar la factua y la lista de facturas pero no se encontró documentación para realizar la integración

##Locales

###vista
Contiene los campos de:

- Numero de local
- Edificio Asignado
- Numero de piso

###formulario
Involucra los siguientes elementos:

- numero de local
- area en m2
- id de luz
- id de agua
- numero de documento de alquiler
- edificio asignado
- piso asignado

####limitaciones
N/A

###Edificios

###vista
Contiene los campos de:

- Nombre del edificio
- Pisos asignados

###formulario
Involucra los siguientes elementos:

- Nombre del edificio
- dirreción
- area de terreno
- area de construcción
- pisos asignados

####limitaciones
N/A

###Pisos

###vista
Contiene los campos de:

- Nombre del piso
- Numero de piso
- Nombre del edificio asignado

###formulario
Involucra los siguientes elementos:

- usuario que alquila
- monto mensual
- monto de mantenimiento
- fecha de inicio
- decha de fin
- porcentaje de aumento
- lista de los locales asignados al alquiler

####limitaciones
N/A














