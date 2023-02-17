# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.select_txt_btn = QPushButton(self.centralwidget)
        self.select_txt_btn.setObjectName(u"select_txt_btn")
        self.select_txt_btn.setGeometry(QRect(90, 110, 141, 41))
        self.selected_txt_lbl = QLabel(self.centralwidget)
        self.selected_txt_lbl.setObjectName(u"selected_txt_lbl")
        self.selected_txt_lbl.setGeometry(QRect(80, 210, 361, 31))
        self.write_new_btn = QPushButton(self.centralwidget)
        self.write_new_btn.setObjectName(u"write_new_btn")
        self.write_new_btn.setGeometry(QRect(400, 110, 131, 41))
        self.file_name_lineEdit = QLineEdit(self.centralwidget)
        self.file_name_lineEdit.setObjectName(u"file_name_lineEdit")
        self.file_name_lineEdit.setGeometry(QRect(410, 160, 113, 22))
        self.select_existing_excel_btn = QPushButton(self.centralwidget)
        self.select_existing_excel_btn.setObjectName(u"select_existing_excel_btn")
        self.select_existing_excel_btn.setGeometry(QRect(400, 350, 181, 51))
        self.write_existing_btn = QPushButton(self.centralwidget)
        self.write_existing_btn.setObjectName(u"write_existing_btn")
        self.write_existing_btn.setGeometry(QRect(400, 420, 181, 41))
        self.selected_xlsx_lbl = QLabel(self.centralwidget)
        self.selected_xlsx_lbl.setObjectName(u"selected_xlsx_lbl")
        self.selected_xlsx_lbl.setGeometry(QRect(600, 340, 181, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.select_txt_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.selected_txt_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d \u0444\u0430\u0439\u043b", None))
        self.write_new_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 \u043d\u043e\u0432\u044b\u0439", None))
        self.file_name_lineEdit.setText(QCoreApplication.translate("MainWindow", u"logs timestamp", None))
        self.select_existing_excel_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439", None))
        self.write_existing_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 \u0441\u0443\u0449\u0435\u0441\u0442\u0443\u044e\u0449\u0438\u0439", None))
        self.selected_xlsx_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d \u0444\u0430\u0439\u043b", None))
    # retranslateUi

