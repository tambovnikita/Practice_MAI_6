"""
Тамбов Никита М1О-309С-19
"""


from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QHBoxLayout, \
    QVBoxLayout, QComboBox
from PyQt5.QtCore import Qt, QObject

from StartWindowWidgets import UserWidget, AirportWidget, NavigationBtn
from MainWindow import MainWindow
from DataBaseMethods import count_all_users, count_all_airports, getUserInfo, getAirportInfo


class MainWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.parent = parent
        self.main_window_create = False     # переменная, проверяющая создан ли объект MainWindow

        self.btns_users = []    # карточки пользователей
        self.btns_airports = []    # карточки аэропортов

        self.count_users = count_all_users()    # кол-во диспетчеров
        self.count_airports = count_all_airports()      # кол-во аэропортов
        self.current_user = 0  # выбранная карточка пользователя
        self.current_airport = 0   # выбранная карточка аэропорта

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
        for i in range(self.count_users):
            self.combobox_count_users.addItem(str(i+1))
        self.combobox_count_users.setCurrentIndex(self.count_users-1)    # устанавливаем значение по умолчанию
        self.combobox_count_users.activated[str].connect(self.onComboBoxCountUsers)     # при выборе кол-ва диспетчеров
        HLayout_count_users.addWidget(self.combobox_count_users)
        VLayout_count_users.addLayout(HLayout_count_users)
        HLayout_users.addLayout(VLayout_count_users)

        # Карточки пользователей
        for i in range(self.count_users):
            self.btns_users.append(UserWidget(self,
                                              user_id=i,
                                              user_name=getUserInfo(i, "name"),
                                              user_img=getUserInfo(i, "img")))
            self.btns_users[-1].clicked.connect(self.onBtnUserClick)    # при клике на карточку пользователя
            HLayout_users.addWidget(self.btns_users[-1])
        self.updateBtnUser(0)

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
        for i in range(self.count_airports):
            self.btns_airports.append(AirportWidget(self,
                                                    airport_id=i,
                                                    airport_name=getAirportInfo(i, "name"),
                                                    count_runways=getAirportInfo(i, "count_runways")))
            self.btns_airports[-1].clicked.connect(self.onBtnAirportClick)  # при клике на карточку аэропорта
            GridLayout_airports.addWidget(self.btns_airports[-1], i//2, i%2)
        self.updateBtnAirport(0)
        HLayout_airports.addLayout(GridLayout_airports)

        VLayout_main.addLayout(HLayout_airports)
        self.setLayout(VLayout_main)

    # Отображение определённого кол-ва карточек пользователей
    def onComboBoxCountUsers(self, text):
        self.count_users = int(text)
        self.current_user = 0
        self.updateBtnUser(0)

        # Убираем выделение у остальных пользовательских карточек
        for i in range(1, len(self.btns_users)):
            self.btns_users[i].setStyleSheet("""
                    QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                    QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
                """)

        # Скрываем фото и имена всех пользователей
        for btn_user in self.btns_users:
            btn_user.user_img.hide()
            btn_user.lbl_name_user.hide()

        # Показываем фото и имена только нужных пользователей
        for i in range(int(text)):
            self.btns_users[i].user_img.show()
            self.btns_users[i].lbl_name_user.show()

    # Изменение стилей у карточек пользователей
    def updateBtnUser(self, btn_id):
        # Выделяем карточку пользователя
        if self.count_users >= btn_id + 1:
            self.btns_users[btn_id].setStyleSheet("QPushButton {background:rgb(39, 39, 61); border-radius: 20px;}")

        if self.current_user != btn_id:
            # Убираем выделение предыдущей карточки пользователя
            if self.count_users >= btn_id+1:
                self.btns_users[self.current_user].setStyleSheet("""
                        QPushButton {background:rgb(135, 136, 160); border-radius: 20px;}
                        QPushButton:hover {background:rgb(70, 70, 116); border-radius: 20px;}
                        """)
                self.current_user = btn_id  # присваиваем новую карточку пользователя

    # Выбор карточки пользователя
    def onBtnUserClick(self):
        btn_id = int(self.sender().objectName())
        self.updateBtnUser(btn_id)

    # Изменение стилей у карточек аэропортов
    def updateBtnAirport(self, btn_id):
        # Выделяем карточку аэропорта
        self.btns_airports[btn_id].setStyleSheet("QPushButton {background:rgb(39, 39, 61); border: 0;}")

        if self.current_airport != btn_id:
            # Убираем выделение предыдущей карточки аэропорта
            self.btns_airports[self.current_airport].setStyleSheet("""
                        QPushButton {background:rgb(135, 136, 160); border: 0;}
                        QPushButton:hover {background:rgb(70, 70, 116); border: 0;}
                        """)
            self.current_airport = btn_id  # присваиваем новую карточку аэропорта

    # Выбор карточки аэропорта
    def onBtnAirportClick(self):
        btn_id = int(self.sender().objectName())
        self.updateBtnAirport(btn_id)

    # Следующий экран
    def btnFurtherClick(self):
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
        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)     # устанавливаем главный виджет

    # Завершаем отдельный поток, если окно хотят закрыть
    def closeEvent(self, event):
        del self.main_widget
