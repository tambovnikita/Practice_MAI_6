
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt


# Карточки рейсов
class FlightWidget(QPushButton):
    def __init__(self, parent, id, number, firm, model):
        QPushButton.__init__(self, parent)
        self.setObjectName("flight"+id)
        self.setFixedWidth(401)
        self.setFixedHeight(42)
        self.setStyleSheet("""
            QPushButton {background:rgb(217, 217, 217); border-radius: 10px; border: 0px;}
            QPushButton:hover {background:rgb(217, 217, 217); border-radius: 10px; border: 3px solid rgb(39, 39, 61);}
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
        self.lbl_firm.setFixedWidth(150)
        self.lbl_firm.setFixedHeight(26)
        self.lbl_firm.setText(firm)
        self.lbl_firm.setAlignment(Qt.AlignCenter)
        HLayout_flight.addWidget(self.lbl_firm)

        self.lbl_model = QLabel(self)
        self.lbl_model.setFont(QtGui.QFont('Helvetica', 20))  # изменяем шрифт
        self.lbl_model.setStyleSheet("background:rgb(217, 217, 217); color:black;")
        self.lbl_model.setFixedWidth(150)
        self.lbl_model.setFixedHeight(26)
        self.lbl_model.setText(model)
        self.lbl_model.setAlignment(Qt.AlignCenter)
        HLayout_flight.addWidget(self.lbl_model)

        self.setLayout(HLayout_flight)


# Кнопки "1", "2", "3", "4"
class NumberBtn(QPushButton):
    def __init__(self, parent, number):
        QPushButton.__init__(self, parent)
        self.setObjectName("btnNumber"+number)
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


# Взлётно-посадочные полосы
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
