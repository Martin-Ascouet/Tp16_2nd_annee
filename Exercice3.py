from PySide2.QtWidgets import QWidget, QTextEdit, QPushButton, QApplication, QVBoxLayout


class IHM(QWidget):
    def __init__(self, n=1):
        QWidget.__init__(self)
        self.n = n
        self.setFixedSize(500, 300)
        self.setWindowTitle('IHM')
        self.layout = QVBoxLayout()

        self.button1 = QPushButton('FERMER LA FENETRE')
        self.button2 = QPushButton('Changer mon texte !')
        self.notificationPanel = QTextEdit()
        self.notificationPanel.setText('Le nombre de clics va être affiché ici')


        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.notificationPanel)


        self.button1.clicked.connect(self.Click)
        self.button2.clicked.connect(self.ComptClick)

        self.setLayout(self.layout)

    def Click(self):
        self.close()

    def ComptClick(self):
        self.button2.setText('clic '+str(self.n))
        self.notificationPanel.setText('clic '+str(self.n))
        self.n += 1


if __name__ == "__main__":
    app = QApplication([])
    win = IHM()
    win.show()
    app.exec_()
