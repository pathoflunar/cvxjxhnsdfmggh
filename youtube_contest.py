from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox

app = QApplication([]) #приложение
window = QWidget() #окно
window.setWindowTitle('Вопросник')
window.resize(500, 200)
# ----------------------------------------

v_line = QVBoxLayout() # < Главная Вертикальная Линия
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()
h3_line = QHBoxLayout()
# ^ Второстепенные Горизонтальные Линии

# ----------------------------------------

def show_true():
    Result = QMessageBox()
    Result.setText('Верно!')
    Result.exec_()

def show_false():
    Result = QMessageBox()
    Result.setText('Ответ неверный')
    Result.exec_()

# ----------------------------------------

quest = QLabel('В каком году MrBeast получил Кастомную кнопку на 300м подписчиков?') #Текст
v1 = QRadioButton('2021') 
v2 = QRadioButton('2022')
v3 = QRadioButton('2023')
v4 = QRadioButton('2024')
# ^ Варианты 1-4 ^

# ----------------------------------------

h1_line.addWidget(quest, alignment = Qt.AlignCenter)

h2_line.addWidget(v1, alignment = Qt.AlignCenter)
h2_line.addWidget(v3, alignment = Qt.AlignCenter)

h3_line.addWidget(v2, alignment = Qt.AlignCenter)
h3_line.addWidget(v4, alignment = Qt.AlignCenter)

v_line.addLayout(h1_line)
v_line.addLayout(h2_line)
v_line.addLayout(h3_line)

window.setLayout(v_line)

# ----------------------------------------

v1.clicked.connect(show_false)
v2.clicked.connect(show_false)
v3.clicked.connect(show_false)

v4.clicked.connect(show_true)

# ----------------------------------------

window.show() #показать окно
app.exec() #открыть окно