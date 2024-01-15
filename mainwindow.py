import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        
        loadUi('maindesign.ui', self)

       
        self.labelProgramInfo = self.findChild(QLabel, 'label_2')
        self.labelUsageTips = self.findChild(QLabel, 'label')

        
        self.actionOpen.triggered.connect(self.open_data)
        self.actionSave.triggered.connect(self.save_data)
        self.actionExit.triggered.connect(self.close)
        self.actionSettings.triggered.connect(self.show_settings)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionManual.triggered.connect(self.show_manual)
        # self.toolButtonAddRecord.clicked.connect(self.show_add_record_form)
        # self.toolButtonAnalysis.clicked.connect(self.show_analysis_form)

    def open_data(self):
        pass

    def save_data(self):
        pass

    def show_about(self):
        self.labelProgramInfo.setText(
            """<html><head/><body><p align="center"><span style=" font-weight:600;">О программе: </span></p><p align="center"><br/></p><p align="center"><span style=" font-style:italic;">Получите информацию о </span></p><p align="center"><span style=" font-style:italic;">версии приложения, авторе и других технических деталях.</span></p></body></html>"""
        )

    def show_manual(self):
        self.labelUsageTips.setText(
            """<html><head/><body><p><span style=" font-weight:600;">Совет по использованию:</span></p><p><span style=" font-style:italic;"><br/></span></p><p><span style=" font-style:italic;">Регулярно вносите данные о доходах и расходах </span></p><p><span style=" font-style:italic;">для актуального отражения вашей финансовой</span></p><p><span style=" font-style:italic;">ситуации.</span></p><p><span style=" font-style:italic;">Используйте функцию анализа, чтобы</span></p><p><span style=" font-style:italic;">определить основные области расходов</span></p><p><span style=" font-style:italic;">и найти возможности для экономии.</span></p><p><span style=" font-style:italic;">Настройте категории так, чтобы они лучше</span></p><p><span style=" font-style:italic;">отражали ваш стиль жизни и финансовые цели.</span></p><p><span style=" font-style:italic;">Спасибо за выбор нашего приложения</span></p><p><span style=" font-style:italic;">"Учет личных финансов". Мы надеемся, что оно</span></p><p><span style=" font-style:italic;">поможет вам лучше управлять вашими </span></p><p><span style=" font-style:italic;">финансами!</span></p></body></html>"""
        )

    def show_add_record_form(self):
        pass

    def show_analysis_form(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
