"""
Тамбов Никита М1О-309С-19
"""


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSizePolicy, QMessageBox
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
import time, random
from datetime import datetime, timedelta

from MainWindowWidgets import FlightWidget, NumberBtn, RunwayWidget, NavigationBtn
from DataBaseMethods import getAirportInfo, getFlightInfo, count_all_flights, count_all_statistics, setUserStatistics, setSessionsInfo
from HelpWindow import HelpWindow

class UpdateInfo(QObject):
    updateTimeSignal = pyqtSignal(str)
    addFlightSignal = pyqtSignal(dict)
    checkCurrentSignal = pyqtSignal()
    finishSignal = pyqtSignal()

    def __init__(self, count_users, current_airport):
        super(UpdateInfo, self).__init__()
        self.count_users = count_users
        self.current_airport = current_airport
        self.btnStartActive = True

    def start(self):
        self.id = 0
        # Синхронизируем время из базы данных с текущим временем
        i = 0
        while True:
            if time.strftime("%H:%M:%S", time.localtime()) == getFlightInfo(i, self.current_airport, "time_show"):
                self.id = i
                break
            i += 1
            if i == count_all_flights(self.current_airport):
                i = 0

        # Начинаем добавлять рейсы из базы данных
        while self.btnStartActive != False:
            self.timeNow()
            self.checkCurrentSignal.emit()
            if time.strftime("%H:%M:%S", time.localtime()) == getFlightInfo(self.id, self.current_airport, "time_show"):
                self.addFlights()
                # Чем больше диспетчеров в аэропорту, тем меньше нагрузка для пользователя
                self.id += self.count_users
            time.sleep(1)

    def timeNow(self):
        time_string = time.strftime("%H:%M:%S", time.localtime())
        self.updateTimeSignal.emit(time_string)

    def addFlights(self):
            self.addFlightSignal.emit(
                {"id": self.id,
                 "type": getFlightInfo(self.id, self.current_airport, "type"),
                 "number": getFlightInfo(self.id, self.current_airport, "number"),
                 "firm": getFlightInfo(self.id, self.current_airport, "firm"),
                 "model": getFlightInfo(self.id, self.current_airport, "model"),
                 "time_show": getFlightInfo(self.id, self.current_airport, "time_show"),
                 "time_on_runway": getFlightInfo(self.id, self.current_airport, "time_on_runway")}
            )

    def stop(self):
        self.btnStartActive = False


class MainWindow(QWidget):
    def __init__(self, count_users, current_user, current_airport, parent=None):
        QWidget.__init__(self, parent)
        self.parent = parent
        self.count_users = count_users
        self.current_user = current_user
        self.current_airport = current_airport
        self.count_runways = getAirportInfo(current_airport, "count_runways")
        self.btnStartActive = True  # при True кнопка имеет надпись "НАЧАТЬ", при False - "СТОП"

        self.btns_flights = []  # карточки рейсов
        self.btns_number = []   # кнопки "1", "2", "3", "4"
        self.runways = []   # взлётно-посадочные полосы

        self.count_all_flights = 0  # кол-во всех задействованных рейсов
        self.count_boarding_flights = 0     # кол-во рейсов на посадку
        self.count_takeoff_flights = 0      # кол-во рейсов на взлёт

        self.count_flights_on_runways = []  # кол-во рейсов на взлётно-посадочных полосах
        for i in range(self.count_runways):
            self.count_flights_on_runways.append(0)

        self.current_runway = -1    # номер выбранной взлётно-посадочной полосы
        self.current_flight = -1    # id выбранного рейса

        # Расстановка элементов
        VLayout_main = QVBoxLayout()
        VLayout_main.setAlignment(Qt.AlignVCenter)
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
        self.widget_flights_and_navigation.setFixedHeight(325)
        HLayout_flights_and_navigation = QHBoxLayout()
        HLayout_flights_and_navigation.setAlignment(Qt.AlignHCenter)
        HLayout_flights_and_navigation.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        HLayout_flights_and_navigation.setSpacing(40)  # расстояние между элементами

        # Рейсы на посадку
        VLayout_boarding_flights = QVBoxLayout()    # рейсы на посадку
        VLayout_boarding_flights.setAlignment(Qt.AlignTop)
        VLayout_boarding_flights.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        VLayout_boarding_flights.setSpacing(5)  # расстояние между элементами

        self.lbl_boarding_flights = QLabel(self)  # заголовок
        self.lbl_boarding_flights.setFont(QtGui.QFont('Helvetica', 36, weight=QtGui.QFont.Bold))  # изменяем шрифт
        self.lbl_boarding_flights.setFixedWidth(327)
        self.lbl_boarding_flights.setFixedHeight(46)
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
        self.lbl_boarding_flights_count.setFixedHeight(22)
        self.lbl_boarding_flights_count.setText("кол-во:")  # меняем текст
        self.lbl_boarding_flights_count.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_boarding_flights_count.addWidget(self.lbl_boarding_flights_count)
        self.boarding_flights_count = QLabel(self)  # заголовок
        self.boarding_flights_count.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.boarding_flights_count.setFixedWidth(20)
        self.boarding_flights_count.setFixedHeight(22)
        self.boarding_flights_count.setText(str(self.count_boarding_flights))  # меняем текст
        self.boarding_flights_count.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_boarding_flights_count.addWidget(self.boarding_flights_count)
        VLayout_boarding_flights.addLayout(HLayout_boarding_flights_count)

        # Карточки рейсов на посадку
        self.scrollA_boarding_flights = QScrollArea()
        self.scrollA_boarding_flights.setFixedWidth(435)
        self.scrollA_boarding_flights.setFixedHeight(242)
        self.scrollA_boarding_flights.setStyleSheet("""
                QScrollArea {
                    background-color: rgb(39, 39, 61);
                    padding: 10px 5px;
                    border-top-left-radius: 15px;
                    border-top-right-radius: 0px;
                    border-bottom-left-radius: 15px;
                    border-bottom-right-radius: 0px;
                }
                QScrollBar:vertical {
                    background-color: rgb(39, 39, 61);
                    width: 10px;
                }
            """)

        self.scrollW_boarding_flights = QWidget()
        self.scrollW_boarding_flights.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scrollW_boarding_flights.setFixedWidth(411)
        self.scrollW_boarding_flights.setStyleSheet("background-color: rgb(39, 39, 61); border-radius: 15px;")
        self.VLayout_scroll_boarding_flights = QVBoxLayout()
        self.VLayout_scroll_boarding_flights.setAlignment(Qt.AlignTop)
        self.VLayout_scroll_boarding_flights.setContentsMargins(5, 5, 5, 5)  # внешние отступы
        self.VLayout_scroll_boarding_flights.setSpacing(5)  # расстояние между элементами
        self.scrollW_boarding_flights.setLayout(self.VLayout_scroll_boarding_flights)
        self.scrollA_boarding_flights.setWidget(self.scrollW_boarding_flights)
        VLayout_boarding_flights.addWidget(self.scrollA_boarding_flights)

        HLayout_flights_and_navigation.addLayout(VLayout_boarding_flights)

        VLayout_numbers = QVBoxLayout()  # кнопки с номерами
        VLayout_numbers.setAlignment(Qt.AlignBottom)
        VLayout_numbers.setContentsMargins(0, 0, 0, 12)  # внешние отступы
        VLayout_numbers.setSpacing(6)  # расстояние между элементами
        for i in range(self.count_runways):
            self.btns_number.append(NumberBtn(self, number=i+1))
            self.btns_number[-1].clicked.connect(self.onBtnNumberClick)  # при клике на кнопку
            VLayout_numbers.addWidget(self.btns_number[-1])

        HLayout_flights_and_navigation.addLayout(VLayout_numbers)

        # Рейсы на взлёт
        VLayout_takeoff_flights = QVBoxLayout()  # рейсы на посадку
        VLayout_takeoff_flights.setAlignment(Qt.AlignTop)
        VLayout_takeoff_flights.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        VLayout_takeoff_flights.setSpacing(5)  # расстояние между элементами

        self.lbl_takeoff_flights = QLabel(self)  # заголовок
        self.lbl_takeoff_flights.setFont(QtGui.QFont('Helvetica', 36, weight=QtGui.QFont.Bold))  # изменяем шрифт
        self.lbl_takeoff_flights.setFixedWidth(327)
        self.lbl_takeoff_flights.setFixedHeight(46)
        self.lbl_takeoff_flights.setText("Рейсы на взлёт")  # меняем текст
        self.lbl_takeoff_flights.setStyleSheet("color: black;")  # меняем цвет текста
        VLayout_takeoff_flights.addWidget(self.lbl_takeoff_flights)

        HLayout_takeoff_flights_count = QHBoxLayout()
        HLayout_takeoff_flights_count.setAlignment(Qt.AlignLeft)
        HLayout_takeoff_flights_count.setSpacing(10)  # расстояние между элементами
        self.lbl_takeoff_flights_count = QLabel(self)  # заголовок
        self.lbl_takeoff_flights_count.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.lbl_takeoff_flights_count.setFixedWidth(58)
        self.lbl_takeoff_flights_count.setFixedHeight(22)
        self.lbl_takeoff_flights_count.setText("кол-во:")  # меняем текст
        self.lbl_takeoff_flights_count.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_takeoff_flights_count.addWidget(self.lbl_takeoff_flights_count)
        self.takeoff_flights_count = QLabel(self)  # заголовок
        self.takeoff_flights_count.setFont(QtGui.QFont('Helvetica', 16))  # изменяем шрифт
        self.takeoff_flights_count.setFixedWidth(20)
        self.takeoff_flights_count.setFixedHeight(22)
        self.takeoff_flights_count.setText(str(self.count_takeoff_flights))  # меняем текст
        self.takeoff_flights_count.setStyleSheet("color: black;")  # меняем цвет текста
        HLayout_takeoff_flights_count.addWidget(self.takeoff_flights_count)
        VLayout_takeoff_flights.addLayout(HLayout_takeoff_flights_count)

        # Карточки рейсов на взлёт
        self.scrollA_takeoff_flights = QScrollArea()
        self.scrollA_takeoff_flights.setFixedWidth(435)
        self.scrollA_takeoff_flights.setFixedHeight(242)
        self.scrollA_takeoff_flights.setStyleSheet("""
                QScrollArea {
                    background-color: rgb(39, 39, 61);
                    padding: 10px 5px;
                    border-top-left-radius: 15px;
                    border-top-right-radius: 0px;
                    border-bottom-left-radius: 15px;
                    border-bottom-right-radius: 0px;
                }
                QScrollBar:vertical {
                    background-color: rgb(39, 39, 61);
                    width: 10px;
                }
            """)

        self.scrollW_takeoff_flights = QWidget()
        self.scrollW_takeoff_flights.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scrollW_takeoff_flights.setFixedWidth(411)
        self.scrollW_takeoff_flights.setStyleSheet("background-color: rgb(39, 39, 61); border-radius: 15px;")
        self.VLayout_scroll_takeoff_flights = QVBoxLayout()
        self.VLayout_scroll_takeoff_flights.setAlignment(Qt.AlignTop)
        self.VLayout_scroll_takeoff_flights.setContentsMargins(5, 5, 5, 5)  # внешние отступы
        self.VLayout_scroll_takeoff_flights.setSpacing(5)  # расстояние между элементами
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
        self.btn_help.clicked.connect(self.onBtnHelpClick)  # при клике на кнопку
        HLayout_btn_help.addWidget(self.btn_help)
        VLayout_btns_navigation.addLayout(HLayout_btn_help)
        HLayout_btn_exit = QHBoxLayout()
        HLayout_btn_exit.setAlignment(Qt.AlignRight)
        HLayout_btn_exit.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        self.btn_exit = NavigationBtn(self, name="exit", width=142, height=37)  # кнопка "Выход"
        self.btn_exit.clicked.connect(self.parent.parent.close)  # при клике на кнопку
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
        for i in range(self.count_runways):
            self.runways.append(RunwayWidget(self, id=i+1))
            HLayout_runway.addWidget(self.runways[-1])
        VLayout_main.addLayout(HLayout_runway)

        self.setLayout(VLayout_main)

    # Выбор номера взлётно-посадочной полосы
    def onBtnNumberClick(self):
        btn_name = int(self.sender().objectName())
        # Выделяем кнопку
        self.btns_number[btn_name].setStyleSheet("""
                QPushButton {background:rgb(70, 70, 116); border-radius: 10px; border: 4px solid rgb(39, 39, 61);}
            """)
        if self.current_runway == -1:
            self.current_runway = btn_name  # присваиваем новый номер взлётно-посадочной полосы
        if self.current_runway != btn_name:
            # Убираем выделение предыдущей кнопки
            self.btns_number[self.current_runway].setStyleSheet("""
                    QPushButton {background:rgb(39, 39, 61); border-radius: 10px; border: 0px;}
                    QPushButton:hover {background:rgb(39, 39, 61); border-radius: 10px; border: 2px solid rgb(172, 177, 202);}
                """)
            self.current_runway = btn_name  # присваиваем новый номер взлётно-посадочной полосы

    # Выбор рейса
    def onBtnFlightClick(self):
        btn_name = int(self.sender().objectName())
        if self.btns_flights[btn_name].can_click == True:
            # Выделяем кнопку
            self.btns_flights[btn_name].setStyleSheet("""
                    QPushButton {background-color:rgb(70, 70, 116); border-radius: 10px; border: 3px solid rgb(39, 39, 61);}
                """)
            self.btns_flights[btn_name].lbl_number.setStyleSheet("background:rgb(70, 70, 116); color:white;")
            self.btns_flights[btn_name].lbl_firm.setStyleSheet("background:rgb(70, 70, 116); color:white;")
            self.btns_flights[btn_name].lbl_model.setStyleSheet("background:rgb(70, 70, 116); color:white;")
            self.btns_flights[btn_name].lbl_time_show.setStyleSheet("background:rgb(70, 70, 116); color:white;")
            if self.current_flight == -1:
                self.current_flight = btn_name  # присваиваем новую карточку рейса
            if self.current_flight != btn_name:
                # Убираем выделение предыдущей кнопки
                self.btns_flights[self.current_flight].setStyleSheet("""
                        QPushButton {background:rgb(217, 217, 217); border-radius: 10px; border: 0px;}
                        QPushButton:hover {background:rgb(217, 217, 217); border-radius: 10px; border: 3px solid rgb(39, 39, 61);}
                    """)
                self.btns_flights[self.current_flight].lbl_number.setStyleSheet("background:rgb(217, 217, 217); color:black;")
                self.btns_flights[self.current_flight].lbl_firm.setStyleSheet("background:rgb(217, 217, 217); color:black;")
                self.btns_flights[self.current_flight].lbl_model.setStyleSheet("background:rgb(217, 217, 217); color:black;")
                self.btns_flights[self.current_flight].lbl_time_show.setStyleSheet("background:rgb(217, 217, 217); color:black;")
                self.current_flight = btn_name  # присваиваем новую карточку рейса

    # Кнопка "Справка"
    def onBtnHelpClick(self):
        help_window = HelpWindow(self)
        help_window.show()

    # Кнопка "НАЧАТЬ"
    def btnStartClick(self, status):
        if status != "failed":
            status = "succeed"
        if self.btnStartActive == True:
            self.date_start = datetime.now()
            self.btn_start.lbl_name.setText("СТОП")
            self.obj_update_info = UpdateInfo(self.count_users, self.current_airport)     # объект, в котором происходит работа со временем и данными из базы данных
            self.thread = QThread()  # отдельный поток для обновления данных на экране
            self.obj_update_info.moveToThread(self.thread)  # добавляем созданный объект в отдельный поток
            self.thread.started.connect(self.obj_update_info.start)     # при старте потока запускается функция start в объекте
            self.obj_update_info.updateTimeSignal.connect(self.updateTime)  # при сигнале updateTimeSignal вызывается функция updateTime
            self.obj_update_info.addFlightSignal.connect(self.addFlight)  # при сигнале addFlightSignal вызывается функция addFlight
            self.obj_update_info.checkCurrentSignal.connect(self.updateRunways)  # при сигнале checkCurrentSignal вызывается функция updateRunways
            self.obj_update_info.finishSignal.connect(self.thread.quit) # при сигнале finishSignal завершаем отдельный поток
            self.thread.start()     # запускаем отдельный поток
            self.btnStartActive = False

        elif self.btnStartActive == False:
            self.date_end = datetime.now()
            self.obj_update_info.stop()     # останавливаем все процессы внутри объекта
            self.thread.quit()  # завершаем отдельный поток
            self.btn_start.lbl_name.setText("НАЧАТЬ")
            self.btnStartActive = True
            # Собираем и отправляем статистику
            setUserStatistics(id=count_all_statistics(),
                              user_id=self.current_user,
                              airport_id=self.current_airport,
                              count_users_in_airport=self.count_users,
                              time_spent=str(self.date_end-self.date_start),
                              data_start=str(self.date_start),
                              data_end=str(self.date_end),
                              status=str(status))
            setSessionsInfo(user_id=self.current_user, status=str(status))

            msg = QMessageBox()
            if status == "failed":
                msg.setIcon(QMessageBox.Critical)
            elif status == "succeed":
                msg.setIcon(QMessageBox.Information)
            msg.setText("Сессия завершена.")
            msg.setInformativeText("user_id: {0},\nairport_id: {1},\ncount_users_in_airport: {2},\ntime_spent: {3},\ndata_start: {4},\ndata_end: {5},\nstatus: {6}".format(self.current_user, self.current_airport, self.count_users, str(self.date_end-self.date_start), str(self.date_start), str(self.date_end), str(status)))
            msg.setWindowTitle("Результаты сохранены")
            msg.exec_()

    def updateTime(self, time_string):
        self.lbl_time.setText(time_string)

    def addFlight(self, flight_info):
        self.btns_flights.append(FlightWidget(self,
                                              object_name=self.count_all_flights,
                                              id=flight_info["id"],
                                              type=flight_info["type"],
                                              number=flight_info["number"],
                                              firm=flight_info["firm"],
                                              model=flight_info["model"],
                                              time_show=flight_info["time_show"],
                                              time_on_runway=flight_info["time_on_runway"])
                                 )
        self.btns_flights[-1].clicked.connect(self.onBtnFlightClick)  # при клике на кнопку
        self.count_all_flights += 1

        if flight_info["type"] == "boarding_flight":
            self.count_boarding_flights += 1
            self.VLayout_scroll_boarding_flights.addWidget(self.btns_flights[-1])
            self.scrollW_boarding_flights.setFixedHeight(self.count_boarding_flights * (34 + 7))
            self.boarding_flights_count.setText(str(self.count_boarding_flights))  # меняем текст

        elif flight_info["type"] == "takeoff_flight":
            self.count_takeoff_flights += 1
            self.VLayout_scroll_takeoff_flights.addWidget(self.btns_flights[-1])
            self.scrollW_takeoff_flights.setFixedHeight(self.count_takeoff_flights * (34 + 7))
            self.takeoff_flights_count.setText(str(self.count_takeoff_flights))  # меняем текст

    def updateRunways(self):
        # Главное ограничение для диспетчера - если кол-во рейсов в одном из блоков больше 10, то программа останавливается
        if self.count_boarding_flights > 10 or self.count_takeoff_flights > 10:
            self.btnStartActive = False
            self.btnStartClick(status="failed")

        if self.current_runway != -1 and self.current_flight != -1:
            if self.btns_flights[self.current_flight].type == "boarding_flight":
                self.count_boarding_flights -= 1
                self.scrollW_boarding_flights.setFixedHeight(self.count_boarding_flights * (42 + 7))
                self.boarding_flights_count.setText(str(self.count_boarding_flights))  # меняем текст
            elif self.btns_flights[self.current_flight].type == "takeoff_flight":
                self.count_takeoff_flights -= 1
                self.scrollW_takeoff_flights.setFixedHeight(self.count_takeoff_flights * (42 + 7))
                self.takeoff_flights_count.setText(str(self.count_takeoff_flights))  # меняем текст
            self.count_flights_on_runways[self.current_runway] += 1
            self.btns_flights[self.current_flight].current_runway = self.current_runway
            self.runways[self.current_runway].VLayout_runway_flights.addWidget(self.btns_flights[self.current_flight])
            self.runways[self.current_runway].scrollW_runway.setFixedHeight(self.count_flights_on_runways[self.current_runway] * (50 + 13))
            self.runways[self.current_runway].runway_count.setText(str(self.count_flights_on_runways[self.current_runway]))  # меняем текст

            # Убираем выделение у кнопки с номером
            self.btns_number[self.current_runway].setStyleSheet("""
                    QPushButton {background:rgb(39, 39, 61); border-radius: 10px; border: 0px;}
                    QPushButton:hover {background:rgb(39, 39, 61); border-radius: 10px; border: 2px solid rgb(172, 177, 202);}
                """)
            self.current_runway = -1

            # Устанавливаем новые стили у карточки рейса
            self.btns_flights[self.current_flight].setStyleSheet("""
                    QPushButton {background:rgb(217, 217, 217); border-radius: 0px; border: 0px;}
                """)
            self.btns_flights[self.current_flight].setFixedWidth(253)
            self.btns_flights[self.current_flight].setFixedHeight(50)
            self.btns_flights[self.current_flight].can_click = False
            self.btns_flights[self.current_flight].start_time_on_runway = time.strftime("%H:%M:%S", time.localtime())
            self.btns_flights[self.current_flight].lbl_number.setStyleSheet("background:rgb(217, 217, 217); color:black;")
            self.btns_flights[self.current_flight].lbl_number.setFont(QtGui.QFont('Helvetica', 11, weight=QtGui.QFont.Bold))  # изменяем шрифт
            self.btns_flights[self.current_flight].lbl_number.setFixedWidth(38)
            self.btns_flights[self.current_flight].lbl_number.setFixedHeight(46)
            self.btns_flights[self.current_flight].lbl_number.setWordWrap(True)  # перенос текста
            self.btns_flights[self.current_flight].lbl_firm.setStyleSheet("background:rgb(217, 217, 217); color:black;")
            self.btns_flights[self.current_flight].lbl_firm.setFont(QtGui.QFont('Helvetica', 11))  # изменяем шрифт
            self.btns_flights[self.current_flight].lbl_firm.setFixedWidth(70)
            self.btns_flights[self.current_flight].lbl_firm.setFixedHeight(45)
            self.btns_flights[self.current_flight].lbl_firm.setWordWrap(True)  # перенос текста
            self.btns_flights[self.current_flight].lbl_model.setStyleSheet("background:rgb(217, 217, 217); color:black;")
            self.btns_flights[self.current_flight].lbl_model.setFont(QtGui.QFont('Helvetica', 11))  # изменяем шрифт
            self.btns_flights[self.current_flight].lbl_model.setFixedWidth(70)
            self.btns_flights[self.current_flight].lbl_model.setFixedHeight(45)
            self.btns_flights[self.current_flight].lbl_model.setWordWrap(True)  # перенос текста
            self.btns_flights[self.current_flight].lbl_time_show.setStyleSheet("background:rgb(217, 217, 217); color:black;")
            self.btns_flights[self.current_flight].lbl_time_show.setFont(QtGui.QFont('Helvetica', 9))  # изменяем шрифт
            self.btns_flights[self.current_flight].lbl_time_show.setFixedWidth(36)
            self.btns_flights[self.current_flight].lbl_time_show.setFixedHeight(22)
            self.btns_flights[self.current_flight].lbl_time_show.setWordWrap(True)  # перенос текста
            self.current_flight = -1

        # Скрываем рейсы, которые уже не должны находиться на взлётно-посадочной полосе
        for i in range(len(self.btns_flights)):
            if self.btns_flights[i].can_click == False and self.btns_flights[i].start_time_on_runway != "":
                if datetime.now() >= datetime(year=datetime.now().year, month=datetime.now().month,
                                              day=datetime.now().day,
                                              hour=int(self.btns_flights[i].start_time_on_runway[:2]),
                                              minute=int(self.btns_flights[i].start_time_on_runway[3:5]),
                                              second=int(self.btns_flights[i].start_time_on_runway[6:])) + timedelta(
                    seconds=int(self.btns_flights[i].time_on_runway)):
                    self.btns_flights[i].hide()  # скрываем устаревший рейс
                    self.btns_flights[i].start_time_on_runway = ""
                    self.count_flights_on_runways[self.btns_flights[i].current_runway] -= 1
                    self.runways[self.btns_flights[i].current_runway].scrollW_runway.setFixedHeight(
                        self.count_flights_on_runways[self.btns_flights[i].current_runway] * (50 + 13))
                    self.runways[self.btns_flights[i].current_runway].runway_count.setText(
                        str(self.count_flights_on_runways[self.btns_flights[i].current_runway]))  # меняем текст
                    break

    def __del__(self):
        if self.btnStartActive == False:
            self.date_end = datetime.now()
            self.obj_update_info.stop()  # останавливаем все процессы внутри объекта
            self.thread.quit()  # завершаем отдельный поток

            # Собираем и отправляем статистику
            setUserStatistics(id=count_all_statistics(),
                              user_id=self.current_user,
                              airport_id=self.current_airport,
                              count_users_in_airport=self.count_users,
                              time_spent=str(self.date_end - self.date_start),
                              data_start=str(self.date_start),
                              data_end=str(self.date_end),
                              status="error")
            setSessionsInfo(user_id=self.current_user, status="error")

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Сессия завершена.")
            msg.setInformativeText(
                "user_id: {0},\nairport_id: {1},\ncount_users_in_airport: {2},\ntime_spent: {3},\ndata_start: {4},\ndata_end: {5},\nstatus: {6}".format(
                    self.current_user, self.current_airport, self.count_users, str(self.date_end - self.date_start),
                    str(self.date_start), str(self.date_end), "error"))
            msg.setWindowTitle("Результаты сохранены")
            msg.exec_()
