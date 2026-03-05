from PyQt5 import QtWidgets,uic
from clases.millas import Millas
class VentanaMillas(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_millas.ui",self)
        self.show()

        self.boton_sumar.clicked.connect(self.botonSumarClick)

    def botonSumarClick(self):
        mil=int(self.edit_numero1.text())
        convertir=Millas(mil)
        convertir.calcularSuma()
        self.label_resultado.setText(str(convertir.resultado))