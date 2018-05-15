# Análisis de Colas con Python

Ya hemos tenido una introducción sobre los modelos de cola, y una descripción de SimuladorQ. Pero como este trabajo está enmarcado en un Proyecto Final de Asignatura, detallaremos a continuación como trabaja el software. En la sección posterior mostraremos resultados del programa comparándolos con los valores obtenidos teóricamente.

## SimComponents

De la librería de *SimComponents* utilizamos las clases Packet, PacketGenerator, PacketSink, SwitchPort y PortMonitor. 


### Packet
Esta clase representa un paquete, el cual recorrerá desde el Generador de Paquetes hasta el Sumidero. El parámetro de salida será un string con los atributos del paquete, como: número de identificación, la fuente que envía, el tiempo en que se genera y el tamaño del mismo. 

```python
class Packet(object):
   
    def __init__(self, time, size, id, src="a", dst="z", flow_id=0):
        self.time = time
        self.size = size
        self.id = id
        self.src = src
        self.dst = dst
        self.flow_id = flow_id

    def __repr__(self):
        return "id: {:<6}, src: {}, time: {:<10f}, size: {:.10}".\
            format(self.id, self.src, self.time, self.size)

```

### PacketGenerator

El PacketGenerator o Generador de Paquetes, emula un cliente que envía trafico a una red, el cual en un nodo se encontrará con un buffer que responderá de determinada manera, dependiendo del modelo de cola que hayamos presentado. 

Los paquetes que genera tendrán un tiempo de inter arribo dado por una distribución que pasaremos como parámetro de entrada.

A partir de esta clase, de *SimComponents* comienza a aparecer el parámetro de entrada **env** el cual nos define el Entorno de Simpy que generará la simulación.

**Adist** será una función que devuelve los tiempos de inter-arribo.

**Sdist** será una función que devuelve los tamaños de los paquetes. Hay que prestar atención a este parámetro, ya que más adelante, por como trabaja la librería *SimComponents*, será fundamental para los tiempos de servicios de los paquetes en la cola.

```python
class PacketGenerator(object):
    def __init__(self, env, id,  adist, sdist, initial_delay=0, finish=float("inf"), flow_id=0):
        self.id = id
        self.env = env
        self.adist = adist
        self.sdist = sdist
        self.initial_delay = initial_delay
        self.finish = finish
        self.out = None
        self.packets_sent = 0
        self.action = env.process(self.run())  # starts the run() method as a SimPy process
        self.flow_id = flow_id

    def run(self):
        #El generador de función utilizado en la simulación.
        yield self.env.timeout(self.initial_delay)
        while self.env.now < self.finish:
            # Espera por la siguiente transmisión
            yield self.env.timeout(self.adist())
            self.packets_sent += 1
            p = Packet(self.env.now, self.sdist(), self.packets_sent, src=self.id, flow_id=self.flow_id)
            self.out.put(p)
```
En definitiva, el generador, pone en la salida de la clase un **Packet**, con las características que vimos anteriormente. Estos atributos, serán utilizados para el cálculo de las medidas de rendimiento del sistema.

### PacketSink
PacketSink o sumidero, es donde terminan los paquetes. El sumidero recibe los paquetes y colecta información sobre los tiempos de espera. 

Se define **env**, el entorno de simulación. La librería posee más información acerca de esta clase.  

```python
class PacketSink(object):
    def __init__(self, env, rec_arrivals=False, absolute_arrivals=False, rec_waits=True, save=True, debug=False, selector=None):
        self.store = simpy.Store(env)
        self.env = env
        self.rec_waits = rec_waits
        self.rec_arrivals = rec_arrivals
        self.absolute_arrivals = absolute_arrivals
        self.waits = []
        self.arrivals = []
        self.debug = debug
        self.packets_rec = 0
        self.bytes_rec = 0
        self.selector = selector
        self.last_arrival = 0.0
        self.save= save 
        self.data=[]

    def put(self, pkt):
        if not self.selector or self.selector(pkt):
            now = self.env.now
            if self.rec_waits:
                self.waits.append(self.env.now - pkt.time)
            if self.rec_arrivals:
                if self.absolute_arrivals:
                    self.arrivals.append(now)
                else:
                    self.arrivals.append(now - self.last_arrival)
                self.last_arrival = now
            self.packets_rec += 1
            self.bytes_rec += pkt.size
            if self.debug:
                print(pkt)
            if self.save:
                self.data.append('{}'.format(pkt))
```
### SwitchPort
El SwitchPort o cola, será el componente mas importante de nuestro sistema.  Modela un puerto de salida con un bitrate dado y un límite de tamaño de búfer, en bytes.
Nuevamente aparece **env** para definir el entorno de simulación. El argumento **rate**, es la tasa a la cual van a ser servidos los clientes (o bytes). El tamaño de la cola dado por **qlimit** en bytes. En caso de cola infinita para los modelos M/M/1 y M/G/1 el parámetro **qlimit**=None. 
 
 
```python
 class SwitchPort(object):
    def __init__(self, env, rate, qlimit=None, limit_bytes=True, debug=False):
        self.store = simpy.Store(env)
        self.rate = rate
        self.env = env
        self.out = None
        self.packets_rec = 0
        self.packets_drop = 0
        self.qlimit = qlimit
        self.limit_bytes = limit_bytes
        self.byte_size = 0  # Tamaño actual de la cola en bytes
        self.debug = debug
        self.sizes = []
        self.busy = 0  # Usado para rastrear si un paquete está siendo enviado actualmente
        self.action = env.process(self.run())#inicia el método run() como un proceso SimPy

    def run(self):
        while True:
            self.msg = (yield self.store.get())
            self.busy = 1
            self.byte_size -= self.msg.size
            delay = abs(self.msg.size*8.0/self.rate)
            yield self.env.timeout(delay)
            self.out.put(self.msg)
            self.sizes.append(self.msg.size)
            self.busy = 0
            if self.debug:
                print(self.msg)

    def put(self, pkt):
        self.packets_rec += 1
        tmp_byte_count = self.byte_size + pkt.size
        if self.qlimit is None:
            self.byte_size = tmp_byte_count
            return self.store.put(pkt)
        if self.limit_bytes and tmp_byte_count >= self.qlimit:
            self.packets_drop += 1
            return
        elif not self.limit_bytes and len(self.store.items) >= self.qlimit-1:
            self.packets_drop += 1
        else:
            self.byte_size = tmp_byte_count
            return self.store.put(pkt)
```

Los paquetes que salen del Generador y llegan al SwitchPort, primero se cuentan, y luego se realiza una validación para saber si entra en el lugar disponible que posee la cola. En caso de no entrar, pasa a ser un paquete *drop* o rechazado. Una vez que entra en la cola, pasa a formar parte de **store**, esperando a ser servido.

El método *run()* va sacando los paquetes de **store** y los va sirviendo. La manera de servir los paquetes 
``` python
 yield self.env.timeout(self.msg.size*8.0/self.rate)
```
El **yield** pasiva el proceso durante un tiempo. Ese tiempo depende del tamaño del paquete que está siendo servido, multiplicado por 8 bit, y dividido por el rate en bit por segundo. 

Entonces se puede pensar que el tiempo de servicio, tendrá la misma distribución que la de los tamaños de paquetes, que habíamos definido en un principio en el Generador de Paquetes.

Como ejemplo, para ver mejor lo que estamos diciendo, pondremos el modelo M/M/1. Tenemos como tasa de servicio en este modelo, valores distribuidos exponencialmente. Entonces la media de una distribución exponencial es $1/\lambda$. No confundir este lambda con la tasa de inter arribo.  

$$\mu = \left ( {\frac {\frac{1}{\lambda} \times 8}{rate}} \right )^{-1} = \frac{byte}{seg}$$

Donde la media esta dada en byte, el 8 es en bit, y el rate en bps.

A partir de conocer $\mu$, tendremos entonces la tasa de servicio de nuestra cola, que en el caso del modelo M/M/1, será el parámetro de la distribución exponencial. 

Para los otros modelos, el análisis será similar, y dependiendo de la distribución del tamaño de los paquetes en el Generador, estaremos definiendo implícitamente el servicio de nuestra cola.

Visto que no tiene demasiado sentido estar haciendo cálculos previos en el tamaño de los paquetes para definir la tasa de servicio, en SimuladorQ se pasa la tasa $\mu$ y se calcula despejando de la fórmula anterior el parámetro que meteremos en el generador. Más adelante mencionaremos esto nuevamente.

### PortMonitor
El PortMonitor lo que hace es mirar el número de clientes, o bytes, que se encuentran en la cola. Con los valores que rescata esta clase, se calculan los valores medios de ocupación en el sistema y la cola.
Además del parámetro **env**, se le pasa como argumento el puerto que debe observar, y la distribución de tiempos de cada cuanto tiene que hacerlo.

```python
class PortMonitor(object):
       def __init__(self, env, port, dist, count_bytes=False):
        self.port = port
        self.env = env
        self.dist = dist
        self.count_bytes = count_bytes
        self.sizes = []
        self.action = env.process(self.run())

    def run(self):
        while True:
            yield self.env.timeout(self.dist())
            if self.count_bytes:
                total = self.port.byte_size
            else:
                total = len(self.port.store.items) + self.port.busy
            self.sizes.append(total)
```
## Modelos
Las librerías de *SimComponents*, nos permite a través de las clases, poder generar los bloques de un sistema de comunicación, con:
1. un cliente que genera tráfico, 
2. una cola con un búfer y cierta capacidad de servir los paquetes que llegan a ella, 
3. y un sumidero donde mueren los paquetes y se contabilizan características de los envíos.

Las siguientes funciones que mencionaremos, nos servirán para introducir y definir parámetros de cada uno de los componentes de SimComponents, realizar los cálculos pertinentes para las medidas de eficiencia que necesitamos para SimuladorQ con su respectivas salidas de la función y la muestra de gráficos.

### MM1

Para el modelo M/M/1 tenemos la función MM1. Para ver en detalle toda la función, ir a $modelos.py$ 

```python
def MM1(lamda, mu, user, port_rate, Tsim, bins, directorio):
```
Vemos que los parámetros de entrada son **lamda**=$\lambda$ para la tasa de inter-arribo, **mu**=$\mu$ para la tasa de servicio, **port_rate** la velocidad para el PortSwitch, **Tsim** es el tiempo de la simulación en segundos (aclaramos que no es en tiempo real la simulación, sino que se genera un tiempo aleatorio cada vez que ocurre un evento), y **directorio**,  que se utiliza para brindar la ubicación de donde se van guardar temporalmente los histogramas para mostrarlo a través de la interfaz gráfica.

Introduciéndonos en la función, con los parámetros que le pasamos, definimos las clases de SimComponents.
```python
    ####Parametros del Sumidero
    debugSink=False 
    #muestra en la salida lo que llega al servidor
    rec_arrivalsSink=True 
    #Si es verdadero los arribos se graban
    abs_arrivalsSink=False 
    # Si es verdadero se graban tiempos de arribo absoluto; False, el tiempo entre arribos consecutivos
```
Con la siguiente línea se convierte la tasa de los tiempos de inter-arribo al parámetro de la distribución exponencial para la distribución de los tamaño de paquetes generados con PacketSink.
```python    
    ####Parametros del Sumidero
	mu=(mu*8)/port_rate
```
Las funciones de distribución de los tiempos de inter-arribo y de los tamaños de los paquetes. 
```python    
    adist = functools.partial(random.expovariate, lamda) #Tiempo de inter arribo de los paquetes
    sdist = functools.partial(random.expovariate, mu)  # Tamaño de los paquetes 
```
El tamaño de la cola no se pasa como parámetro de entrada de la función MM1, ya que al tener búfer infinito este modelo, éste ya lo  definimos internamente.
```python    
    #Parametros de la Cola
    ql=None #byte. Largo de cola infinita
```
Por último, en la definición de los componentes,  PortMonitor, el cual necesita la distribución de tiempos en que observará la cola. 
```python    
    #Parametros del Monitor 
    Smd = 0.5
    samp_dist = functools.partial(random.expovariate,Smd)
```
Una vez cargados los parámetros de las clases de *SimComponents*, definimos cada uno de ellos. Vemos como creamos el entorno de simulación **env**, el cual se lo damos como entrada a las demás clases de *SimComponents*. 
```python     
    ############# CREACION DEL ENTORNO Y SUS COMPONENTES  #########################
    
    # Creación del Entorno de Simpy
    env = simpy.Environment()  
    
    # Creación del Generador de Paquetes, Servidor, Cola y Monitor.
    psink = PacketSink(env, 
                    debug=debugSink, 
                    rec_arrivals=rec_arrivalsSink, 
                    absolute_arrivals=abs_arrivalsSink)
    pg = PacketGenerator(env, 
                         user, 
                         adist, 
                         sdist)
    switch_port= SwitchPort(env, 
                             rate=port_rate, 
                             qlimit=ql)
    pm = PortMonitor(env, 
                     switch_port, 
                     samp_dist)
```
A continuación, vemos cómo se realiza el conexionado de cada uno de los bloques. Se define que bloque se coloca a la salida. 
```python    
    ############# CONEXION DE LOS COMPONENTES DEL MODELO  #########################
    
    pg.out = switch_port
    switch_port.out = psink
```
En este caso, la conexión nos quedaría de la siguiente manera.

![](https://raw.githubusercontent.com/maxxxis182/trafico/master/docs/img/diagrama.png)

Una vez todo definido, corremos la simulación, con el tiempo **Tsim**.
```python    
    # Correr la simulacion del entorno. Parametro el tiempo
    env.run(until=Tsim)
```
El tiempo de simulación no es más que un parámetro que necesita la librería *Simpy* para generar un clock interno, poder hacer la generación de paquetes y así darle consecuencia a los mismos de una manera ordenada. Es decir, da marcas temporales a los eventos, en este caso la generación de los paquetes. Cabe destacar que esta variable no representa una unidad temporal real, como el segundo (mas allá de que internamente, la identidad que le da es el segundo). Puede apreciarse que no hay una analogía directa entre el *segundo* del clock interno y el *segundo* de tiempo real. La frecuencia de éste clock depende del procesamiento de CPU, por eso, la duración de la simulación puede variar de un equipo a otro. Para mas información, visitar la documentación de [Simpy](https://simpy.readthedocs.io/en/latest/).

Una vez simulado, calculamos, a partir de los atributos, las diferentes medidas de eficiencia del modelo.

Los paquetes enviados, perdidos y recibidos, son atributos de cada una de las clases. Se puede ver mejor en *SimComponents* como se generan.
```python
    pkt_drop=switch_port.packets_drop
    pkt_enviados=pg.packets_sent
    pkt_recibidos_serv = psink.packets_rec
```
El tiempo medio que van a esperar los paquetes en ser servidos, lo veremos haciendo un promedio de todas las esperas que sufren cada uno de los paquetes que llegan al sumidero.
```python
	espera_sist_W=sum(psink.waits)/len(psink.waits)
```
El tamaño medio, entre la cola y el paquete que está siendo servido, también es posible pensarlo como un promedio con todas las veces que el monitor mira la longitud de la misma.
```python
	ocup_sistema_L=float(sum(pm.sizes))/len(pm.sizes)
```  
La pérdida en este modelo es nula. Entendiendo que el sistema es estacionario y todos los paquetes en algún momento serán servidos. 
La manera en que se calcula puede traer algún error si hay algún paquete que no se consume en el sumidero, problema que existe cuando, por el tiempo de simulación, quedan paquetes en el camino. 
```python    	
	tasa_perdida=1.0 - float(pg.packets_sent)/switch_port.packets_rec
```
Como se dijo anteriormente, la manera de calcular la tasa de servicio, es a partir del parámetro de la distribución exponencial a la hora de generar los paquetes en el PacketGenerator.  Es por esto que, sabiendo que la intensidad de tráfico es $\lambda / \mu$ obtenemos a $\mu$ como  $$\mu = \left ( {\frac {\frac{1}{\lambda_{paq}} \times8}{rate}} \right )^{-1}$$ siendo el  $\lambda_{paq}$ el parámetro anteriormente mencionado.
Entonces se calcula la intensidad de tráfico $\rho$ de esa manera. 
```python    
    intensidad_trafico = (lamda)*((float(sum(switch_port.sizes)/len(switch_port.sizes))*8.0/port_rate))
```
Conociendo la intensidad de tráfico y $\lambda$ definido como argumento de entrada de la función MM1, podemos calcular los demás parámetros por Little.

```python
	espera_sist_W=sum(psink.waits)/len(psink.waits)
    pkt_drop=switch_port.packets_drop
    pkt_enviados=pg.packets_sent
    tasa_perdida=1.0 - float(pg.packets_sent)/switch_port.packets_rec
    ocup_sistema_L=float(sum(pm.sizes))/len(pm.sizes)
    pkt_recibidos_serv = psink.packets_rec
    intensidad_trafico = (lamda)*((float(sum(switch_port.sizes)/len(switch_port.sizes))*8.0/port_rate))
    mu_serv=1/(intensidad_trafico/lamda)
    espera_cola_Wq=espera_sist_W - 1/mu_serv
    ocup_cola_Lq= espera_cola_Wq * lamda 
```
Es de esperar que *mu_serv*, que calculamos en la línea anterior, se corresponda con el $\mu$ que se pasa como argumento.

También, se realizan los gráficos que se explicarán en la sección siguiente, *Pruebas del Funcionamiento*. 

Por último, los datos que calculamos, se devuelven con un **return**, que se llaman desde el archivo principal para mostrarlos en SimuladorQ.

### MG1
A nivel general, la función MG1, trabaja de la misma manera que MM1. Se puede sospechar que cambiará la distribución de servicio de la cola. 

Anteriormente habíamos dicho que la distribución y su respectiva tasa dependía de los tamaños de los paquetes. En el caso de MG1, esta definición se pasa de la siguiente manera:
```python
#Parametros del Generador de Paquetes. 
    if G==1:
        sdist = functools.partial(random.normalvariate, a, b)  
    elif G==2:
        sdist = functools.partial(random.uniform, a, b)  
```
Primero, vemos que ahora también se pasa como parámetro la distribución general que queremos. Como opción proponemos trabajar con la distribución Normal y la Uniforme.

En esta función, ahora no existe más el parámetro $\mu$. Se pasa los valores de **a** y **b**. En la distribución Normal, representan la media y la desviación estándar respectivamente. En la Uniforme, los valores mínimo y máximo del rango que define la función de densidad de probabilidad.

Ahora entonces, la tasa de servicio de la cola estará dada por
$$ \mu = \left ( {\frac {{Media} \times8}{rate}} \right )^{-1}$$

donde la media de la Normal está definida en el argumento, y la de la distribución uniforme es $\frac{a+b}{2}$.


### MM1K
La función MM1K trabaja de la misma manera que MM1, con la salvedad de que en este modelo, la cola es finita, por lo que el parámetro **ql** ya no es *None* como en el anterior, y se define directamente en los parámetros de entrada de la función.
```python    
def MM1K(lamda, mu, ql, user, port_rate, Tsim, bins, directorio):
```

## Histogramas

El simulador provee 3 histogramas: Tiempos de inter-arribos de paquetes, Tiempos de espera de los paquetes y Tiempos de ocupación del sistema.

### Tiempos de inter-arribos de paquetes
Para el caso de los tiempos de inter-arribos de paquetes tenemos que analizar como van a ser servidos los paquetes. Es por eso, que en `modelos.py` se definen

```python    
	debugSink=False #False, muestra en la salida lo que llega al servidor
    rec_arrivalsSink=True #Si es verdadero los arribos se graban
    abs_arrivalsSink=False # true, se graban tiempos de arribo absoluto; False, el tiempo entre arribos consecutivos
    [...]
    psink = PacketSink(env, 
                        debug=debugSink, 
                        rec_arrivals=rec_arrivalsSink, 
                        absolute_arrivals=abs_arrivalsSink)
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

### Tiempos de espera de los paquetes
Para el caso de los tiempos de espera de los paquetes hacemos un análisis similar al de los tiempos de inter-arribo, porque lo vemos con `psink`, pero ahora solicitamos el tiempo de espera que experimentan los paquetes con `psink.waits`. El resto se mantiene igual en el código, pero cambiamos `psink.arrivals` por `psink.waits`.

### Tiempo de ocupación en el sistema
Para el caso de los tiempos de ocupación en el sistema el análisis es parecido a los anteriores. Solo agregamos un monitor en la cola.

```python    
#Parametros del Monitor 
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
Se utiliza `PortMonitor` para controlar el tamaño de la cola a lo largo del tiempo para un `SwitchPort`. Observa la cantidad de elementos en `SwitchPort` en servicio en la cola y registra esa información en la lista de `sizes`. El monitor mira el puerto a intervalos de tiempo dados por la distribución elegida. 

Se especifica una distribución de muestreo, es decir, una distribución que proporcione el tiempo entre muestras sucesivas. Para todos los casos y modelos, se utiliza un distribución exponencial especificando su tasa de arribo. En este caso usamos $\lambda = Smd = 0.5$. Al `SwitchPort` se le da como argumento la tasa de salida de la cola`port_rate`, y el limite de la cola `qlimit`(infinito para todas los modelos, salvo para el M/M/1/K). 

Para graficar el histograma, es bastante parecido a los anteriores, cambia en el argumento `pm.sizes` para trabajar con los tamaños de los paquetes de la cola.
```python    
fig, axis = plt.subplots()
axis.hist(pm.sizes, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
axis.set_title("Tiempos de Ocupación del Sistema - Normalizado")
axis.set_xlabel("Nro")
axis.set_ylabel("Frecuencia de ocurrencia")
fig.savefig(directorio + "QueueHistogram_normal.png")
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUxMDkxNzE3LC0xMjkxMzc0MTA0LC0xMT
YwOTE3MTY0LDE1MjU4MTQ4NDQsLTI4MTI4Njk1NCwtODgxOTYw
MjhdfQ==
-->