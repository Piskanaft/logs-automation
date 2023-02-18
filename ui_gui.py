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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(404, 314)
        MainWindow.setBaseSize(QSize(300, 300))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.select_txt_btn = QPushButton(self.centralwidget)
        self.select_txt_btn.setObjectName(u"select_txt_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_txt_btn.sizePolicy().hasHeightForWidth())
        self.select_txt_btn.setSizePolicy(sizePolicy)
        self.select_txt_btn.setMinimumSize(QSize(150, 50))
        self.select_txt_btn.setMaximumSize(QSize(150, 50))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        self.select_txt_btn.setFont(font)

        self.verticalLayout.addWidget(self.select_txt_btn, 0, Qt.AlignTop)

        self.selected_txt_lbl = QLabel(self.centralwidget)
        self.selected_txt_lbl.setObjectName(u"selected_txt_lbl")
        sizePolicy.setHeightForWidth(self.selected_txt_lbl.sizePolicy().hasHeightForWidth())
        self.selected_txt_lbl.setSizePolicy(sizePolicy)
        self.selected_txt_lbl.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.selected_txt_lbl.setFont(font1)
        self.selected_txt_lbl.setAcceptDrops(True)
        self.selected_txt_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.selected_txt_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.selected_txt_lbl)

        self.found_events_lbl = QLabel(self.centralwidget)
        self.found_events_lbl.setObjectName(u"found_events_lbl")
        sizePolicy.setHeightForWidth(self.found_events_lbl.sizePolicy().hasHeightForWidth())
        self.found_events_lbl.setSizePolicy(sizePolicy)
        self.found_events_lbl.setFont(font1)
        self.found_events_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.found_events_lbl, 0, Qt.AlignTop)

        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.RightMenu = QWidget(self.centralwidget)
        self.RightMenu.setObjectName(u"RightMenu")
        self.formLayout = QFormLayout(self.RightMenu)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setContentsMargins(-1, 0, 0, -1)
        self.write_new_btn = QPushButton(self.RightMenu)
        self.write_new_btn.setObjectName(u"write_new_btn")
        self.write_new_btn.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.write_new_btn.sizePolicy().hasHeightForWidth())
        self.write_new_btn.setSizePolicy(sizePolicy1)
        self.write_new_btn.setMinimumSize(QSize(150, 50))
        self.write_new_btn.setMaximumSize(QSize(150, 50))
        self.write_new_btn.setFont(font)
        self.write_new_btn.setCheckable(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.write_new_btn)

        self.file_name_lineEdit = QLineEdit(self.RightMenu)
        self.file_name_lineEdit.setObjectName(u"file_name_lineEdit")
        self.file_name_lineEdit.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.file_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.file_name_lineEdit.setSizePolicy(sizePolicy2)
        self.file_name_lineEdit.setMinimumSize(QSize(150, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.file_name_lineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.verticalSpacer)

        self.select_existing_excel_btn = QPushButton(self.RightMenu)
        self.select_existing_excel_btn.setObjectName(u"select_existing_excel_btn")
        self.select_existing_excel_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.select_existing_excel_btn.sizePolicy().hasHeightForWidth())
        self.select_existing_excel_btn.setSizePolicy(sizePolicy1)
        self.select_existing_excel_btn.setMinimumSize(QSize(150, 50))
        self.select_existing_excel_btn.setMaximumSize(QSize(150, 50))
        self.select_existing_excel_btn.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.select_existing_excel_btn)

        self.selected_xlsx_lbl = QLabel(self.RightMenu)
        self.selected_xlsx_lbl.setObjectName(u"selected_xlsx_lbl")
        self.selected_xlsx_lbl.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.selected_xlsx_lbl.sizePolicy().hasHeightForWidth())
        self.selected_xlsx_lbl.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        self.selected_xlsx_lbl.setFont(font2)
        self.selected_xlsx_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.selected_xlsx_lbl)

        self.write_existing_btn = QPushButton(self.RightMenu)
        self.write_existing_btn.setObjectName(u"write_existing_btn")
        self.write_existing_btn.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.write_existing_btn.sizePolicy().hasHeightForWidth())
        self.write_existing_btn.setSizePolicy(sizePolicy1)
        self.write_existing_btn.setMinimumSize(QSize(150, 50))
        self.write_existing_btn.setMaximumSize(QSize(150, 50))
        self.write_existing_btn.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.write_existing_btn)

        self.existing_done_tick = QLabel(self.RightMenu)
        self.existing_done_tick.setObjectName(u"existing_done_tick")
        self.existing_done_tick.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.existing_done_tick.sizePolicy().hasHeightForWidth())
        self.existing_done_tick.setSizePolicy(sizePolicy3)
        self.existing_done_tick.setMinimumSize(QSize(50, 50))
        self.existing_done_tick.setMaximumSize(QSize(50, 50))
        self.existing_done_tick.setSizeIncrement(QSize(1, 1))
        self.existing_done_tick.setBaseSize(QSize(0, 0))
        self.existing_done_tick.setPixmap(QPixmap(u"tick.png"))
        self.existing_done_tick.setScaledContents(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.existing_done_tick)

        self.new_done_tick = QLabel(self.RightMenu)
        self.new_done_tick.setObjectName(u"new_done_tick")
        self.new_done_tick.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.new_done_tick.sizePolicy().hasHeightForWidth())
        self.new_done_tick.setSizePolicy(sizePolicy4)
        self.new_done_tick.setMinimumSize(QSize(50, 50))
        self.new_done_tick.setMaximumSize(QSize(50, 50))
        self.new_done_tick.setSizeIncrement(QSize(1, 1))
        self.new_done_tick.setBaseSize(QSize(1, 1))
        self.new_done_tick.setLineWidth(0)
        self.new_done_tick.setPixmap(QPixmap(u"tick.png"))
        self.new_done_tick.setScaledContents(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.new_done_tick)

        self.horizontalSpacer_3 = QSpacerItem(50, 17, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.horizontalSpacer_3)


        self.horizontalLayout.addWidget(self.RightMenu)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.select_existing_excel_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.select_txt_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.selected_txt_lbl.setText(QCoreApplication.translate("MainWindow", u"Txt \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.found_events_lbl.setText("")
        self.write_new_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 \n"
"\u043d\u043e\u0432\u044b\u0439", None))
        self.file_name_lineEdit.setText(QCoreApplication.translate("MainWindow", u"logs timestamp", None))
        self.select_existing_excel_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \n"
"\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439", None))
        self.selected_xlsx_lbl.setText(QCoreApplication.translate("MainWindow", u"Excel \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.write_existing_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 \n"
"\u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439", None))
        self.existing_done_tick.setText("")
        self.new_done_tick.setText("")
    # retranslateUi

