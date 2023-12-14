Sitio web: ProComputers

El sitio cuenta con un total de 4 páginas cuyos contenidos se detallan a continuación.

Página principal
La página cuenta con 3 secciones principales: Encabezado, cuerpo y pie. Dentro del cuerpo hay 3 secciones: Banner, Nosotros e Iconos). El encabezado tiene 3 hipervínculos (Contactos, Empleados y Servicios), que se esconden cuando se achica la ventana. Cuando desaparecen los hipervínculos aparece el icono ≡ (hamburguesa), que al hacerle click, aparece un menu desplegable con los 3 Hipervínculos escondidos.

En la sección llamada Banner hay una imagen de fondo y un ::before, usado para la estética de la página. Se le aplicó a todo el Banner un comportamiento responsive para ajustar el alto del mismo en función del ancho de la pantalla (a partir de un ancho de 1000px).

En la sección llamada nosotros hay unos avatares que ilustran a los integrantes del emprendimiento, una descripción simbólica y un botón (ver Perfil) que lleva a la página principal de linkedin. Cada boton tiene la animacion que cambia de color de fondo y de la letra cuando pasamos el mouse por encima.

En el sector iconos, usamos los iconos de font awesome que corresponden a las redes sociales IG, FB TW y YT. cada una de los botones apunta a las redes sociales del programa codo a codo V4.0. Los iconos tienen la animación que cambia de tamaño cuando le pasamos el mouse por encima.

El footer está hecho en CSS.

Para todo el HTML se usaron fuentes de google fonts.

Página Empleados

La página tiene por finalidad la carga de empleados al sistema. Tiene un botón para cargar un nuevo empleado donde se despliega tipo tarjeta de identificación. En el campo edad, se puede ir cambiando de forma interactiva o se puede escribir directamente. En el campo fecha, se puede elegir desde un calendario y además se puede cargar una foto del empleado.

Una vez cargado el nuevo empleado, aparece en el listado de empleados, mostrando la información de todos los empleados cargados con anterioridad.

El header y el footer es el mismo que el de la página principal y el resto del sitio web.

Página Contacto

La página Contacts.html, despliega un formulario de contacto con tres campos, nombre, correo electrónico y comentarios y un botón con la etiqueta "enviar", para remitir los campos ingresados a una casilla de mail predefinida.

Con un script (funcion validarFormulario() en el archivo validacion.js), se validan los datos ingresados en los campos.

La función devuelve un bool (true si los campos ingresados son válidos), muestra un mensaje de error si los campos requeridos no se completan (o si los datos ingresados no cumplen ciertos criterios). Si el formulario es validado, se envían los datos ingresados por mail y se muestra un mensaje de confirmación que los datos han sido enviados y que próximamente tendrá una respuesta.

Los criterios de validación son, en caso de nombre y comentarios, un mínimo de tres caracteres, en el caso de mail, se usa verifica que no sea un string vacío y que no tenga determinados caracteres. Se usa en el caso del email el parámetro type="email", lo que fuerza una doble validación (la implementada en el código javascript y la implementada por el navegador).

Para el envío de los datos ingresados en los campos, se utiliza un servicio externo. Se descarga el implementar un servidor de correo en la aplicación por la complejidad, o usar un servidor de correo externo, porque habría que implementar una cuenta de mail y password dentro del código. En lugar, se utiliza un servicio externo, provisto por Formsubmit (https://formsubmit.co/), es un servicio que envía el contenido de un formulario, por email a una cuenta de correo (que está encriptada dentro del código).

Página Servicios
La página Servicios presenta información sobre diferentes asistencias en el ámbito de la tecnología a los clientes.

En el main del documento Servicios.html se dispone de un iframe de Google Maps con información de donde se ubica el local físico e información en texto sobre los servicios que brinda el emprendimiento.

Dispone de los mismos header y footer que el resto de las páginas. Todo aquello con el mismo comportamiento responsive.

Finalmente, realizamos una integración de lo trabajado mediante el framework Django de Python. Realizamos algunas templates base a partir de las cuáles completamos los archivos html propios de cada página del sitio web.
Manejamos todo mediante un entorno virtual para no complicar la compatibilidad de las librerías a utilizar.
Finalmente realizamos un deploy del sitio en la plataforma Pythonanywhere vinculandolo con lo trabajado y subido al presente repositorio. El link del sitio web deployado es el siguiente: https://francogal1.pythonanywhere.com/


Integrantes y funciones del grupo 28:

Sebastian Ulibarri (organización, contenido y desarrollo)
Gustavo San Martin (desarrollo y contenido)
Hector Fernandez (desarrollo, contenido y diseño)
Franco Galgano ( organización, desarrollo y diseño)
