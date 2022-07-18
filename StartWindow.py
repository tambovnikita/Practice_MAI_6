
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QHBoxLayout, \
    QVBoxLayout, QComboBox
from PyQt5.QtCore import Qt

from StartWindowWidgets import UserWidget, AirportWidget, NavigationBtn
from MainWindow import MainWindow


class MainWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.parent = parent
        self.main_window_create = False     # переменная, проверяющая создан ли объект MainWindow

        self.count_users = 4    # кол-во диспетчеров
        self.current_user = "user0"  # выбранная карточка пользователя
        self.current_airport = ""   # выбранная карточка аэропорта

        # Расстановка элементов
        VLayout_main = QVBoxLayout()
        VLayout_main.setAlignment(Qt.AlignVCenter)
        VLayout_main.setSpacing(50)     # расстояние между элементами
        VLayout_main.setContentsMargins(0, 0, 0, 0)  # внешние отступы

        HLayout_users = QHBoxLayout()
        HLayout_users.setAlignment(Qt.AlignHCenter)
        HLayout_users.setSpacing(40)    # расстояние между элементами

        # Кол-во диспетчеров
        VLayout_count_users = QVBoxLayout()
        VLayout_count_users.setAlignment(Qt.AlignVCenter)
        VLayout_count_users.setSpacing(15)  # расстояние между элементами
        VLayout_count_users.setContentsMargins(0, 0, 40, 0)  # внешние отступы
        self.lbl_count_users = QLabel(self)  # заголовок
        self.lbl_count_users.setFont(QtGui.QFont('Helvetica', 32, weight=QtGui.QFont.Bold))  # изменяем шрифт
        self.lbl_count_users.setFixedWidth(210)
        self.lbl_count_users.setFixedHeight(78)
        self.lbl_count_users.setWordWrap(True)  # перенос текста
        self.lbl_count_users.setText("Количество диспетчеров")  # меняем текст
        self.lbl_count_users.setStyleSheet("color: black;")  # меняем цвет текста
        self.lbl_count_users.setAlignment(Qt.AlignCenter)
        VLayout_count_users.addWidget(self.lbl_count_users)
        HLayout_count_users = QHBoxLayout()
        HLayout_count_users.setAlignment(Qt.AlignHCenter)
        HLayout_count_users.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        self.combobox_count_users = QComboBox(self)
        self.combobox_count_users.setStyleSheet("""
                #comboBoxCountUsers {background-color: white; color: black; border: 0px;}
                #comboBoxCountUsers QListView {background-color: white; color: black; border: 0px; outline: 0px;}
            """)
        self.combobox_count_users.setObjectName("comboBoxCountUsers")
        self.combobox_count_users.setFont(QtGui.QFont('Helvetica', 20))  # изменяем шрифт
        self.combobox_count_users.setFixedWidth(80)
        self.combobox_count_users.setFixedHeight(40)
        self.combobox_count_users.addItem("1")
        self.combobox_count_users.addItem("2")
        self.combobox_count_users.addItem("3")
        self.combobox_count_users.addItem("4")
        self.combobox_count_users.setCurrentIndex(3)    # устанавливаем значение по умолчанию
        self.combobox_count_users.activated[str].connect(self.onComboBoxCountUsers)     # при выборе кол-ва диспетчеров
        HLayout_count_users.addWidget(self.combobox_count_users)
        VLayout_count_users.addLayout(HLayout_count_users)
        HLayout_users.addLayout(VLayout_count_users)

        # Карточки пользователей
        self.user_widget0 = UserWidget(self, user_id=0)
        self.user_widget0.clicked.connect(self.onBtnUserClick)    # при клике на карточку пользователя
        self.updateBtnUser("user0")
        HLayout_users.addWidget(self.user_widget0)
        self.user_widget1 = UserWidget(self, user_id=1)
        self.user_widget1.clicked.connect(self.onBtnUserClick)    # при клике на карточку пользователя
        HLayout_users.addWidget(self.user_widget1)
        self.user_widget2 = UserWidget(self, user_id=2)
        self.user_widget2.clicked.connect(self.onBtnUserClick)    # при клике на карточку пользователя
        HLayout_users.addWidget(self.user_widget2)
        self.user_widget3 = UserWidget(self, user_id=3)
        self.user_widget3.clicked.connect(self.onBtnUserClick)    # при клике на карточку пользователя
        HLayout_users.addWidget(self.user_widget3)

        self.lbl_user = QLabel(self)  # заголовок
        self.lbl_user.setFont(QtGui.QFont('Helvetica', 32, weight=QtGui.QFont.Bold))  # изменяем шрифт
        self.lbl_user.setFixedWidth(237)
        self.lbl_user.setFixedHeight(78)
        self.lbl_user.setWordWrap(True)  # перенос текста
        self.lbl_user.setText("Выберите пользователя")  # меняем текст
        self.lbl_user.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_users.addWidget(self.lbl_user)

        VLayout_main.addLayout(HLayout_users)

        self.lbl_line = QLabel(self)  # Заголовок
        self.lbl_line.setFixedWidth(QApplication.desktop().screenGeometry().width())
        self.lbl_line.setFixedHeight(1)
        self.lbl_line.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        self.lbl_line.setStyleSheet("background-color: black;")  # меняем цвет текста
        VLayout_main.addWidget(self.lbl_line)


        HLayout_airports = QHBoxLayout()
        HLayout_airports.setAlignment(Qt.AlignHCenter)
        HLayout_airports.setSpacing(80)     # расстояние между элементами

        VLayout_title_btns = QVBoxLayout()
        VLayout_title_btns.setAlignment(Qt.AlignTop)
        VLayout_title_btns.setContentsMargins(0, 40, 0, 0)  # внешние отступы
        VLayout_title_btns.setSpacing(25)  # расстояние между элементами

        self.lbl_airport = QLabel(self)  # заголовок
        self.lbl_airport.setFont(QtGui.QFont('Helvetica', 40, weight=QtGui.QFont.Bold))  # изменяем шрифт
        self.lbl_airport.setFixedWidth(203)
        self.lbl_airport.setFixedHeight(150)
        self.lbl_airport.setAlignment(Qt.AlignTop)
        self.lbl_airport.setWordWrap(True)  # перенос текста
        self.lbl_airport.setText("Выберите аэропорт")  # меняем текст
        self.lbl_airport.setStyleSheet("color: black;")  # меняем цвет текста
        VLayout_title_btns.addWidget(self.lbl_airport)

        # Кнопки "Далее" и "Выход"
        self.btn_further = NavigationBtn(self, name="further")    # кнопка "Далее"
        self.btn_further.clicked.connect(self.btnFurtherClick)  # при клике на кнопку
        VLayout_title_btns.addWidget(self.btn_further)
        self.btn_exit = NavigationBtn(self, name="exit")  # кнопка "Выход"
        self.btn_exit.clicked.connect(parent.close)  # при клике на кнопку
        VLayout_title_btns.addWidget(self.btn_exit)

        HLayout_airports.addLayout(VLayout_title_btns)

        # Карточки аэропортов
        GridLayout_airports = QGridLayout()
        GridLayout_airports.setHorizontalSpacing(25)    # расстояние между столбцами
        GridLayout_airports.setVerticalSpacing(25)  # расстояние между строками
        self.airport_widget0 = AirportWidget(self, airport_id=0, airport_name="ALEKSIN")
        self.airport_widget0.clicked.connect(self.onBtnAirportClick)  # при клике на карточку аэропорта
        GridLayout_airports.addWidget(self.airport_widget0, 0, 0)
        self.airport_widget1 = AirportWidget(self, airport_id=1, airport_name="KURSK")
        self.airport_widget1.clicked.connect(self.onBtnAirportClick)  # при клике на карточку аэропорта
        GridLayout_airports.addWidget(self.airport_widget1, 0, 1)
        self.airport_widget2 = AirportWidget(self, airport_id=2, airport_name="TULA")
        self.airport_widget2.clicked.connect(self.onBtnAirportClick)  # при клике на карточку аэропорта
        GridLayout_airports.addWidget(self.airport_widget2, 1, 0)
        self.airport_widget3 = AirportWidget(self, airport_id=3, airport_name="MOSCOW")
        self.airport_widget3.clicked.connect(self.onBtnAirportClick)  # при клике на карточку аэропорта
        GridLayout_airports.addWidget(self.airport_widget3, 1, 1)
        HLayout_airports.addLayout(GridLayout_airports)

        VLayout_main.addLayout(HLayout_airports)
        self.setLayout(VLayout_main)

    # Отображение определённого кол-ва карточек пользователей
    def onComboBoxCountUsers(self, text):
        self.count_users = int(text)
        self.current_user = "user0"
        self.updateBtnUser("user0")
        self.user_widget1.setStyleSheet("""
                QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
            """)
        self.user_widget2.setStyleSheet("""
                QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
            """)
        self.user_widget3.setStyleSheet("""
                QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
            """)
        self.user_widget0.user_img.hide()
        self.user_widget0.lbl_name_user.hide()
        self.user_widget1.user_img.hide()
        self.user_widget1.lbl_name_user.hide()
        self.user_widget2.user_img.hide()
        self.user_widget2.lbl_name_user.hide()
        self.user_widget3.user_img.hide()
        self.user_widget3.lbl_name_user.hide()
        if text == "1":
            self.user_widget0.user_img.show()
            self.user_widget0.lbl_name_user.show()
        elif text == "2":
            self.user_widget0.user_img.show()
            self.user_widget0.lbl_name_user.show()
            self.user_widget1.user_img.show()
            self.user_widget1.lbl_name_user.show()
        elif text == "3":
            self.user_widget0.user_img.show()
            self.user_widget0.lbl_name_user.show()
            self.user_widget1.user_img.show()
            self.user_widget1.lbl_name_user.show()
            self.user_widget2.user_img.show()
            self.user_widget2.lbl_name_user.show()
        elif text == "4":
            self.user_widget0.user_img.show()
            self.user_widget0.lbl_name_user.show()
            self.user_widget1.user_img.show()
            self.user_widget1.lbl_name_user.show()
            self.user_widget2.user_img.show()
            self.user_widget2.lbl_name_user.show()
            self.user_widget3.user_img.show()
            self.user_widget3.lbl_name_user.show()

    # Изменение стилей у карточек пользователей
    def updateBtnUser(self, btn_name):
        # Выделяем карточку пользователя
        if btn_name == "user0" and self.count_users >= 1:
            self.user_widget0.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border-radius: 20px;}")
        elif btn_name == "user1" and self.count_users >= 2:
            self.user_widget1.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border-radius: 20px;}")
        elif btn_name == "user2" and self.count_users >= 3:
            self.user_widget2.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border-radius: 20px;}")
        elif btn_name == "user3" and self.count_users == 4:
            self.user_widget3.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border-radius: 20px;}")

        if self.current_user != btn_name:
            # Убираем выделение предыдущей карточки пользователя
            if self.count_users >= int(btn_name[-1])+1:
                if self.current_user == "user0":
                    self.user_widget0.setStyleSheet("""
                        QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                        QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
                        """)
                    self.current_user = btn_name  # присваиваем новую карточку пользователя
                elif self.current_user == "user1":
                    self.user_widget1.setStyleSheet("""
                        QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                        QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
                        """)
                    self.current_user = btn_name  # присваиваем новую карточку пользователя
                elif self.current_user == "user2":
                    self.user_widget2.setStyleSheet("""
                        QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                        QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
                        """)
                    self.current_user = btn_name  # присваиваем новую карточку пользователя
                elif self.current_user == "user3":
                    self.user_widget3.setStyleSheet("""
                        QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                        QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
                        """)
                    self.current_user = btn_name  # присваиваем новую карточку пользователя

    # Выбор карточки пользователя
    def onBtnUserClick(self):
        btn_name = self.sender().objectName()
        self.updateBtnUser(btn_name)

    # Выбор карточки аэропорта
    def onBtnAirportClick(self):
        btn_name = self.sender().objectName()
        # Выделяем карточку аэропорта
        if btn_name == "airport0":
            self.airport_widget0.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border: 0;}")
        elif btn_name == "airport1":
            self.airport_widget1.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border: 0;}")
        elif btn_name == "airport2":
            self.airport_widget2.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border: 0;}")
        elif btn_name == "airport3":
            self.airport_widget3.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border: 0;}")

        if self.current_airport != btn_name:
            # Убираем выделение предыдущей карточки аэропорта
            if self.current_airport == "airport0":
                self.airport_widget0.setStyleSheet("""
                    QPushButton {background:rgb(135, 136, 160); border: 0;}
                    QPushButton:hover {background:rgb(70, 70, 116); border: 0;}
                    """)
            elif self.current_airport == "airport1":
                self.airport_widget1.setStyleSheet("""
                    QPushButton {background:rgb(135, 136, 160); border: 0;}
                    QPushButton:hover {background:rgb(70, 70, 116); border: 0;}
                    """)
            elif self.current_airport == "airport2":
                self.airport_widget2.setStyleSheet("""
                    QPushButton {background:rgb(135, 136, 160); border: 0;}
                    QPushButton:hover {background:rgb(70, 70, 116); border: 0;}
                    """)
            elif self.current_airport == "airport3":
                self.airport_widget3.setStyleSheet("""
                    QPushButton {background:rgb(135, 136, 160); border: 0;}
                    QPushButton:hover {background:rgb(70, 70, 116); border: 0;}
                    """)
            self.current_airport = btn_name  # присваиваем новую карточку аэропорта

    # Проверка и следующий экран
    def btnFurtherClick(self):
        if len(self.current_user) != 0 and len(self.current_airport) != 0:
            self.main_window = MainWindow(self.count_users, self.current_user, self.current_airport, self)
            self.main_window_create = True
            self.parent.setCentralWidget(self.main_window)     # меняем экран

    def __del__(self):
        if self.main_window_create == True:
            del self.main_window


class StartWindow(QMainWindow):
    def __init__(self, app):
        super(StartWindow, self).__init__()
        self.setGeometry(0, 0, QApplication.desktop().screenGeometry().width(), QApplication.desktop().screenGeometry().height())
        self.setWindowTitle('Симулятор диспетчера аэропорта')   # название окна
        self.setWindowIcon(QtGui.QIcon('imgs/main.ico'))    # иконка окна
        self.setStyleSheet("background:rgb(172, 177, 202);")  # фон окна
        #self.main_widget = MainWidget(self)
        #self.setCentralWidget(self.main_widget)     # устанавливаем главный виджет
        self.setCentralWidget(MainWindow(parent=self, count_users=1, current_user="user0", current_airport="airport0"))  # устанавливаем главный виджет

    # Завершаем отдельный поток, если окно хотят закрыть
    def closeEvent(self, event):
        pass
        #del self.main_widget
