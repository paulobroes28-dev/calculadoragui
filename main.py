from load.load_ventana_calculadora import VentanaCalculadora
from load.load_ventana_galones import VentanaGalones
from load.load_ventana_grados import VentanaGrados
from load.load_ventana_millas import VentanaMillas
from PyQt5 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaCalculadora()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()