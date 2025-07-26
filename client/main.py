# client/main.py - минимальный рабочий пример
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("TaskFlow")
window.setGeometry(100, 100, 400, 200)

label = QLabel("Добро пожаловать в TaskFlow!", parent=window)
label.move(50, 50)

window.show()
sys.exit(app.exec())