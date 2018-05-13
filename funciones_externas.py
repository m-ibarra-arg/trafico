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
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys
import traceback

import webbrowser

def setFolderDialog():
    try:
        folderName = QtWidgets.QFileDialog.getExistingDirectory(None,"Seleccionar directorio","", QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks)
        if folderName != "":
            folder = folderName.split('/')
            folderName = '/'.join(folder) + '/'
        else:
            folderName = ""
        return folderName
    except FileNotFoundError:
        error = traceback.format_exc()
        QMessageBox.critical(None, 'Error al seleccionar directorio', "Provea una carpeta valida.             ", QMessageBox.Ok)
        sys.exit(0)
    except:
        error = traceback.format_exc()
        QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)

def openFileNameDialog():
    try:
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = ""
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Abrir archivo", "","SimuladorQ Files (*.siq);;Python Files (*.py);;Text Files (*.txt);;Image Files (*.png);;Image Files(*.jpg);;All Files (*)", options=options)

        if fileName != "":
            folder = fileName.split('/')
            folderName = '/'.join(folder[0:len(folder)-1]) + '/'
        else:
            fileName = ""
            folderName = ""
        return fileName, folderName
    except FileNotFoundError:
        error = traceback.format_exc()
        QMessageBox.critical(None, 'Error al seleccionar directorio', "Provea una carpeta valida.             ", QMessageBox.Ok)
        sys.exit(0)
    except:
        error = traceback.format_exc()
        QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)

def saveFileDialog():
    try:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None,"Guardar archivo","","All Files (*);;Python Files (*.py);;SimuladorQ Files (*.siq);;Text Files (*.txt);;Image Files (*.png);;Image Files(*.jpg)", options=options)
        
        if fileName != "":
            folder = fileName.split('/')
            folderName = '/'.join(folder[0:len(folder)-1]) + '/'
                
            if fileName.find(".siq",0,len(fileName)) != -1:
                fileName= fileName.replace('.siq','')
                fileName = fileName + ".siq"
            elif fileName.find(".txt",0,len(fileName)) != -1:
                fileName= fileName.replace('.txt','')
                fileName = fileName + ".txt"
            elif fileName.find(".txt",0,len(fileName)) == -1 and fileName.find(".siq",0,len(fileName)) == -1 :
                fileName= fileName + '.siq'
        else:
            fileName = ""
            folderName = ""
        return fileName, folderName
    
    except FileNotFoundError:
        error = traceback.format_exc()
        QMessageBox.critical(None, 'Error al seleccionar directorio', "Provea una carpeta valida.             ", QMessageBox.Ok)
        sys.exit(0)
    except:
        error = traceback.format_exc()
        QMessageBox.critical(None, 'Error de ejecucion', "Detalle del error:\n\n" + error + '\n\nPor favor, revise la documentacion del programa.', QMessageBox.Ok)
        
def doc_python_web():
    webbrowser.open("https://www.python.org/doc/", new=2, autoraise=True)
        
def doc_simpy_web():
    webbrowser.open("https://simpy.readthedocs.io/en/latest/", new=2, autoraise=True)
    webbrowser.open("https://www.grotto-networking.com/DiscreteEventPython.html#Intro", new=2, autoraise=True)
    
def doc_pyqt_web():
    webbrowser.open("https://riverbankcomputing.com/software/pyqt/intro", new=2, autoraise=True)
    webbrowser.open("http://pyqt.sourceforge.net/Docs/PyQt5/", new=2, autoraise=True)
    
def doc_simuladorQ_web():
    webbrowser.open("http://simuladorq.readthedocs.io/es/latest/", new=2, autoraise=True)
    
def gen_corutinas_web():
    webbrowser.open("http://www.dabeaz.com/coroutines/Coroutines.pdf", new=2, autoraise=True)
    
def tuto_python_web():
    webbrowser.open("http://librosweb.es/libro/algoritmos_python/", new=2, autoraise=True)
    
def tuto_pyqt_web():
    webbrowser.open("https://www.tutorialspoint.com/pyqt/index.htm", new=2, autoraise=True)
    webbrowser.open("https://www.youtube.com/playlist?list=PLgHCrivozIb0-aaqXCbzVfzv535DVnMyi", new=2, autoraise=True)
    

    