from PyQt5 import QtWidgets,uic
from clases.grados import Grados
class VentanaGrados(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_grados.ui",self)
        self.show()

        self.boton_sumar.clicked.connect(self.botonSumarClick)

    def botonSumarClick(self):
        grad=int(self.edit_numero1.text())
        convertir=Grados(grad)
        convertir.calcularSuma()
        self.label_resultado.setText(str(convertir.resultado))