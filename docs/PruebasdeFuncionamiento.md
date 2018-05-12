# Pruebas de Funcionamiento

En la tablas siguientes, haremos la comparación de los resultados de la simulación, calculados como se desarrolló en el apartado *Análisis del Código* y los resultados dados con las fórmulas de rendimiento dadas en *Modelos*.


## M/M/1

### Prueba 01

El sistema es estacionario, es decir $\rho<1$. Los resultados del simulador convergen al resultado teórico. 

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^3		|$\rho$		|0.50781	|0.5           
|$Port_{rate}$	|100		|$L$       	|0.84211    |1	           
|$\lambda$   	|1			|$L_q$     	|0.46159	|0.5
|$\mu$      	|2			|$W$       	|0.96940	|1
|$K$          	|$\infty$	|$W_q$     	|0.46159	|0.5
|      			|			|$Loss$ 	|0.0%		|0%

Los tiempos de inter-arribo tienen una distribución exponencial, con parámetro $\lambda$. Vemos esto gráficamente:

![Tiempo inter-arribo Matlab](github.com/maxxxis182/trafico/blob/master/docs/img/matlab/prueba_01_arribo.png?raw=true)

**EXPLICAR GRAFICOS DEL SIMULADOR**

El simulador provee 3 histogramas: Tiempos de inter-arribos de paquetes, Tiempos de espera de los paquetes y Tiempos de ocupación del sistema.
#### Tiempos de inter-arribos de paquetes
Para el caso de los tiempos de inter-arribos de paquetes emos or
    )
```
El servidor esta definido para que no se muestre en el programa lo que llega al servidor, porque no nos enfocamos en el específicamente, sino en la cola, y lo que entra, transcurre y sale de ella. Además solo nos interesan los tiempos entre arribos consecutivos, y no los absolutos.
La variable `psink` indica que recibe paquetes y recopila información de delay en la lista de espera de paquetes.

Ahora bien, para graficar el histograma, se realiza de la siguiente forma:
```python    
fig, axis = plt.subplots()
axis.hist(psink.arrivals, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
axis.set_title("Tiempos de Inter-Arribo a la Cola - Normalizado")
axis.set_xlabel("Tiempo")
axis.set_ylabel("Frecuencia de ocurrencia")
fig.savefig(directorio + "ArrivalHistogram_normal.png")
```
El histograma se genera con el método `.hist` y como argumentos están los arribos (`psink.arrivals`); los bins (explicados en la sección de *Funcionamiento de SimuladorQ*); si se desea que este normalizado o no (`normed=True` o `normed = False`); el grado de opacidad (`alpha=1`), en nuestro caso al máximo; color de bordes de las barras (`edgecolor = 'black'`) y su grosor (`linewidth = 1`).

SimuladorQ brinda las opciones de normalización. Por defecto `normed = False` la frecuencia es proporcional a la altura, no al área. La opción `normed=True` cambia la representación a proporcionalidad con el área, y además cambia la escala para que el área total sea 1.

#### Tiempos de espera de los paquetes
Para el caso de los tiempos de espera de los paquetes hactenemos un análisis similar al de los tiempos de inter-arribo, porque lo vemos con `psink`, pero ahora solicitamos el tiempo de espera que experimentan los paquetes con `psink.waits`. El resto se mantiene igual en el código, pero cambiamos `psink.arrivals` por `psink.waits`.

#### Tiempo de ocupación en el sistema
Para el caso de los tiempos de ocupación en el sistema el análisis es parecido a los anteriores. Solo agregamos un monitor en la cola.

```python    
#Parametros del Monitque analizar como van a ser servidos los paquetes. Es por eso, que en `modelos.py` se definen

```python    
	debugSink=False #False, muestra en la salida lo que llega al servidor 
       Smd= 0.5
       samp_dist = functools.partial(random.expovariate,Smd)
       [...]
       switch_port= SwitchPort(env, 
                                rate=port_rate, 
                                qlimit=ql)
       [...]
# PortMonitor para rastrear los tamaños de cola a lo largo del tiempo
       pm = PortMonitor(env, 
                        switch_port, 
                        samp_dist)
```
Se utiliza `PortMonitor` para controlar el tamaño de la cola a lo largo del tiempo para un `SwitchPort`. Observa la cantidad de elementos en `SwitchPort` en servicio en la cola y registra esa información en la lista de `sizes`. El monitor mira el puerto a intervalos de tiempo dados por la distribución dist.Se especifica una distribución de muestreo, es decir, una distribución que proporcione el tiempo entre muestras sucesivas. Para todos los casos y modelos, se utiliza un distribución exponencial especificando su tasa de arribo. En este caso usamos $\lambda = Smd = 0.5$. Al `SwitchPort` se le da como argumento la tasa de salida de la cola`port_rate`, y el limite de la cola `qlimit`(infinito para todas los modelos, salvo para el M/M/1/K). 
Para graficar el histograma, es bastante parecido a los anteriores, cambia en el argumento `pm.sizes` para trabajar con los tamaños de los paquetes de la cola.
```python    
fig, axis = plt.subplots()
axis.hist(pm.sizes, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
axis.set_title("Tiempos de Ocupación del Sistema - Normalizado")
axis.set_xlabel("Nro")
axis.set_ylabel("Frecuencia de ocurrencia")
fig.savefig(directorio + "QueueHistogram_normal.png"rec_arrivalsSink=True #Si es verdadero los arribos se graban
    abs_arrivalsSink=False # true, se graban tiempos de arribo absoluto; False, el tiempo entre arribos consecutivos
    [...]
    psink = PacketSink(env, 
                        debug=debugSink, 
                        rec_arrivals=rec_arrivalsSink, 
                        absolute_arrivals=abs_arrivalsSink)
```




El resultado de la simulación. Tiempos de Inter-arribo a la cola:

![Tiempo inter-arribo Simulador](https://github.com/maxxxis182/trafico/blob/master/docs/img/prueba_01/ArrivalHistogram_normal.png?raw=true )

En cuanto a los tiempos de servicio de la cola:

![Tiempo servicio Matlab](https://github.com/maxxxis182/trafico/blob/master/docs/img/matlab/prueba_01_espera.png?raw=true )

![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/master/docs/img/prueba_01/WaitHistogram_normal.png?raw=true )

Se puede ver que en la teoría, la función de distribución tiene amplitud igual a dos, y en el simulador es uno. Esto se debe al tamaño de los paquetes, consecuente con el valor de $\mu$. Al ser muy pronunciada la curva de la distribución con parámetros grandes (ej: $\lambda=2$ ), no se llega  a notar esta diferencia. Pruebe con valores de $\lambda$ mas pequeños, que hacen que la curva decrezca suavemente, y se ve la convergencia de ambas gráficas.  

### Prueba 02

Aumentando el tiempo de simulación, con respecto a la **Prueba 01**, vemos que más se aproxima al valor teórico. 

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^4		|$\rho$		|0.49871|0.5           
|$Port_{rate}$	|100		|$L$       	|0.97883    |1	           
|$\lambda$   	|1			|$L_q$     	|0.49032	|0.5
|$\mu$      	|2			|$W$       	|0.98903	|1
|$K$          	|$\infty$	|$W_q$     	|0.49032	|0.5
|      			|			|$Loss$ 	|0.0%		|0%

Tiempos de inter-arribo a la cola:

![Tiempo inter-arribo Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_02/ArrivalHistogram_normal.png?raw=true )

Tiempos de servicio:

![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_02/WaitHistogram_normal.png?raw=true )


### Prueba 03

Aumentando la intensidad de tráfico del sistema:

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^4		|$\rho$		|0.80888|0.8           
|$Port_{rate}$	|100		|$L$       	|4.41489    |4	           
|$\lambda$   	|0.8		|$L_q$     	|3.52663	|3.2
|$\mu$      	|1			|$W$       	|5.41938	|5
|$K$          	|$\infty$	|$W_q$     	|4.40828	|4
|      			|			|$Loss$ 	|0.0%		|0%

Aumenta considerablemente el tiempo de servicio.

### Prueba 04

Aumentando el tiempo de simulación:

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$		|0.80150|0.8           
|$Port_{rate}$	|100		|$L$       	|4.00154    |4	           
|$\lambda$   	|0.8		|$L_q$     	|3.22265	|3.2
|$\mu$      	|1			|$W$       	|5.03019	|5
|$K$          	|$\infty$	|$W_q$     	|4.02831	|4
|      			|			|$Loss$ 	|0.0%		|0%

La convergencia a los valores teóricos se vuelve mas notable.
Ocurre en la simulación de este modelo, que por tiempos de simulación, paquetes generados en el PacketGenerator no alcanzan a llegar al PacketSink. Lo vemos en los parámetros de salida.

![Tiempo inter-arribo Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_04/ArrivalHistogram_normal.png?raw=true )

![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_04/WaitHistogram_normal.png?raw=true )

Ocurre lo mismo que en la **Prueba 01** con respecto a la amplitud del gráfico.

### Prueba 05

Con un sistema no estacionario, es decir $\rho>1$:

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|2.00922		|2            
|$Port_{rate}$	|100		|$L$    |50164.32158    |negativo	           
|$\lambda$   	|2			|$L_q$  |50205.38164	|negativo
|$\mu$      	|1			|$W$    |25103.69543	|negativo
|$K$          	|$\infty$	|$W_q$  |25102.69082	|negativo
|      			|			|$Loss$	|0.0			|

Teóricamente tenemos valores negativos, que no concuerdan con el problema físico que enfrentamos. En la simulación se acumulan paquetes en la cola. Los valores dependerán del tiempo de la simulación.

![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_05/WaitHistogram_normal.png?raw=true )

Gráficamente, los tiempos que deben esperar los paquetes.

## M/G/1. Distribución Normal

### Prueba 06

En este modelo, la tasa de servicio no está definida explicitamente.
Recordando la relación con la que trabaja el SwitchPort para servir los paquetes, tenemos el valor de la tasa de servicio:
$$ \mu = ({\frac {{Media} *8}{rate}})^{-1}$$



|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|0.24000	|  0.24          
|$Port_{rate}$	|100		|$L$    |0.27980    |0.2845	           
|$\lambda$   	|1			|$L_q$  |0.03785	|0.0445
|$Media$      	|3			|$W$    |0.27784	|0.2845
|$\sigma$        |0.1	|$W_q$  |0.03785	|0.0445
| $K$     		|$\infty$			|$Loss$	|0	|0
|  	    		|				|$\mu$	|4.16	|4.1666

Para verificar $\mu$ del simulador, basta dividir la intensidad de trafico con la tasa de inter-arribo.

![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_06/WaitHistogram_normal.png?raw=true )

![Tiempo inter-arribo Matlab](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/matlab/prueba_06_espera.png?raw=true)

La distribución de los tiempos de inter-arribo es exponencial, como habíamos visto en los ejemplos M/M/1. 
Lo que deberíamos ver es un cambio en la distribución de los tiempos de servicio. La distribución en este caso es *Normal*, como se observa en el gráfico con media $1/\mu$ y varianza $\sigma^2$. El simulador entrega los paquetes con esta media, aunque en este caso no se llega a distinguir la forma característica de la función de densidad.

### Prueba 07

Si aumentamos la varianza, con respecto a la prueba anterior:

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|0.24000	|  0.24          
|$Port_{rate}$	|100		|$L$    |0.29104    |1.7582	           
|$\lambda$   	|1			|$L_q$  |0.04981	|1.5182
|$Media$      	|3			|$W$    |0.29019	|1.7582
|$\sigma$        |1.5	|$W_q$  |0.04981	|1.5182
| $K$     		|$\infty$			|$Loss$	|0	|0
|  	    		|				|$\mu$	|4.16	|4.1666


![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_07/WaitHistogram_normal.png?raw=true )

Se ve claramente la forma de la distribución Normal. En este caso, los parámetros de performance se alejan de los valores teóricos.

## M/G/1. Distribución Uniforme

### Prueba 08

La media y varianza de la distribución uniforme para calcular $\mu$ y $L_q$:

$$media = \frac{a + b}{2}$$
$$var = \frac{(b-a)^2}{12}$$


|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|0.11985	|0.12            
|$Port_{rate}$	|100		|$L$    |0.12952    |0.3807	           
|$\lambda$   	|0.5		|$L_q$  |0.00922	|0.2607
|$Min$      	|1			|$W$    |0.25814	|0.7604
|$Max$        |5	|$W_q$  |0.01844	|0.5214
| $K$     		|$\infty$			|$Loss$	|0	|0
|  	    		|				|$\mu$	|4.1718	|4.1666

A partir de los valores de **a** y  **b** que introducimos en el simulador, se corresponden con los límites de la distribución de los tiempos de servicio de la siguiente manera:

$$ min = ({\frac {{a} *8}{rate}})$$
$$ max = ({\frac {{b} *8}{rate}})$$

![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_08/WaitHistogram_normal.png?raw=true )

![Tiempo Servicio de la cola Matlab](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/matlab/prueba_08_espera.png?raw=true)

Los errores con los valores teóricos de las medidas de rendimiento son notables. Al igual que con la distribución Normal, una varianza grande nos aleja del resultado.

### Prueba 09

Disminuyendo la varianza. Tenemos que acortar el rango de la distribución.

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|0.05999	|0.06            
|$Port_{rate}$	|100		|$L$    |0.06352    |0.0628	           
|$\lambda$   	|0.5		|$L_q$  |0.00201	|0.0028
|$Min$      	|1			|$W$    |0.12399	|0.1257
|$Max$        |2	|$W_q$  |0.00402			|0.0057
| $K$     		|$\infty$	|$Loss$		|0	|0
|  	    		|			|$\mu$	|8.3347	|8.3333

Con respecto a la prueba anterior, los valores mejoraron.

![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_09/WaitHistogram_normal.png?raw=true )

## M/M/1/K

### Prueba 10

Recordemos que el modelo M/M/1/K es estacionario tanto si $\rho$ es mayor o igual a uno. Entonces probamos primero con $\rho<1$.


|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$		|0.83333	|0.8333           
|$Port_{rate}$	|100		|$L$       	|3.58574    |4.5334	           
|$\lambda$   	|10			|$L_q$     	|2.75611	|3.7038
|$\mu$      	|12			|$W$       	|0.36017	|0.4554
|$K$          	|20		|$W_q$     	|0.27684	|0.3720
|      			|			|$Loss$ 	|0.0444		|0.0444

Si bien el desempeño de la cola es con una intensidad de tráfico menor a uno, nos encontramos con una tasa de pérdida distinta de cero, pequeña en el este caso.

![Tiempo inter-arribo Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_10/ArrivalHistogram_normal.png?raw=true )

![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_10/WaitHistogram_normal.png?raw=true )

Vemos que los tiempos de inter-arribo y de servicio, responden a una distribución exponencial.

### Prueba 11

Con un sistema recargado, $\rho>1$: 

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$		|1.25000	|1.25           
|$Port_{rate}$	|100		|$L$       	|14.54642    |16.1955	           
|$\lambda$   	|15			|$L_q$     	|13.54875	|15.1978
|$\mu$      	|12			|$W$       	|1.21503	|1.3528
|$K$          	|20		|$W_q$     	|1.13170	|1.2694
|      			|			|$Loss$ 	|3.0279		|3.0279

La perdida es considerable. Tenemos una longitud de la cola, u ocupación media del sistema, casi del %75 de la longitud de la misma.

![Tiempo inter-arribo Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_11/ArrivalHistogram_normal.png?raw=true )

Vemos como se va llenando la cola de forma exponencial.

![Tiempo de Servicio de la cola Simulador](https://github.com/maxxxis182/trafico/blob/simuladorQ/img/prueba_11/WaitHistogram_normal.png?raw=true )

## Conclusiones

Se deja una primera impresión de los resultados de este simulador y los valores de entrada, que en una primera instancia, nos dejan resultados aceptables para discutir el funcionamiento de cada modelo. Queda en el estudiante variar todos los parámetros y ver como responde cada sistema. 
Como todo proyecto en su primera versión de desarrollo, quedarán problemas para resolver en el futuro. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk5NTE1NTk5MywtMTY3NjY0NjIxOCwtOT
EyNjYxMDU2LC0xMDYwNzc5MzA1XX0=
-->