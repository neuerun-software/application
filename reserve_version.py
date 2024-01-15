import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QFileDialog, 
    QGridLayout,
    QPushButton, 
    QLabel,
    QListWidget
)
from PyQt5.QtCore import pyqtSignal
from pathlib import Path


class MainWindow(QWidget):
    file_selected = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt File Dialog')
        self.setGeometry(100, 100, 300, 150)

        layout = QGridLayout()
        self.setLayout(layout)

        # file selection
        file_browser_btn = QPushButton('Browse')
        file_browser_btn.clicked.connect(self.open_file_dialog)

        self.file_list = QListWidget(self)

        layout.addWidget(QLabel('Files:'), 0, 0)
        layout.addWidget(self.file_list, 1, 0)
        layout.addWidget(file_browser_btn, 2 ,0)

        self.show()

    def open_file_dialog(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                selected_path = str(Path(filenames[0]))
                self.file_selected.emit(selected_path)


class Application(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Main Application')
        self.setGeometry(200, 200, 300, 150)

        layout = QGridLayout()
        self.setLayout(layout)

        self.label = QLabel('Selected File:', self)

        layout.addWidget(self.label)

        self.way_to_path = None

        self.main_window = MainWindow()
        self.main_window.file_selected.connect(self.update_label)

        self.show()

    def update_label(self, selected_path):
        self.way_to_path = selected_path
        self.label.setText(f'Selected File: {self.way_to_path}')

        # Вывод пути в командной строке (терминале)
        return(self.way_to_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Application()
    sys.exit(app.exec())
