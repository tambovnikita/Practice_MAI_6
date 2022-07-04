
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QFrame,\
    QGridLayout, QScrollArea, QWidget, QFormLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
import sys


class UserWidget(QPushButton):
    def __init__(self, parent, user_id):
        QPushButton.__init__(self, parent)
        self.setObjectName("user"+str(user_id))
        self.setFixedWidth(221)
        self.setFixedHeight(265)
        self.setStyleSheet("""
            QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
            QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
            """)

        VLayout_user = QVBoxLayout()
        VLayout_user.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        self.user_img = QLabel(self)
        self.user_img.setStyleSheet("background:rgb(217, 217, 217); border-radius: 0px;")
        self.user_img.setFixedWidth(170)
        self.user_img.setFixedHeight(170)
        self.pixmap = QtGui.QPixmap('./imgs/users/user{}.png'.format(user_id))
        self.user_img.setPixmap(self.pixmap)
        self.user_img.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)  # выравнивание (центр)
        VLayout_user.addWidget(self.user_img)

        self.lbl_name_user = QLabel(self)
        self.lbl_name_user.setFont(QtGui.QFont('Helvetica', 40, weight=QtGui.QFont.Bold))
        self.lbl_name_user.setFixedWidth(170)
        self.lbl_name_user.setFixedHeight(42)
        self.lbl_name_user.setContentsMargins(0, 8, 0, 0)  # внешние отступы
        if user_id == 0:
            self.lbl_name_user.setText("Nikita")
        elif user_id == 1:
            self.lbl_name_user.setText("Ivan")
        elif user_id == 2:
            self.lbl_name_user.setText("Maria")
        self.lbl_name_user.setStyleSheet("background: 0; color: white;")
        VLayout_user.addWidget(self.lbl_name_user)

        self.setLayout(VLayout_user)


class MainWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.current_user = ""  # выбранная карточка пользователя

        # Расстановка элементов
        VLayout_main = QVBoxLayout()
        VLayout_main.setContentsMargins(0, 0, 0, 0)  # внешние отступы

        HLayout_users = QHBoxLayout()

        self.lbl_user = QLabel(self)  # Заголовок
        self.lbl_user.setFont(QtGui.QFont('Helvetica', 48, weight=QtGui.QFont.Bold))  # Изменяем шрифт
        self.lbl_user.setFixedWidth(339)
        self.lbl_user.setFixedHeight(103)
        self.lbl_user.setWordWrap(True)  # перенос текста
        self.lbl_user.setText("Выберите пользователя")  # Меняем текст
        self.lbl_user.setStyleSheet("color: black;")  # меняем цвет текста
        #self.lbl_user.setAlignment(Qt.AlignTop)  # направление выравнивания (наверх)
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
        self.lbl_line.setStyleSheet("background-color: black;")  # меняем цвет текста
        VLayout_main.addWidget(self.lbl_line)

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
