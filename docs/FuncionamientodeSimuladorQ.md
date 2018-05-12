# Interfaz gráfica
En esencia, SimuladorQ está compuesto por una ventana principal, en la que se establecen los modelos de colas (según Kendall) disponibles para simular, los cuales son M/M/1, M/G/1 y M/M/1/K. 
![Ventana Principal](https://github.com/maxxxis182/trafico/blob/docs/principal.png?raw=true "Ventana Principal")

Una vez elegido el modelo, nos envía a la siguiente ventana, donde podemos ingresar los parámetros de entrada del modelo elegido. 
Se puede dividir esta pantalla en varias secciones, las cuales describiremos detalladamente a continuación. 

## Parámetros de entrada

En esta sección es donde ingresamos las características principales de cada uno de los modelos dispuestos. 

### Modelo M/M/1:
![Ventana Secundaria](https://github.com/maxxxis182/trafico/blob/docs/mm1.png?raw=true "Ventana Secundaria")
- Tasa de arribos $\lambda$, medida en $\frac{bytes}{seg}$
- Tasa de servicio $\mu$, medida $\frac{bytes}{seg}$
- Usuario, identificación del cliente
- Bitrate de salida, medida en $bps$ o bien $\frac{bit}{seg}$ 
- Tiempo de simulación, medido en $seg$. 
- Bins, para generar histogramas con los resultados. Los valores disponibles son 50, 100, 150 y 200, para elección del usuario.
	 
### Modelo M/G/1:
![Ventana Secundaria](https://github.com/maxxxis182/trafico/blob/docs/mg1.png?raw=true "Ventana Secundaria")
- Tasa de arribos $\lambda$
 - Distribución de probabilidad general, las disponibles son Normal y Uniforme. La primeral necesita los siguientes parámetros Media $\mu$ y Desviación estándar $\sigma$. La segunda, necesita Limite inferior y superior.
- Usuario
- Bitrate de salida
- Tiempo de simulación
- Bins
 	 
### Modelo M/M/1/K:

![Ventana Secundaria](https://github.com/maxxxis182/trafico/blob/docs/mm1k.png?raw=true "Ventana Secundaria")
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

 - Tiempo medio de espera $W$, medido en $seg$
 - Tiempo medio de espera en la cola $W_{q}$, medido en $seg$
 - Paquetes enviados
 - Paquetes servidos
 - Paquetes perdidos
 - Porcentaje de pérdida
 - Número medio de bytes en la cola
 - Número medio de bytes en el sistema
 - Intensidad de tráfico $\rho$
 
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
	- Guardar gráficos: Normalizados o sin normalizar
	- Todo. Genera un solo archivo que contiene la información de los parámetros de entrada, de salida y el detalle de los paquetes servidos. Ademas crea una carpeta con el nombre *Gráficos - SimuladorQ_ fecha_hora* que contiene los histogramas del modelo simulado, tanto normalizados, como no normalizados.

En todos los casos que se generen archivos, se debe escoger el nombre y el directorio donde se guardarán. Todos ellos, salvo los histogramas, tienen una extensión propia del programa, la cual es *.siq* (por SimuladorQ). Por ejemplo: `parametros_entrada.siq`. Esto es así, salvo que se indique lo contrario al ingresar el nombre del archivo a generar (*.txt* es recomendado también, disponible para elección) Los gráficos tienen una extensión por defecto *.png*. 

### Simulación
- Correr simulación
- Interrumpir simulación actual
- Resetear parámetros
	 
### Ayuda
- Documentación
	- Sobre Python
	- Sobre PyQt
	- Librerías utilizadas
			 - Simpy
	 - Información Adicional
	 - Acerca de SimuladorQ

## Errores de simulación



<!--stackedit_data:
eyJoaXN0b3J5IjpbOTM0MzM2NTIwLDExMzEwNzQ5MTcsLTExND
g2MjgxOTcsMTEyOTk0NTE5MiwtMTYxOTk3MDY4XX0=
-->