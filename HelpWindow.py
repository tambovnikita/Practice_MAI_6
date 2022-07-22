
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel, QScrollArea, QWidget, QSizePolicy
from PyQt5.QtCore import Qt


class HelpWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setGeometry(QApplication.desktop().screenGeometry().width()//4,
                         QApplication.desktop().screenGeometry().height()//4,
                         QApplication.desktop().screenGeometry().width()//2,
                         QApplication.desktop().screenGeometry().height()//2)
        self.setWindowTitle('Справка. Симулятор диспетчера аэропорта')  # название окна
        self.setWindowIcon(QtGui.QIcon('imgs/main.ico'))  # иконка окна
        self.setStyleSheet("background-color:rgb(172, 177, 202);")  # фон окна

        # Расстановка элементов
        VLayout_main = QVBoxLayout()
        VLayout_main.setAlignment(Qt.AlignVCenter)
        VLayout_main.setSpacing(0)     # расстояние между элементами
        VLayout_main.setContentsMargins(0, 0, 0, 0)  # внешние отступы

        self.scrollA = QScrollArea()
        self.scrollA.setFixedWidth(QApplication.desktop().screenGeometry().width()//2)
        self.scrollA.setFixedHeight(QApplication.desktop().screenGeometry().height()//2)
        self.scrollA.setStyleSheet("""
                        QScrollArea {
                            background-color: rgb(135, 136, 160);
                            padding: 10px 5px;
                            border-radius: 0px;
                        }
                        QScrollBar:vertical {
                            background-color: rgb(135, 136, 160);
                            width: 10px;
                        }
                    """)

        self.scrollW = QWidget()
        self.scrollW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.scrollW.setFixedWidth((QApplication.desktop().screenGeometry().width()//2)-20)
        self.scrollW.setStyleSheet("background-color: rgb(135, 136, 160);")
        VLayout_lbls = QVBoxLayout()
        VLayout_lbls.setAlignment(Qt.AlignCenter)
        VLayout_lbls.setContentsMargins(0, 20, 0, 40)  # внешние отступы
        VLayout_lbls.setSpacing(7)  # расстояние между элементами

        self.lbl0 = QLabel()
        self.lbl0.setFixedWidth(QApplication.desktop().screenGeometry().width() // 2.5)
        self.lbl0.setWordWrap(True)  # перенос текста
        self.lbl0.setFont(QtGui.QFont('Helvetica', 18))  # изменяем шрифт
        self.lbl0.setContentsMargins(30, 20, 30, 30)  # внешние отступы
        self.lbl0.setText("""<html><head/><body>
                    <p style="line-height:30px;"><span>
                    <b>Добро пожаловать в программу "Симулятор диспетчера аэропорта".</b>
                    </span></p>
                    </body></html>
                """)
        self.lbl0.setStyleSheet("background-color:rgb(172, 177, 202); border-radius: 10px;")
        VLayout_lbls.addWidget(self.lbl0)

        self.lbl_ogr = QLabel()
        self.lbl_ogr.setFixedWidth(QApplication.desktop().screenGeometry().width() // 2.5)
        self.lbl_ogr.setWordWrap(True)  # перенос текста
        self.lbl_ogr.setFont(QtGui.QFont('Helvetica', 18))  # изменяем шрифт
        self.lbl_ogr.setContentsMargins(30, 20, 30, 30)  # внешние отступы
        self.lbl_ogr.setText("""<html><head/><body>
                            <p style="line-height:30px;"><span>
                            <b>Ограничение для диспетчера:</b> допустимо иметь в блоках "Рейсы на посадку" и "Рейсы на взлёт" не больше 10 карточек рейсов.
                            </span></p>
                            </body></html>
                        """)
        self.lbl_ogr.setStyleSheet("background-color:rgb(172, 177, 202); border-radius: 10px;")
        VLayout_lbls.addWidget(self.lbl_ogr)

        self.lbl1 = QLabel()
        self.lbl1.setFixedWidth(QApplication.desktop().screenGeometry().width()//2.5)
        self.lbl1.setWordWrap(True)  # перенос текста
        self.lbl1.setFont(QtGui.QFont('Helvetica', 18))  # изменяем шрифт
        self.lbl1.setContentsMargins(30, 20, 30, 30)  # внешние отступы
        self.lbl1.setText("""<html><head/><body>
            <p style="line-height:30px;"><span>
            После того, как Вы выберите пользователя и аэропорт на <b>Начальном экране</b>, откроется <b>Главный экран</b> симулятора.<br><br>
            После нажатия кнопки <b>"НАЧАТЬ"</b> в блоках <b>"Рейсы на посадку"</b> и <b>"Рейсы на взлёт"</b> будут перечислены все рейсы, ожидающие назначения взлётно-посадочной полосы в реальном времени.
            </span></p>
            </body></html>
        """)
        self.lbl1.setStyleSheet("background-color:rgb(172, 177, 202); border-radius: 10px;")
        VLayout_lbls.addWidget(self.lbl1)

        self.lbl2 = QLabel()
        self.lbl2.setFixedWidth(QApplication.desktop().screenGeometry().width() // 2.5)
        self.lbl2.setWordWrap(True)  # перенос текста
        self.lbl2.setFont(QtGui.QFont('Helvetica', 18))  # изменяем шрифт
        self.lbl2.setContentsMargins(30, 20, 30, 30)  # внешние отступы
        self.lbl2.setText("""<html><head/><body>
            <p style="line-height:30px;"><span>
            Между двумя блоками находятся кнопки в том же количестве, что и взлётно-посадочные полосы.<br><br>
            Чтобы назначить взлётно-посадочную полосу для рейса, нужно нажать на кнопку с номером полосы и карточку рейса в одном из блоков.
            </span></p>
            </body></html>
        """)
        self.lbl2.setStyleSheet("background-color:rgb(172, 177, 202); border-radius: 10px;")
        VLayout_lbls.addWidget(self.lbl2)

        self.lbl3 = QLabel()
        self.lbl3.setFixedWidth(QApplication.desktop().screenGeometry().width() // 2.5)
        self.lbl3.setWordWrap(True)  # перенос текста
        self.lbl3.setFont(QtGui.QFont('Helvetica', 18))  # изменяем шрифт
        self.lbl3.setContentsMargins(30, 20, 30, 30)  # внешние отступы
        self.lbl3.setText("""<html><head/><body>
                    <p style="line-height:30px;"><span>
                    В нижней части экрана находятся области, прикреплённые за отдельными взлётно-посадочными полосами аэропорта.<br><br>
                    Их количество определяется при выборе аэропорта на <b>Начальном экране</b>.<br><br>
                    После назначения определённой полосы, одна из областей автоматически обновится, добавив выбранный рейс.
                    </span></p>
                    </body></html>
                """)
        self.lbl3.setStyleSheet("background-color:rgb(172, 177, 202); border-radius: 10px;")
        VLayout_lbls.addWidget(self.lbl3)

        self.lbl4 = QLabel()
        self.lbl4.setFixedWidth(QApplication.desktop().screenGeometry().width() // 2.5)
        self.lbl4.setWordWrap(True)  # перенос текста
        self.lbl4.setFont(QtGui.QFont('Helvetica', 18))  # изменяем шрифт
        self.lbl4.setContentsMargins(30, 20, 30, 30)  # внешние отступы
        self.lbl4.setText("""<html><head/><body>
                            <p style="line-height:30px;"><span>
                            Нажмите кнопку <b>"НАЧАТЬ"</b>, чтобы приступить к работе.<br><br>
                            Кнопка <b>"СТОП"</b> останавливает симулятор.<br><br>
                            Кнопка <b>"Справка"</b> открывает окно, содержащее всю необходимую информацию по работе программы.<br><br>
                            Кнопка <b>"Выход"</b> полностью закрывает программу.
                            </span></p>
                            </body></html>
                        """)
        self.lbl4.setStyleSheet("background-color:rgb(172, 177, 202); border-radius: 10px;")
        VLayout_lbls.addWidget(self.lbl4)

        self.lbl5 = QLabel()
        self.lbl5.setFixedWidth(QApplication.desktop().screenGeometry().width() // 2.5)
        self.lbl5.setWordWrap(True)  # перенос текста
        self.lbl5.setFont(QtGui.QFont('Helvetica', 18))  # изменяем шрифт
        self.lbl5.setContentsMargins(30, 20, 30, 30)  # внешние отступы
        self.lbl5.setText("""<html><head/><body>
                                    <p style="line-height:30px;"><span>
                                    <b>Продуктивной работы и хороших полётов!</b>
                                    </span></p>
                                    </body></html>
                                """)
        self.lbl5.setStyleSheet("background-color:rgb(172, 177, 202); border-radius: 10px;")
        VLayout_lbls.addWidget(self.lbl5)

        self.scrollW.setLayout(VLayout_lbls)
        self.scrollA.setWidget(self.scrollW)
        VLayout_main.addWidget(self.scrollA)

        self.setLayout(VLayout_main)
