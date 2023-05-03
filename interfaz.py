import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QGridLayout

class MainWindow(QWidget):
    def __init__(self, matriz_juego: list):
        super().__init__()
        self.setWindowTitle("Mi ventana principal")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.show()
        self.botones = []
        for i, fila in enumerate(matriz_juego):
            fila_botones = []
            for j, elemento in enumerate(fila):
                boton = QPushButton("")
                boton.setMinimumSize(50, 50)
                boton.setMaximumSize(50, 50)
                boton.setStyleSheet("QPushButton {"
                                    "   min-width: 50px;"
                                    "   max-width: 50px;"
                                    "   min-height: 50px;"
                                    "   max-height: 50px;"
                                    "}")
                boton.setCheckable(True)
                boton.clicked.connect(lambda _, i=i, j=j: self.mostrar_celda(i, j, matriz_juego))
                fila_botones.append(boton)
                self.layout.addWidget(boton, i, j)
            self.botones.append(fila_botones)
        self.show()

    def mostrar_celda(self, i, j, matriz_juego):
        if matriz_juego[i][j] == "\U0001F4A3":
            self.botones[i][j].setText("\U0001F4A3")
        else:
            self.botones[i][j].setText(str(matriz_juego[i][j]))
        self.botones[i][j].setChecked(True)

if __name__ == "__main__":
    # Ejemplo de matriz de juego:
    import buscaminas

    app = QApplication(sys.argv)
    window = MainWindow(buscaminas.juego)
    sys.exit(app.exec_())

