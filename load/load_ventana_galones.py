from PyQt5 import QtWidgets,uic
from clases.galones import Galones
class VentanaGalones(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_galones.ui",self)
        self.show()

        self.boton_sumar.clicked.connect(self.botonSumarClick)

    def botonSumarClick(self):
        gal=int(self.edit_numero1.text())
        convertir=Galones(gal)
        convertir.calcularSuma()
        self.label_resultado.setText(str(convertir.resultado))