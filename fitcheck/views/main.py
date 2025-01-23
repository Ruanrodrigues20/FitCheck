import sys
from PySide6.QtWidgets import QApplication, QPushButton


#QApplication e QPushButton de PySyde¨.QtWidgets
#1 O widget principal da aplicacao
#2 um botão
#3 Onde estao os widgets do pyside6 

app = QApplication(sys.argv)

botao = QPushButton('Ola cara')
botao.setStyleSheet('font-size: 40px; color: red')
botao.show()


app.exec()