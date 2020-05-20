from PySide2.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QLabel
import random as rd

class fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500, 300)
        self.setWindowTitle('Ma fenetre')

        self.layout = QVBoxLayout()
        self.label = QLabel('CSI')
        self.button1 = QPushButton('Changer le cycle')

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button1)
        self.button1.clicked.connect(self.buttononClick)

        self.setLayout(self.layout)

    def buttononClick(self):
        liste = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        self.label.setText(rd.choice(liste))



if __name__ == "__main__":
   app = QApplication([])
   win = fenetre()
   win.show()
   app.exec_()
