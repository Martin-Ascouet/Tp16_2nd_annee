from PySide2.QtWidgets import QWidget,QHBoxLayout,QProgressBar,QSlider, QPushButton, QApplication, QVBoxLayout, QLabel

class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500, 300)
        self.setWindowTitle('IHM')
        self.layout = QHBoxLayout()

        self.progressBar = QProgressBar()
        self.progressBar.setValue(50)
        self.slider = QSlider()
        self.slider.setValue(50)

        self.layout.addWidget(self.progressBar)
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.OnSlider)
        self.setLayout(self.layout)

    def OnSlider(self):
        val = self.slider.value()
        self.progressBar.setValue(val)

if __name__ == "__main__":
   app = QApplication([])
   win = IHM()
   win.show()
   app.exec_()
