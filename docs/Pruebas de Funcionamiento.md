# Pruebas de Funcionamiento

En la tablas siguientes, haremos la comparación de los resultados de la simulación, calculados como se desarrolló en el apartado *Análisis del Código* y los resultados dados con las fórmulas de rendimiento dadas en *Modelos*.


## M/M/1

### Prueba 01
Estacionario

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^3		|$\rho$		|0.50781	|0.5           
|$Port_{rate}$	|100		|$L$       	|0.84211    |1	           
|$\lambda$   	|1			|$L_q$     	|0.46159	|0.5
|$\mu$      	|2			|$W$       	|0.96940	|1
|$K$          	|$\infty$	|$W_q$     	|0.46159	|0.5
|      			|			|$Loss$ 	|0.0%		|0%

### Prueba 02

Aumentando el tiempo de simulacion

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^4		|$\rho$		|0.49871|0.5           
|$Port_{rate}$	|100		|$L$       	|0.97883    |1	           
|$\lambda$   	|1			|$L_q$     	|0.49032	|0.5
|$\mu$      	|2			|$W$       	|0.98903	|1
|$K$          	|$\infty$	|$W_q$     	|0.49032	|0.5
|      			|			|$Loss$ 	|0.0%		|0%


### Prueba 03
valores mas cercanos

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^4		|$\rho$		|0.80888|0.8           
|$Port_{rate}$	|100		|$L$       	|4.41489    |4	           
|$\lambda$   	|0.8		|$L_q$     	|3.52663	|3.2
|$\mu$      	|1			|$W$       	|5.41938	|5
|$K$          	|$\infty$	|$W_q$     	|4.40828	|4
|      			|			|$Loss$ 	|0.0%		|0%


### Prueba 04
otra vez aumentando tsim
|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$		|0.80150|0.8           
|$Port_{rate}$	|100		|$L$       	|4.00154    |4	           
|$\lambda$   	|0.8		|$L_q$     	|3.22265	|3.2
|$\mu$      	|1			|$W$       	|5.03019	|5
|$K$          	|$\infty$	|$W_q$     	|4.02831	|4
|      			|			|$Loss$ 	|0.0%		|0%


### Prueba 05
no estacionario
diverge el resultado dependiendo del tiempo de sim
|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|2.00922		|2            
|$Port_{rate}$	|100		|$L$    |50164.32158    |negativo	           
|$\lambda$   	|2			|$L_q$  |50205.38164	|negativo
|$\mu$      	|1			|$W$    |25103.69543	|negativo
|$K$          	|$\infty$	|$W_q$  |25102.69082	|negativo
|      			|			|$Loss$	|0.0			|

## M/G/1. Distribución Normal

### Prueba 06

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|0.24000	|  0.24          
|$Port_{rate}$	|100		|$L$    |0.27980    |0.2845	           
|$\lambda$   	|1			|$L_q$  |0.03785	|0.0445
|$Media$      	|3			|$W$    |0.27784	|0.2845
|$\sigma$        |0.1	|$W_q$  |0.03785	|0.0445
| $K$     		|$\infty$			|$Loss$	|0	|0
|  	    		|				|$\mu$	|4.16	|4.1666
mu con ro y lambda definido calculamos la tasa lamda/ro

### Prueba 07
aumentando la varianza
|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|0.24000	|  0.24          
|$Port_{rate}$	|100		|$L$    |0.29104    |1.7582	           
|$\lambda$   	|1			|$L_q$  |0.04981	|1.5182
|$Media$      	|3			|$W$    |0.29019	|1.7582
|$\sigma$        |1.5	|$W_q$  |0.04981	|1.5182
| $K$     		|$\infty$			|$Loss$	|0	|0
|  	    		|				|$\mu$	|4.16	|4.1666
vemos mejor la campana. pero el resultado se aleja de valores teoricos


## M/G/1. Distribución Uniforme

### Prueba 08

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|0.11985	|0.12            
|$Port_{rate}$	|100		|$L$    |0.12952    |0.3807	           
|$\lambda$   	|0.5		|$L_q$  |0.00922	|0.2607
|$Min$      	|1			|$W$    |0.25814	|0.7604
|$Max$        |5	|$W_q$  |0.01844	|0.5214
| $K$     		|$\infty$			|$Loss$	|0	|0
|  	    		|				|$\mu$	|4.1718	|4.1666

### Prueba 09

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$	|0.05999	|0.06            
|$Port_{rate}$	|100		|$L$    |0.06352    |0.0628	           
|$\lambda$   	|0.5		|$L_q$  |0.00201	|0.0028
|$Min$      	|1			|$W$    |0.12399	|0.1257
|$Max$        |2	|$W_q$  |0.00402			|0.0057
| $K$     		|$\infty$	|$Loss$		|0	|0
|  	    		|			|$\mu$	|8.3347	|8.3333

## M/M/1/K

### Prueba 10

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$		|0.83333	|0.8333           
|$Port_{rate}$	|100		|$L$       	|3.58574    |4.5334	           
|$\lambda$   	|10			|$L_q$     	|2.75611	|3.7038
|$\mu$      	|12			|$W$       	|0.36017	|0.4554
|$K$          	|20		|$W_q$     	|0.27684	|0.3720
|      			|			|$Loss$ 	|0.0444%		|0.0444

### Prueba 11

|Valores de la Sim.| | |SimuladorQ    |Teóricos |
|--------|----|----|----|----|
|$Tsim$	      	|10^5		|$\rho$		|1.25000	|1.25           
|$Port_{rate}$	|100		|$L$       	|14.54642    |16.1955	           
|$\lambda$   	|15			|$L_q$     	|13.54875	|15.1978
|$\mu$      	|12			|$W$       	|1.21503	|1.3528
|$K$          	|20		|$W_q$     	|1.13170	|1.2694
|      			|			|$Loss$ 	|3.0279		|3.0279

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk3ODc5Njk5MSwxNDA5Mzg2NjAxLDM0OT
Q2MDg5NiwxMDMzMDUzMDEzLDE4MzM2NjI3MTgsMjEzMzY2MjQy
NywtMTM3ODMwNDAxNSwtOTk2MzE2NTk3LDk5ODM3NjM4MywzNj
M0ODQ4ODgsMjA1MDQwNTM3OSwtMTYwMDE3MDA1NiwtOTkxNDA1
NCwxODc2MjA3MjM3LC0xMjk2NzE0OTc5LDM5MDU4MDkwNSwtMT
EwNjMzNzc5NywxMTExNjk4NzQsLTk4MDQ1MDI3NiwtNjQ5NjA4
NTMyXX0=
-->