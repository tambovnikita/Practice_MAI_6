
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class UserWidget(QPushButton):
    def __init__(self, parent, user_id, user_name, user_img):
        QPushButton.__init__(self, parent)
        self.setObjectName(str(user_id))
        self.setFixedWidth(125)
        self.setFixedHeight(152)
        self.setStyleSheet("""
            QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
            QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
            """)

        VLayout_user = QVBoxLayout()
        VLayout_user.setContentsMargins(0, 0, 0, 0)  # внешние отступы
        VLayout_user.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.user_img = QLabel(self)
        self.user_img.setStyleSheet("background:rgb(217, 217, 217); border-radius: 10px;")
        self.user_img.setFixedWidth(100)
        self.user_img.setFixedHeight(100)
        self.pixmap = QtGui.QPixmap(user_img)
        self.user_img.setPixmap(self.pixmap)
        self.user_img.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)  # выравнивание (центр)
        VLayout_user.addWidget(self.user_img)

        self.lbl_name_user = QLabel(self)
        self.lbl_name_user.setFont(QtGui.QFont('Helvetica', 18, weight=QtGui.QFont.Bold))
        self.lbl_name_user.setFixedWidth(100)
        self.lbl_name_user.setFixedHeight(24)
        self.lbl_name_user.setContentsMargins(0, 5, 0, 0)  # внешние отступы
        self.lbl_name_user.setAlignment(Qt.AlignCenter)
        self.lbl_name_user.setText(user_name)
        self.lbl_name_user.setStyleSheet("background: 0; color: white;")
        VLayout_user.addWidget(self.lbl_name_user)

        self.setLayout(VLayout_user)


class AirportWidget(QPushButton):
    def __init__(self, parent, airport_id, airport_name, count_runways):
        QPushButton.__init__(self, parent)
        self.setObjectName(str(airport_id))
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
        self.lbl_count_runways.setText("Кол-во полос: "+str(count_runways))
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
