import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from TaxisTarifa import Ui_Taxis
if __name__ == '__main__':
    #crear la aplicación
    app = QApplication(sys.argv)
    #instanciamos un objeto de ventana principal
    window = QMainWindow()
    #ui de los objetos a renderizar
    ventana=Ui_Taxis()
    #renderizar los objetos en la main windoe
    ventana.setupUi(window)
    #mostrar la ventana
    window.show()
    sys.exit(app.exec_())