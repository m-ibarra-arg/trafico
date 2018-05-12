
# Desarrollo de interfaz gráfica

Para introducir parámetros, ejecutar y visualizar los resultados de las simulación, se realiza un interfaz gráfica, de uso amigable e intuitivo, que facilite el uso del código antes mencionado.

Para esto utilizamos PyQt, para vincular las funciones creadas para la simulación de los modelos, y Qt Designer, para hacer mas sencilla el desarrollo de la parte gráfica de la interfaz. Este ultimo permite arrastrar y colocar botones, etiquetas, lineas de edición, etc, necesarias para que el usuario pueda interaccionar con el programa. Ademas se puede editar muy fácilmente.

## SimuladorQ_EXE.py
Aquí se encuentran la mayoría de las clases y funciones que dan vida al programa. Para el funcionamiento se requiere importar las siguientes librerías y/o módulos:

```python    
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
```
Donde *QtGui, uic, QtWidgets, QMessageBox, QPixmap* son submódulos de *PyQt5*, que regulan ciertas funciones y sobre todo la visualización del programa. Luego esta *modelos*, aclarado en el Análisis del código. Otro módulo que se crea es *funciones_externas*, que contienen las funciones para el tratamiento de ficheros, carpetas e hiperenlaces para la documentación. Las demás librerías las detallaremos mas adelante.

### Ventanas
El programa esta compuesto por 2 ventanas, una principal (presentación y elección del modelo de simulación) y una secundaria (ingreso de parámetros y visualización de resultados). Esta ultima se podría decir que son 3, cada una para un modelo distinto (Ver *Análisis de funcionamiento*). En *SimuladorQ_EXE.py* cada ventana esta representada por un clase, y cada clase contiene todas las funciones necesarias para levantar el modelo y el funcionamiento. Lo esencial es tomar los datos xml generados por Qt Designer y construir el objeto que contiene la información de visualización. Para esto se utiliza el modulo *uic* de la siguiente forma:
```python    
qtCreatorFile_main = "SimuladorQ.ui"
qtCreatorFile_mm1 = "entrada_salida_MM1.ui"  
qtCreatorFile_mg1 = "entrada_salida_MG1.ui" 
qtCreatorFile_mm1k = "entrada_salida_MM1K.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile_main) 
Ui_entrada_salida_mm1, QtBaseClass = uic.loadUiType(qtCreatorFile_mm1)
Ui_entrada_salida_mg1, QtBaseClass = uic.loadUiType(qtCreatorFile_mg1)
Ui_entrada_salida_mm1k, QtBaseClass = uic.loadUiType(qtCreatorFile_mm1k)
```
 De los archivos *.ui* se toma la información gráfica de la interfaz y se convierten a objetos que sean los argumentos de entrada de las clases. Estas son:
```python    
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow)
[...]
class MyApp_mm1(QtWidgets.QMainWindow, Ui_entrada_salida_mm1)
[...]
class MyApp_mg1(QtWidgets.QMainWindow, Ui_entrada_salida_mg1)
[...]
class MyApp_mm1k(QtWidgets.QMainWindow, Ui_entrada_salida_mm1k)
```
Para la inicialización, presentación, visualización y funcionalidad, cada clase tiene una estructura similar para la función `__init__`:
```python    
def __init__(self): 
        try:
            QtWidgets.QMainWindow.__init__(self) 
            Ui_MainWindow.__init__(self) 
            self.setupUi(self) 
            self.move(475,200)
            directorio = os.getcwd() + '/'
            pixmap = QPixmap(directorio  + "logo simulatorQ_titulo.png")
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
```
*QtWidgets.QMainWindow* Manejan la ventana como si fuera la principal. Aquí utilizamos la librería os para crear, modificar y eliminar ficheros y directorios. En este caso, para tomar el path del directorio desde el cual se esta ejecutando y poder mostrar la imagen del logo del programa.

Luego podemos ver que los botones se indican con `self.NOMBRE_BOTON.clicked.connect(FUNCION)`. Qt trabaja de una forma en la que la vinculación de los botones del entorno con alguna función es a través de señales y slots, y en todo el programa, las señales se producen al hacer click sobre un botón(`Nombre_Boton.clicked.[...]`), esto las conecta con la función a ejecutar(`[...].clicked.connect(Funcion)`). 

Para las acciones del menú es similar al caso anterior, pero se indica con los métodos `ACCION.triggered.connect(FUNCION)`.

En los lugares que se hace referencia a `self.NOMBRE_FUNCION`, quiere decir que la función esta declarada dentro de la misma clase (ventana) y la utiliza con los mismos atributos dentro de ella. Las funciones que no se les indica *self* por delante, son aquellas que están por fuera y son importadas (`funciones_externas`).

Por último, vemos que todo esta basado en la estructura try/except. Esto es porque en primera instancia se intenta ejecutar la clase tal cual se pretende, sin embargo pueden existir errores y excepciones que impiden el normal funcionamiento del programa. El error mas común es el de falta de permisos (Ver *Análisis de funcionamiento*). Se advierte con un mensaje en forma pop-up gracias a la instrucción `QMessageBox`, submódulo propio de `QtWidgets`. Tiene variantes como mensajes críticos (`QMessageBox.critical`), de advertencia (`QMessageBox.warning`), y de interrogantes (`QMessageBox.critical`), muy usados en todo el programa. También existen de información y mas. Para todo el resto de los errores, se captura la excepción mostrada por la terminal de Python y se muestra en un `QMessageBox.critical` con su detalle, gracias a `traceback.format_exc()`, para que el usuario, llegado al caso de incurrir en este error, pueda solucionarlo accediendo al código del software.

### Funciones de la clase `MyApp`
Describimos algunas de las funciones de MyApp, clase que representa la ventana principal.

#### `openWindow_MODELO()`
```python    
	def openWindow_mm1(self):
        self.anotherwindow = MyApp_mm1()
        self.anotherwindow.showMaximized()
        self.hide()
```
Abre la ventana donde se ingresarán los parámetros de simulación y se visualizarán los resultados, para el modelo M/M/1. Por comodidad se usa el método `showMaximized()` para ventana maximizada. Y se oculta la ventana principal para mostrar la nueva con `hide()`. Similar para las demás ventanas de modelos.

#### `closeEvent()`
```python    
     def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',"¿Está seguro que desea salir?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
```
Esta función existe para capturar el evento que se dispara al intentar cerrar el programa. Al detectarlo, con `QMessageBox.cuestion` se crea el mensaje pop-up preguntando si se desea cerrar o no. De acuerdo a la respuesta, *Yes* o *No*, el evento se acepta, o se descarta, y se sigue utilizando el simulador.

#### `open_modelos()`
```python    
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
```
Se ejecuta cuando se selecciona el modelo y se presiona el botón *Confirmar*. Si no hay ningún modelo seleccionado al presionar *Confirmar* se le advierte al usuario con un mensaje. 

La forma de verificar si esta seleccionado el modelo es con la instrucción `self.radio_MODELO.isChecked()`, que devuelve un booleano.

### Funciones de la clase de las subventanas
Como en la ventana principal, también tiene una función `__init__` con todos los botones y visualización. Usaremos el caso de la clase creada para el modelo M/M/1, pero para las demás, el tratamiento es similar. Lo mas destacable, sin redundar en lo que ya se ha analizado, es:

```python    
def __init__(self): 
        try:
            [...]      
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
            [...]
```
Se realiza un validación de datos para que el usuario no ingrese caracteres que no sirvan al momento de ejecutar la simulación. Lo que se solicita es que los caracteres cumplan con la condición de que se puedan ser convertidos a variables tipo `double`. Entonces no se pueden ingresar letras, comas, o caracteres mas propios de un string. La única letra que no se prohíbe con esta validación es la "e", que puede utilizarse para escribir con notación científica. El campo de "Usuario" esta libre de esta validación y puede ingresarse cualquier carácter, ya que se interpreta como string.

Todas las instrucciones que sean del tipo `line_VARIABLE` indican los campos donde el usuario ingresa valores y se transforman a variables. Para el caso de los menú desplegables, llamados por Qt como `comboBox`, se indican de la forma `comboBox_VARIABLE`.

Los `comboBox` crean las señales cuando cambian de estado, y se puede identificar de acuerdo al *currentText* (texto actual) o con *int* que es el numero que representa el estado del `comboBox`, es por eso que se usa `comboBox_norm.currentIndexChanged['int']`, menú de histogramas normalizados o sin normalizar, para desatar el evento y conectarla a una función.

La instrucción `self.radio_HISTOGRAMA.clicked.connect(self.graficos)` llama a la función gráficos de acuerdo al gráfico que quiera el usuario, y siempre se llama cuando se hace click en un botón de histograma distinto.

#### `reinicio()` , `limpiar()` y `resetear()`
```python    
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
        pixmap = QPixmap(directorio  + "logo_simulatorQ-reemplazo.png")
        self.label_imagen.setPixmap(pixmap)
```
Con esta funcion se limpian los parametros de entrada, llamando a `resetear()`, los parametros de salida (seteando caracter vacio en todas las lineas), borra el detalle de los paquetes servidos mostrando el mensaje original y deshace los histogramas, mostrando nuevamente el logo del programa.

```python    
	def limpiar(self):
        self.resetear()
```
Solo limpia los parámetros de entrada llamando a `resetear()`
```python    
    def resetear(self):
        self.comboBox_bins.setCurrentText('Seleccione')   
        self.line_lambda.setText("")
        self.line_mu.setText("")
        self.line_portrate.setText("")
        self.line_user.setText("")
        self.line_tsim.setText("")
```
##### `salir_programa()`
```python    
    def salir_programa(self):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',"¿Está seguro que desea salir?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            directorio = os.getcwd() + '/'
            if os.path.exists(directorio + 'temp_graficos'):
                shutil.rmtree(directorio + 'temp_graficos')
            sys.exit(0)
```
Se ejecuta cuando se pide salir utilizando la acción del menú `Archivo -> Salir`. Como en todos los casos, pide autorización para cerrar, y si es afirmativo, se borra la carpeta temporal donde se generan los histogramas, chequeando previamente si se creo alguno o no.

#### `guardar_entrada()`
```python    
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
```
Función para guardar los parámetros de entrada y posteriormente importarlos para realizar una simulación nueva. Llama a la función `saveFileDialog()` de `funciones_externas` y verifica los permisos para guardar, sino manda un mensaje de error. Superado este paso, se procede a guardar en variables los string de los campos de ingreso, convirtiéndolos al tipo de dato correcto, para posteriormente guardarlos en el fichero que tenga el nombre que ingresa el usuario. 

La única forma de verificar si es un archivo genuino de SimuladorQ y que sea el modelo correcto al momento de importarlo, es inspeccionando dentro del archivo la primer linea que debe tener el nombre del modelo solicitado. Es por eso que lo primero que se guarda en el archivo es ese dato, y luego el resto de los parámetros deseados.

Hay mas funciones para guardar aspectos de la simulación que trabajan de una forma similar.

#### `importar()`
```python    
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
```
Esta función copia las lineas del archivo que se genera al utilizar la función `guardar_entrada()` y las pega en los campos de ingreso de datos de la ventana. Como dijimos antes, la única validación que tiene, ademas de verificar los permisos, para poder ejecutarse, es leer la primer linea del fichero. Si es el modelo que corresponde, sigue la ejecución. SimuladorQ no repara en los casos que exista un archivo, en la que su primer linea sea MM1, MG1 o MM1K, y que después el resto sean datos ilegibles. No hay una comprobación de ese estilo. La única alternativa es que se se muestre un mensaje de error al momento de simular con datos incorrectos.

#### `simular()`
```python    
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
```
La función mas importante de SimuladorQ. Es donde se llama a la función `MM1` de `modelos.py`. 

Primero verifica que estén todos los campos correctamente ingresados. Si falta alguno, o hay números negativos (salvo el campo *Usuario*), se advierte con un error y no se realiza la simulación. Posteriormente se guarda la información de todos los campos de los parámetros de entrada en variables. 
```python    
            datos, twait_medio, pkt_drop, pkt_enviados, tasa_perdida, ocup_sistema, pkt_recibidos_serv, intensidad_trafico, espera_cola_Wq, ocup_cola_Lq = MM1(lamda, mu, user, portrate, tsim, bins, directorio)
```
Aquí se llama a la función de `modelos.py`
```python    
			self.text_consola.setTextColor(QtGui.QColor("white"))
            self.text_consola.setFont(QtGui.QFont(u'Ubuntu', 11))
            self.text_consola.setText("Información detallada de paquetes servidos:" + "\n \n" + datos)
            self.text_consola.setReadOnly(True)
```
La variable de salida `datos` contiene la información del detalle de los paquetes servidos, en forma de string. En la ventana se muestran en el campo correspondiente de la mano de `text_consola` y con el método `.setText()`. También se le pide que esos datos string sean de solo lectura con `.setReadOnly(True)` para  evitar modificaciones accidentales.
```python    
            self.line_pkt_drop.setText(format(pkt_drop))
            self.line_pkt_enviados.setText(format(pkt_enviados))
            self.line_pkt_recibidos.setText(format(pkt_recibidos_serv))
```   
```python    
			if twait_medio < 0.001:
                self.line_twait_medio.setText(format(twait_medio))
            else:
                self.line_twait_medio.setText("{:.5f}".format(twait_medio))
			[...]
			self.line_twait_medio.setReadOnly(True)   
			[...]
```               
Los parámetros de salida se llenan con los demás argumentos de salida de la función `MM1`, pegándolos en los campos correspondientes y convirtiéndolos en tipo de dato `float`. Dependiendo del orden del resultado, se pueden mostrar mas o menos decimales. Además también se pide al mostrarse sean de solo lectura.
```python    
    #        Setear una imagen de entrada
            self.label_imagen.setStyleSheet("background-color: rgb(255, 255, 255);")
            pixmap_3_N = QPixmap(directorio  + "temp_graficos/" + 'WaitHistogram_normal.png')
            self.label_imagen.setPixmap(pixmap_3_N) 
```     
Se graba una imagen predeterminada de histograma, que luego puede cambiar de acuerdo a la preferencia del usuario. `QPixmap` es el submodelo que permite crear generar imágenes dentro de un elemento `Qlabel`.

#### gráficos()

```python    
    def graficos(self):
        directorio=os.getcwd() + '/'
```     
Esta función se ejecuta siempre que se quiere cambiar de gráfico para visualizarlo, ya sea en forma normalizada o no. Primero se guarda en la variable `directorio` el directorio actual donde se esta ejecutando el programa. Esto se hace invocando el modulo estándar *os* con su método *getcwd* `os.getcwd()`). Como es un string, y para que sea un directorio, se le agrega una barra "/" para finalizar. 

```python    
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
```     
Se verifica si el texto actual del *comboBox_norm* dice "Si". En caso afirmativo se corrobora paso a paso cual es el ítem de histograma que es seleccionado, grabando la imagen que corresponde, buscándola en la carpeta temporal creada para este fin.

```python    
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
```     
 Lo mismo para el caso en que el texto actual del *comboBox_norm* sea "No".

## funciones_externas.py

Se crea este modulo para extraer todas aquellas funciones que no necesitaban una vinculación directa con los objetos de Qt. Podemos separarlas en 2 grupos, por un lado las funciones para manejo de archivos y carpetas, y por el otro aquellas que nos llevan a las paginas web de interés y de documentación.

### setFolderDialog()

```python    
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
``` 
Con esta función se establece un directorio donde se va a trabajar, determinado por el usuario. Usada para exportar la salida de la simulación con el menú `Archivo -> Guardar -> Todo`.

Con la instrucción `QtWidgets.QFileDialog.getExistingDirectory(None,"Seleccionar directorio","", QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks)` se solicita al usuario con un menú que indique un directorio, y se guarda como string en la variable `folderName`.

Siempre y cuando el usuario elija el directorio, por una cuestión de manejo de la variable, se le agrega una barra mas "/" para posteriormente trabajar con es carpeta. Si no se elije nada, se devuelve la variable `folderName` con un string vacío. En otra instancia del programa se le da un tratamiento distinto.

Luego pueden existir errores de permisos o de funcionamiento que tiene su correspondiente mensaje de error. 

### openFileNameDialog()
```python    
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
``` 
Similar al anterior, esta función selecciona archivos. Es usada al momento de buscar y elegir archivos para importar parámetros de entrada.

Utiliza los módulos y submódulos de la función `setFolderDialog()`, pero ademas en los argumentos de entrada de `QtWidgets.QFileDialog.getOpenFileName` da la posibilidad de visualizar al momento de elegir archivos con diferentes formatos.

Ademas del nombre del archivo, la función devuelve el directorio de ese archivo.

### saveFileDialog()

```python    
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
``` 
Similar a los anteriores, esta función es usada para guardar los parámetros de entrada, salida, y detalle de paquetes servidos. También devuelve nombre y directorio del archivo que se va a guardar.

El usuario debe brindar un nombre para el archivo a guardar. Si no lo hace, incurre en un error y se devuelve variables con string vacíos. En el caso en que se provea un nombre, pero sin una extensión, el programa le da una extensión *.siq*, propia de SimuladorQ, pero puede escoger entre elegir entre esa, o *.txt*.

### doc_python_web() y similares
```python    
def doc_python_web():
    webbrowser.open("https://www.python.org/doc/", new=2, autoraise=True)
``` 
Funciones con el objetivo de llevar al usuario a las paginas web de documentaciones importantes para el uso, desarrollo y mejor conocimiento de SimuladorQ.

Para eso se importa el modulo `webbrowser`, que permite abrir una `url` , en una nueva pestaña del navegador web por defecto, y que ademas, se abra y/o se levante automáticamente.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMwMjE3MjczMF19
-->