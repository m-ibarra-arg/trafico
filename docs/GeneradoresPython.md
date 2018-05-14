# Generadores con Python

Este apartado es una introducción al concepto general que nos permite realizar las *simulaciones*. 

Un generador es una función que produce una secuencia de resultados en lugar de un único valor.
Es decir, cada vez que llamemos a la función nos darán un nuevo resultado. 

Para construir generadores sólo tenemos que usar la orden **yield**. Esta orden devolverá un valor (igual que hace **return**) pero, además, pasivará la ejecución de la función hasta la próxima vez que le pidamos un valor.

Ejemplo:
```python
def countdown(n):
    print "Counting down from", n
    while n > 0:
        yield n
        n -= 1
    print "Done counting down"
```

La orden **yield** la veremos sobre todo en las librerías de SimComponents, para generar los paquetes y para que sean servidos en la cola.

En definitiva,  genera  datos en tiempo de ejecución. Además también podemos acelerar búsquedas y crear bucles más rápidos. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2OTcxMTI1MDYsLTEzNzQ4MjAzLDE4Nz
c4Njk4OTcsMTM5NTIwMjEwOSwtMzEyODkzOTddfQ==
-->