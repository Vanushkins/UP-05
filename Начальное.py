from PyQt5 import QtCore, QtGui, QtWidgets
# Класс для главного окна
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 40, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 120, 261, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 0, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 200, 261, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 290, 261, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Привязка кнопки к функции показа правил
        self.pushButton_2.clicked.connect(self.show_rules)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра \"Слова из слова\""))
        self.label.setText(_translate("MainWindow", "Слова из слова"))
        self.pushButton.setText(_translate("MainWindow", "Начать игру"))
        self.pushButton_2.setText(_translate("MainWindow", "Правила игры"))
        self.pushButton_3.setText(_translate("MainWindow", "Настройки"))
        self.pushButton_4.setText(_translate("MainWindow", "Выход из игры"))
        self.pushButton_4.clicked.connect(MainWindow.close) # сам написал)))

    def show_rules(self):
        # Создаем и показываем диалоговое окно с правилами
        self.dialog = QtWidgets.QDialog()
        self.ui_rules = Ui_Dialog()
        self.ui_rules.setupUi(self.dialog)
        self.dialog.exec_()

# Класс для диалогового окна с правилами игры
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 511)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 450, 131, 41))
        self.pushButton.setObjectName("pushButton")

        # Связываем нажатие кнопки "Понятно" с функцией закрытия окна
        self.pushButton.clicked.connect(Dialog.close)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 571, 381))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Правила Игры"))
        self.pushButton.setText(_translate("Dialog", "Я понял!"))
        self.label.setText(_translate("Dialog", "Правила Игры"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">1.Создавать можно только нарицательные существительные </span></p><p align=\"justify\"><span style=\" font-size:9pt;\">в единственном числе</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">2.Чтобы добавить или убрать букву из слова, </span></p><p align=\"justify\"><span style=\" font-size:9pt;\">нужно нажать на букву внизу.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">3.Когда слово будет набрано, нажмите на галочку</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">4.Чтобы перейти на следующий уровень нужно набрать определённое </span></p><p align=\"justify\"><span style=\" font-size:9pt;\">количество слов(оно указано в нижней строчке), </span></p><p align=\"justify\"><span style=\" font-size:9pt;\">как только пользователь находит нужное количество слов, он может </span></p><p align=\"justify\"><span style=\" font-size:9pt;\">переходить на следующий уровень</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">5.Буква «Е» и «Ё» взаимозаменяемы по техническим причинам.</span></p><p align=\"justify\"><span style=\" font-size:9pt;\">6.Нажатие на слово позволит вам узнать его значение</span></p><p align=\"justify\"><span style=\" font-size:9pt;\"><br/></span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

