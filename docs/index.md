
# Bienvenido a SimuladorQ  

SimuladorQ es un simulador de modelos de colas, el cual nos permitirá introducir parámetros de entrada característicos de cada uno de los modelos que se proponen, y obtener valores medios e histogramas del comportamiento de los mismos. 
En las siguientes secciones, se vera la fundamentación teórica de la herramienta, el lenguaje en el cual fue escrita y las herramientas que se utilizaron, y como trabaja el simulador.
  
## Teoría de Colas 
Es fundamental para entender el comportamiento de las redes de telecomunicaciones,  el tráfico que pasa por estas, el cual en algunos puntos de las dichas redes, se puede modelar a través de la teoría de colas.

La teoría de colas se ocupa, de alguna manera, del análisis matemático de los fenómenos de las lineas de espera o colas. Nos vamos a encontrar con estas esperas, cada vez que nos topemos con un servidor y que exista mas de un cliente para acceder a él. 

No solamente vemos estos comportamientos en las redes de telecomunicaciones. También aparecen en un semáforo, la cola de espera de un banco, la fila para comprar un boleto, etc. El análisis de la cola, nos mostrara el comportamiento a través del tiempo y las condiciones del sistema.

Existen varios tipos de cola, sin embargo, como el objetivo de este trabajo es crear una herramienta que nos ayude a entender el comportamiento de las mismas, con simulaciones a partir de la variación de algunos parámetros que las definen, nos enfocamos en las colas M/M/1, M/G/1,  y M/M/1/K, las cuales son las que se nos presentan primero a la hora de encaminarnos en este tema.

## Notación y terminología

La notación y terminología estándar que utilizaremos en este trabajo será:

- Estado del sistema. También números de clientes en el sistema, o en nuestro caso, cantidad de bytes. 
- Longitud de la cola o número de clientes en cola. 
- *n(t)*: número de clientes en el sistema en el instante t
- *p~n~(t)*: Probabilidad de que hayan n clientes en el sistema en el instante t.
- *s*: Número de servidores en el sistema.  
- *λ~n~*: Tasa media de llegadas o tasa de inter-arribos. (número esperado de llegadas por unidad de tiempo) de nuevos clientes cuando hay n clientes en el sistema.  
- *μ~n~*: tasa media de servicio para todo el sistema (número esperado de clientes que son servidos por unidad de tiempo) cuando hay n clientes en el sistema.

Cuando *λ~n~* es constante para todo n, se denota por *λ*. Esto significaría que el número medio de clientes que llega al sistema por unidad de tiempo no depende del estado del sistema. Lo mismo cuando la tasa media de servicio por servidor ocupado es constante, se denota por *μ*. Tenemos que *μ~n~* = **s** *μ*, cuando *n*≥**s**, es decir, cuando los **s** servidores están ocupados. En estas circunstancias, $\frac{1}{λ}$ es el tiempo esperado entre llegadas, $\frac{1}{μ}$ es  el tiempo de servicio esperado y *$ρ=\frac{λ}{s μ}$*  es el factor de utilización del sistema o intensidad de tráfico, es decir, la fracción media de tiempo que los servidores están ocupados.
Los modelos que presentaremos son con un solo servidor, por lo que la intensidad de trafico que manejaremos será:  *$ρ=\frac{λ}{μ}$*

## Sistemas en estado estacionario 
Los sistemas inicialmente se encuentra influenciado por sus condiciones de origen y se dice que el sistema se encuentra en estado transitorio. Una vez que ha pasado suficiente tiempo, usualmente, los factores del sistema se vuelven independientes de las condiciones iniciales y del tiempo transcurrido, y se dice que el sistema se encuentra en estado estacionario. 

Para analizar nuestros sistemas, tendremos que obtener probabilidades de estado, *p~n~(t)*: probabilidad de que el sistema esté en el estado *n* (haya n clientes en el sistema) en el instante t. En general lo interesante es conocer las probabilidades $p_{n}=\lim _{t\rightarrow \infty }p_{n}(t)$, es decir, cuando el sistema se encuentra en estado estable. De algún modo esto significa que esperamos que el sistema se vuelva independiente de las condiciones iniciales y del tiempo que ha transcurrido desde el inicio del mismo. Por lo tanto, la probabilidades estacionaria *p~n~* se puede interpretar como la probabilidad de que haya n clientes en el sistema cuando éste ha alcanzado el estado estacionario. Se aclara que no todos los sistemas tienen estado estacionario.

La siguiente notación asume que el sistema se encuentra en estado estacionario, y cada uno de estos parámetros, serán las que nos permitan conocer el comportamiento de nuestro sistema.

- *p~n~* : probabilidad de que haya n clientes en el sistema. Cantidad de Bytes en nuestro simulador.
- L : número esperado de clientes en el sistema. Cantidad de Bytes en nuestro simulador.  
- Lq :  número esperado de clientes en la cola. Longitud de la cola. Cantidad de Bytes para nuestro simulador.  
- W : tiempo medio de espera en el sistema para cada cliente.
- Wq : tiempo medio de espera en cola.

## Notación de Kendall

La notación utilizada para identificar las características de una cola se conoce como notación de Kendall, por ser éste matemático quien ideo la misma.

La notación de Kendall se lee 1/2/3/4/5/6

1. Distribución del tiempo entre llegadas.
	- M: Markovianos. Tiempos exponenciales. 
	- D: Deterministas.  
	- E_k: Erlang (k)  
	- G: Distribuciones Generales
2. Distribución de tiempo de servicio. Toma los mismos valores que 1.  
3. Número de servidores.  
4. Capacidad del sistema. Número máximo de clientes.
5. Disciplina de la cola.
	- First in first out. FIFO
	- Last in first out. LIFO
	- Prioridades.  
7. Tamaño de la fuente de entrada

Como se dijo anteriormente, los modelos que se desarrollaron son 
- M/M/1. Distribución de tiempo entre llegadas del tipo Markoviano, es decir, distribuidas exponencialmente. Lo mismo que los tiempos de servicio. Con un servidor. Capacidad del sistema infinito. Disciplinas FIFO.
-  M/G/1. Distribución de tiempo entre llegadas del tipo Markoviano, es decir, distribuidas exponencialmente. Los tiempos de servicio poseen una distribución general, las cuales se eligieron para el  programa de simulación las distribuciones Normal y Uniforme. Con un servidor. Capacidad del sistema infinito. Disciplinas FIFO.
- M/M/1/K. Idem al primer modelo. Capacidad del sistema **K**. 

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkxMDIwOTQ0MCwtMjAxODU0MzcyNCwtMT
IwMDQwMjg4NiwtNzA2OTYzMTQsLTEyMDA0MDI4ODYsLTcwNjk2
MzE0LDk1MTI1OTU4NCwxMDA4MDI1MDE5LDE0OTAyNDE4NjUsNz
UzNjcwODQyLC0xNzMzMDE4OTgwLC04NzQ4NzI1NTYsLTE2MTYy
MDQ3MzcsMTQ3MDEzMDc1NywxMTEzMjcyMzg5LDE1MzIyMTM5Mj
AsLTM5MTk1MDY1OCw4MTc0NzMzOCwtMTk0NDMwODExMiwtMTkw
NjAzODY1NF19
-->