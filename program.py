import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QPushButton, QToolButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file
        self.load_ui("design.ui")

        # Set up UI components
        self.setup_ui()

    def load_ui(self, filename):
        from PyQt5 import uic
        uic.loadUi(filename, self)

    def setup_ui(self):
        # Extracting widgets from UI
        label_2 = self.findChild(QLabel, "label_2")
        pushButton_2 = self.findChild(QPushButton, "pushButton_2")
        pushButton = self.findChild(QPushButton, "pushButton")
        pushButton_3 = self.findChild(QPushButton, "pushButton_3")
        checkBox_2 = self.findChild(QCheckBox, "checkBox_2")
        checkBox = self.findChild(QCheckBox, "checkBox")
        toolButton = self.findChild(QToolButton, "toolButton")

        # Connecting signals and slots
        pushButton_2.clicked.connect(self.add_record)
        pushButton.clicked.connect(self.analyze)
        pushButton_3.clicked.connect(self.open_file)
        toolButton.clicked.connect(self.read_help)

    def add_record(self):
        print("Add Record button clicked")

    def analyze(self):
        print("Analyze button clicked")

    def open_file(self):
        print("Open File button clicked")

    def read_help(self):
        print("Read Help button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
