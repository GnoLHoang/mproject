import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QStackedWidget, QDateTimeEdit, QMainWindow, QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from . uipage1 import Ui_Page1
from . uipage2 import Ui_Page2

class Ui_TranslateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Countdown & Clock")

        # Set property main windown
        self.setObjectName("Test")
        self.resize(1280, 720)
        self.setMinimumSize(QtCore.QSize(1, 1))
        self.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(159, 199, 240);")
        self.setProperty("fa", "")

        # Main layout (horizontal)
        self.main_layout = QHBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_layout)

        # Stacked widget (main content)
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Page 1
        self.page1 = Ui_Page1()
        self.page1_widget = QWidget()
        self.page1.setupUi(self.page1_widget)
        self.stacked_widget.addWidget(self.page1_widget)

        # Page 2
        self.page2 = Ui_Page2()
        self.page2_widget = QWidget()
        self.page2.setupUi(self.page2_widget)
        self.stacked_widget.addWidget(self.page2_widget)

        # Navigation buttons
        self.page1.page2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.page2.page1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        self.ui = merge_property(self.page1, self.page2)

class merge_property:
    def __init__(self, page1, page2):
        self.page1 = page1
        self.page2 = page2

    def __getattr__(self, name):
        # Try to get the attribute from page1 first
        try:
            return getattr(self.page1, name)
        except AttributeError:
            # If not found in page1, try page2
            return getattr(self.page2, name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_TranslateApp()
    window.show()
    sys.exit(app.exec_())