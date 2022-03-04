import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from vista.main import Ui_MainWindow as ventanaPrincipal
from sintactico import ejecucionAlgoritmo

class MyApp(PyQt5.QtWidgets.QMainWindow, ventanaPrincipal):
    def __init__(self):
        PyQt5.QtWidgets.QMainWindow.__init__(self)
        ventanaPrincipal.__init__(self)
        self.setupUi(self)
        acciones(self)

def acciones(ventana):
    redireccionarTabla(ventana)
    ventana.uploadTxt.clicked.connect(lambda: cargarArchivo(ventana))
    ventana.exportTxt.clicked.connect(lambda: salidaTexto(ventana))

def redireccionarTabla(ventana):
    linkTemplate = '<a href={0}>{1}</a>'
    ventana.labelRedireccion.setText(linkTemplate.format('https://docs.google.com/spreadsheets/d/1-fjoJEN6XNvIwNLi4aHbaexLVrrE6pTmhKY8W-7ITlE/edit#gid=0','Tabla De Analisis'))
    ventana.labelRedireccion.setStyleSheet('font-size: 18px')

def cargarArchivo(ventana):
    eleccion = PyQt5.QtWidgets.QFileDialog.getOpenFileName(None,"Seleccione Archivo","", "Text Files (*.txt)")
    try:
        with open(eleccion[0]) as f:
            lines = f.read().splitlines()
        texto = ''.join(lines)
        ventana.inputText.setPlainText(texto)
    except:
        print("escoja un archivo txt")

def llenadoTabla(ventana,sintaxis):
    ventana.tabla.setRowCount(0) #limpia la tabla
    ventana.tabla.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #no edita la tabla
    fila = 0
    for registro in sintaxis:
        columna = 0
        ventana.tabla.insertRow(fila)
        for elemento in registro:
            celda = QTableWidgetItem(elemento)
            ventana.tabla.setItem(fila, columna, celda)
            columna+=1
        fila+=1

def salidaTexto(ventana):
    lista = []
    entrada = ventana.inputText.toPlainText()
    ejecucionAlgoritmo(entrada)
    #llenadoTabla(ventana,lista)
    #ventana.outputText.setPlainText(lista)

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)  # crea un objeto de aplicación (Argumentos de sys)
    window = MyApp()
    window.show()
    window.setFixedSize(window.size())
    app.exec_()
