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

"""
CODIGO PARA EJECUTAR PROGRAMA
Levanta la interfaz grafica y desde este mismo script se asignan botones y 
funciones. La interfaz grafica es generada y modificada con Qt Designer.
"""

from PyQt5 import QtGui, uic, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPixmap
from modelos import MM1, MG1, MM1K
from funciones_externas import openFileNameDialog, saveFileDialog, setFolderDialog, doc_python_web, doc_simpy_web, doc_pyqt_web, doc_simuladorQ_web, gen_corutinas_web, tuto_pyqt_web, tuto_python_web
import sys
import os
import shutil
import time
import traceback

qtCreatorFile_main = "SimuladorQ.ui"
qtCreatorFile_mm1 = "entrada_salida_MM1.ui"  
qtCreatorFile_mg1 = "entrada_salida_MG1.ui" 
qtCreatorFile_mm1k = "entrada_salida_MM1K.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile_main) 
Ui_entrada_salida_mm1, QtBaseClass = uic.loadUiType(qtCreatorFile_mm1)
Ui_entrada_salida_mg1, QtBaseClass = uic.loadUiType(qtCreatorFile_mg1)
Ui_entrada_salida_mm1k, QtBaseClass = uic.loadUiType(qtCreatorFile_mm1k)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow): 
    def __init__(self): 
        try:
            QtWidgets.QMainWindow.__init__(self) 
            Ui_MainWindow.__init__(self) 
            self.setupUi(self) 
            self.move(475,200)
            
            directorio = os.getcwd() + '/'
            pixmap = QPixmap(directorio  + "Im/logo simulatorQ_titulo.png")
            self.label_titulo.setPixmap(pixmap) 
            
            self.texto_descripcion.setOpenExternalLinks(True)
            
    #---------------------------FUNCIONALIDAD BOTONES ----------------------------
            self.push_confirmar.clicked.connect(self.open_modelos)
            self.radio_mm1.clicked.connect(self.cargar_descripcion)
            self.radio_mg1.clicked.connect(self.cargar_descripcion)
            self.radio_mm1k.clicked.connect(self.cargar_descripcion)
    #-----------------------------------------------------------------------------
    #-------------------------------- MENU AYUDA ---------------------------------
            self.actionSobre_Python.triggered.connect(doc_python_web)
            self.actionSimpy.triggered.connect(doc_simpy_web)
            self.actionSobre_PyQt.triggered.connect(doc_pyqt_web)
            self.actionSobre_SimuladorQ.triggered.connect(doc_simuladorQ_web)
            self.actionAcerca_de_SimuladorQ.triggered.connect(self.acerca_de)
            self.actionTutorial_Python.triggered.connect(tuto_python_web)
            self.actionTutorial_PyQt.triggered.connect(tuto_pyqt_web)
            self.actionGeneradores_y_corutinas_Python.triggered.connect(gen_corutinas_web)
        except PermissionError:
            QMessageBox.critical(self, 'Error de ejecucion',"Revise la documentacion del programa.", QtWidgets.QMessageBox.Ok)
            sys.exit(0)
        except:
            error = traceback.format_exc()
            QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)
            sys.exit(0)
            
#-----------------------------------------------------------------------------
#---------------------------------FUNCIONES-----------------------------------
    def openWindow_mm1(self):
        self.anotherwindow = MyApp_mm1()
        self.anotherwindow.showMaximized()
        self.hide()
    def openWindow_mg1(self):
        self.anotherwindow = MyApp_mg1()
        self.anotherwindow.showMaximized()
        self.hide()
    def openWindow_mm1k(self):
        self.anotherwindow = MyApp_mm1k()
        self.anotherwindow.showMaximized()
        self.hide()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',"¿Está seguro que desea salir?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def cargar_descripcion (self):
        if self.radio_mm1.isChecked() == True:
            self.texto_descripcion.toHtml()
            self.texto_descripcion.setText('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Modelo M/M/1</span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· Tanto los tiempos de llegada de los clientes como los tiempos de servicio son exponenciales e independientes entre sí.</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· El sistema tiene un único servidor.</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· La disciplina de servicio es FIFO (First In First Out).</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· La capacidad del sistema infinita de clientes.</p></body></html>''')

        elif self.radio_mg1.isChecked() == True:
            self.texto_descripcion.toHtml()
            self.texto_descripcion.setText('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Modelo M/G/1</span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· Las llegadas se producen según un proceso de Poisson de tasa λ.</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· El sistema tiene un único servidor.</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· La disciplina de servicio es FIFO (First In First Out).</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· Los clientes tienen Tiempos de servicio no exponencial, independientes e idénticamente distribuidos de media 1\μ y varianza σ^2.</p></body></html>''')
            
            
        elif self.radio_mm1k.isChecked() == True:
            self.texto_descripcion.toHtml()
            self.texto_descripcion.setText('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;">
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600;">Modelo M/M/1/K</span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· Tiempos de arribo y de servicio de los clientes son exponenciales e independientes entre sí.</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· El sistema tiene un único servidor.</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· Disciplina de servicio FIFO (First In First Out).</p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">· Es una variante del modelo M/M/1, que se basa en suponer que la capacidad del sistema está limitada a K clientes.</p></body></html>''')
            
    def open_modelos(self):
        if self.radio_mm1.isChecked() == False and self.radio_mg1.isChecked() == False and self.radio_mm1k.isChecked() == False:
            QtWidgets.QMessageBox.warning(self, 'Atención',"Primero seleccione algun modelo.", QtWidgets.QMessageBox.Ok)
        else:    
            if self.radio_mm1.isChecked() == True:
                self.openWindow_mm1()
            elif self.radio_mg1.isChecked() == True:
                self.openWindow_mg1()
            elif self.radio_mm1k.isChecked() == True:
                self.openWindow_mm1k()
        
    def acerca_de(self):
        QMessageBox.information(self, 'Acerca de SimuladorQ',"<a href='http://simuladorq.readthedocs.io/'>SimuladorQ</a> es un simulador de modelos de colas, el cual nos permitirá introducir parámetros de entrada característicos de cada uno de los modelos que se proponen, y obtener valores medios e histogramas del comportamiento de los mismos.<br><br>Por problemas de software, por favor dirijase a nuestro sitio de Github, o bien a la documentacion del programa.<br><br>Desarrollo del código:<br><a href='https://www.python.org/'>Python</a> 3.6.4 64bits, <a href='https://www.qt.io/'>Qt</a>  5.6.2 y <a href='https://riverbankcomputing.com/software/pyqt/intro'>PyQt</a> 5.6, en Linux y MacOS.<br><br>Creado por Maximiliano Ibarra y Joaquín Manchado, en el marco del Trabajo Final de la asignatura Trafico [55], perteneciente al plan de estudios de la carrera <a href='https://www.ing.unrc.edu.ar/grado-teleco.php'>Ingeniería en Telecomunicaciones</a> , Facultad de Ingeniería, UNRC.", QMessageBox.Ok)

#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#--------------------------------CLASE MM1------------------------------------
#-----------------------------------------------------------------------------            
class MyApp_mm1(QtWidgets.QMainWindow, Ui_entrada_salida_mm1): 
    def __init__(self): 
        try:
            QtWidgets.QMainWindow.__init__(self) 
            Ui_entrada_salida_mm1.__init__(self) 
            self.setupUi(self)
    
            directorio = os.getcwd() + '/'
            pixmap = QPixmap(directorio  + "Im/logo_simulatorQ-reemplazo.png")
            self.label_imagen.setPixmap(pixmap)         
    #---------------------------VALIDAR DATOS DE ENTRADA---------------------------
            self.line_lambda.setValidator(QtGui.QDoubleValidator())      
            self.line_mu.setValidator(QtGui.QDoubleValidator())
            self.line_portrate.setValidator(QtGui.QDoubleValidator())
            self.line_tsim.setValidator(QtGui.QDoubleValidator())
    #------------------------FUNCIONALIDAD BOTONES --------------------------------              
            self.push_reset.clicked.connect(self.resetear)
            self.push_simular.clicked.connect(self.simular)
            
            self.comboBox_norm.currentIndexChanged['int'].connect(self.graficos)
            self.radio_tinter_arribo.clicked.connect(self.graficos)
            self.radio_tespera.clicked.connect(self.graficos)
            self.radio_tocup_sist.clicked.connect(self.graficos)
    #---------------------------------MENU BAR------------------------------------
    #        Archivo        
            self.actionRegresar.triggered.connect(self.open_back)
            self.actionReiniciar_2.triggered.connect(self.reinicio)
            self.actionImportar_datos.triggered.connect(self.importar)
            self.actionParametros_de_entrada.triggered.connect(self.guardar_entrada)
            self.actionParametros_de_salida.triggered.connect(self.guardar_salida)
            self.actionInformacion_de_secuencia_de_paquetes.triggered.connect(self.guardar_paquetes)
            self.actionTodo.triggered.connect(self.guardar_todo)
            self.actionSalir.triggered.connect(self.salir_programa)
    #        Simulacion
            self.actionCorrer_simulacion.triggered.connect(self.simular)
            self.actionResetear_parametros.triggered.connect(self.limpiar)
    #        Ayuda
            self.actionSobre_Python_2.triggered.connect(doc_python_web)
            self.actionSimpy.triggered.connect(doc_simpy_web)
            self.actionSobre_PyQt5_2.triggered.connect(doc_pyqt_web)
            self.actionSobre_SimuladorQ.triggered.connect(doc_simuladorQ_web)
            self.actionAcerca_de_SimuladorQ.triggered.connect(self.acerca_de)
            self.actionTutorial_Python.triggered.connect(tuto_python_web)
            self.actionTutorial_PyQt.triggered.connect(tuto_pyqt_web)
            self.actionGeneradores_y_corutinas_Python.triggered.connect(gen_corutinas_web)
        except PermissionError:
            QMessageBox.critical(self, 'Error de ejecucion',"Revise la documentacion del programa.", QtWidgets.QMessageBox.Ok)
            sys.exit(0)
        except:
            error = traceback.format_exc()
            QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)
            sys.exit(0)
#------------------------------------------------------------------------------
#----------------------------- FUNCIONES -------------------------------------
    def acerca_de(self):
        QMessageBox.information(self, 'Acerca de SimuladorQ',"<a href='http://simuladorq.readthedocs.io/'>SimuladorQ</a> es un simulador de modelos de colas, el cual nos permitirá introducir parámetros de entrada característicos de cada uno de los modelos que se proponen, y obtener valores medios e histogramas del comportamiento de los mismos.<br><br>Por problemas de software, por favor dirijase a nuestro sitio de Github, o bien a la documentacion del programa.<br><br>Desarrollo del código:<br><a href='https://www.python.org/'>Python</a> 3.6.4 64bits, <a href='https://www.qt.io/'>Qt</a>  5.6.2 y <a href='https://riverbankcomputing.com/software/pyqt/intro'>PyQt</a> 5.6, en Linux y MacOS.<br><br>Creado por Maximiliano Ibarra y Joaquín Manchado, en el marco del Trabajo Final de la asignatura Trafico [55], perteneciente al plan de estudios de la carrera <a href='https://www.ing.unrc.edu.ar/grado-teleco.php'>Ingeniería en Telecomunicaciones</a>, Facultad de Ingeniería, UNRC.", QMessageBox.Ok)
        
    def reinicio(self):
        self.resetear()
        
        self.line_twait_medio.setText("")
        self.line_espera_cola_Wq.setText("")
        self.line_inten_trafico.setText("")
        self.line_ocup_cola_Lq.setText("")
        self.line_pkt_drop.setText("")
        self.line_pkt_enviados.setText("")
        self.line_pkt_recibidos.setText("")
        self.line_tasa_perdida.setText("")
        self.line_ocup_sistema.setText("")
        
        self.text_consola.setTextColor(QtGui.QColor("white"))
        self.text_consola.setFont(QtGui.QFont(u'Ubuntu', 11))
        self.text_consola.setText("Información detallada de paquetes servidos.\nEstado actual: Esperando...")
        
        self.label_imagen.setStyleSheet("background-color: rgb(138, 146, 179);")
        directorio = os.getcwd() + '/'
        pixmap = QPixmap(directorio  + "Im/logo_simulatorQ-reemplazo.png")
        self.label_imagen.setPixmap(pixmap)
        
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',"¿Está seguro que desea salir?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            directorio = os.getcwd() + '/'
            if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
            event.accept()
        else:
            event.ignore()
        
    def salir_programa(self):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',"¿Está seguro que desea salir?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            directorio = os.getcwd() + '/'
            if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
            sys.exit(0)
        
    def limpiar(self):
        self.resetear()

    def guardar_entrada(self):
        try:
            path_archivo, path_folder = saveFileDialog()
            fichero = open(path_archivo, 'w+')
            cod = 1
        except(PermissionError):
                QMessageBox.critical(self, 'Error al guardar',"No tiene los permisos necesarios para guardar el archivo en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                cod = 0
                exit
        if path_archivo == "" or cod == 0:
            exit
        else:        
            lamda = (self.line_lambda.text())
            mu = (self.line_mu.text())
            user = (self.line_user.text())
            portrate = (self.line_portrate.text())
            tsim = (self.line_tsim.text())
            bins = (self.comboBox_bins.currentText())
            
            if lamda == "" or mu == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                fichero.close()
                if os.path.isfile(path_archivo):
                    os.remove(path_archivo)
                exit
            else:    
                modelo = "MM1"
                parametros=[modelo, lamda, mu, user, portrate, tsim, bins, path_folder]
                for items in range(len(parametros)):
                    fichero.write("{}\n".format(parametros[items]))
                fichero.close()

    def guardar_salida(self):
        try:
            path_archivo, path_folder = saveFileDialog()
            fichero = open(path_archivo, 'w+')
            cod = 1
        except(PermissionError):
                QMessageBox.critical(self, 'Error al guardar',"No tiene los permisos necesarios para guardar el archivo en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                cod = 0
                exit
        if path_archivo == "" or cod == 0:
            exit
        else:
            lamda = (self.line_lambda.text())
            mu = (self.line_mu.text())
            user = (self.line_user.text())
            portrate = (self.line_portrate.text())
            tsim = (self.line_tsim.text())
            bins = (self.comboBox_bins.currentText())
            if lamda == "" or mu == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                fichero.close()
                if os.path.isfile(path_archivo):
                    os.remove(path_archivo)
                exit
            else:
                parametros_in=[lamda, mu, user, portrate, tsim, bins]
                labels_in = [self.label_lambda.text(), self.label_mu.text(), self.label_user.text(), self.label_portrate.text(), self.label_tsim.text(), self.label_bins.text()]
                cont = 0
                largo_max_in = 0
                for cont in range(len(labels_in)):
                    largo=len(labels_in[cont])
                    if largo_max_in <= largo:
                        largo_max_in = largo
        
                t_wait_medio = (self.line_twait_medio.text())
                pkt_enviados = (self.line_pkt_enviados.text())
                pkt_drop = (self.line_pkt_drop.text())
                pkt_recibidos = (self.line_pkt_recibidos.text())
                tasa_perdida = (self.line_tasa_perdida.text())
                ocup_sistema = (self.line_ocup_sistema.text())
                intensidad_trafico = (self.line_inten_trafico.text())
                espera_cola_Wq = self.line_espera_cola_Wq.text()
                ocup_cola_Lq = self.line_ocup_cola_Lq.text()
                
                if t_wait_medio == "":
                    QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación", QtWidgets.QMessageBox.Ok)
                    fichero.close()
                    if os.path.isfile(path_archivo):
                        os.remove(path_archivo)
                    exit        
                else:
                    parametros_out=[t_wait_medio, espera_cola_Wq, pkt_enviados, pkt_recibidos, pkt_drop, tasa_perdida, ocup_cola_Lq, ocup_sistema, intensidad_trafico]
                    labels_out = [self.label_twait_medio.text(), self.label_espera_cola_Wq.text(), self.label_pkt_enviados.text(), self.label_pkt_recibidos.text(), self.label_pkt_drop.text(), self.label_tasa_perdida.text(), self.label_ocup_cola_Lq.text(), self.label_ocup_sistema.text(), self.label_inten_trafico.text()]
                    cont = 0
                    largo_max_out = 0
                    for cont in range(len(labels_out)):
                        largo=len(labels_out[cont])
                        if largo_max_out <= largo:
                            largo_max_out = largo
        
                    fichero.write("RESULTADOS DE LA SIMULACION\n\n")
                    fichero.write("   #   Parámetros en la entrada del simulador\n\n")
                    items_in=0
                    for items_in in range(len(parametros_in)):
                        fichero.write(labels_in[items_in] + " " * (largo_max_in-len(labels_in[items_in])) + "    ")
                        fichero.write("{}\n".format(parametros_in[items_in]))
                    fichero.write("\n\n")
                    fichero.write("   #   Parámetros de salida del simulador\n\n")
                    items_out = 0
                    for items_out in range(len(parametros_out)):
                        fichero.write(labels_out[items_out] + " " * (largo_max_out-len(labels_out[items_out])) + "    ")
                        fichero.write("{}\n".format(parametros_out[items_out]))
                    fichero.close()

    def guardar_paquetes(self):
        try:
            path_archivo, path_folder = saveFileDialog()
            fichero = open(path_archivo, 'w+')
            cod = 1
        except(PermissionError):
                QMessageBox.critical(self, 'Error al guardar',"No tiene los permisos necesarios para guardar el archivo en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                cod = 0
                exit
        if path_archivo == "" or cod == 0:
            exit
        else:
            lamda = (self.line_lambda.text())
            mu = (self.line_mu.text())
            user = (self.line_user.text())
            portrate = (self.line_portrate.text())
            tsim = (self.line_tsim.text())
            bins = (self.comboBox_bins.currentText())
            if lamda == "" or mu == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                fichero.close()
                if os.path.isfile(path_archivo):
                    os.remove(path_archivo)
                exit
            else:
                parametros_in=[lamda, mu, user, portrate, tsim, bins]
                labels_in = [self.label_lambda.text(), self.label_mu.text(), self.label_user.text(), self.label_portrate.text(), self.label_tsim.text(), self.label_bins.text()]
                cont = 0
                largo_max_in = 0
                for cont in range(len(labels_in)):
                    largo=len(labels_in[cont])
                    if largo_max_in <= largo:
                        largo_max_in = largo
                        
                texto = self.text_consola.toPlainText()
                if texto == "Información detallada de paquetes servidos.\nEstado actual: Esperando..." :
                    QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación.", QtWidgets.QMessageBox.Ok)
                    fichero.close()
                    if os.path.isfile(path_archivo):
                        os.remove(path_archivo)                
                    exit
                else:
                    fichero.write("DETALLE DE LOS PAQUETES SERVIDOS\n\n")
                    fichero.write("   #   Parámetros en la entrada del simulador\n\n")
                    items_in=0
                    for items_in in range(len(parametros_in)):
                        fichero.write(labels_in[items_in] + " " * (largo_max_in-len(labels_in[items_in])) + "    ")
                        fichero.write("{}\n".format(parametros_in[items_in]))
                    fichero.write("\n\n")
                    fichero.write("   #   ")
                    fichero.write("{}\n".format(texto))
                    fichero.close()
        
    def guardar_todo(self):
        try:
            path_folder = setFolderDialog()
        except(PermissionError):
                QMessageBox.critical(self, 'Error al crear carpeta',"No tiene los permisos necesarios para crear la carpeta en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                exit
        if path_folder == "":
            exit
        else:
            tiempo_creacion = time.strftime("%d-%m-%y") + " _ " + time.strftime("%H-%M-%S")
            dir_sim_new = path_folder + 'SimuladorQ-MM1 __ ' + tiempo_creacion 
            try:
                os.makedirs(dir_sim_new)
                fichero = open (dir_sim_new + '/MM1_outfile.txt', 'w+')
            
                fichero.write("SIMULADORQ 1.0\n\n")
                fichero.write("Simulacion realizada: ")
                fichero.write(time.strftime("%x") + " - " + time.strftime("%X") + "hs" +'\n')
                fichero.write("Modelo utilizado en la simulacion: M/M/1\n\n")
        
                lamda = (self.line_lambda.text())
                mu = (self.line_mu.text())
                user = (self.line_user.text())
                portrate = (self.line_portrate.text())
                tsim = (self.line_tsim.text())
                bins = (self.comboBox_bins.currentText())
                if lamda == "" or mu == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                    QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                    fichero.close()
                    if os.path.isfile(dir_sim_new + '/MM1_outfile.txt'):
                        os.remove(dir_sim_new + '/MM1_outfile.txt')
                        shutil.rmtree(dir_sim_new)
                    exit
                else:
                    parametros_in=[lamda, mu, user, portrate, tsim, bins]
                    labels_in = [self.label_lambda.text(), self.label_mu.text(), self.label_user.text(), self.label_portrate.text(), self.label_tsim.text(), self.label_bins.text()]
                    cont = 0
                    largo_max_in = 0
                    for cont in range(len(labels_in)):
                        largo=len(labels_in[cont])
                        if largo_max_in <= largo:
                            largo_max_in = largo
                    
                    fichero.write("   #   Parámetros en la entrada del simulador\n\n")
                    items_in=0
                    for items_in in range(len(parametros_in)):
                        fichero.write(labels_in[items_in] + " " * (largo_max_in-len(labels_in[items_in])) + "    ")
                        fichero.write("{}\n".format(parametros_in[items_in]))
                    fichero.write("\n\n")
                    
                    
                    t_wait_medio = (self.line_twait_medio.text())
                    pkt_enviados = (self.line_pkt_enviados.text())
                    pkt_drop = (self.line_pkt_drop.text())
                    pkt_recibidos = (self.line_pkt_recibidos.text())
                    tasa_perdida = (self.line_tasa_perdida.text())
                    ocup_sistema = (self.line_ocup_sistema.text())
                    intensidad_trafico = (self.line_inten_trafico.text())
                    espera_cola_Wq = self.line_espera_cola_Wq.text()
                    ocup_cola_Lq = self.line_ocup_cola_Lq.text()
                    if t_wait_medio == "":
                        QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación", QtWidgets.QMessageBox.Ok)
                        fichero.close()
                        if os.path.isfile(dir_sim_new + '/MM1_outfile.txt'):
                            os.remove(dir_sim_new + '/MM1_outfile.txt')
                            shutil.rmtree(dir_sim_new)
                        exit        
                    else:
                        parametros_out=[t_wait_medio, espera_cola_Wq, pkt_enviados, pkt_recibidos, pkt_drop, tasa_perdida, ocup_cola_Lq, ocup_sistema, intensidad_trafico]
                        labels_out = [self.label_twait_medio.text(), self.label_espera_cola_Wq.text(), self.label_pkt_enviados.text(), self.label_pkt_recibidos.text(), self.label_pkt_drop.text(), self.label_tasa_perdida.text(), self.label_ocup_cola_Lq.text(), self.label_ocup_sistema.text(), self.label_inten_trafico.text()]
                        cont = 0
                        largo_max_out = 0
                        for cont in range(len(labels_out)):
                            largo=len(labels_out[cont])
                            if largo_max_out <= largo:
                                largo_max_out = largo
                                
                        fichero.write("   #   Parámetros de salida del simulador\n\n")
                        items_out = 0
                        for items_out in range(len(parametros_out)):
                            fichero.write(labels_out[items_out] + " " * (largo_max_out-len(labels_out[items_out])) + "    ")
                            fichero.write("{}\n".format(parametros_out[items_out]))
                        
                        texto = self.text_consola.toPlainText()       
                        
                        fichero.write("\n\n")
                        fichero.write("   #   ")
                        fichero.write("{}\n".format(texto))
                        fichero.close()
                        
                        directorio = dir_sim_new + '/'
                        directorio_actual = os.getcwd() + '/temp_graficos/'
                        
                        os.makedirs(directorio + 'Graficos Normalizados')
                        shutil.copy(directorio_actual + 'WaitHistogram_normal.png', directorio + 'Graficos Normalizados/WaitHistogram_normal.png')
                        shutil.copy(directorio_actual + 'ArrivalHistogram_normal.png', directorio + 'Graficos Normalizados/ArrivalHistogram_normal.png')
                        shutil.copy(directorio_actual + 'QueueHistogram_normal.png', directorio + 'Graficos Normalizados/QueueHistogram_normal.png')
                        
                        os.makedirs(directorio + 'Graficos No Normalizados')
                        shutil.copy(directorio_actual + 'WaitHistogram.png', directorio + 'Graficos No Normalizados/WaitHistogram.png')
                        shutil.copy(directorio_actual + 'ArrivalHistogram.png', directorio + 'Graficos No Normalizados/ArrivalHistogram.png')
                        shutil.copy(directorio_actual + 'QueueHistogram.png', directorio + 'Graficos No Normalizados/QueueHistogram.png')
            except(PermissionError):
                    QMessageBox.critical(self, 'Error al crear carpeta',"No tiene los permisos necesarios para crear la carpeta en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                    exit
        
    def resetear(self):
        self.comboBox_bins.setCurrentText('Seleccione')   
        self.line_lambda.setText("")
        self.line_mu.setText("")
        self.line_portrate.setText("")
        self.line_user.setText("")
        self.line_tsim.setText("")
        
    def importar(self):
        path_archivo, directorio = openFileNameDialog()
        if path_archivo == "" and directorio == "":
            QMessageBox.warning(None, 'No se pudo importar', "Debe seleccionar un archivo.", QMessageBox.Ok)
            exit
        else:
            fichero = open (path_archivo, 'r')
            modelo = "MM1"
            prueba = str(fichero.readline())
            prueba = prueba.replace('\n','')
            if prueba == modelo:
    #            Parametros necesarios para MM1 = 6
                linea_fin = 6 
                parametros = [0] * linea_fin
                for linea in range(linea_fin):
                    parametros[linea] = str(fichero.readline())
                    parametros[linea] = parametros[linea].replace('\n','')
                    parametros[linea] = str(parametros[linea])    
                fichero.close()
            
                self.line_lambda.setText(parametros[0])
                self.line_mu.setText(parametros[1])
                self.line_user.setText(parametros[2])
                self.line_portrate.setText(parametros[3])
                self.line_tsim.setText(parametros[4])
                self.comboBox_bins.setCurrentText(parametros[5])
            else:
                QMessageBox.critical(None, 'No se pudo importar', "Archivo inválido.             ", QMessageBox.Ok)
                fichero.close()
                exit

    def open_back(self):       
        self.anotherwindow = MyApp()
        self.anotherwindow.show()
        self.hide()
        
    def simular (self):
        if self.line_lambda.text() == "" or self.line_mu.text() == "" or self.line_user.text() == "" or self.line_portrate.text() == "" or self.line_tsim.text() == "" or self.comboBox_bins.currentText() == "Seleccione":
            QMessageBox.critical(None, 'Simulación fallida', "Faltan ingresar parámetros de entrada.", QMessageBox.Ok)
        elif float(self.line_lambda.text()) < 0 or float(self.line_mu.text()) < 0 or float(self.line_portrate.text()) < 0 or int(self.line_tsim.text()) < 0:
            QMessageBox.warning(None, 'Atención', "Ingreso de datos negativos. Utilice valores mayores a cero.", QMessageBox.Ok)
        else:
            lamda = float(self.line_lambda.text())
            mu = float(self.line_mu.text())
            user = (self.line_user.text())
            portrate = float(self.line_portrate.text())
            tsim = float(self.line_tsim.text())
            bins = int(self.comboBox_bins.currentText())
            directorio = os.getcwd() + '/'
            
            datos, twait_medio, pkt_drop, pkt_enviados, tasa_perdida, ocup_sistema, pkt_recibidos_serv, intensidad_trafico, espera_cola_Wq, ocup_cola_Lq = MM1(lamda, mu, user, portrate, tsim, bins, directorio)
            
            self.text_consola.setTextColor(QtGui.QColor("white"))
            self.text_consola.setFont(QtGui.QFont(u'Ubuntu', 11))
            self.text_consola.setText("Información detallada de paquetes servidos:" + "\n \n" + datos)
            self.text_consola.setReadOnly(True)
            
            self.line_pkt_drop.setText(format(pkt_drop))
            self.line_pkt_enviados.setText(format(pkt_enviados))
            self.line_pkt_recibidos.setText(format(pkt_recibidos_serv))
            
            if twait_medio < 0.001:
                self.line_twait_medio.setText(format(twait_medio))
            else:
                self.line_twait_medio.setText("{:.5f}".format(twait_medio))   
                
            if tasa_perdida < 0.001:
                self.line_tasa_perdida.setText(format((tasa_perdida)* 100) + '%')
            else:
                self.line_tasa_perdida.setText("{:.4f}".format((tasa_perdida) * 100) + '%')            
            
            if ocup_sistema < 0.001:
                self.line_ocup_sistema.setText(format(ocup_sistema))
            else:
                self.line_ocup_sistema.setText("{:.5f}".format(ocup_sistema))
                
            if intensidad_trafico < 0.001:
                self.line_inten_trafico.setText(format(intensidad_trafico))  
            else:
                self.line_inten_trafico.setText("{:.5f}".format(intensidad_trafico))       

            if espera_cola_Wq < 0.001:
                self.line_espera_cola_Wq.setText(format(espera_cola_Wq))
            else:
                self.line_espera_cola_Wq.setText("{:.5f}".format(espera_cola_Wq))
            
            if espera_cola_Wq < 0.001:
                self.line_ocup_cola_Lq.setText(format(ocup_cola_Lq))
            else:
                self.line_ocup_cola_Lq.setText("{:.5f}".format(ocup_cola_Lq))
            
            self.line_twait_medio.setReadOnly(True)
            self.line_pkt_drop.setReadOnly(True)
            self.line_pkt_enviados.setReadOnly(True)
            self.line_tasa_perdida.setReadOnly(True)
            self.line_ocup_sistema.setReadOnly(True)
            self.line_inten_trafico.setReadOnly(True)
            self.line_pkt_recibidos.setReadOnly(True)
            self.line_espera_cola_Wq.setReadOnly(True)
            self.line_ocup_cola_Lq.setReadOnly(True)
            
    #        Setear una imagen de entrada
            self.label_imagen.setStyleSheet("background-color: rgb(255, 255, 255);")
            pixmap_3_N = QPixmap(directorio  + "temp_graficos/" + 'WaitHistogram_normal.png')
            self.label_imagen.setPixmap(pixmap_3_N) 


    def graficos(self):
        directorio=os.getcwd() + '/'
        if self.comboBox_norm.currentText() == "Si":
            pixmap_1_N = QPixmap(directorio + "temp_graficos/" + 'ArrivalHistogram_normal.png')
            pixmap_2_N = QPixmap(directorio + "temp_graficos/" + 'QueueHistogram_normal.png')
            pixmap_3_N = QPixmap(directorio + "temp_graficos/" + 'WaitHistogram_normal.png')
        
            if self.radio_tespera.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_3_N)
            elif self.radio_tinter_arribo.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_1_N)
            elif self.radio_tocup_sist.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_2_N)
            elif (self.radio_tespera.isChecked() == True) and (self.radio_tinter_arribo.isChecked() == True) and (self.radio_tocup_sist.isChecked() == True):
                self.label_imagen.setPixmap(pixmap_3_N)
                
        elif self.comboBox_norm.currentText() == "No":
            pixmap_1 = QPixmap(directorio + "temp_graficos/" + 'ArrivalHistogram.png')
            pixmap_2 = QPixmap(directorio + "temp_graficos/" + 'QueueHistogram.png')
            pixmap_3 = QPixmap(directorio + "temp_graficos/" + 'WaitHistogram.png')
            
            if self.radio_tespera.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_3)
            elif self.radio_tinter_arribo.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_1)
            elif self.radio_tocup_sist.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_2)
            elif (self.radio_tespera.isChecked() == True) and (self.radio_tinter_arribo.isChecked() == True) and (self.radio_tocup_sist.isChecked() == True):
                self.label_imagen.setPixmap(pixmap_3)
#------------------------------------------------------------------------------
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#--------------------------------CLASE MG1------------------------------------
#-----------------------------------------------------------------------------
class MyApp_mg1(QtWidgets.QMainWindow, Ui_entrada_salida_mg1): 
    def __init__(self): 
        try:
            QtWidgets.QMainWindow.__init__(self) 
            Ui_entrada_salida_mg1.__init__(self) 
            self.setupUi(self)
    #----------------------------Seteo imagen de entrada---------------------------
            directorio = os.getcwd() + '/'
            pixmap = QPixmap(directorio  + "Im/logo_simulatorQ-reemplazo.png")
            self.label_imagen.setPixmap(pixmap)         
    #---------------------------VALIDAR DATOS DE ENTRADA---------------------------
            self.line_lambda.setValidator(QtGui.QDoubleValidator())      
            self.line_a.setValidator(QtGui.QDoubleValidator())
            self.line_b.setValidator(QtGui.QDoubleValidator())
            self.line_portrate.setValidator(QtGui.QDoubleValidator())
            self.line_tsim.setValidator(QtGui.QDoubleValidator())
    #----------------------------------BOTONES-------------------------------------
            self.push_reset.clicked.connect(self.resetear)
    
            self.push_simular.clicked.connect(self.simular)
            
            self.comboBox_norm.currentIndexChanged['int'].connect(self.graficos)
            self.radio_tinter_arribo.clicked.connect(self.graficos)
            self.radio_tespera.clicked.connect(self.graficos)
            self.radio_tocup_sist.clicked.connect(self.graficos)
    
            self.comboBox.currentIndexChanged['int'].connect(self.cambia_label)
    
    #---------------------------------MENU BAR------------------------------------
    #        Archivo 
            self.actionReiniciar_2.triggered.connect(self.reinicio)
            self.actionRegresar.triggered.connect(self.open_back)
            self.actionImportar_datos.triggered.connect(self.importar)
            self.actionParametros_de_entrada.triggered.connect(self.guardar_entrada)
            self.actionParametros_de_salida.triggered.connect(self.guardar_salida)
            self.actionInformacion_de_secuencia_de_paquetes.triggered.connect(self.guardar_paquetes)
            self.actionTodo.triggered.connect(self.guardar_todo)
            self.actionSalir.triggered.connect(self.salir_programa)
    #        Simulacion
            self.actionCorrer_simulacion.triggered.connect(self.simular)
            self.actionResetear_parametros.triggered.connect(self.limpiar)
    #        Ayuda
            self.actionSobre_Python_2.triggered.connect(doc_python_web)
            self.actionSimpy.triggered.connect(doc_simpy_web)
            self.actionSobre_PyQt5_2.triggered.connect(doc_pyqt_web)
            self.actionSobre_SimuladorQ.triggered.connect(doc_simuladorQ_web)
            self.actionAcerca_de_SimuladorQ.triggered.connect(self.acerca_de)
            self.actionTutorial_Python.triggered.connect(tuto_python_web)
            self.actionTutorial_PyQt.triggered.connect(tuto_pyqt_web)
            self.actionGeneradores_y_corutinas_Python.triggered.connect(gen_corutinas_web)
        except PermissionError:
            QMessageBox.critical(self, 'Error de ejecucion',"Revise la documentacion del programa.", QtWidgets.QMessageBox.Ok)
            sys.exit(0)
        except:
            error = traceback.format_exc()
            QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)
            sys.exit(0)
#----------------------------- FUNCIONES -------------------------------------
    def acerca_de(self):
        QMessageBox.information(self, 'Acerca de SimuladorQ',"<a href='http://simuladorq.readthedocs.io/'>SimuladorQ</a> es un simulador de modelos de colas, el cual nos permitirá introducir parámetros de entrada característicos de cada uno de los modelos que se proponen, y obtener valores medios e histogramas del comportamiento de los mismos.<br><br>Por problemas de software, por favor dirijase a nuestro sitio de Github, o bien a la documentacion del programa.<br><br>Desarrollo del código:<br><a href='https://www.python.org/'>Python</a> 3.6.4 64bits, <a href='https://www.qt.io/'>Qt</a>  5.6.2 y <a href='https://riverbankcomputing.com/software/pyqt/intro'>PyQt</a> 5.6, en Linux y MacOS.<br><br>Creado por Maximiliano Ibarra y Joaquín Manchado, en el marco del Trabajo Final de la asignatura Trafico [55], perteneciente al plan de estudios de la carrera <a href='https://www.ing.unrc.edu.ar/grado-teleco.php'>Ingeniería en Telecomunicaciones</a>, Facultad de Ingeniería, UNRC.", QMessageBox.Ok)
        
    def reinicio(self):
        self.resetear()
        
        self.line_twait_medio.setText("")
        self.line_espera_cola_Wq.setText("")
        self.line_inten_trafico.setText("")
        self.line_ocup_cola_Lq.setText("")
        self.line_pkt_drop.setText("")
        self.line_pkt_enviados.setText("")
        self.line_pkt_recibidos.setText("")
        self.line_tasa_perdida.setText("")
        self.line_ocup_sistema.setText("")
        
        self.text_consola.setTextColor(QtGui.QColor("white"))
        self.text_consola.setFont(QtGui.QFont(u'Ubuntu', 11))
        self.text_consola.setText("Información detallada de paquetes servidos.\nEstado actual: Esperando...")
        
        self.label_imagen.setStyleSheet("background-color: rgb(138, 146, 179);")
        directorio = os.getcwd() + '/'
        pixmap = QPixmap(directorio  + "Im/logo_simulatorQ-reemplazo.png")
        self.label_imagen.setPixmap(pixmap)
    
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',"¿Está seguro que desea salir?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            directorio = os.getcwd() + '/'
            if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
            event.accept()
        else:
            event.ignore()
        
    def limpiar(self):
        self.resetear()
        
    def salir_programa(self):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',"¿Está seguro que desea salir?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            directorio = os.getcwd() + '/'
            if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
            sys.exit(0)

    def guardar_entrada(self):
        try:
            path_archivo, path_folder = saveFileDialog()
            fichero = open(path_archivo, 'w+')
            cod = 1
        except(PermissionError):
            QMessageBox.critical(self, 'Error al guardar',"No tiene los permisos necesarios para guardar el archivo en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
            cod = 0
            exit
        if path_archivo == "" or cod == 0:
            exit
        else:
            lamda = (self.line_lambda.text())
            a = (self.line_a.text())
            b = (self.line_b.text())
            user = (self.line_user.text())
            portrate = (self.line_portrate.text())
            tsim = (self.line_tsim.text())
            bins = (self.comboBox_bins.currentText())
            distribucion = self.comboBox.currentText()

            if lamda == "" or a == "" or b == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                fichero.close()
                if os.path.isfile(path_archivo):
                    os.remove(path_archivo)                
                exit
            else:
                modelo = "MG1"
                parametros=[modelo,lamda, a, b, user, portrate, tsim, bins, distribucion, path_folder]
                for items in range(len(parametros)):
                    fichero.write("{}\n".format(parametros[items]))
                fichero.close()
       
    def guardar_salida(self):
        try:
            path_archivo, path_folder = saveFileDialog()
            fichero = open(path_archivo, 'w+')
            cod = 1
        except(PermissionError):
                QMessageBox.critical(self, 'Error al guardar',"No tiene los permisos necesarios para guardar el archivo en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                cod = 0
                exit
        if path_archivo == "" or cod == 0:
            exit
        else:
            lamda = (self.line_lambda.text())
            a = (self.line_a.text())
            b = (self.line_b.text())
            user = (self.line_user.text())
            portrate = (self.line_portrate.text())
            tsim = (self.line_tsim.text())
            bins = (self.comboBox_bins.currentText())
            if lamda == "" or a == "" or b == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                fichero.close()
                if os.path.isfile(path_archivo):
                    os.remove(path_archivo)                
                exit
            else:
                parametros_in=[self.comboBox.currentText(), lamda, a, b, user, portrate, tsim, bins]
                labels_in = [self.label_dist_general.text(), self.label_lambda.text(), self.label_a.text(), self.label_b.text(), self.label_user.text(), self.label_portrate.text(), self.label_tsim.text(), self.label_bins.text()]
                cont = 0
                largo_max_in = 0
                for cont in range(len(labels_in)):
                    largo=len(labels_in[cont])
                    if largo_max_in <= largo:
                        largo_max_in = largo
                
                t_wait_medio = (self.line_twait_medio.text())
                pkt_enviados = (self.line_pkt_enviados.text())
                pkt_drop = (self.line_pkt_drop.text())
                pkt_recibidos = (self.line_pkt_recibidos.text())
                tasa_perdida = (self.line_tasa_perdida.text())
                ocup_sistema = (self.line_ocup_sistema.text())
                intensidad_trafico = (self.line_inten_trafico.text())
                espera_cola_Wq = self.line_espera_cola_Wq.text()
                ocup_cola_Lq = self.line_ocup_cola_Lq.text()
                
                if t_wait_medio == "":
                    QMessageBox.critical(self, 'Error al guardar',"No se ha realizado ninguna simulación", QtWidgets.QMessageBox.Ok)
                    fichero.close()
                    if os.path.isfile(path_archivo):
                        os.remove(path_archivo)
                    exit 
                else:
                    parametros_out=[t_wait_medio, espera_cola_Wq, pkt_enviados, pkt_recibidos, pkt_drop, tasa_perdida, ocup_cola_Lq, ocup_sistema, intensidad_trafico]
                    labels_out = [self.label_twait_medio.text(), self.label_espera_cola_Wq.text(), self.label_pkt_enviados.text(), self.label_pkt_recibidos.text(), self.label_pkt_drop.text(), self.label_tasa_perdida.text(), self.label_ocup_cola_Lq.text(), self.label_ocup_sistema.text(), self.label_inten_trafico.text()]
                    cont = 0
                    largo_max_out = 0
                    for cont in range(len(labels_out)):
                        largo=len(labels_out[cont])
                        if largo_max_out <= largo:
                            largo_max_out = largo
                
                    fichero.write("RESULTADOS DE LA SIMULACION\n\n")
                    fichero.write("   #   Parámetros en la entrada del simulador\n\n")
                    items_in=0
                    for items_in in range(len(parametros_in)):
                        fichero.write(labels_in[items_in] + " " * (largo_max_in-len(labels_in[items_in])) + "    ")
                        fichero.write("{}\n".format(parametros_in[items_in]))
                    fichero.write("\n\n")
                    fichero.write("   #   Parámetros de salida del simulador\n\n")
                    items_out = 0
                    for items_out in range(len(parametros_out)):
                        fichero.write(labels_out[items_out] + " " * (largo_max_out-len(labels_out[items_out])) + "    ")
                        fichero.write("{}\n".format(parametros_out[items_out]))
                    fichero.close()
        
    def guardar_paquetes(self):
        try:
            path_archivo, path_folder = saveFileDialog()
            fichero = open(path_archivo, 'w+')
            cod = 1
        except(PermissionError):
                QMessageBox.critical(self, 'Error al guardar',"No tiene los permisos necesarios para guardar el archivo en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                cod = 0
                exit
        if path_archivo == "" or cod == 0:
            exit
        else:        
            lamda = (self.line_lambda.text())
            a = (self.line_a.text())
            b = (self.line_b.text())
            user = (self.line_user.text())
            portrate = (self.line_portrate.text())
            tsim = (self.line_tsim.text())
            bins = (self.comboBox_bins.currentText())
            if lamda == "" or a == "" or b == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                fichero.close()
                if os.path.isfile(path_archivo):
                    os.remove(path_archivo)                
                exit
            else:
                parametros_in=[self.comboBox.currentText(), lamda, a, b, user, portrate, tsim, bins]
                labels_in = [self.label_dist_general.text(), self.label_lambda.text(), self.label_a.text(), self.label_b.text(), self.label_user.text(), self.label_portrate.text(), self.label_tsim.text(), self.label_bins.text()]
                cont = 0
                largo_max_in = 0
                for cont in range(len(labels_in)):
                    largo=len(labels_in[cont])
                    if largo_max_in <= largo:
                        largo_max_in = largo        
                
                
                texto = self.text_consola.toPlainText()
                if texto == "Información detallada de paquetes servidos.\nEstado actual: Esperando..." :
                    QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación.", QtWidgets.QMessageBox.Ok)
                    fichero.close()
                    if os.path.isfile(path_archivo):
                        os.remove(path_archivo)                
                    exit
                else:
                    fichero.write("DETALLE DE LOS PAQUETES SERVIDOS\n\n")
                    fichero.write("   #   Parámetros en la entrada del simulador\n\n")
                    items_in=0
                    for items_in in range(len(parametros_in)):
                        fichero.write(labels_in[items_in] + " " * (largo_max_in-len(labels_in[items_in])) + "    ")
                        fichero.write("{}\n".format(parametros_in[items_in]))
                    fichero.write("\n\n")
                    fichero.write("   #   ")
                    fichero.write("{}\n".format(texto))
                    fichero.close()
        
    def guardar_todo(self):
        try:
            path_folder = setFolderDialog()
        except(PermissionError):
                QMessageBox.critical(self, 'Error al crear carpeta',"No tiene los permisos necesarios para crear la carpeta en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                exit
        if path_folder == "":
            exit
        else:
            tiempo_creacion = time.strftime("%d-%m-%y") + " _ " + time.strftime("%H-%M-%S")
            dir_sim_new = path_folder + 'SimuladorQ-MG1 __ ' + tiempo_creacion 
            try:
                os.makedirs(dir_sim_new)
                fichero = open (dir_sim_new + '/MG1_outfile.txt', 'w+')
            
                fichero.write("SIMULADORQ 1.0\n\n")
                fichero.write("Simulacion realizada: ")
                fichero.write(time.strftime("%x") + " - " + time.strftime("%X") + "hs" + '\n')
                fichero.write("Modelo utilizado en la simulacion: M/G/1\n")
                fichero.write("Distribucion General: ")
                fichero.write(self.comboBox.currentText() + "\n\n")
                lamda = (self.line_lambda.text())
                a = (self.line_a.text())
                b = (self.line_b.text())
                user = (self.line_user.text())
                portrate = (self.line_portrate.text())
                tsim = (self.line_tsim.text())
                bins = (self.comboBox_bins.currentText())
                if lamda == "" or a == "" or b == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                    QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                    fichero.close()
                    if os.path.isfile(dir_sim_new + '/MG1_outfile.txt'):
                        os.remove(dir_sim_new + '/MG1_outfile.txt')
                        shutil.rmtree(dir_sim_new)
                    exit
                else:                
                    parametros_in=[self.comboBox.currentText(), lamda, a, b, user, portrate, tsim, bins]
                    labels_in = [self.label_dist_general.text(), self.label_lambda.text(), self.label_a.text(), self.label_b.text(), self.label_user.text(), self.label_portrate.text(), self.label_tsim.text(), self.label_bins.text()]
                    cont = 0
                    largo_max_in = 0
                    for cont in range(len(labels_in)):
                        largo=len(labels_in[cont])
                        if largo_max_in <= largo:
                            largo_max_in = largo    
                    
                    fichero.write("   #   Parámetros en la entrada del simulador\n\n")
                    items_in=0
                    for items_in in range(len(parametros_in)):
                        fichero.write(labels_in[items_in] + " " * (largo_max_in-len(labels_in[items_in])) + "    ")
                        fichero.write("{}\n".format(parametros_in[items_in]))
                    fichero.write("\n\n")
                    
                    t_wait_medio = (self.line_twait_medio.text())
                    pkt_enviados = (self.line_pkt_enviados.text())
                    pkt_drop = (self.line_pkt_drop.text())
                    pkt_recibidos = (self.line_pkt_recibidos.text())
                    tasa_perdida = (self.line_tasa_perdida.text())
                    ocup_sistema = (self.line_ocup_sistema.text())
                    intensidad_trafico = (self.line_inten_trafico.text())
                    espera_cola_Wq = self.line_espera_cola_Wq.text()
                    ocup_cola_Lq = self.line_ocup_cola_Lq.text()
                    if t_wait_medio == "":
                        QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación", QtWidgets.QMessageBox.Ok)
                        fichero.close()
                        if os.path.isfile(dir_sim_new + '/MG1_outfile.txt'):
                            os.remove(dir_sim_new + '/MG1_outfile.txt')
                            shutil.rmtree(dir_sim_new)
                        exit        
                    else:                    
                        parametros_out=[t_wait_medio, espera_cola_Wq, pkt_enviados, pkt_recibidos, pkt_drop, tasa_perdida, ocup_cola_Lq, ocup_sistema, intensidad_trafico]
                        labels_out = [self.label_twait_medio.text(), self.label_espera_cola_Wq.text(), self.label_pkt_enviados.text(), self.label_pkt_recibidos.text(), self.label_pkt_drop.text(), self.label_tasa_perdida.text(), self.label_ocup_cola_Lq.text(), self.label_ocup_sistema.text(), self.label_inten_trafico.text()]
                        cont = 0
                        largo_max_out = 0
                        for cont in range(len(labels_out)):
                            largo=len(labels_out[cont])
                            if largo_max_out <= largo:
                                largo_max_out = largo
                                
                        fichero.write("   #   Parámetros de salida del simulador\n\n")
                        items_out = 0
                        for items_out in range(len(parametros_out)):
                            fichero.write(labels_out[items_out] + " " * (largo_max_out-len(labels_out[items_out])) + "    ")
                            fichero.write("{}\n".format(parametros_out[items_out]))
                        
                        texto = self.text_consola.toPlainText()       
                        
                        fichero.write("\n\n")
                        fichero.write("   #   ")
                        fichero.write("{}\n".format(texto))
                        fichero.close()
                        
                        directorio = dir_sim_new + '/'
                        directorio_actual = os.getcwd() + '/temp_graficos/'
                        
                        os.makedirs(directorio + 'Graficos Normalizados')
                        shutil.copy(directorio_actual + 'WaitHistogram_normal.png', directorio + 'Graficos Normalizados/WaitHistogram_normal.png')
                        shutil.copy(directorio_actual + 'ArrivalHistogram_normal.png', directorio + 'Graficos Normalizados/ArrivalHistogram_normal.png')
                        shutil.copy(directorio_actual + 'QueueHistogram_normal.png', directorio + 'Graficos Normalizados/QueueHistogram_normal.png')
                        
                        os.makedirs(directorio + 'Graficos No Normalizados')
                        shutil.copy(directorio_actual + 'WaitHistogram.png', directorio + 'Graficos No Normalizados/WaitHistogram.png')
                        shutil.copy(directorio_actual + 'ArrivalHistogram.png', directorio + 'Graficos No Normalizados/ArrivalHistogram.png')
                        shutil.copy(directorio_actual + 'QueueHistogram.png', directorio + 'Graficos No Normalizados/QueueHistogram.png')
            except(PermissionError):
                QMessageBox.critical(self, 'Error al crear carpeta',"No tiene los permisos necesarios para crear la carpeta en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                exit
        
    def resetear(self):
        self.comboBox_bins.setCurrentText('Seleccione')
        self.comboBox.setCurrentText('Normal')
        self.line_lambda.setText("")
        self.line_a.setText("")
        self.line_b.setText("")
        self.line_portrate.setText("")
        self.line_user.setText("")
        self.line_tsim.setText("")
        
    def importar(self):
        path_archivo, directorio = openFileNameDialog()
        if path_archivo == "" and directorio == "":
            QMessageBox.warning(None, 'No se pudo importar', "Debe seleccionar un archivo.", QMessageBox.Ok)
            exit
        else:
            fichero = open (path_archivo, 'r')
            modelo = "MG1"
            prueba = str(fichero.readline())
            prueba = prueba.replace('\n','')
            if prueba == modelo:
    #            Parametros necesarios para MG1 = 8
                linea_fin = 8
                parametros = [0] * linea_fin
                for linea in range(linea_fin):
                    parametros[linea] = str(fichero.readline())
                    parametros[linea] = parametros[linea].replace('\n','')
                    parametros[linea] = str(parametros[linea])    
                fichero.close()
            
                self.line_lambda.setText(parametros[0])
                self.line_a.setText(parametros[1])
                self.line_b.setText(parametros[2])
                self.line_user.setText(parametros[3])
                self.line_portrate.setText(parametros[4])
                self.line_tsim.setText(parametros[5])
                self.comboBox_bins.setCurrentText(parametros[6])
                self.comboBox.setCurrentText(parametros[7])
            else:
                QMessageBox.critical(None, 'No se pudo importar', "Archivo inválido.             ", QMessageBox.Ok)
                fichero.close()
                exit
            
    def cambia_label(self):
        if self.comboBox.currentText() == "Normal":
            self.label_a.setText("Media [μ]:")
            self.label_b.setText("Desviacion Estandar [σ]:")
        elif self.comboBox.currentText() == "Uniforme":
            self.label_a.setText("Limite inferior:")
            self.label_b.setText("Limite superior:")
            
    def open_back(self):
        self.anotherwindow = MyApp()
        self.anotherwindow.show()
        self.hide()
        
    def simular (self):
        if self.line_lambda.text() == "" or self.line_a.text() == "" or self.line_b.text() == "" or self.line_user.text() == "" or self.line_portrate.text() == "" or self.line_tsim.text() == "" or self.comboBox_bins.currentText() == "Seleccione":
            QMessageBox.critical(None, 'Simulación fallida', "Faltan ingresar parámetros de entrada.", QMessageBox.Ok)
        else:
            if self.comboBox.currentText() == "Normal":
                G = 1
            else:
                G = 2
            lamda = float(self.line_lambda.text())
            a = float(self.line_a.text())
            b = float(self.line_b.text())
            user = (self.line_user.text())
            portrate = float(self.line_portrate.text())
            tsim = float(self.line_tsim.text())
            bins = int(self.comboBox_bins.currentText())
            directorio = os.getcwd() + '/'

            if lamda < 0 or a < 0 or b < 0 or portrate < 0 or tsim < 0:
                QMessageBox.warning(None, 'Atención', "Ingreso de datos negativos. Utilice valores mayores a cero.", QMessageBox.Ok)
            elif G == 2 and (b < a or b < 0 or a < 0):
                QMessageBox.critical(None, 'Atención', "Intervalo de distribucion uniforme inválido. El limite superior debe ser mayor al limite inferior, y ambos positivos.", QMessageBox.Ok)
            else:   
                datos, twait_medio, pkt_drop, pkt_enviados, tasa_perdida, ocup_sistema, pkt_recibidos_serv, intensidad_trafico, espera_cola_Wq, ocup_cola_Lq = MG1(lamda, G, a, b, user, portrate, tsim, bins, directorio)
                
                self.text_consola.setTextColor(QtGui.QColor("white"))
                self.text_consola.setFont(QtGui.QFont(u'Ubuntu', 11))
                self.text_consola.setText("Información detallada de paquetes servidos:" + "\n \n" + datos)
                self.text_consola.setReadOnly(True)
                
                self.line_pkt_drop.setText(format(pkt_drop))
                self.line_pkt_enviados.setText(format(pkt_enviados))
                self.line_pkt_recibidos.setText(format(pkt_recibidos_serv))
                
                if twait_medio < 0.001:
                    self.line_twait_medio.setText(format(twait_medio))
                else:
                    self.line_twait_medio.setText("{:.5f}".format(twait_medio))   
                    
                if tasa_perdida < 0.001:
                    self.line_tasa_perdida.setText(format((tasa_perdida)* 100) + '%')
                else:
                    self.line_tasa_perdida.setText("{:.4f}".format((tasa_perdida) * 100) + '%')            
                
                if ocup_sistema < 0.001:
                    self.line_ocup_sistema.setText(format(ocup_sistema))
                else:
                    self.line_ocup_sistema.setText("{:.5f}".format(ocup_sistema))
                    
                if intensidad_trafico < 0.001:
                    self.line_inten_trafico.setText(format(intensidad_trafico))  
                else:
                    self.line_inten_trafico.setText("{:.5f}".format(intensidad_trafico))       
    
                if espera_cola_Wq < 0.001:
                    self.line_espera_cola_Wq.setText(format(espera_cola_Wq))
                else:
                    self.line_espera_cola_Wq.setText("{:.5f}".format(espera_cola_Wq))
                
                if espera_cola_Wq < 0.001:
                    self.line_ocup_cola_Lq.setText(format(ocup_cola_Lq))
                else:
                    self.line_ocup_cola_Lq.setText("{:.5f}".format(ocup_cola_Lq))
                
                self.line_twait_medio.setReadOnly(True)
                self.line_pkt_drop.setReadOnly(True)
                self.line_pkt_enviados.setReadOnly(True)
                self.line_tasa_perdida.setReadOnly(True)
                self.line_ocup_sistema.setReadOnly(True)
                self.line_inten_trafico.setReadOnly(True)
                self.line_pkt_recibidos.setReadOnly(True)
                self.line_espera_cola_Wq.setReadOnly(True)
                self.line_ocup_cola_Lq.setReadOnly(True)
                
        #        Para setear una imagen de entrada
                self.label_imagen.setStyleSheet("background-color: rgb(255, 255, 255);")
                pixmap_3_N = QPixmap(directorio  + "temp_graficos/" + 'WaitHistogram_normal.png')
                self.label_imagen.setPixmap(pixmap_3_N) 


    def graficos(self):
        directorio=os.getcwd() + '/'
        if self.comboBox_norm.currentText() == "Si":
            pixmap_1_N = QPixmap(directorio + "temp_graficos/" + 'ArrivalHistogram_normal.png')
            pixmap_2_N = QPixmap(directorio + "temp_graficos/" + 'QueueHistogram_normal.png')
            pixmap_3_N = QPixmap(directorio + "temp_graficos/" + 'WaitHistogram_normal.png')
        
            if self.radio_tespera.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_3_N)
            elif self.radio_tinter_arribo.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_1_N)
            elif self.radio_tocup_sist.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_2_N)
            elif (self.radio_tespera.isChecked() == True) and (self.radio_tinter_arribo.isChecked() == True) and (self.radio_tocup_sist.isChecked() == True):
                self.label_imagen.setPixmap(pixmap_3_N)
                
        elif self.comboBox_norm.currentText() == "No":
            pixmap_1 = QPixmap(directorio + "temp_graficos/" + 'ArrivalHistogram.png')
            pixmap_2 = QPixmap(directorio + "temp_graficos/" + 'QueueHistogram.png')
            pixmap_3 = QPixmap(directorio + "temp_graficos/" + 'WaitHistogram.png')
            
            if self.radio_tespera.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_3)
            elif self.radio_tinter_arribo.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_1)
            elif self.radio_tocup_sist.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_2)
            elif (self.radio_tespera.isChecked() == True) and (self.radio_tinter_arribo.isChecked() == True) and (self.radio_tocup_sist.isChecked() == True):
                self.label_imagen.setPixmap(pixmap_3)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#--------------------------------CLASE MM1K-----------------------------------
#------------------------------------------------------------------------------
class MyApp_mm1k(QtWidgets.QMainWindow, Ui_entrada_salida_mm1k): 
    def __init__(self): 
        try:
            QtWidgets.QMainWindow.__init__(self) 
            Ui_entrada_salida_mm1k.__init__(self) 
            self.setupUi(self)
    
    #----------------------------SETEAR IMAGEN DE ENTRADA--------------------------
            directorio = os.getcwd() + '/'
            pixmap = QPixmap(directorio  + "Im/logo_simulatorQ-reemplazo.png")
            self.label_imagen.setPixmap(pixmap)         
    #---------------------------VALIDAR DATOS DE ENTRADA---------------------------
            self.line_lambda.setValidator(QtGui.QDoubleValidator())
            self.line_mu.setValidator(QtGui.QDoubleValidator())  
            self.line_portrate.setValidator(QtGui.QDoubleValidator())
            self.line_tsim.setValidator(QtGui.QDoubleValidator())
            
    #------------------------FUNCIONALIDAD BOTONES --------------------------------
            self.push_reset.clicked.connect(self.resetear)
            self.push_simular.clicked.connect(self.simular)
            self.comboBox_norm.currentIndexChanged['int'].connect(self.graficos)
            self.radio_tinter_arribo.clicked.connect(self.graficos)
            self.radio_tespera.clicked.connect(self.graficos)
            self.radio_tocup_sist.clicked.connect(self.graficos)
    #---------------------------------MENU BAR------------------------------------
            self.actionRegresar.triggered.connect(self.open_back)
            self.actionReiniciar_2.triggered.connect(self.reinicio)
            self.actionImportar_datos.triggered.connect(self.importar)
            self.actionParametros_de_entrada.triggered.connect(self.guardar_entrada)
            self.actionParametros_de_salida.triggered.connect(self.guardar_salida)
            self.actionInformacion_de_secuencia_de_paquetes.triggered.connect(self.guardar_paquetes)
            self.actionTodo.triggered.connect(self.guardar_todo)
            self.actionSalir.triggered.connect(self.salir_programa)
    #        Simulacion
            self.actionCorrer_simulacion.triggered.connect(self.simular)
            self.actionResetear_parametros.triggered.connect(self.limpiar)
    #        Ayuda
            self.actionSobre_Python_2.triggered.connect(doc_python_web)
            self.actionSimpy.triggered.connect(doc_simpy_web)
            self.actionSobre_PyQt5_2.triggered.connect(doc_pyqt_web)
            self.actionSobre_SimuladorQ.triggered.connect(doc_simuladorQ_web)
            self.actionAcerca_de_SimuladorQ.triggered.connect(self.acerca_de)
            self.actionTutorial_Python.triggered.connect(tuto_python_web)
            self.actionTutorial_PyQt.triggered.connect(tuto_pyqt_web)
            self.actionGeneradores_y_corutinas_Python.triggered.connect(gen_corutinas_web)
        except PermissionError:
            QMessageBox.critical(self, 'Error de ejecucion',"Revise la documentacion del programa.", QtWidgets.QMessageBox.Ok)
            sys.exit(0)
        except:
            error = traceback.format_exc()
            QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)
            sys.exit(0)
#------------------------------------------------------------------------------
#----------------------------- FUNCIONES -------------------------------------
    def acerca_de(self):
        QMessageBox.information(self, 'Acerca de SimuladorQ',"<a href='http://simuladorq.readthedocs.io/'>SimuladorQ</a> es un simulador de modelos de colas, el cual nos permitirá introducir parámetros de entrada característicos de cada uno de los modelos que se proponen, y obtener valores medios e histogramas del comportamiento de los mismos.<br><br>Por problemas de software, por favor dirijase a nuestro sitio de Github, o bien a la documentacion del programa.<br><br>Desarrollo del código:<br><a href='https://www.python.org/'>Python</a> 3.6.4 64bits, <a href='https://www.qt.io/'>Qt</a>  5.6.2 y <a href='https://riverbankcomputing.com/software/pyqt/intro'>PyQt</a> 5.6, en Linux y MacOS.<br><br>Creado por Maximiliano Ibarra y Joaquín Manchado, en el marco del Trabajo Final de la asignatura Trafico [55], perteneciente al plan de estudios de la carrera <a href='https://www.ing.unrc.edu.ar/grado-teleco.php'>Ingeniería en Telecomunicaciones</a>, Facultad de Ingeniería, UNRC.", QMessageBox.Ok)
        
    def reinicio(self):
        self.resetear()
        
        self.line_twait_medio.setText("")
        self.line_espera_cola_Wq.setText("")
        self.line_inten_trafico.setText("")
        self.line_ocup_cola_Lq.setText("")
        self.line_pkt_drop.setText("")
        self.line_pkt_enviados.setText("")
        self.line_pkt_recibidos.setText("")
        self.line_tasa_perdida.setText("")
        self.line_ocup_sistema.setText("")
        
        self.text_consola.setTextColor(QtGui.QColor("white"))
        self.text_consola.setFont(QtGui.QFont(u'Ubuntu', 11))
        self.text_consola.setText("Información detallada de paquetes servidos.\nEstado actual: Esperando...")
        
        self.label_imagen.setStyleSheet("background-color: rgb(138, 146, 179);")
        directorio = os.getcwd() + '/'
        pixmap = QPixmap(directorio  + "Im/logo_simulatorQ-reemplazo.png")
        self.label_imagen.setPixmap(pixmap)
    
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',"¿Está seguro que desea salir?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            directorio = os.getcwd() + '/'
            if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
            event.accept()
        else:
            event.ignore()
    
    def salir_programa(self):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',"¿Está seguro que desea salir?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            directorio = os.getcwd() + '/'
            if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
            sys.exit(0)
        
    def limpiar(self):
        self.resetear()

    def guardar_entrada(self):
        try:
            path_archivo, path_folder = saveFileDialog()
            fichero = open(path_archivo, 'w+')
            cod = 1
        except(PermissionError):
                QMessageBox.critical(self, 'Error al guardar',"No tiene los permisos necesarios para guardar el archivo en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                cod = 0
                exit
        if path_archivo == "" or cod == 0:
            exit
        else:
            lamda = (self.line_lambda.text())
            mu = (self.line_mu.text())
            ql = self.comboBox_ql.currentText()
            user = (self.line_user.text())
            portrate = (self.line_portrate.text())
            tsim = (self.line_tsim.text())
            bins = (self.comboBox_bins.currentText())
            
            if lamda == "" or mu == "" or ql == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                fichero.close()
                if os.path.isfile(path_archivo):
                    os.remove(path_archivo)                
                exit 
            else:
                modelo = "MM1K"
                parametros=[modelo, lamda, mu, ql, user, portrate, tsim, bins, path_folder]
                for items in range(len(parametros)):
                    fichero.write("{}\n".format(parametros[items]))
                fichero.close()

    def guardar_salida(self):
        try:
            path_archivo, path_folder = saveFileDialog()
            fichero = open(path_archivo, 'w+')
            cod = 1
        except(PermissionError):
                QMessageBox.critical(self, 'Error al guardar',"No tiene los permisos necesarios para guardar el archivo en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                cod = 0
                exit
        if path_archivo == "" or cod == 0:
            exit
        else:
            lamda = (self.line_lambda.text())
            mu = (self.line_mu.text())
            ql = self.comboBox_ql.currentText()
            user = (self.line_user.text())
            portrate = (self.line_portrate.text())
            tsim = (self.line_tsim.text())
            bins = (self.comboBox_bins.currentText())
            if lamda == "" or mu == "" or ql == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                fichero.close()
                if os.path.isfile(path_archivo):
                    os.remove(path_archivo)                
                exit 
            else:
                parametros_in=[lamda, mu, ql, user, portrate, tsim, bins]
                labels_in = [self.label_lambda.text(), self.label_mu.text(), self.label_ql.text(), self.label_user.text(), self.label_portrate.text(), self.label_tsim.text(), self.label_bins.text()]
                cont = 0
                largo_max_in = 0
                for cont in range(len(labels_in)):
                    largo=len(labels_in[cont])
                    if largo_max_in <= largo:
                        largo_max_in = largo
        
                t_wait_medio = (self.line_twait_medio.text())
                pkt_enviados = (self.line_pkt_enviados.text())
                pkt_drop = (self.line_pkt_drop.text())
                pkt_recibidos = (self.line_pkt_recibidos.text())
                tasa_perdida = (self.line_tasa_perdida.text())
                ocup_sistema = (self.line_ocup_sistema.text())
                intensidad_trafico = (self.line_inten_trafico.text())
                espera_cola_Wq = self.line_espera_cola_Wq.text()
                ocup_cola_Lq = self.line_ocup_cola_Lq.text()
                
                if t_wait_medio == "":
                    QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación.", QtWidgets.QMessageBox.Ok)
                    fichero.close()
                    if os.path.isfile(path_archivo):
                        os.remove(path_archivo)                
                    exit
                else:
                    parametros_out=[t_wait_medio, espera_cola_Wq, pkt_enviados, pkt_recibidos, pkt_drop, tasa_perdida, ocup_cola_Lq, ocup_sistema, intensidad_trafico]
                    labels_out = [self.label_twait_medio.text(), self.label_espera_cola_Wq.text(), self.label_pkt_enviados.text(), self.label_pkt_recibidos.text(), self.label_pkt_drop.text(), self.label_tasa_perdida.text(), self.label_ocup_cola_Lq.text(), self.label_ocup_sistema.text(), self.label_inten_trafico.text()]
                    cont = 0
                    largo_max_out = 0
                    for cont in range(len(labels_out)):
                        largo=len(labels_out[cont])
                        if largo_max_out <= largo:
                            largo_max_out = largo
        
                    fichero.write("RESULTADOS DE LA SIMULACION\n\n")
                    fichero.write("   #   Parámetros en la entrada del simulador\n\n")
                    items_in=0
                    for items_in in range(len(parametros_in)):
                        fichero.write(labels_in[items_in] + " " * (largo_max_in-len(labels_in[items_in])) + "    ")
                        fichero.write("{}\n".format(parametros_in[items_in]))
                    fichero.write("\n\n")
                    fichero.write("   #   Parámetros de salida del simulador\n\n")
                    items_out = 0
                    for items_out in range(len(parametros_out)):
                        fichero.write(labels_out[items_out] + " " * (largo_max_out-len(labels_out[items_out])) + "    ")
                        fichero.write("{}\n".format(parametros_out[items_out]))
                    fichero.close()

    def guardar_paquetes(self):
        try:
            path_archivo, path_folder = saveFileDialog()
            fichero = open(path_archivo, 'w+')
            cod = 1
        except(PermissionError):
                QMessageBox.critical(self, 'Error al guardar',"No tiene los permisos necesarios para guardar el archivo en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                cod = 0
                exit
        if path_archivo == "" or cod == 0:
            exit
        else:
            lamda = (self.line_lambda.text())
            mu = (self.line_mu.text())
            ql = self.comboBox_ql.currentText()
            user = (self.line_user.text())
            portrate = (self.line_portrate.text())
            tsim = (self.line_tsim.text())
            bins = (self.comboBox_bins.currentText())
            if lamda == "" or mu == "" or ql == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                fichero.close()
                if os.path.isfile(path_archivo):
                    os.remove(path_archivo)                
                exit 
            else:
                parametros_in=[lamda, mu, ql, user, portrate, tsim, bins]
                labels_in = [self.label_lambda.text(), self.label_mu.text(), self.label_ql.text(), self.label_user.text(), self.label_portrate.text(), self.label_tsim.text(), self.label_bins.text()]
                cont = 0
                largo_max_in = 0
                for cont in range(len(labels_in)):
                    largo=len(labels_in[cont])
                    if largo_max_in <= largo:
                        largo_max_in = largo
                
                texto = self.text_consola.toPlainText()
                if texto == "Información detallada de paquetes servidos.\nEstado actual: Esperando..." :
                    QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación.", QtWidgets.QMessageBox.Ok)
                    fichero.close()
                    if os.path.isfile(path_archivo):
                        os.remove(path_archivo)                
                    exit
                else:
                    fichero.write("DETALLE DE LOS PAQUETES SERVIDOS\n\n")
                    fichero.write("   #   Parámetros en la entrada del simulador\n\n")
                    items_in=0
                    for items_in in range(len(parametros_in)):
                        fichero.write(labels_in[items_in] + " " * (largo_max_in-len(labels_in[items_in])) + "    ")
                        fichero.write("{}\n".format(parametros_in[items_in]))
                    fichero.write("\n\n")
                    fichero.write("   #   ")
                    fichero.write("{}\n".format(texto))
                    fichero.close()
                
    def guardar_todo(self):
        try:
            path_folder = setFolderDialog()
        except(PermissionError):
                QMessageBox.critical(self, 'Error al crear carpeta',"No tiene los permisos necesarios para crear la carpeta en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                exit
        if path_folder == "":
            exit
        else:
            tiempo_creacion = time.strftime("%d-%m-%y") + " _ " + time.strftime("%H-%M-%S")
            dir_sim_new = path_folder + 'SimuladorQ-MM1K __ ' + tiempo_creacion 
            try:
                os.makedirs(dir_sim_new)
                fichero = open (dir_sim_new + '/MM1K_outfile.txt', 'w+')
            
                fichero.write("SIMULADORQ 1.0\n\n")
                fichero.write("Simulacion realizada: ")
                fichero.write(time.strftime("%x") + " - " + time.strftime("%X") + "hs" +'\n')
                fichero.write("Modelo utilizado en la simulacion: M/M/1/K \n\n")
        
                lamda = (self.line_lambda.text())
                mu = (self.line_mu.text())
                ql = self.comboBox_ql.currentText()
                user = (self.line_user.text())
                portrate = (self.line_portrate.text())
                tsim = (self.line_tsim.text())
                bins = (self.comboBox_bins.currentText())
                if lamda == "" or mu == "" or ql == "" or user == "" or portrate == "" or tsim == "" or bins == "Seleccione":
                    QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación o no se han ingresado todos los parametros de entrada.", QtWidgets.QMessageBox.Ok)
                    fichero.close()
                    if os.path.isfile(dir_sim_new + '/MM1K_outfile.txt'):
                        os.remove(dir_sim_new + '/MM1K_outfile.txt')
                        shutil.rmtree(dir_sim_new)
                    exit
                else: 
                    parametros_in=[lamda, mu, ql, user, portrate, tsim, bins]
                    labels_in = [self.label_lambda.text(), self.label_mu.text(), self.label_ql.text(), self.label_user.text(), self.label_portrate.text(), self.label_tsim.text(), self.label_bins.text()]
                    cont = 0
                    largo_max_in = 0
                    for cont in range(len(labels_in)):
                        largo=len(labels_in[cont])
                        if largo_max_in <= largo:
                            largo_max_in = largo
                            
                    fichero.write("   #   Parámetros en la entrada del simulador\n\n")
                    items_in=0
                    for items_in in range(len(parametros_in)):
                        fichero.write(labels_in[items_in] + " " * (largo_max_in-len(labels_in[items_in])) + "    ")
                        fichero.write("{}\n".format(parametros_in[items_in]))
                    fichero.write("\n\n")
                    
                    t_wait_medio = (self.line_twait_medio.text())
                    pkt_enviados = (self.line_pkt_enviados.text())
                    pkt_drop = (self.line_pkt_drop.text())
                    pkt_recibidos = (self.line_pkt_recibidos.text())
                    tasa_perdida = (self.line_tasa_perdida.text())
                    ocup_sistema = (self.line_ocup_sistema.text())
                    intensidad_trafico = (self.line_inten_trafico.text())
                    espera_cola_Wq = self.line_espera_cola_Wq.text()
                    ocup_cola_Lq = self.line_ocup_cola_Lq.text()
                    if t_wait_medio == "":
                        QMessageBox.warning(self, 'Error al guardar',"No se ha realizado ninguna simulación", QtWidgets.QMessageBox.Ok)
                        fichero.close()
                        if os.path.isfile(dir_sim_new + '/MM1K_outfile.txt'):
                            os.remove(dir_sim_new + '/MM1K_outfile.txt')
                            shutil.rmtree(dir_sim_new)
                        exit        
                    else:                    
                        parametros_out=[t_wait_medio, espera_cola_Wq, pkt_enviados, pkt_recibidos, pkt_drop, tasa_perdida, ocup_cola_Lq, ocup_sistema, intensidad_trafico]
                        labels_out = [self.label_twait_medio.text(), self.label_espera_cola_Wq.text(), self.label_pkt_enviados.text(), self.label_pkt_recibidos.text(), self.label_pkt_drop.text(), self.label_tasa_perdida.text(), self.label_ocup_cola_Lq.text(), self.label_ocup_sistema.text(), self.label_inten_trafico.text()]
                        cont = 0
                        largo_max_out = 0
                        for cont in range(len(labels_out)):
                            largo=len(labels_out[cont])
                            if largo_max_out <= largo:
                                largo_max_out = largo
                                
                        fichero.write("   #   Parámetros de salida del simulador\n\n")
                        items_out = 0
                        for items_out in range(len(parametros_out)):
                            fichero.write(labels_out[items_out] + " " * (largo_max_out-len(labels_out[items_out])) + "    ")
                            fichero.write("{}\n".format(parametros_out[items_out]))
                        
                        texto = self.text_consola.toPlainText()       
                        
                        fichero.write("\n\n")
                        fichero.write("   #   ")
                        fichero.write("{}\n".format(texto))
                        fichero.close()
                        
                        directorio = dir_sim_new + '/'
                        directorio_actual = os.getcwd() + '/temp_graficos/'
                        
                        os.makedirs(directorio + 'Graficos Normalizados')
                        shutil.copy(directorio_actual + 'WaitHistogram_normal.png', directorio + 'Graficos Normalizados/WaitHistogram_normal.png')
                        shutil.copy(directorio_actual + 'ArrivalHistogram_normal.png', directorio + 'Graficos Normalizados/ArrivalHistogram_normal.png')
                        shutil.copy(directorio_actual + 'QueueHistogram_normal.png', directorio + 'Graficos Normalizados/QueueHistogram_normal.png')
                        
                        os.makedirs(directorio + 'Graficos No Normalizados')
                        shutil.copy(directorio_actual + 'WaitHistogram.png', directorio + 'Graficos No Normalizados/WaitHistogram.png')
                        shutil.copy(directorio_actual + 'ArrivalHistogram.png', directorio + 'Graficos No Normalizados/ArrivalHistogram.png')
                        shutil.copy(directorio_actual + 'QueueHistogram.png', directorio + 'Graficos No Normalizados/QueueHistogram.png')
            except(PermissionError):
                QMessageBox.critical(self, 'Error al crear carpeta',"No tiene los permisos necesarios para crear la carpeta en este directorio. Considere utilizar otro.", QtWidgets.QMessageBox.Ok)
                exit

    def resetear(self):
        self.comboBox_bins.setCurrentText('Seleccione')   
        self.line_lambda.setText("")
        self.line_mu.setText("")
        self.comboBox_ql.setCurrentText('Seleccione')
        self.line_portrate.setText("")
        self.line_user.setText("")
        self.line_tsim.setText("")
        
    def importar(self):
        path_archivo, directorio = openFileNameDialog()
        if path_archivo == "" and directorio == "":
            QMessageBox.warning(None, 'No se pudo importar', "Debe seleccionar un archivo.", QMessageBox.Ok)
            exit
        else:
            fichero = open (path_archivo, 'r')
            modelo = "MM1K"
            prueba = str(fichero.readline())
            prueba = prueba.replace('\n','')
            if prueba == modelo:
    #            Parametros necesarios para MM1K = 7
                linea_fin = 7
                parametros = [0] * linea_fin
                for linea in range(linea_fin):
                    parametros[linea] = str(fichero.readline())
                    parametros[linea] = parametros[linea].replace('\n','')
                    parametros[linea] = str(parametros[linea])    
                fichero.close()
            
                self.line_lambda.setText(parametros[0])
                self.line_mu.setText(parametros[1])
                self.comboBox_ql.setCurrentText(parametros[2])
                self.line_user.setText(parametros[3])
                self.line_portrate.setText(parametros[4])
                self.line_tsim.setText(parametros[5])
                self.comboBox_bins.setCurrentText(parametros[6])
            else:
                QMessageBox.critical(None, 'No se pudo importar', "Archivo inválido.             ", QMessageBox.Ok)
                fichero.close()
                exit
            
    def open_back(self):
        self.anotherwindow = MyApp()
        self.anotherwindow.show()
        self.hide()
        
    def simular (self):
        if self.line_lambda.text() == "" or self.line_mu.text() == "" or self.comboBox_ql.currentText() == "Seleccione" or self.line_user.text() == "" or self.line_portrate.text() == "" or self.line_tsim.text() == "" or self.comboBox_bins.currentText() == "Seleccione":
            QMessageBox.critical(None, 'Simulación fallida', "Faltan ingresar parámetros de entrada.", QMessageBox.Ok)
        elif int(self.line_lambda.text()) < 10 or int(self.line_mu.text()) < 10:
            QMessageBox.critical(None, 'Simulación fallida', "Parametros muy pequeños producen errores de simulacion. Considere utilizar valores de tasa de arribo y de servicio mayores a 10.", QMessageBox.Ok)
        elif float(self.line_lambda.text()) < 0 or float(self.line_mu.text()) < 0 or float(self.line_portrate.text()) < 0 or int(self.line_tsim.text()) < 0:
            QMessageBox.warning(None, 'Atención', "Ingreso de datos negativos. Utilice valores mayores a cero.", QMessageBox.Ok)
        else:
            lamda = float(self.line_lambda.text())
            mu = float(self.line_mu.text())
            ql = int(self.comboBox_ql.currentText())
            user = (self.line_user.text())
            portrate = float(self.line_portrate.text())
            tsim = float(self.line_tsim.text())
            bins = int(self.comboBox_bins.currentText())
            directorio = os.getcwd() + '/'

            datos, twait_medio, pkt_drop, pkt_enviados, tasa_perdida, ocup_sistema, pkt_recibidos_serv, intensidad_trafico, espera_cola_Wq, ocup_cola_Lq = MM1K(lamda, mu, ql, user, portrate, tsim, bins, directorio)
            
            self.text_consola.setTextColor(QtGui.QColor("white"))
            self.text_consola.setFont(QtGui.QFont(u'Ubuntu', 11))
            self.text_consola.setText("Información detallada de paquetes servidos:" + "\n \n" + datos)
            self.text_consola.setReadOnly(True)

            self.line_pkt_drop.setText(format(pkt_drop))
            self.line_pkt_enviados.setText(format(pkt_enviados))
            self.line_pkt_recibidos.setText(format(pkt_recibidos_serv))
            
            if twait_medio < 0.001:
                self.line_twait_medio.setText(format(twait_medio))
            else:
                self.line_twait_medio.setText("{:.5f}".format(twait_medio))   
                
            if tasa_perdida < 0.001:
                self.line_tasa_perdida.setText(format((tasa_perdida)))
            else:
                self.line_tasa_perdida.setText("{:.4f}".format((tasa_perdida)))            
            
            if ocup_sistema < 0.001:
                self.line_ocup_sistema.setText(format(ocup_sistema))
            else:
                self.line_ocup_sistema.setText("{:.5f}".format(ocup_sistema))
                
            if intensidad_trafico < 0.001:
                self.line_inten_trafico.setText(format(intensidad_trafico))  
            else:
                self.line_inten_trafico.setText("{:.5f}".format(intensidad_trafico))       

            if espera_cola_Wq < 0.001:
                self.line_espera_cola_Wq.setText(format(espera_cola_Wq))
            else:
                self.line_espera_cola_Wq.setText("{:.5f}".format(espera_cola_Wq))
            
            if espera_cola_Wq < 0.001:
                self.line_ocup_cola_Lq.setText(format(ocup_cola_Lq))
            else:
                self.line_ocup_cola_Lq.setText("{:.5f}".format(ocup_cola_Lq))
            
            self.line_twait_medio.setReadOnly(True)
            self.line_pkt_drop.setReadOnly(True)
            self.line_pkt_enviados.setReadOnly(True)
            self.line_tasa_perdida.setReadOnly(True)
            self.line_ocup_sistema.setReadOnly(True)
            self.line_inten_trafico.setReadOnly(True)
            self.line_pkt_recibidos.setReadOnly(True)
            self.line_espera_cola_Wq.setReadOnly(True)
            self.line_ocup_cola_Lq.setReadOnly(True)
            
    #        Para setear una imagen de entrada
            self.label_imagen.setStyleSheet("background-color: rgb(255, 255, 255);")
            pixmap_3_N = QPixmap(directorio  + "temp_graficos/" + 'WaitHistogram_normal.png')
            self.label_imagen.setPixmap(pixmap_3_N) 

    def graficos(self):
        directorio=os.getcwd() + '/'
        if self.comboBox_norm.currentText() == "Si":
            pixmap_1_N = QPixmap(directorio + "temp_graficos/" + 'ArrivalHistogram_normal.png')
            pixmap_2_N = QPixmap(directorio + "temp_graficos/" + 'QueueHistogram_normal.png')
            pixmap_3_N = QPixmap(directorio + "temp_graficos/" + 'WaitHistogram_normal.png')
        
            if self.radio_tespera.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_3_N)
            elif self.radio_tinter_arribo.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_1_N)
            elif self.radio_tocup_sist.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_2_N)
            elif (self.radio_tespera.isChecked() == True) and (self.radio_tinter_arribo.isChecked() == True) and (self.radio_tocup_sist.isChecked() == True):
                self.label_imagen.setPixmap(pixmap_3_N)
                
        elif self.comboBox_norm.currentText() == "No":
            pixmap_1 = QPixmap(directorio + "temp_graficos/" + 'ArrivalHistogram.png')
            pixmap_2 = QPixmap(directorio + "temp_graficos/" + 'QueueHistogram.png')
            pixmap_3 = QPixmap(directorio + "temp_graficos/" + 'WaitHistogram.png')
            
            if self.radio_tespera.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_3)
            elif self.radio_tinter_arribo.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_1)
            elif self.radio_tocup_sist.isChecked() == True:
                self.label_imagen.setPixmap(pixmap_2)
            elif (self.radio_tespera.isChecked() == True) and (self.radio_tinter_arribo.isChecked() == True) and (self.radio_tocup_sist.isChecked() == True):
                self.label_imagen.setPixmap(pixmap_3)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv) 
    window_central = MyApp() 
    window_central.show() 
    sys.exit(app.exec_())