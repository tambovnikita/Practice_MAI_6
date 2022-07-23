"""
Тамбов Никита М1О-309С-19
"""


from PyQt5.QtWidgets import QApplication
import sys

from StartWindow import StartWindow


app = QApplication(sys.argv)
win = StartWindow(app)
win.show()
sys.exit(app.exec_())
