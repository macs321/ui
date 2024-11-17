from PyQt6.QtWidgets import QMainWindow, QApplication
from ui import Ui_MainWindow

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)



def func():
    text = "Привіт"
    ui.result.setText(text)

ui.generate.clicked.connect(func)



win.show()
app.exec()