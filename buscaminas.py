from emoji import iconos
from random import random as rand
from PyQt5.QtWidgets import QSpinBox, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QApplication
import sys
import interfaz

app = QApplication(sys.argv)
class Buscaminas(QWidget):
    def __init__(self):
        super().__init__()
        x = 10
        y = 10
        dificultad = 10
        self.juego = []
        self.celdas_activadas = []

        # Crear la interfaz gráfica
        self.setWindowTitle("Buscaminas")
        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        # Crear un layout para los QSpinBoxes
        layout_spinboxes = QHBoxLayout()

        label_x = QLabel("Ancho del juego:")
        self.spinbox_x = QSpinBox()
        self.spinbox_x.setMinimum(10)
        self.spinbox_x.setMaximum(50)
        self.spinbox_x.setValue(x)

        label_y = QLabel("Alto del juego:")
        self.spinbox_y = QSpinBox()
        self.spinbox_y.setMinimum(10)
        self.spinbox_y.setMaximum(50)
        self.spinbox_y.setValue(y)

        label_dificultad = QLabel("Dificultad (% de minas):")
        self.spinbox_dificultad = QSpinBox()
        self.spinbox_dificultad.setMinimum(10)
        self.spinbox_dificultad.setMaximum(80)
        self.spinbox_dificultad.setValue(dificultad)

        layout_spinboxes.addWidget(label_x)
        layout_spinboxes.addWidget(self.spinbox_x)
        layout_spinboxes.addWidget(label_y)
        layout_spinboxes.addWidget(self.spinbox_y)
        layout_spinboxes.addWidget(label_dificultad)
        layout_spinboxes.addWidget(self.spinbox_dificultad)

        # Agregar los spinboxes al layout principal
        self.layout_principal.addLayout(layout_spinboxes)

        # Agregar el botón para iniciar el juego
        boton_iniciar = QPushButton("Iniciar")
        boton_iniciar.clicked.connect(self.iniciar_juego)
        self.layout_principal.addWidget(boton_iniciar)

    def iniciar_juego(self):
        # Obtener los valores de los spinboxes
        x = self.spinbox_x.value()
        y = self.spinbox_y.value()
        dificultad = self.spinbox_dificultad.value()
        # Agregar muro de fondo al juego
        i = 0 
        while i < y: 
            j = 0
            fila = []
            while j < x:
                fila.append(iconos.MURO.value)
                j += 1
            self.juego.append(fila)
            i += 1

        # Calcula de la cantidad de minas 
        cantidad_minas = int(((x * y) * dificultad) / 100)

        # Coloca las minas en la matriz del juego sin duplicar
        while cantidad_minas > 0:
            nuevox = int(x * rand())
            nuevoy = int(y * rand())
            if self.juego[nuevoy][nuevox] != iconos.MINA.value:
                self.juego[nuevoy][nuevox] = iconos.MINA.value
                cantidad_minas -= 1

        # Rellenar las pistas
        
        import logica
        y = 0 
        while y < len(self.juego): 
            x = 0
            fila = []
            while x < len(self.juego[y]):
                if self.juego[y][x] != iconos.MINA.value:
                    self.juego[y][x] = logica.bombas_vecinas(x, y, self.juego)  
                x += 1
            y += 1


        interfaz.MainWindow(self.juego)

ventana = Buscaminas()
ventana.show()
sys.exit(app.exec_())


