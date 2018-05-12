# Interfaz gráfica
En esencia, SimuladorQ está compuesto por una ventana principal, en la que se establecen los modelos de colas (según Kendall) disponibles para simular, los cuales son M/M/1, M/G/1 y M/M/1/K. 
![Ventana Principal](https://raw.githubusercontent.com/maxxxis182/trafico/master/docs/img/principal.png "Ventana Principal")

Una vez elegido el modelo, nos envía a la siguiente ventana, donde podemos ingresar los parámetros de entrada del modelo elegido. 
Se puede dividir esta pantalla en varias secciones, las cuales describiremos detalladamente a continuación. 

## Parámetros de entrada

En esta sección es donde ingresamos las características principales de cada uno de los modelos dispuestos. 

### Modelo M/M/1:
![Ventana Secundaria](https://raw.githubusercontent.com/maxxxis182/trafico/master/docs/img/mm1.png "Ventana Secundaria")

- Tasa de arribos $\lambda$, medida en $\frac{bytes}{seg}$
- Tasa de servicio $\mu$, medida $\frac{bytes}{seg}$
- Usuario, identificación del cliente
- Bitrate de salida, medida en $bps$ o bien $\frac{bit}{seg}$ 
- Tiempo de simulación, medido en $seg$. 
- Bins, para generar histogramas con los resultados. Los valores disponibles son 50, 100, 150 y 200, para elección del usuario.
	 
### Modelo M/G/1:
![Ventana Secundaria](https://raw.githubusercontent.com/maxxxis182/trafico/master/docs/img/mg1.png "Ventana Secundaria")

- Tasa de arribos $\lambda$
 - Distribución de probabilidad general, las disponibles son Normal y Uniforme. La primera necesita los siguientes parámetros Media $\mu$ y Desviación estándar $\sigma$. La segunda, necesita Limite inferior y superior.
- Usuario
- Bitrate de salida
- Tiempo de simulación
- Bins
 	 
### Modelo M/M/1/K:

![Ventana Secundaria](https://raw.githubusercontent.com/maxxxis182/trafico/master/docs/img/mm1k.png "Ventana Secundaria")

- Tasa de arribos $\lambda$
- Media de paquetes (o servicio) $\mu$
- Largo de cola K. Los valores disponibles van de 10 en 10 hasta 100.
- Usuario
- Bitrate de salida
- Tiempo de simulación
- Bins
	 
Una vez determinados los parámetros, se puede efectuar la simulación presionando el botón *Simular*, o bien, con el botón *Reset* se pueden borrar los mismo para ingresarlos nuevamente. Ambos botones se encuentran debajo de la zona de ingreso de valores.

## Parámetros de salida
Para todos los modelos, las variables de salida de la simulación realizada son:

 - Paquetes enviados
 - Paquetes servidos
 - Paquetes perdidos
- Porcentaje de pérdida
 - Intensidad de tráfico $\rho$
 - Número medio de bytes en la cola $L$
 - Número medio de bytes en el sistema $L_q$
 - Tiempo medio de espera $W$, medido en $seg$
 - Tiempo medio de espera en la cola $W_{q}$, medido en $seg$

## Detalle de los paquetes servidos
En esta sección, se puede identificar los paquetes que han sido enviados y que lograron servirse. La información que está disponible de cada paquete es:

 - **Id:** Identificador único, para diferenciar un paquete de cualquier otro.
 - **Source *(src)*:** Nombre, dirección, o información para identificar la fuente de tráfico, o bien el cliente. Es el mismo que se ingresó en la línea *Usuario* de la sección *parámetros de entrada*.
 - **Time:** Tiempo, medido desde el comienzo de la simulación, en el cual el paquete fue creado. 
 - **Size:** Tamaño del paquete servido, medido en $bytes$.
 
## Histogramas

Se utilizan histogramas para poder observar mejor el comportamiento del sistema elegido. Los bins que se ingresan en la entrada son los que afectan la cantidad de barras que se estarán mostrando en el eje temporal. Estos definen la cantidad de intervalos de la variable temporal. Podemos decir que la resolución de un histograma es proporcional a la cantidad de bins.

Al inicio del programa sólo se observa el logo del mismo, pero al momento de finalizar una simulación correctamente, el primer gráfico que se observa por defecto es el de *Tiempos de espera*, con una *frecuencia de ocurrencia* normalizada. Luego, el usuario puede cambiar de histograma con las opciones que se encuentran debajo, y además, elegir si desea verlo en un formato normalizado o no, de acuerdo al análisis que le parezca más conveniente. Cuando hablamos de normalización en los histogramas no pretendemos que la altura máxima de las barras sean la unidad, sino que el área debajo de la curva sea uno.

Las opciones de histogramas son:

 - Tiempos de espera
 - Tiempos de ocupación del sistema
 - Tiempos de ínter-arribo a la cola

## Menú y acciones
Por encima de las secciones antes mencionadas se encuentra el menú del programa. Las opciones de menú y acciones son:

### Archivo
- *Regresar a la pantalla principal*: Permite volver a la ventana inicial, donde se puede escoger los modelos disponibles de simulación.
- *Reiniciar*: Borra la información generada o introducida en todos las secciones, volviendo al estado inicial.
- *Importar datos*: Permite seleccionar un archivo previamente generado que solo contiene datos de ingreso para poder realizar una simulación.
- *Guardar:*
	- Parámetros de entrada. Sirve para posteriormente poder importarlos y realizar una simulación.
	- Parámetros de salida. Contiene información de los valores de entrada, y su salida correspondiente.
	-  Información de secuencia de paquetes. Contiene información de los valores de entrada, y el detalle de los paquetes servidos (visto en la sección *Detalle de los paquetes servidos*). Se debe darle un nombre y escoger el directorio donde se va a guardar.
	- Todo. Genera una carpeta, llamada *SimuladorQ-MODELO __ hora _ fecha,* que contiene un archivo con la información de los parámetros de entrada, de salida y el detalle de los paquetes servidos. Ademas crea una carpeta dentro con el nombre *Gráficos - SimuladorQ_ fecha_hora* que contiene los histogramas del modelo simulado, tanto normalizados, como no normalizados.

En todos los casos que se generen archivos, se debe escoger el nombre y el directorio donde se guardarán. Salvo los histogramas, todos los archivos tienen una extensión propia del programa, la cual es *.siq* (por SimuladorQ). Por ejemplo: `parametros_entrada.siq`. Esto es así, salvo que se indique lo contrario al ingresar el nombre del archivo a generar (*.txt* es recomendado también, disponible para elección) Los gráficos tienen una extensión por defecto *.png* . 

### Simulación
 - Correr simulación
 - Resetear parámetros
	 
### Ayuda
 - Documentación
	- Sobre Python
	- Sobre PyQt
	- Librerías utilizadas
		- Simpy
	 - Información Adicional
		 - Tutorial Python
		 - Tutorial PyQt
		 - Generadores y corutinas
 - Acerca de SimuladorQ

	
## Posibles errores de uso

Para empezar, el uso esta destinado a personas que ya tienen un conocimiento previo en el análisis de colas. Es decir, que si bien la entrada de valores para la simulación es libre, existen rangos o limites al momento de simular. El objetivo es tratar de representar los escenarios de la manera mas cercana la realidad que se pueda, por eso es que algunas veces, con determinados parámetros de entrada, el usuario puede incurrir en errores y concretar una simulación. Los errores comunes pueden ser, según cada modelo:

 - **Errores por falta de permisos.** Sucede cuando intentamos guardar parámetros o resultados en archivos *.siq* o *.txt* en directorios en los cuales no tenemos acceso para leer (*r*), escribir (*w*) o ejecutar (*x*). Esto depende del usuario que ejecute el software y el alcance de permisos *(r, w, x)* que tenga. Sucede lo mismo cuando deseamos exportar toda la simulación con el menú: *Archivo -> Guardar -> Todo*, que genera una nueva carpeta con información de la simulación realizada. Si no tenemos los permisos necesario para determinar el lugar donde se va a crear la carpeta, se nos avisará con un mensaje de error.
  
 - **Errores de no simulación.** Sucede cuando pretendemos guardar parámetros o algún aspecto de la simulación pero no la hemos realizado aun. Puede suceder también si en el medio de la simulación ocurrió un imprevisto y no se termino de realizar correctamente. Es necesario revisar las entradas, y modificarlas dentro de los rangos establecidos.
 
 - **Errores por falta de parámetros de entrada.** Ninguna simulación puede ejecutarse si no están correctamente seteados los parámetros de entrada. SimuladorQ no omite ningún parámetro, ni tampoco tiene entradas por defecto para obviar el defecto en ellas.

 - **Errores por ingreso incorrecto de parámetros de entrada.** Cuando incurrimos en estos tipos de error, el software nos lo advierte con un mensaje de error, con los alcances del parámetro y las recomendaciones correspondientes para solucionarlo. Varían de modelo a modelo y generalmente tiene que ver con la matemática del calculo de la simulación. Por eso, también recomendamos la lectura de la bibliografía, la teoría sobre colas, y la documentación del programa para facilitar el uso.
 
 - **Errores externos y otros errores.** Pueden ocurrir otros errores que no estén previstos, ya sea por deficiencia en las librerías (actualización o desactualización de las mismas, error de instalación, etc), borrado accidental de componentes, y demás cosas ajenas que atenten con el correcto funcionamiento. Ante estas situaciones, SimuladorQ puede capturar en un mensaje de error la salida de la terminal de Python y dar detalle de lo ocurrido. No garantizamos que pueda solucionarse con modificar aspectos superficiales, quizás simplemente no pueda realizarse la acción debido a las causas antes mencionadas. Sería necesario acudir al código para verlo con mas detenimiento. Para eso, diríjase a nuestra web de Github. Tampoco garantizamos que todos los errores externos sean capturados. En el peor de los casos, es necesario verificar en la terminal de Python para poder salvarlo. 

### Recomendaciones finales

- Para un mejor uso, se recomienda instalar el programa en una carpeta que no este usada por otros archivos. 

- La generación de histogramas es temporal, por ende al cerrar el programa se eliminan. Si necesita exportarlos, hágalo al momento de terminar la simulación por los medios antes indicados. Si realiza otra simulación, el histograma correspondiente a la nueva ejecución reescribirá el anterior gráfico. Estos se generan en la carpeta temporal *temp_graficos*, en el path destinado a los archivos de ejecución.

- Por más que estén seteados los mismos parámetros de entrada, entre una simulación y otra, los resultados pueden ser diferentes. Recuerde que trabajamos con variables aleatorias, y los modelos de generación de paquetes son estocásticos. 


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NjExNDY1OTYsLTE2ODI5NzI5MTAsLT
Q1NDQyODA1NiwyNzMwOTk5NzZdfQ==
-->