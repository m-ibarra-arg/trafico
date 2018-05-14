# Generadores con Python

Este apartado es una introducción al concepto general que nos permite realizar las *simulaciones*.

Un generador es una función que produce una secuencia de resultados en lugar de un único valor.

## ¿Qué son los generadores?

Son funciones que nos permitirán obtener sus resultados poco a poco. Es decir, cada vez que llamemos a la función nos darán un nuevo resultado. Por ejemplo, una función para generar todos los números pares que cada vez que la llamemos nos devuelva el siguiente número par. ¿Podemos construir una función que nos devuelva  **todos**  los números pares? Esto no es posible si no usamos generadores. Como sabemos los números pares son infinitos.

#### ¿PARA QUÉ SIRVEN LOS GENERADORES?

Pues, como el propio nombre indica, para  **generar**  datos en tiempo de ejecución. Además también podemos acelerar búsquedas y crear bucles más rápidos. Por este motivo, utilizar  _range_  es más lento que usar  _xrange_.  _range_  genera todos los valores del rango y los devuelve en un array. En cambio,  _xrange_  genera cada valor del rango cuando se le solicita.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzQ4MjAzLDE4Nzc4Njk4OTcsMTM5NT
IwMjEwOSwtMzEyODkzOTddfQ==
-->