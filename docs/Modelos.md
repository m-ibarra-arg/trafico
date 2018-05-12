# Modelo M/M/1
El modelo más sencillo de analizar es aquel en el que tanto los tiempos de llegada de los clientes como los tiempos de servicio son exponenciales e independientes entre sí, el sistema tiene un único servidor y la disciplina de servicio es FIFO.

El desarrollo teórico de las ecuaciones de probabilidad, como las de medida de eficiencia del sistema se dejan para que se consulten directamente de los autores de la bibliografía utilizada para este trabajo.

El análisis que se realizara será exclusivamente en condición de estacionariedad, es decir, cuando alcanzo un estado estable. Si consideramos el estado de saturación, el numero de bytes en la cola de nuestro simulador crecerá indefinidamente, y los resultados dependerán del tiempo de la simulación.

Definimos la intensidad de trafico, o factor de utilización del sistema, como:

$$ρ = \frac{λ}{μ}$$

- ρ es *Intensidad de Trafico*
- λ es *Tasa de inter arribo*
- μ es *Tasa de servicio*

Por lo tanto, para que el sistema sea estable
$$ρ < 1$$

Se puede ver esta relación como la capacidad de atender los paquetes que entran a la cola, o como estará cargado nuestro sistema.
Si se cumple la condición de estacionariedad, las probabilidades de estado estable existen y están dadas por:
$$ρ_n = ρ^n * (1-ρ) $$
donde $ρ_n$ es la probabilidad de que haya n  paquetes (o bytes) en el sistema.

### Las medidas de rendimiento
A través de la distribución de probabilidad del estado del sistema para el caso estacionario podemos obtener algunas medidas para conocer la eficiencia del sistema, como son el número medio de clientes, paquetes o bytes en el sistema y el número medio de clientes, paquetes o bytes en cola (siempre suponiendo que el sistema se encuentra en estado estacionario).

El número medio de clientes en el sistema estará dado por:
$$L = \frac{λ}{μ-λ}$$
El número medio de clientes en cola estará dado por:
$$L _q= \frac{λ^2}{μ(μ-λ)}$$
El número medio de clientes en cola cuando ésta no esta vacia:
$$\overline{L _q}= \frac{μ}{(μ-λ)}$$

### Tiempos de Espera
Si no hay clientes en el sistema (n = 0), claramente el tiempo de espera en cola es 0. Si hay n ≥ 1 clientes en el sistema, entonces el nuevo cliente tiene que esperar a que se completen los n servicios que tiene delante; el de los n−1 clientes que hay en cola delante de él más el del cliente que esta siendo servido. Los n−1 clientes que están en cola tardarán cada uno un tiempo exponencial de parámetro μ, para el cliente que esta siendo servido, como la propiedad exponencial tiene la propiedad de pérdida de memoria, el tiempo que le queda una vez que se ha producido la llegada del nuevo cliente sigue siendo exponencial de parámetro μ. Por lo tanto, cuando el nuevo cliente llega tiene delante n clientes con tiempos exponenciales de parámetro μ, por lo tanto $$ W_q= \frac{λ}{μ(μ-λ)}$$
En total, la espera en el sistema será  $$ W= \frac{1}{(μ-λ)}$$

### Fórmulas de Little
Se pueden encontrar relaciones entre las distintas medidas de eficiencia. Estas relaciones se conocen con el nombre de fórmulas de Little y en algunos casos se verifican de modo general y en otro para modelos más restrictivos.

$$W = W_q + \frac{1}{μ}$$ Esta relación es bastante intuitiva y se fundamenta en el siguiente razonamiento. Esta relación, no sólo se verifica en el modelo M/M/1 sino en cualquier modelo general de colas.

$$L_q = λ W_q$$ Supongamos que un cliente llega al sistema. En promedio entrará al servicio después de un tiempo $W_q$. Supongamos que justo cuando va a entrar al servicio se da la vuelta y cuenta los clientes que están en cola detrás de él; en promedio ese número será $L_q$. Puesto que en promedio cada uno de los $L_q$ que están en la cola han tardado en llegar $\frac{1}{λ}$ respecto del anterior, el tiempo que ha estado esperando nuestro cliente en cola ha sido $L_q$ $\frac{1}{λ}$

$$L = λW$$  Esta expresión se conoce comúnmente como la fórmula de Little, pues se debe a un trabajo de Little de 1961. Se puede demostrar que esta  condición y la anterior se siguen verificando para un modelo de colas de un único canal con llegadas exponenciales y disciplina FIFO, sin importar la distribución del tiempo de servicio.

$$L = L_q + \frac{λ}{μ}$$ Es consecuencia inmediata de las anteriores. Se verifica en aquellos modelos en los que la fórmula de Little también lo haga.
  
$$W_q = \frac{L}{μ}$$ Justo cuando un cliente llega al sistema espera encontrarse L clientes delante de él. Para empezar su servicio tendrá que esperar a que finalice el servicio de los L anteriores. Puesto que el tiempo de servicio promedio es $\frac{λ}{μ}$ , el tiempo medio que espera en cola es $\frac{L}{μ}$.


# Modelo M/M/1/K

Este modelo, es una modificación del modelo M/M/1 que se basa en suponer que la capacidad del sistema está limitada a K clientes.

Las probabilidades de estado:

$$ p_{n}=\begin{cases}\dfrac {\left( 1-\rho\right) \rho ^{n}}{1-\rho^{K+1}},\rho\neq 1\\ \dfrac {1}{K+1},\rho =1\end{cases}$$

Observe que en este caso la solución para el estado estacionario existe incluso si ρ ≥ 1. Intuitivamente esto se debe a que la limitación en la capacidad del sistema
provoca que éste no se desborde. También se observa que si $K → ∞$ y $ρ < 1$, entonces $p_n → (1-ρ) ρ^n$, lo cual es consistente con los resultados obtenidos en el modelo M/M/1.

### Medidas de Eficiencia
Número medio de clientes en el sistema 
$$ L= \frac {\rho [1 - (K+1)\rho^K  + K \rho^{K+1} ]}{(1-\rho^{K+1})(1- \rho)}$$

cuando $\rho = 1$

$$L=\frac{K}{2}$$

cuando $\rho \neq 1$

Tamaño medio de la cola
$$L_q = L - (1-p_0)$$

En este modelo, para aplicar las igualdades con la formula de Little, debemos tener en cuenta, que ya no tenemos la tasa de arribos como en el M/M/1, sino que existe ahora una tasa de arribo efectiva, que es la que entra a la cola. Entonces:

$$\lambda_{ef}= \lambda(1-p_k)$$ 

donde $p_k$ es la probabilidad que haya *k* paquetes en el sistema.

Tiempo medio en el sistema, condicionado por el número de clientes en el sistema cuando el cliente se incorpora al mismo. Para que el cliente no sea rechazado tiene que haber a lo sumo *K−1* clientes en el sistema
$$W= \frac{L}{\lambda(1-p_K)  }$$
o también $$W= \frac{L}{\lambda_{ef}  }$$
Tiempo medio de espera en la cola
$$W_q= \frac{L_q}{\lambda(1-p_K)  }$$
o tambíen
$$W_q= \frac{L_q}{\lambda_{ef}  }$$

## Perdida de Clientes.

En este modelo, al tener una capacidad finita en la cola, una vez que ésta este llena, no sera capaz de alojar a los clientes que arriben.

Entonces pensamos la perdida como la tasa de arribo por la probabilidad que la cola este llena.

$$Pérdida = \lambda * p_k$$
o también, la tasa de arribo menos la tasa efectiva que entra en la cola:
$$Pérdida = \lambda - \lambda_{ef}$$


# Modelo M/G/1
Modelo de colas con tiempos de servicio no exponencial. En este modelo se supone que el sistema de colas tiene un servidor, las llegadas se producen según un proceso de Poisson de tasa λ y los clientes tienen tiempos de servicio independientes e idénticamente distribuidos de media $\frac{1}{μ}$ y varianza $σ^2$. 

Cualquier sistema de colas de este tipo alcanza en algún momento el estado estable si $ρ = \frac{\lambda}{μ}< 1$. Las medidas de eficiencia para este modelo toman las siguientes expresiones (la referente a $L_q$ recibe el nombre de fórmula de Pollaczek-Khintchine).

Probabilidad de estado estacionario
$$ p_0 = 1 - ρ $$
Número medio de clientes en la cola. Bytes en la cola de la simulación.
$$L_q =\frac{ λ^2σ^2 + ρ^2}{2(1-ρ)}$$
Número medio de clientes en el sistema.
$$L = L_q + ρ$$
Tiempo medio de espera en la cola
$$W_q = L_q λ$$
Tiempo medio en el sistema
$$W = \frac{L}{\lambda}  = W_q + \frac{1}{μ}$$

Obsérvese que las medidas de eficiencia incrementan su valor conforme $σ^2$ aumenta. Esto indica que el funcionamiento del servidor tiene gran transcendencia en la eficiencia global de la instalación. Asimismo, se observa que las fórmulas anteriores se reducen a las del modelo M/M/1 cuando los tiempos de servicio siguen una distribución exponencial.




<!--stackedit_data:
eyJoaXN0b3J5IjpbMjE0NjI2ODg1OCwtMTY3Nzk0NjMzMCwtND
QyODg3NDM1LDEzNDY2NTUzNzIsLTEzNzM4ODcxOTEsMTM0NjY1
NTM3MiwtMTM3Mzg4NzE5MSwxMzQ2NjU1MzcyLC0xNDEzMDc4Mz
I4LC0xMjY5Nzc3ODE1LC01MjY3MDU4NTAsLTEyNjk3Nzc4MTUs
MjEwNzY1MDgxNSwxOTE1ODY5MDUyLDk1MzIwNDQyNl19
-->