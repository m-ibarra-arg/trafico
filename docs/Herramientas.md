#  Herramientas 
Para crear el SimuladorQ se utilizó python como lenguaje de programación, principalmente por las librerías a disposición que existen para la implementación, así también con la integración con Qt para el entorno gráfico. Se desarrollan estas herramientas a continuación.  

## Python
[**Python**](https://www.python.org)  es un  lenguaje de programación  interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible. 

Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, usa tipado dinámico y es multiplataforma. Posee una licencia de  código abierto.

Para la utilización de Python se empleo [**Anaconda**](https://anaconda.org), una distribución orientada a simplificar el despliegue y administración de los paquetes de software, donde las diferentes versiones de los paquetes se administran mediante el sistema de administración de paquetes *conda*, el cual favorece instalar, correr, y actualizar software. 

El entorno de desarrollo integrado (IDE) que se utilizo fue [**Spyder**](https://anaconda.org/anaconda/spyder), incluido en Anaconda. Es multiplataforma de código abierto para programación científica en el lenguaje Python. Spyder integra NumPy, SciPy, Matplotlib e IPython, así como otro software de código abierto. 

## Simpy
[**SimPy**](http://simpy.readthedocs.io/en/latest/index.html) es un entorno de simulación de eventos discretos basado en procesos para Python.

Una simulación de eventos discretos es aquella en la que los cambios de estado de las variables se realizan en puntos discretos del tiempo accionados por eventos. Eventos de simulación típicos pueden incluir la llegada de un cliente, la falla de un recurso, la terminación de una actividad, la finalización de un turno de trabajo.

Los procesos en SimPy están definidos por las funciones [**generator**](https://docs.python.org/3/glossary.html#term-generator) de Python y pueden, por ejemplo, usarse para modelar componentes activos como clientes, vehículos o agentes. SimPy también proporciona varios tipos de recursos compartidos para modelar puntos de congestión de capacidad limitada (como servidores, buffer y túneles).

Las simulaciones se pueden realizar en tiempo real o recorriendo manualmente los eventos.

Entonces, a partir de la funcionalidad que nos brinda SimPy, se piensa en la generación de paquetes desde un generador, el cual nos provee paquetes con atributos como ID, tiempo del paquete, el usuario que lo manda, y principalmente el tamaño, para luego entrar en un buffer, en el cual los paquetes serán servidos de alguna manera para terminar en un sumidero. 

## SimComponents
Si bien SimPy nos da el entorno para simulación discreta de eventos, para poder adentrarnos en las simulaciones de redes y observar el comportamiento de modelos de cola, el [*Dr. Greg Bernstein*](https://www.grotto-networking.com/index.html), docente y especialista en comunicaciones, desarrolló a partir de SimPy, componentes necesarios para esta tarea.  

Nosotros tomamos [*SimComponents.py*](https://www.grotto-networking.com/DiscreteEventPython.html) desarrollado por Bernstein, y agregamos variables de salida para mostrar los resultados en el SimuladorQ.

En definitiva, con los componentes de *SimComponents*, se armaron los modelos M/M/1, M/G/1 (con distribuciones de servicio Uniforme y Normal), y M/M/1/K, los cuales se mostraran en las secciones siguiente, con los resultados de las simulaciones.
 
## Qt
[**Qt**](https://www.qt.io/) es un framework multiplataforma orientado a objetos ampliamente usado para desarrollar programas (software) que utilicen interfaz gráfica de usuario, así como también diferentes tipos de herramientas para la línea de comandos y consolas para servidores que no necesitan una interfaz gráfica de usuario. Es desarrollada como un software libre y de código abierto a través de Qt Project.

Qt utiliza el lenguaje de programación C++ de forma nativa, adicionalmente puede ser utilizado en varios otros lenguajes de programación a través de bindings (adaptación de una librería para ser usada en un lenguaje de programación distinto de aquel en el que ha sido escrita). 

Incluye abstracciones de sockets de red, subprocesos, Unicode, expresiones regulares, bases de datos SQL, SVG, OpenGL, XML, un navegador web completamente funcional, un sistema de ayuda, un marco multimedia, así como una rica colección de widgets GUI.

Las clases Qt emplean un mecanismo de signal / slot para comunicarse entre objetos que es seguro pero, está acoplado de forma flexible, lo que facilita la creación de componentes de software reutilizables.

Qt también incluye Qt Designer, un diseñador gráfico de interfaz de usuario.

## PyQt

[**PyQt**](https://www.riverbankcomputing.com/software/pyqt/intro) es un binding de la biblioteca gráfica Qt para el lenguaje de programación Python. La biblioteca está desarrollada por la firma británica [Riverbank Computing](https://www.riverbankcomputing.com/news) y está disponible para Windows, GNU/Linux y Mac OS X bajo diferentes licencias. 

PyQt puede generar código Python desde Qt Designer. También es posible agregar nuevos controles GUI escritos en Python a Qt Designer.

Python es un lenguaje simple pero poderoso orientado a objetos. Su simplicidad hace que sea fácil de aprender, pero su poder significa que se pueden crear aplicaciones grandes y complejas. 

PyQt combina todas las ventajas de Qt y Python. Un programador tiene todo el poder de Qt, pero es capaz de explotarlo con la simplicidad de Python. Es por todo esto que utilizamos el binding antes mencionado para crear la interfaz gráfica de SimuladorQ.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyOTI2ODY0NzMsMTI3MzE3MTc3OV19
-->