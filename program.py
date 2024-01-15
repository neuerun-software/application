import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QPushButton, QToolButton, QFileDialog, QDialog, QVBoxLayout, QLineEdit
from pathlib import Path


class DataEntryWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Расчет для предпринимателя")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label_income = QLabel("Введите данные о прибыле:")
        self.text_income = QLineEdit(self)

        self.label_expense = QLabel("Введите данные о расходах:")
        self.text_expense = QLineEdit(self)

        self.label_loan_amount = QLabel("Сумма кредита:")
        self.text_loan_amount = QLineEdit(self)

        self.label_loan_duration = QLabel("Количество месяцев обязательства:")
        self.text_loan_duration = QLineEdit(self)

        self.label_interest_rate = QLabel("Процентная ставка в месяц:")
        self.text_interest_rate = QLineEdit(self)

        self.label_net_income = QLabel("Чистая прибыль:")
        self.text_net_income = QLabel(self)

        self.label_total_payment = QLabel("Итоговая сумма по кредиту:")
        self.text_total_payment = QLabel(self)

        self.button_calculate = QPushButton("Рассчитать", self)
        self.button_calculate.clicked.connect(self.calculate_net_income_and_loan)

        self.button_clear = QPushButton("Очистить", self)
        self.button_clear.clicked.connect(self.clear_fields)

        layout.addWidget(self.label_income)
        layout.addWidget(self.text_income)
        layout.addWidget(self.label_expense)
        layout.addWidget(self.text_expense)
        layout.addWidget(self.label_loan_amount)
        layout.addWidget(self.text_loan_amount)
        layout.addWidget(self.label_loan_duration)
        layout.addWidget(self.text_loan_duration)
        layout.addWidget(self.label_interest_rate)
        layout.addWidget(self.text_interest_rate)
        layout.addWidget(self.button_calculate)
        layout.addWidget(self.label_net_income)
        layout.addWidget(self.text_net_income)
        layout.addWidget(self.label_total_payment)
        layout.addWidget(self.text_total_payment)
        layout.addWidget(self.button_clear)

        self.setLayout(layout)

    def calculate_net_income_and_loan(self):
        income = float(self.text_income.text()) if self.text_income.text() else 0.0
        expense = float(self.text_expense.text()) if self.text_expense.text() else 0.0
        net_income = income - expense
        self.text_net_income.setText(str(net_income))

        loan_amount = float(self.text_loan_amount.text()) if self.text_loan_amount.text() else 0.0
        loan_duration = int(self.text_loan_duration.text()) if self.text_loan_duration.text() else 0
        interest_rate = float(self.text_interest_rate.text()) if self.text_interest_rate.text() else 0.0

        total_payment = loan_amount * (1 + interest_rate / 100) ** loan_duration
        self.text_total_payment.setText(str(total_payment))

    def clear_fields(self):
        self.text_income.clear()
        self.text_expense.clear()
        self.text_loan_amount.clear()
        self.text_loan_duration.clear()
        self.text_interest_rate.clear()
        self.text_net_income.clear()
        self.text_total_payment.clear()


# class CheckYourDataInFile():
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Работа с excel файлами")
#         self.setGeometry(100, 100, 400, 300)

#         layout = QVBoxLayout()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.load_ui("design.ui")

        self.setup_ui()

    def load_ui(self, filename):
        from PyQt5 import uic
        uic.loadUi(filename, self)

    def setup_ui(self):
        label_2 = self.findChild(QLabel, "label_2")
        pushButton_2 = self.findChild(QPushButton, "pushButton_2")
        pushButton = self.findChild(QPushButton, "pushButton")
        pushButton_3 = self.findChild(QPushButton, "pushButton_3")
        checkBox_2 = self.findChild(QCheckBox, "checkBox_2")
        checkBox = self.findChild(QCheckBox, "checkBox")
        toolButton = self.findChild(QToolButton, "toolButton")

        pushButton_2.clicked.connect(self.add_record)
        pushButton.clicked.connect(self.show_data_entry_window)
        pushButton_3.clicked.connect(self.open_file)
        toolButton.clicked.connect(self.read_help)

    def add_record(self):
        print("Add Record button clicked")

    def show_data_entry_window(self):
        data_entry_window = DataEntryWindow()
        data_entry_window.exec_()

    def open_file(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        if dialog.exec_():
            filenames = dialog.selectedFiles()
            if filenames:
                selected_paths = [str(Path(file)) for file in filenames]
                return selected_paths

    def read_help(self):
        print("Read Help button clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
