from PyQt5 import QtWidgets,uic
from load.load_ventana_calculadora import VentanaCalculadora
from load.load_ventana_galones import VentanaGalones
from load.load_ventana_grados import VentanaGrados
from load.load_ventana_millas import VentanaMillas

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/menu_principal.ui", self)
        self.showMaximized()

        self.actionCalculadora.triggered.connect(self.ingresarCalculadora)
        self.actionConversi_n_a_gal.triggered.connect(self.ingresarGalones)
        self.actionConversi_n_de_grados.triggered.connect(self.ingresarGrados)
        self.actionConversi_n_de_millas.triggered.connect(self.ingresarMillas)
        self.actionSalir.triggered.connect(self.salir)

    def ingresarCalculadora(self):
        calculadora = VentanaCalculadora()
        calculadora.exec()
    def ingresarGalones(self):
        galones = VentanaGalones()
        galones.exec()
    def ingresarGrados(self):
        grados = VentanaGrados()
        grados.exec()
    def ingresarMillas(self):
        millas = VentanaMillas()
        millas.exec()
    def salir(self):
        self.close()
