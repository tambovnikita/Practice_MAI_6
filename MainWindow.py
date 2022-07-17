
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QPushButton, QFrame, QSizePolicy
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
import time

# Кнопки "1", "2", "3", "4"


class NumberBtn(QPushButton):
    def __init__(self, parent, number):
        QPushButton.__init__(self, parent)
        self.setObjectName("btn"+number)
        self.setFixedWidth(50)
        self.setFixedHeight(50)
        self.setStyleSheet("background:rgb(39, 39, 61); border-radius: 10px;")

        VLayout_lbl = QVBoxLayout()
        self.lbl_name = QLabel(self)
        self.lbl_name.setText(number)
        self.lbl_name.setFont(QtGui.QFont('Helvetica', 32, weight=QtGui.QFont.Bold))
        self.lbl_name.setFixedWidth(50)
        self.lbl_name.setFixedHeight(50)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.lbl_name.setStyleSheet("background: 0; color: white;")
        VLayout_lbl.addWidget(self.lbl_name)

        VLayout_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)  # выравнивание (центр)
        VLayout_lbl.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        self.setLayout(VLayout_lbl)


# Кнопки "НАЧАТЬ", "Справка" и "Выход"
class NavigationBtn(QPushButton):
    def __init__(self, parent, name, width, height):
        QPushButton.__init__(self, parent)
        self.setObjectName(name)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setStyleSheet("""
            QPushButton {background:rgb(39, 39, 61); border-radius: 15px;}
            QPushButton:hover {background:rgb(70, 70, 116); border-radius: 15px;}
            QPushButton:pressed {background:rgb(135, 136, 160); border-radius: 15px;}
            """)

        VLayout_lbl = QVBoxLayout()
        self.lbl_name = QLabel(self)

        if name == "start":
            self.lbl_name.setText("НАЧАТЬ")
            self.lbl_name.setFont(QtGui.QFont('Helvetica', 24, weight=QtGui.QFont.Bold))
            self.lbl_name.setFixedWidth(101)
            self.lbl_name.setFixedHeight(26)
        if name == "help":
            self.lbl_name.setText("Справка")
            self.lbl_name.setFont(QtGui.QFont('Helvetica', 20))
            self.lbl_name.setFixedWidth(82)
            self.lbl_name.setFixedHeight(22)
        elif name == "exit":
            self.lbl_name.setText("Выход")
            self.lbl_name.setFont(QtGui.QFont('Helvetica', 20))
            self.lbl_name.setFixedWidth(82)
            self.lbl_name.setFixedHeight(22)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.lbl_name.setStyleSheet("background: 0; color: white;")
        VLayout_lbl.addWidget(self.lbl_name)

        VLayout_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)  # выравнивание (центр)
        VLayout_lbl.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        self.setLayout(VLayout_lbl)


class FlightWidget(QPushButton):
    def __init__(self, parent, id, number, firm, model):
        QPushButton.__init__(self, parent)
        self.setObjectName("flight"+str(id))
        self.setFixedWidth(401)
        self.setFixedHeight(42)
        self.setStyleSheet("""
            QPushButton {background:rgb(217, 217, 217); border-radius: 10; outline: 0;}
            QPushButton:hover {background:rgb(217, 217, 217); border-radius: 10px; outline: 3px solid rgb(39, 39, 61);}
            QPushButton:pressed {background:rgb(70, 70, 116); border-radius: 10px; outline: 3px solid rgb(39, 39, 61);}
            """)

        HLayout_flight = QHBoxLayout()
        HLayout_flight.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        HLayout_flight.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.lbl_number = QLabel(self)
        self.lbl_number.setFont(QtGui.QFont('Helvetica', 20, weight=QtGui.QFont.Bold))  # изменяем шрифт
        self.lbl_number.setStyleSheet("background:rgb(217, 217, 217); color:black;")
        self.lbl_number.setFixedWidth(77)
        self.lbl_number.setFixedHeight(26)
        self.lbl_number.setText(number)
        self.lbl_number.setAlignment(Qt.AlignCenter)
        HLayout_flight.addWidget(self.lbl_number)

        self.lbl_firm = QLabel(self)
        self.lbl_firm.setFont(QtGui.QFont('Helvetica', 20))  # изменяем шрифт
        self.lbl_firm.setStyleSheet("background:rgb(217, 217, 217); color:black;")
        self.lbl_firm.setFixedWidth(154)
        self.lbl_firm.setFixedHeight(26)
        self.lbl_firm.setText(firm)
        self.lbl_firm.setAlignment(Qt.AlignCenter)
        HLayout_flight.addWidget(self.lbl_firm)

        self.lbl_model = QLabel(self)
        self.lbl_model.setFont(QtGui.QFont('Helvetica', 20))  # изменяем шрифт
        self.lbl_model.setStyleSheet("background:rgb(217, 217, 217); color:black;")
        self.lbl_model.setFixedWidth(154)
        self.lbl_model.setFixedHeight(26)
        self.lbl_model.setText(model)
        self.lbl_model.setAlignment(Qt.AlignCenter)
        HLayout_flight.addWidget(self.lbl_model)

        self.setLayout(HLayout_flight)


class RunwayWidget(QWidget):
    def __init__(self, parent, id):
        QWidget.__init__(self, parent)
        self.setObjectName("runway"+str(id))
        self.setFixedWidth(280)
        self.setFixedHeight(334)

        self.btns_runway = []  # карточки рейсов на данную полосу

        VLayout_runway = QVBoxLayout()
        VLayout_runway.setAlignment(Qt.AlignTop)
        VLayout_runway.setSpacing(0)  # расстояние между элементами
        VLayout_runway.setContentsMargins(0, 0, 0, 0)  # внешние отступы

        self.scrollA_runway = QScrollArea()
        self.scrollA_runway.setFixedWidth(280)
        self.scrollA_runway.setFixedHeight(334)
        self.scrollA_runway.setStyleSheet("background:rgb(135, 136, 160); border-radius: 0px;")

        self.scrollW_runway = QWidget()
        self.scrollW_runway.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scrollW_runway.setFixedWidth(253)
        self.VLayout_runway_flights = QVBoxLayout()
        self.VLayout_runway_flights.setAlignment(Qt.AlignTop)
        self.VLayout_runway_flights.setContentsMargins(5, 5, 5, 5)  # внешние отступы
        self.VLayout_runway_flights.setSpacing(5)  # расстояние между элементами
        self.scrollW_runway.setLayout(self.VLayout_runway_flights)
        self.scrollA_runway.setWidget(self.scrollW_runway)

        VLayout_runway.addWidget(self.scrollA_runway)

        # Нижний блок с названием полосы и количеством рейсов
        self.title_runway = QWidget()
        self.title_runway.setFixedHeight(44)
        self.title_runway.setFixedWidth(280)
        self.title_runway.setStyleSheet("background:rgb(70, 70, 116);")  # меняем цвет текста
        HLayout_runway_title = QHBoxLayout()
        HLayout_runway_title.setAlignment(Qt.AlignHCenter)
        HLayout_runway_title.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        HLayout_runway_title.setSpacing(5)  # расстояние между элементами
        self.lbl_runway_title = QLabel(self)  # заголовок
        self.lbl_runway_title.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.lbl_runway_title.setFixedWidth(150)
        self.lbl_runway_title.setFixedHeight(18)
        self.lbl_runway_title.setText("ПОЛОСА №"+str(id))  # меняем текст
        self.lbl_runway_title.setStyleSheet("color: white;")  # меняем цвет текста
        HLayout_runway_title.addWidget(self.lbl_runway_title)
        self.lbl_runway_count = QLabel(self)  # заголовок
        self.lbl_runway_count.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.lbl_runway_count.setFixedWidth(58)
        self.lbl_runway_count.setFixedHeight(18)
        self.lbl_runway_count.setText("кол-во:")  # меняем текст
        self.lbl_runway_count.setStyleSheet("color: white;")  # меняем цвет текста
        self.lbl_runway_count.setAlignment(Qt.AlignBottom)
        HLayout_runway_title.addWidget(self.lbl_runway_count)
        self.runway_count = QLabel(self)  # заголовок
        self.runway_count.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.runway_count.setFixedWidth(20)
        self.runway_count.setFixedHeight(18)
        self.runway_count.setText(str(len(self.btns_runway)))  # меняем текст
        self.runway_count.setStyleSheet("color: white;")  # меняем цвет текста
        self.runway_count.setAlignment(Qt.AlignBottom)
        HLayout_runway_title.addWidget(self.runway_count)
        self.title_runway.setLayout(HLayout_runway_title)

        VLayout_runway.addWidget(self.title_runway)

        self.setLayout(VLayout_runway)


class UpdateInfo(QObject):
    updateSignal = pyqtSignal(str)
    finishSignal = pyqtSignal()

    def __init__(self):
        super(UpdateInfo, self).__init__()
        self.btnStartActive = True

    def start(self):
        while self.btnStartActive != False:
            self.timeNow()

    def timeNow(self):
        time.sleep(1)
        time_string = time.strftime("%H:%M:%S", time.localtime())
        self.updateSignal.emit(time_string)

    def stop(self):
        self.btnStartActive = False


class MainWindow(QWidget):
    def __init__(self, count_users, current_user, current_airport, parent=None):
        QWidget.__init__(self, parent)
        self.parent = parent
        self.btnStartActive = True  # при True кнопка имеет надпись "НАЧАТЬ", при False - "СТОП"

        self.btns_boarding_flights = []  # карточки рейсов на посадку
        self.btns_takeoff_flights = []  # карточки рейсов на взлёт

        # Расстановка элементов
        VLayout_main = QVBoxLayout()
        VLayout_main.setAlignment(Qt.AlignTop)
        VLayout_main.setSpacing(15)     # расстояние между элементами
        VLayout_main.setContentsMargins(0, 0, 0, 0)  # внешние отступы

        # Time
        HLayout_time = QHBoxLayout()
        HLayout_time.setAlignment(Qt.AlignRight)
        HLayout_time.setContentsMargins(10, 10, 10, 0)  # внешние отступы
        self.lbl_time = QLabel(self)  # заголовок
        self.lbl_time.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.lbl_time.setFixedWidth(66)
        self.lbl_time.setFixedHeight(18)
        self.lbl_time.setText("00:00:00")  # меняем текст
        self.lbl_time.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_time.addWidget(self.lbl_time)
        VLayout_main.addLayout(HLayout_time)

        self.widget_flights_and_navigation = QWidget()
        self.widget_flights_and_navigation.setFixedWidth(QApplication.desktop().screenGeometry().width())
        self.widget_flights_and_navigation.setFixedHeight(320)
        HLayout_flights_and_navigation = QHBoxLayout()
        HLayout_flights_and_navigation.setAlignment(Qt.AlignHCenter)
        HLayout_flights_and_navigation.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        HLayout_flights_and_navigation.setSpacing(40)  # расстояние между элементами

        # Рейсы на посадку
        VLayout_boarding_flights = QVBoxLayout()    # рейсы на посадку
        VLayout_boarding_flights.setAlignment(Qt.AlignTop)
        VLayout_boarding_flights.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        VLayout_boarding_flights.setSpacing(10)  # расстояние между элементами

        self.lbl_boarding_flights = QLabel(self)  # заголовок
        self.lbl_boarding_flights.setFont(QtGui.QFont('Helvetica', 36, weight=QtGui.QFont.Bold))  # изменяем шрифт
        self.lbl_boarding_flights.setFixedWidth(327)
        self.lbl_boarding_flights.setFixedHeight(48)
        self.lbl_boarding_flights.setText("Рейсы на посадку")  # меняем текст
        self.lbl_boarding_flights.setStyleSheet("color: black;")  # меняем цвет текста
        VLayout_boarding_flights.addWidget(self.lbl_boarding_flights)

        HLayout_boarding_flights_count = QHBoxLayout()
        HLayout_boarding_flights_count.setAlignment(Qt.AlignLeft)
        HLayout_boarding_flights_count.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        HLayout_boarding_flights_count.setSpacing(4)  # расстояние между элементами
        self.lbl_boarding_flights_count = QLabel(self)  # заголовок
        self.lbl_boarding_flights_count.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.lbl_boarding_flights_count.setFixedWidth(58)
        self.lbl_boarding_flights_count.setFixedHeight(18)
        self.lbl_boarding_flights_count.setText("кол-во:")  # меняем текст
        self.lbl_boarding_flights_count.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_boarding_flights_count.addWidget(self.lbl_boarding_flights_count)
        self.boarding_flights_count = QLabel(self)  # заголовок
        self.boarding_flights_count.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.boarding_flights_count.setFixedWidth(20)
        self.boarding_flights_count.setFixedHeight(18)
        self.boarding_flights_count.setText(str(len(self.btns_boarding_flights)))  # меняем текст
        self.boarding_flights_count.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_boarding_flights_count.addWidget(self.boarding_flights_count)
        VLayout_boarding_flights.addLayout(HLayout_boarding_flights_count)

        # Карточки рейсов на посадку
        self.scrollA_boarding_flights = QScrollArea()
        self.scrollA_boarding_flights.setFixedWidth(421)
        self.scrollA_boarding_flights.setFixedHeight(222)
        self.scrollA_boarding_flights.setStyleSheet("background:rgb(39, 39, 61); border-radius: 15px;")

        self.scrollW_boarding_flights = QWidget()
        self.scrollW_boarding_flights.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.VLayout_scroll_boarding_flights = QVBoxLayout()
        self.VLayout_scroll_boarding_flights.setAlignment(Qt.AlignTop)
        self.VLayout_scroll_boarding_flights.setContentsMargins(5, 5, 5, 5)  # внешние отступы
        self.VLayout_scroll_boarding_flights.setSpacing(5)  # расстояние между элементами
        for i in range(2):
            self.btns_boarding_flights.append(FlightWidget(self, id=0, number="2456", firm='"Победа"', model="Airbus-24"))
            self.VLayout_scroll_boarding_flights.addWidget(self.btns_boarding_flights[-1])
        self.scrollW_boarding_flights.setLayout(self.VLayout_scroll_boarding_flights)
        self.scrollA_boarding_flights.setWidget(self.scrollW_boarding_flights)

        VLayout_boarding_flights.addWidget(self.scrollA_boarding_flights)

        HLayout_flights_and_navigation.addLayout(VLayout_boarding_flights)

        VLayout_numbers = QVBoxLayout()  # кнопки с номерами
        VLayout_numbers.setAlignment(Qt.AlignBottom)
        VLayout_numbers.setContentsMargins(0, 0, 0, 12)  # внешние отступы
        VLayout_numbers.setSpacing(6)  # расстояние между элементами
        for i in range(4):
            VLayout_numbers.addWidget(NumberBtn(self, number=str(i+1)))

        HLayout_flights_and_navigation.addLayout(VLayout_numbers)

        # Рейсы на взлёт
        VLayout_takeoff_flights = QVBoxLayout()  # рейсы на посадку
        VLayout_takeoff_flights.setAlignment(Qt.AlignTop)
        VLayout_takeoff_flights.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        VLayout_takeoff_flights.setSpacing(10)  # расстояние между элементами

        self.lbl_takeoff_flights = QLabel(self)  # заголовок
        self.lbl_takeoff_flights.setFont(QtGui.QFont('Helvetica', 36, weight=QtGui.QFont.Bold))  # изменяем шрифт
        self.lbl_takeoff_flights.setFixedWidth(327)
        self.lbl_takeoff_flights.setFixedHeight(48)
        self.lbl_takeoff_flights.setText("Рейсы на взлёт")  # меняем текст
        self.lbl_takeoff_flights.setStyleSheet("color: black;")  # меняем цвет текста
        VLayout_takeoff_flights.addWidget(self.lbl_takeoff_flights)

        HLayout_takeoff_flights_count = QHBoxLayout()
        HLayout_takeoff_flights_count.setAlignment(Qt.AlignLeft)
        HLayout_takeoff_flights_count.setSpacing(10)  # расстояние между элементами
        self.lbl_takeoff_flights_count = QLabel(self)  # заголовок
        self.lbl_takeoff_flights_count.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.lbl_takeoff_flights_count.setFixedWidth(58)
        self.lbl_takeoff_flights_count.setFixedHeight(18)
        self.lbl_takeoff_flights_count.setText("кол-во:")  # меняем текст
        self.lbl_takeoff_flights_count.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_takeoff_flights_count.addWidget(self.lbl_takeoff_flights_count)
        self.takeoff_flights_count = QLabel(self)  # заголовок
        self.takeoff_flights_count.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.takeoff_flights_count.setFixedWidth(20)
        self.takeoff_flights_count.setFixedHeight(18)
        self.takeoff_flights_count.setText(str(len(self.btns_takeoff_flights)))  # меняем текст
        self.takeoff_flights_count.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_takeoff_flights_count.addWidget(self.takeoff_flights_count)
        VLayout_takeoff_flights.addLayout(HLayout_takeoff_flights_count)

        # Карточки рейсов на взлёт
        self.scrollA_takeoff_flights = QScrollArea()
        self.scrollA_takeoff_flights.setFixedWidth(421)
        self.scrollA_takeoff_flights.setFixedHeight(222)
        self.scrollA_takeoff_flights.setStyleSheet("background:rgb(39, 39, 61); border-radius: 15px;")

        self.scrollW_takeoff_flights = QWidget()
        self.scrollW_takeoff_flights.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.VLayout_scroll_takeoff_flights = QVBoxLayout()
        self.VLayout_scroll_takeoff_flights.setAlignment(Qt.AlignTop)
        self.VLayout_scroll_takeoff_flights.setContentsMargins(5, 5, 5, 5)  # внешние отступы
        self.VLayout_scroll_takeoff_flights.setSpacing(5)  # расстояние между элементами
        for i in range(2):
            self.btns_takeoff_flights.append(
                FlightWidget(self, id=0, number="2456", firm='"Победа"', model="Airbus-24"))
            self.VLayout_scroll_takeoff_flights.addWidget(self.btns_takeoff_flights[-1])
        self.scrollW_takeoff_flights.setLayout(self.VLayout_scroll_takeoff_flights)
        self.scrollA_takeoff_flights.setWidget(self.scrollW_takeoff_flights)

        VLayout_takeoff_flights.addWidget(self.scrollA_takeoff_flights)

        HLayout_flights_and_navigation.addLayout(VLayout_takeoff_flights)

        # Кнопки "НАЧАТЬ", "Справка" и "Выход"
        self.widget_btns_navigation = QWidget()
        self.widget_btns_navigation.setFixedWidth(200)
        self.widget_btns_navigation.setFixedHeight(217)
        VLayout_btns_navigation = QVBoxLayout()  # кнопки с номерами
        VLayout_btns_navigation.setAlignment(Qt.AlignVCenter)
        VLayout_btns_navigation.setContentsMargins(30, 0, 0, 0)  # внешние отступы
        VLayout_btns_navigation.setSpacing(8)  # расстояние между элементами
        self.btn_start = NavigationBtn(self, name="start", width=170, height=61)  # кнопка "НАЧАТЬ"
        self.btn_start.clicked.connect(self.btnStartClick)  # при клике на кнопку
        VLayout_btns_navigation.addWidget(self.btn_start)
        HLayout_btn_help = QHBoxLayout()
        HLayout_btn_help.setAlignment(Qt.AlignRight)
        HLayout_btn_help.setContentsMargins(0, 30, 0, 0)  # внешние отступы
        self.btn_help = NavigationBtn(self, name="help", width=142, height=37)  # кнопка "Справка"
        HLayout_btn_help.addWidget(self.btn_help)
        VLayout_btns_navigation.addLayout(HLayout_btn_help)
        HLayout_btn_exit = QHBoxLayout()
        HLayout_btn_exit.setAlignment(Qt.AlignRight)
        HLayout_btn_exit.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        self.btn_exit = NavigationBtn(self, name="exit", width=142, height=37)  # кнопка "Выход"
        self.btn_exit.clicked.connect(parent.close)  # при клике на кнопку
        HLayout_btn_exit.addWidget(self.btn_exit)
        VLayout_btns_navigation.addLayout(HLayout_btn_exit)
        self.widget_btns_navigation.setLayout(VLayout_btns_navigation)
        HLayout_flights_and_navigation.addWidget(self.widget_btns_navigation)

        self.widget_flights_and_navigation.setLayout(HLayout_flights_and_navigation)
        VLayout_main.addWidget(self.widget_flights_and_navigation)

        self.lbl_line = QLabel(self)  # Заголовок
        self.lbl_line.setFixedWidth(QApplication.desktop().screenGeometry().width())
        self.lbl_line.setFixedHeight(1)
        self.lbl_line.setStyleSheet("background-color: black;")  # меняем цвет текста
        VLayout_main.addWidget(self.lbl_line)


        # Полосы
        HLayout_runway = QHBoxLayout()
        HLayout_runway.setAlignment(Qt.AlignHCenter)
        HLayout_runway.setSpacing(30)  # расстояние между элементами

        # Полоса №1
        self.runway1 = RunwayWidget(self, id=1)
        HLayout_runway.addWidget(self.runway1)

        # Полоса №2
        self.runway1 = RunwayWidget(self, id=2)
        HLayout_runway.addWidget(self.runway1)

        # Полоса №3
        self.runway1 = RunwayWidget(self, id=3)
        HLayout_runway.addWidget(self.runway1)

        # Полоса №4
        self.runway1 = RunwayWidget(self, id=4)
        HLayout_runway.addWidget(self.runway1)

        VLayout_main.addLayout(HLayout_runway)

        self.setLayout(VLayout_main)

    # Кнопка "НАЧАТЬ"
    def btnStartClick(self):
        if self.btnStartActive == True:
            self.btn_start.lbl_name.setText("СТОП")
            self.obj_update_info = UpdateInfo()     # объект, в котором происходит работа со временем и данными из базы данных
            self.thread = QThread()  # отдельный поток для обновления данных на экране
            self.obj_update_info.moveToThread(self.thread)  # добавляем созданный объект в отдельный поток
            self.thread.started.connect(self.obj_update_info.start)     # при старте потока запускается функция start в объекте
            self.obj_update_info.updateSignal.connect(self.updateTime)  # при сигнале updateSignal вызывается функция updateTime
            self.obj_update_info.finishSignal.connect(self.thread.quit) # при сигнале finishSignal завершаем отдельный поток
            self.thread.start()     # запускаем отдельный поток
            self.btnStartActive = False

        elif self.btnStartActive == False:
            self.obj_update_info.stop()     # останавливаем все процессы внутри объекта
            self.thread.quit()  # завершаем отдельный поток
            self.btn_start.lbl_name.setText("НАЧАТЬ")
            self.btnStartActive = True

        """self.btns_boarding_flights.append(FlightWidget(self, id=0, number="2456", firm='"Победа"', model="Airbus-24"))
        self.VLayout_scroll_boarding_flights.addWidget(self.btns_boarding_flights[-1])
        self.scrollW_boarding_flights.setFixedHeight(len(self.btns_boarding_flights) * (42 + 10))
        self.boarding_flights_count.setText(str(len(self.btns_boarding_flights)))  # меняем текст

        self.btns_takeoff_flights.append(FlightWidget(self, id=0, number="2456", firm='"Победа"', model="Airbus-24"))
        self.VLayout_scroll_takeoff_flights.addWidget(self.btns_takeoff_flights[-1])
        #self.scrollW_takeoff_flights.setFixedHeight(len(self.btns_takeoff_flights) * (42 + 10))
        self.takeoff_flights_count.setText(str(len(self.btns_takeoff_flights)))  # меняем текст"""


        self.runway1.VLayout_runway_flights.addWidget(self.btns_takeoff_flights[-2])
        #self.runway1.scrollW_runway.setFixedHeight(len(self.btns_takeoff_flights) * (42 + 10))

    def updateTime(self, time_string):
        self.lbl_time.setText(time_string)

    def __del__(self):
        if self.btnStartActive == False:
            self.obj_update_info.stop()  # останавливаем все процессы внутри объекта
            self.thread.quit()  # завершаем отдельный поток
