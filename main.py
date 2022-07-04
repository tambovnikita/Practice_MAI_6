
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QFrame,\
    QGridLayout, QScrollArea, QWidget, QFormLayout, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
import sys


class UserWidget(QPushButton):
    def __init__(self, parent, user_id):
        QPushButton.__init__(self, parent)
        self.setObjectName("user"+str(user_id))
        self.setFixedWidth(161)
        self.setFixedHeight(208)
        self.setStyleSheet("""
            QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
            QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
            """)

        VLayout_user = QVBoxLayout()
        VLayout_user.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        VLayout_user.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.user_img = QLabel(self)
        self.user_img.setStyleSheet("background:rgb(217, 217, 217); border-radius: 10px;")
        self.user_img.setFixedWidth(130)
        self.user_img.setFixedHeight(130)
        self.pixmap = QtGui.QPixmap('./imgs/users/user{}.png'.format(user_id))
        self.user_img.setPixmap(self.pixmap)
        self.user_img.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)  # выравнивание (центр)
        VLayout_user.addWidget(self.user_img)

        self.lbl_name_user = QLabel(self)
        self.lbl_name_user.setFont(QtGui.QFont('Helvetica', 32, weight=QtGui.QFont.Bold))
        self.lbl_name_user.setFixedWidth(130)
        self.lbl_name_user.setFixedHeight(34)
        self.lbl_name_user.setContentsMargins(0, 5, 0, 0)  # внешние отступы
        if user_id == 0:
            self.lbl_name_user.setText("Nikita")
        elif user_id == 1:
            self.lbl_name_user.setText("Ivan")
        elif user_id == 2:
            self.lbl_name_user.setText("Maria")
        self.lbl_name_user.setStyleSheet("background: 0; color: white;")
        VLayout_user.addWidget(self.lbl_name_user)

        self.setLayout(VLayout_user)


class AirportWidget(QPushButton):
    def __init__(self, parent, airport_id, airport_name):
        QPushButton.__init__(self, parent)
        self.setObjectName("airport"+str(airport_id))
        self.setFixedWidth(350)
        self.setFixedHeight(163)
        self.setStyleSheet("""
            QPushButton {background:rgb(135, 136, 160); border: 0;}
            QPushButton:hover {background:rgb(70, 70, 116); border: 0;}
            """)

        VLayout_airport = QVBoxLayout()
        VLayout_airport.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        VLayout_airport.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.airport_name = QLabel(self)
        self.airport_name.setStyleSheet("background:rgb(217, 217, 217);")
        self.airport_name.setFixedWidth(300)
        self.airport_name.setFixedHeight(85)
        self.airport_name.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)  # выравнивание (центр)
        VLayout_lbl = QVBoxLayout()
        self.lbl_name = QLabel(self)
        self.lbl_name.setFont(QtGui.QFont('Helvetica', 40))
        self.lbl_name.setFixedWidth(203)
        self.lbl_name.setFixedHeight(42)
        self.lbl_name.setText(airport_name)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.lbl_name.setStyleSheet("background: 0; color: black;")
        VLayout_lbl.addWidget(self.lbl_name)
        VLayout_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)  # выравнивание (центр)
        VLayout_lbl.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        self.airport_name.setLayout(VLayout_lbl)
        VLayout_airport.addWidget(self.airport_name)

        self.lbl_count_runways = QLabel(self)
        self.lbl_count_runways.setFont(QtGui.QFont('Helvetica', 24, weight=QtGui.QFont.Bold))
        self.lbl_count_runways.setFixedWidth(300)
        self.lbl_count_runways.setFixedHeight(28)
        self.lbl_count_runways.setContentsMargins(0, 5, 0, 0)  # внешние отступы
        if airport_id == 0:
            self.lbl_count_runways.setText("Кол-во полос: 1")
        elif airport_id == 1:
            self.lbl_count_runways.setText("Кол-во полос: 2")
        elif airport_id == 2:
            self.lbl_count_runways.setText("Кол-во полос: 3")
        elif airport_id == 3:
            self.lbl_count_runways.setText("Кол-во полос: 4")
        self.lbl_count_runways.setStyleSheet("background: 0; color: white;")
        VLayout_airport.addWidget(self.lbl_count_runways)

        self.setLayout(VLayout_airport)


# Кнопки "Далее" и "Выход"
class NavigationBtn(QPushButton):
    def __init__(self, parent, name):
        QPushButton.__init__(self, parent)
        self.setObjectName(name)
        self.setFixedWidth(182)
        self.setFixedHeight(52)
        self.setStyleSheet("""
            QPushButton {background:rgb(39, 39, 61); border-radius: 20px;}
            QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
            QPushButton:pressed {background:rgb(135, 136, 160); border-radius: 20px;}
            """)

        VLayout_lbl = QVBoxLayout()
        self.lbl_name = QLabel(self)
        self.lbl_name.setFont(QtGui.QFont('Helvetica', 24))
        self.lbl_name.setFixedWidth(77)
        self.lbl_name.setFixedHeight(26)
        if name == "further":
            self.lbl_name.setText("Далее")
        elif name == "exit":
            self.lbl_name.setText("Выход")
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.lbl_name.setStyleSheet("background: 0; color: white;")
        VLayout_lbl.addWidget(self.lbl_name)

        VLayout_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)  # выравнивание (центр)
        VLayout_lbl.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        self.setLayout(VLayout_lbl)


class MainWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.current_user = ""  # выбранная карточка пользователя
        self.current_airport = ""   # выбранная карточка аэропорта

        # Расстановка элементов
        VLayout_main = QVBoxLayout()
        VLayout_main.setAlignment(Qt.AlignVCenter)
        VLayout_main.setSpacing(50)     # расстояние между элементами
        VLayout_main.setContentsMargins(0, 0, 0, 0)  # внешние отступы

        HLayout_users = QHBoxLayout()
        HLayout_users.setAlignment(Qt.AlignHCenter)
        HLayout_users.setSpacing(40)    # расстояние между элементами

        self.lbl_user = QLabel(self)  # заголовок
        self.lbl_user.setFont(QtGui.QFont('Helvetica', 40, weight=QtGui.QFont.Bold))  # изменяем шрифт
        self.lbl_user.setFixedWidth(340)
        self.lbl_user.setFixedHeight(90)
        self.lbl_user.setWordWrap(True)  # перенос текста
        self.lbl_user.setText("Выберите пользователя")  # меняем текст
        self.lbl_user.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_users.addWidget(self.lbl_user)

        # Карточки пользователей
        self.user_widget0 = UserWidget(self, user_id=0)
        self.user_widget0.clicked.connect(self.btnUserClick)    # при клике на карточку пользователя
        HLayout_users.addWidget(self.user_widget0)
        self.user_widget1 = UserWidget(self, user_id=1)
        self.user_widget1.clicked.connect(self.btnUserClick)    # при клике на карточку пользователя
        HLayout_users.addWidget(self.user_widget1)
        self.user_widget2 = UserWidget(self, user_id=2)
        self.user_widget2.clicked.connect(self.btnUserClick)    # при клике на карточку пользователя
        HLayout_users.addWidget(self.user_widget2)

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
        self.airport_widget0.clicked.connect(self.btnAirportClick)  # при клике на карточку аэропорта
        GridLayout_airports.addWidget(self.airport_widget0, 0, 0)
        self.airport_widget1 = AirportWidget(self, airport_id=1, airport_name="KURSK")
        self.airport_widget1.clicked.connect(self.btnAirportClick)  # при клике на карточку аэропорта
        GridLayout_airports.addWidget(self.airport_widget1, 0, 1)
        self.airport_widget2 = AirportWidget(self, airport_id=2, airport_name="TULA")
        self.airport_widget2.clicked.connect(self.btnAirportClick)  # при клике на карточку аэропорта
        GridLayout_airports.addWidget(self.airport_widget2, 1, 0)
        self.airport_widget3 = AirportWidget(self, airport_id=3, airport_name="MOSCOW")
        self.airport_widget3.clicked.connect(self.btnAirportClick)  # при клике на карточку аэропорта
        GridLayout_airports.addWidget(self.airport_widget3, 1, 1)
        HLayout_airports.addLayout(GridLayout_airports)

        VLayout_main.addLayout(HLayout_airports)
        self.setLayout(VLayout_main)

    # Выбор карточки пользователя
    def btnUserClick(self):
        btn_name = self.sender().objectName()
        # Выделяем карточку пользователя
        if btn_name == "user0":
            self.user_widget0.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border-radius: 20px;}")
        elif btn_name == "user1":
            self.user_widget1.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border-radius: 20px;}")
        elif btn_name == "user2":
            self.user_widget2.setStyleSheet("QPushButton {background:rgb(39, 39, 61); border-radius: 20px;}")

        if self.current_user != btn_name:
            # Убираем выделение предыдущей карточки пользователя
            if self.current_user == "user0":
                self.user_widget0.setStyleSheet("""
                    QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                    QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
                    """)
            elif self.current_user == "user1":
                self.user_widget1.setStyleSheet("""
                    QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                    QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
                    """)
            elif self.current_user == "user2":
                self.user_widget2.setStyleSheet("""
                    QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                    QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
                    """)
            self.current_user = btn_name    # присваиваем новую карточку пользователя

    # Выбор карточки аэропорта
    def btnAirportClick(self):
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
            print('Открывается следующий экран')


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, QApplication.desktop().screenGeometry().width(), QApplication.desktop().screenGeometry().height())
        self.setWindowTitle('Симулятор диспетчера аэропорта')   # название окна
        self.setWindowIcon(QtGui.QIcon('imgs/main.ico'))    # иконка окна
        self.setStyleSheet("background:rgb(172, 177, 202);")  # фон окна

        self.setCentralWidget(MainWidget(self))     # устанавливаем главный виджет


app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
