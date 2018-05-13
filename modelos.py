#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
###########################################################################
                    SIMULADORQ 1.0 -TRABAJO PRACTICO FINAL  
  AUTORES:
        Ibarra, Maximiliano
        Manchado, Joaquín
        
        Estudiantes Ing. en Telecomunicaciones
  
    CONTACTO:        
        maximiliano.a.ibarra@hotmail.com
        jnmanchado@gmail.com
    
  MODIFICADO POR ULTIMA VEZ:
                            16/05/2018
                                                               Tráfico [55]
                                           Ingeniería en Telecomunicaciones
                                                     Facultad de Ingeniería
                                                                       UNRC
###########################################################################
"""
import os
import shutil
import random
import functools
import simpy
import matplotlib.pyplot as plt
from SimComponents import PacketGenerator, PacketSink, SwitchPort, PortMonitor
from PyQt5.QtWidgets import QMessageBox
import sys
import traceback

def MM1(lamda, mu, user, port_rate, Tsim, bins, directorio):
    try:
############# DEFINICION DE LOS PARAMETROS DEL MODELO #########################
    #    Creacion de carpeta temporal para guardar graficos
        if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
        os.mkdir(directorio + 'temp_graficos')
        #Parametros del Sumidero
        debugSink=False #o False, muestra en la salida lo que llega al servidor
        rec_arrivalsSink=True #Si es verdadero los arribos se graban
        abs_arrivalsSink=False # true, se graban tiempos de arribo absoluto; False, el tiempo entre arribos consecutivos

        mu=(mu*8)/port_rate
        
        adist = functools.partial(random.expovariate, lamda) #Tiempo de inter arribo de los paquetes
        sdist = functools.partial(random.expovariate, mu)  # Tamaño de los paquetes 
        
        #Parametros de la Cola
        #       Modela un puerto de salida de conmutador con una tasa dada y un límite de 
        #tamaño de búfer en bytes.
        
        ql=None #byte. Largo de cola infinita
            
        #Parametros del Monitor 
        Smd= 0.5
        samp_dist = functools.partial(random.expovariate,Smd)
        
###############################################################################

############# CREACION DEL ENTORNO Y SUS COMPONENTES  #########################
        
        # Creación del Entorno de Simpy
        env = simpy.Environment()  
        
        # Creación del Generador de Paquetes y Servidor
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
        
        # PortMonitor para rastrear los tamaños de cola a lo largo del tiempo
        pm = PortMonitor(env, 
                         switch_port, 
                         samp_dist)
        
        
###############################################################################

############# CONEXION DE LOS COMPONENTES DEL MODELO  #########################
        
        pg.out = switch_port
        switch_port.out = psink
        
        # Correr la simulacion del entorno. Parametro el tiempo
        env.run(until=Tsim)
    
###############################################################################

############# MUESTRA DE RESULTADOS  ##########################################
        
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
            
###############################################################################

############# GRAFICOS  #######################################################
        directorio = directorio + "temp_graficos/"
#--------- NORMALIZADOS-----------------------------------------------------
        fig, axis = plt.subplots()
        axis.hist(psink.waits, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Espera - Normalizado")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "WaitHistogram_normal.png")
    
        fig, axis = plt.subplots()
        axis.hist(pm.sizes, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Ocupación del Sistema - Normalizado")
        axis.set_xlabel("Nro")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "QueueHistogram_normal.png")
    
        fig, axis = plt.subplots()
        axis.hist(psink.arrivals, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Inter-Arribo a la Cola - Normalizado")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "ArrivalHistogram_normal.png")
    

#---------SIN NORMALIZAR-----------------------------------------------------

        fig, axis = plt.subplots()
        axis.hist(psink.waits, bins, normed=False, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Espera")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia ")
        fig.savefig(directorio + "WaitHistogram.png")
    
        fig, axis = plt.subplots()
        axis.hist(pm.sizes, bins, normed=False, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Ocupación del Sistema")
        axis.set_xlabel("Nro")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "QueueHistogram.png")
    
        fig, axis = plt.subplots()
        axis.hist(psink.arrivals, bins, normed=False, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Inter-Arribo a la Cola")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "ArrivalHistogram.png")
    
        datos = psink.data
        str1 = '&'.join(datos)
        aux_str1=str1
        str1=aux_str1.replace('&','\n')
        aux_str1=str1
        str1=(aux_str1.replace(',','  \t  '))
        
        return str1, espera_sist_W, pkt_drop, pkt_enviados, tasa_perdida, ocup_sistema_L , pkt_recibidos_serv, intensidad_trafico, espera_cola_Wq, ocup_cola_Lq
    
    except:
        error = traceback.format_exc()
        QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)
        sys.exit(0)
        
def MG1(lamda, G, a, b, user, port_rate, Tsim, bins, directorio):
    try:
        plt.close('all')    
        
############# DEFINICION DE LOS PARAMETROS DEL MODELO #########################
        #    Creacion de carpeta temporal para guardar graficos
        if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
        os.mkdir(directorio + 'temp_graficos')
        #Parametros del Sumidero
        debugSink=False #o False, muestra en la salida lo que llega al servidor
        rec_arrivalsSink=True #Si es verdadero los arribos se graban
        abs_arrivalsSink=False # true, se graban tiempos de arribo absoluto; False, el tiempo entre arribos consecutivos
        
        #Parametros del Generador de Paquetes. 
        
        adist = functools.partial(random.expovariate, lamda) #Tiempo de inter arribo de los paquetes
        if G==1:
            sdist = functools.partial(random.normalvariate, a, b)  # Tamaño de los paquetes. media y desviacion standar 
        elif G==2:
            sdist = functools.partial(random.uniform, a, b)  
        
        #Parametros de la Cola
        #       Modela un puerto de salida de conmutador con una tasa dada y un límite de 
        #tamaño de búfer en bytes.
        
        ql=None #byte
        
        #Parametros del Monitor 
        Smd= 0.5
        samp_dist = functools.partial(random.expovariate,Smd)
        
###############################################################################

############# CREACION DEL ENTORNO Y SUS COMPONENTES  #########################
        
        # Creación del Entorno de Simpy
        env = simpy.Environment()  
        
        # Creación del Generador de Paquetes y Servidor
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
        
        # PortMonitor para rastrear los tamaños de cola a lo largo del tiempo
        pm = PortMonitor(env, 
                         switch_port, 
                         samp_dist)
        
        
###############################################################################

############# CONEXION DE LOS COMPONENTES DEL MODELO  #########################
        
        pg.out = switch_port
        switch_port.out = psink
        
        
        # Correr la simulacion del entorno. Paramatro el tiempo
        env.run(until=Tsim)
        
###############################################################################

############# MUESTRA DE RESULTADOS  ##########################################
        
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
      
###############################################################################

############# GRAFICOS  #######################################################
        directorio = directorio + "temp_graficos/"
#--------- NORMALIZADOS -----------------------------------------------------
        fig, axis = plt.subplots()
        axis.hist(psink.waits, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Espera - Normalizado")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "WaitHistogram_normal.png")
    
        fig, axis = plt.subplots()
        axis.hist(pm.sizes, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Ocupación del Sistema - Normalizado")
        axis.set_xlabel("Nro")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "QueueHistogram_normal.png")
    
        fig, axis = plt.subplots()
        axis.hist(psink.arrivals, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Inter-Arribo a la Cola - Normalizado")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "ArrivalHistogram_normal.png")
    
        
#---------SIN NORMALIZAR-----------------------------------------------------
        fig, axis = plt.subplots()
        axis.hist(psink.waits, bins, normed=False, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Espera")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia ")
        fig.savefig(directorio + "WaitHistogram.png")
    
        fig, axis = plt.subplots()
        axis.hist(pm.sizes, bins, normed=False, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Ocupación del Sistema")
        axis.set_xlabel("Nro")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "QueueHistogram.png")
    
        fig, axis = plt.subplots()
        axis.hist(psink.arrivals, bins, normed=False, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Inter-Arribo a la Cola")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "ArrivalHistogram.png")
    
        datos = psink.data
        str1 = '&'.join(datos)
        aux_str1=str1
        str1=aux_str1.replace('&','\n')
        aux_str1=str1
        str1=(aux_str1.replace(',','  \t  '))
    
        return str1, espera_sist_W, pkt_drop, pkt_enviados, tasa_perdida, ocup_sistema_L , pkt_recibidos_serv, intensidad_trafico, espera_cola_Wq, ocup_cola_Lq
    
    except:
        error = traceback.format_exc()
        QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)
#        sys.exit(0)
        
def MM1K(lamda, mu, ql, user, port_rate, Tsim, bins, directorio):
    try:    
        plt.close('all')    
        
############# DEFINICION DE LOS PARAMETROS DEL MODELO #########################
        #    Creacion de carpeta temporal para guardar graficos
        if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
        os.mkdir(directorio + 'temp_graficos')
        #Parametros del Sumidero
        debugSink=False #o False, muestra en la salida lo que llega al servidor
        rec_arrivalsSink=True #Si es verdadero los arribos se graban
        abs_arrivalsSink=False # true, se graban tiempos de arribo absoluto; False, el tiempo entre arribos consecutivos
          
        #Parametros del Generador de Paquetes. 
        mu_paq=((mu*8)/port_rate)
        
        adist = functools.partial(random.expovariate, lamda) #Tiempo de inter arribo de los paquetes
        sdist = functools.partial(random.expovariate, mu_paq)  # Tamaño de los paquetes 
        
        #Parametros del Monitor 
        Smd= lamda
        samp_dist = functools.partial(random.expovariate,Smd)
        
###############################################################################

############# CREACION DEL ENTORNO Y SUS COMPONENTES  #########################
        
        # Creación del Entorno de Simpy
        env = simpy.Environment()  
        
        # Creación del Generador de Paquetes y Servidor
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
        
        # PortMonitor para rastrear los tamaños de cola a lo largo del tiempo
        pm = PortMonitor(env, switch_port, samp_dist, count_bytes=True)
            
###############################################################################

############# CONEXION DE LOS COMPONENTES DEL MODELO  #########################
        
        pg.out = switch_port
        switch_port.out =psink
           
        # Correr la simulacion del entorno. Paramatro el tiempo
        env.run(until=Tsim)
        
###############################################################################

############# MUESTRA DE RESULTADOS  ##########################################
    
        pkt_drop=switch_port.packets_drop
        pkt_recibidos_serv = psink.packets_rec
        pkt_enviados=pg.packets_sent
        ocup_sistema_L=float(sum(pm.sizes))/len(pm.sizes)
        intensidad_trafico = lamda/mu
        if lamda != mu:
            pk=(((1-intensidad_trafico)*intensidad_trafico**(ql))/(1-intensidad_trafico**(ql+1)))
        else:
            pk=1/(ql+1)
    
        lamda_eficaz = lamda*(1-pk)
        espera_sist_W = ocup_sistema_L / lamda_eficaz
        espera_cola_Wq = espera_sist_W - 1/mu
        ocup_cola_Lq = espera_cola_Wq * lamda_eficaz 
        tasa_perdida = lamda * pk
        
###############################################################################

############# GRAFICOS  #######################################################
        directorio = directorio + "temp_graficos/"
#--------- NORMALIZADOS-----------------------------------------------------
        fig, axis = plt.subplots()
        axis.hist(psink.waits, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Espera - Normalizado")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "WaitHistogram_normal.png")
    
        fig, axis = plt.subplots()
        axis.hist(pm.sizes, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Ocupación del Sistema - Normalizado")
        axis.set_xlabel("Nro")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "QueueHistogram_normal.png")
    
        fig, axis = plt.subplots()
        axis.hist(psink.arrivals, bins, normed=True, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Inter-Arribo a la Cola - Normalizado")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "ArrivalHistogram_normal.png")
    
        
#---------SIN NORMALIZAR-----------------------------------------------------
        fig, axis = plt.subplots()
        axis.hist(psink.waits, bins, normed=False, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Espera")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia ")
        fig.savefig(directorio + "WaitHistogram.png")
    
        fig, axis = plt.subplots()
        axis.hist(pm.sizes, bins, normed=False, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Ocupación del Sistema")
        axis.set_xlabel("Nro")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "QueueHistogram.png")
    
        fig, axis = plt.subplots()
        axis.hist(psink.arrivals, bins, normed=False, alpha=1, edgecolor = 'black',  linewidth=1)
        axis.set_title("Tiempos de Inter-Arribo a la Cola")
        axis.set_xlabel("Tiempo")
        axis.set_ylabel("Frecuencia de ocurrencia")
        fig.savefig(directorio + "ArrivalHistogram.png")
    
        datos = psink.data
        str1 = '&'.join(datos)
        aux_str1=str1
        str1=aux_str1.replace('&','\n')
        aux_str1=str1
        str1=(aux_str1.replace(',','  \t  '))
    
        return str1, espera_sist_W, pkt_drop, pkt_enviados, tasa_perdida, ocup_sistema_L , pkt_recibidos_serv, intensidad_trafico, espera_cola_Wq, ocup_cola_Lq
    
    except:
        error = traceback.format_exc()
        QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)
        sys.exit(0)