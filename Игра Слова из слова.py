from PyQt5 import QtCore, QtGui, QtWidgets
# Класс для главного окна игры
class Ui_MainWindowGame(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Кнопка "Выход в меню"
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.pushButton.setObjectName("pushButton")
        
        # Кнопки с буквами
        self.Bukva1 = QtWidgets.QPushButton(self.centralwidget)
        self.Bukva1.setGeometry(QtCore.QRect(150, 20, 51, 51))
        self.Bukva1.setObjectName("Bukva1")
        
        self.Burkva2 = QtWidgets.QPushButton(self.centralwidget)
        self.Burkva2.setGeometry(QtCore.QRect(220, 20, 51, 51))
        self.Burkva2.setObjectName("Burkva2")
        
        self.Bukva3 = QtWidgets.QPushButton(self.centralwidget)
        self.Bukva3.setGeometry(QtCore.QRect(290, 20, 51, 51))
        self.Bukva3.setObjectName("Bukva3")
        
        self.Burkva4 = QtWidgets.QPushButton(self.centralwidget)
        self.Burkva4.setGeometry(QtCore.QRect(360, 20, 51, 51))
        self.Burkva4.setObjectName("Burkva4")
        
        self.Bukva5 = QtWidgets.QPushButton(self.centralwidget)
        self.Bukva5.setGeometry(QtCore.QRect(430, 20, 51, 51))
        self.Bukva5.setObjectName("Bukva5")
        
        self.Bukva6 = QtWidgets.QPushButton(self.centralwidget)
        self.Bukva6.setGeometry(QtCore.QRect(500, 20, 51, 51))
        self.Bukva6.setObjectName("Bukva6")
        
        self.Bukva7 = QtWidgets.QPushButton(self.centralwidget)
        self.Bukva7.setGeometry(QtCore.QRect(570, 20, 51, 51))
        self.Bukva7.setObjectName("Bukva7")
        
        # Надпись "Введённое слово:"
        self.wordLabel = QtWidgets.QLabel(self.centralwidget)
        self.wordLabel.setGeometry(QtCore.QRect(100, 80, 250, 50))
        self.wordLabel.setText("Введённое слово:")
        self.wordLabel.setObjectName("wordLabel")
        
        # Поле для отображения текущего составленного слова 
        self.currentWordLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentWordLabel.setGeometry(QtCore.QRect(200, 80, 400, 50))
        self.currentWordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentWordLabel.setStyleSheet("font-size: 28px; font-weight: bold;")
        self.currentWordLabel.setText("")
        self.currentWordLabel.setObjectName("currentWordLabel")
        
        # Поле для отображения списка отгаданных слов
        self.Spisok_Slov = QtWidgets.QTextBrowser(self.centralwidget)
        self.Spisok_Slov.setGeometry(QtCore.QRect(20, 140, 661, 321))
        self.Spisok_Slov.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.Spisok_Slov.setObjectName("Spisok_Slov")
        
        # Кнопки "Предыдущий уровень" и "Следующий уровень"
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 470, 141, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(540, 470, 141, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Список допустимых слов
        self.dopustimye_slova = ["коза", "роза", "икра", "кора", "зона", "рак", "нора", "кран", "рок", "корзина"]
        self.otgadannye_slova = []  # Список отгаданных слов
        self.otgadano = 0  # Счетчик отгаданных слов
        self.tekushee_slovo = ""  # Текущее составленное слово
        self.aktivnye_bukvy = []  # Список активных (нажатых) букв

        # Подключаем обработчики нажатий на кнопки с буквами
        self.Bukva1.clicked.connect(lambda: self.dobavit_bukvu(self.Bukva1))
        self.Burkva2.clicked.connect(lambda: self.dobavit_bukvu(self.Burkva2))
        self.Bukva3.clicked.connect(lambda: self.dobavit_bukvu(self.Bukva3))
        self.Burkva4.clicked.connect(lambda: self.dobavit_bukvu(self.Burkva4))
        self.Bukva5.clicked.connect(lambda: self.dobavit_bukvu(self.Bukva5))
        self.Bukva6.clicked.connect(lambda: self.dobavit_bukvu(self.Bukva6))
        self.Bukva7.clicked.connect(lambda: self.dobavit_bukvu(self.Bukva7))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Слова из слова"))
        self.pushButton.setText(_translate("MainWindow", "Выход в меню"))
        
        # Устанавливаем буквы на кнопки
        self.Bukva1.setText(_translate("MainWindow", "к"))
        self.Burkva2.setText(_translate("MainWindow", "о"))
        self.Bukva3.setText(_translate("MainWindow", "р"))
        self.Burkva4.setText(_translate("MainWindow", "з"))
        self.Bukva5.setText(_translate("MainWindow", "и"))
        self.Bukva6.setText(_translate("MainWindow", "н"))
        self.Bukva7.setText(_translate("MainWindow", "а"))
        
        self.Spisok_Slov.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:bold; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Список отгаданных слов (0 из 5):</p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "Предыдущий уровень"))
        self.pushButton_9.setText(_translate("MainWindow", "Следующий уровень"))

    def dobavit_bukvu(self, button):
        # Подсветка кнопки
        if button not in self.aktivnye_bukvy:
            button.setStyleSheet("background-color: yellow;")  # Подсветка
            self.aktivnye_bukvy.append(button)
            self.tekushee_slovo += button.text()
        else:
            button.setStyleSheet("")  # Убираем подсветку
            self.aktivnye_bukvy.remove(button)
            self.tekushee_slovo = self.tekushee_slovo.replace(button.text(), "", 1)
        
        # Обновляем поле с текущим словом
        self.currentWordLabel.setText(self.tekushee_slovo)

    def proverit_slovo(self):
        # Проверяем, есть ли слово в списке допустимых
        if self.tekushee_slovo in self.dopustimye_slova:
            if self.tekushee_slovo not in self.otgadannye_slova:
                self.otgadannye_slova.append(self.tekushee_slovo)
                self.otgadano += 1
                self.obnovit_spisok_slov()
                self.obnovit_schetchik()
        
        # Сбрасываем текущее слово и подсветку кнопок
        self.sbrosit_tekushee_slovo()

    def obnovit_spisok_slov(self):
        # Обновляем список отгаданных слов (слова в столбик)
        words_html = "<br>".join(self.otgadannye_slova)  # Каждое слово на новой строке
        self.Spisok_Slov.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                 "p, li { white-space: pre-wrap; }\n"
                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:bold; font-style:normal;\">\n"
                                 f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Список отгаданных слов ({self.otgadano} из 5):<br>{words_html}</p></body></html>")

    def obnovit_schetchik(self):
        # Обновляем счетчик отгаданных слов
        words_html = "<br>".join(self.otgadannye_slova)  # Каждое слово на новой строке
        self.Spisok_Slov.setHtml(f"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                 "p, li { white-space: pre-wrap; }\n"
                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:bold; font-style:normal;\">\n"
                                 f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Список отгаданных слов ({self.otgadano} из 5):<br>{words_html}</p></body></html>")

    def sbrosit_tekushee_slovo(self):
        # Сбрасываем текущее слово
        self.tekushee_slovo = ""
        self.currentWordLabel.setText("")  # Очищаем поле с текущим словом
        # Сбрасываем подсветку кнопок
        for button in self.aktivnye_bukvy:
            button.setStyleSheet("")
        self.aktivnye_bukvy.clear()


# Класс для главного окна игры (наследует QMainWindow и Ui_MainWindowGame)
class MainWindowGame(QtWidgets.QMainWindow, Ui_MainWindowGame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent  # Сохраняем ссылку на главное меню
        # Привязываем кнопку "Выход в меню" к функции возврата в меню
        self.pushButton.clicked.connect(self.return_to_menu)

    def keyPressEvent(self, event):
        # Обрабатываем нажатие клавиши "Enter"
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.proverit_slovo()

    def return_to_menu(self):
        # Закрываем текущее окно игры и показываем главное меню
        self.close()
        if self.parent:
            self.parent.show()


# Класс для главного окна меню
class Ui_MainWindowMenu(object):
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
        # Привязка кнопки "Начать игру" к функции открытия окна игры
        self.pushButton.clicked.connect(self.start_game)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра \"Слова из слова\""))
        self.label.setText(_translate("MainWindow", "Слова из слова"))
        self.pushButton.setText(_translate("MainWindow", "Начать игру"))
        self.pushButton_2.setText(_translate("MainWindow", "Правила игры"))
        self.pushButton_3.setText(_translate("MainWindow", "Настройки"))
        self.pushButton_4.setText(_translate("MainWindow", "Выход из игры"))
        self.pushButton_4.clicked.connect(MainWindow.close) 

    def show_rules(self):
        # Создаем и показываем диалоговое окно с правилами
        self.dialog = QtWidgets.QDialog()
        self.ui_rules = Ui_Dialog()
        self.ui_rules.setupUi(self.dialog)
        self.dialog.exec_()

    def start_game(self):
        # Создаем и показываем окно игры
        self.game_window = MainWindowGame(self)  # Передаем ссылку на главное меню
        self.game_window.show()
        self.hide()  # Скрываем главное меню


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


# Основной класс для запуска приложения
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindowMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())