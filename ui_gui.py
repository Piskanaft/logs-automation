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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 400)
        MainWindow.setBaseSize(QSize(300, 300))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(32, 4, 4, 4)
        self.write_existing_btn = QPushButton(self.centralwidget)
        self.write_existing_btn.setObjectName(u"write_existing_btn")
        self.write_existing_btn.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.write_existing_btn, 5, 2, 1, 1)

        self.select_existing_excel_btn = QPushButton(self.centralwidget)
        self.select_existing_excel_btn.setObjectName(u"select_existing_excel_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_existing_excel_btn.sizePolicy().hasHeightForWidth())
        self.select_existing_excel_btn.setSizePolicy(sizePolicy)
        self.select_existing_excel_btn.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.select_existing_excel_btn, 3, 2, 1, 1)

        self.existing_done_tick = QLabel(self.centralwidget)
        self.existing_done_tick.setObjectName(u"existing_done_tick")
        self.existing_done_tick.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.existing_done_tick.sizePolicy().hasHeightForWidth())
        self.existing_done_tick.setSizePolicy(sizePolicy1)
        self.existing_done_tick.setMinimumSize(QSize(0, 0))
        self.existing_done_tick.setMaximumSize(QSize(50, 50))
        self.existing_done_tick.setSizeIncrement(QSize(1, 1))
        self.existing_done_tick.setBaseSize(QSize(0, 0))
        self.existing_done_tick.setPixmap(QPixmap(u"tick.png"))
        self.existing_done_tick.setScaledContents(True)

        self.gridLayout.addWidget(self.existing_done_tick, 5, 3, 1, 1)

        self.file_name_lineEdit = QLineEdit(self.centralwidget)
        self.file_name_lineEdit.setObjectName(u"file_name_lineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.file_name_lineEdit.sizePolicy().hasHeightForWidth())
        self.file_name_lineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.file_name_lineEdit, 1, 2, 1, 1)

        self.new_done_tick = QLabel(self.centralwidget)
        self.new_done_tick.setObjectName(u"new_done_tick")
        self.new_done_tick.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.new_done_tick.sizePolicy().hasHeightForWidth())
        self.new_done_tick.setSizePolicy(sizePolicy3)
        self.new_done_tick.setMinimumSize(QSize(0, 0))
        self.new_done_tick.setMaximumSize(QSize(50, 50))
        self.new_done_tick.setSizeIncrement(QSize(1, 1))
        self.new_done_tick.setBaseSize(QSize(1, 1))
        self.new_done_tick.setLineWidth(0)
        self.new_done_tick.setPixmap(QPixmap(u"tick.png"))
        self.new_done_tick.setScaledContents(True)

        self.gridLayout.addWidget(self.new_done_tick, 0, 3, 1, 1)

        self.write_new_btn = QPushButton(self.centralwidget)
        self.write_new_btn.setObjectName(u"write_new_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.write_new_btn.sizePolicy().hasHeightForWidth())
        self.write_new_btn.setSizePolicy(sizePolicy4)
        self.write_new_btn.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.write_new_btn, 0, 2, 1, 1)

        self.select_txt_btn = QPushButton(self.centralwidget)
        self.select_txt_btn.setObjectName(u"select_txt_btn")
        sizePolicy4.setHeightForWidth(self.select_txt_btn.sizePolicy().hasHeightForWidth())
        self.select_txt_btn.setSizePolicy(sizePolicy4)
        self.select_txt_btn.setMinimumSize(QSize(150, 50))

        self.gridLayout.addWidget(self.select_txt_btn, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.selected_xlsx_lbl = QLabel(self.centralwidget)
        self.selected_xlsx_lbl.setObjectName(u"selected_xlsx_lbl")
        sizePolicy4.setHeightForWidth(self.selected_xlsx_lbl.sizePolicy().hasHeightForWidth())
        self.selected_xlsx_lbl.setSizePolicy(sizePolicy4)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        self.selected_xlsx_lbl.setFont(font)
        self.selected_xlsx_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.selected_xlsx_lbl, 4, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.selected_txt_lbl = QLabel(self.centralwidget)
        self.selected_txt_lbl.setObjectName(u"selected_txt_lbl")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.selected_txt_lbl.sizePolicy().hasHeightForWidth())
        self.selected_txt_lbl.setSizePolicy(sizePolicy5)
        self.selected_txt_lbl.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.selected_txt_lbl.setFont(font1)
        self.selected_txt_lbl.setAcceptDrops(True)
        self.selected_txt_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.selected_txt_lbl.setWordWrap(True)

        self.gridLayout.addWidget(self.selected_txt_lbl, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.write_existing_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 \u0441\u0443\u0449\u0435\u0441\u0432\u0442\u0443\u044e\u0449\u0438\u0439", None))
        self.select_existing_excel_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439", None))
        self.existing_done_tick.setText("")
        self.file_name_lineEdit.setText(QCoreApplication.translate("MainWindow", u"logs timestamp", None))
        self.new_done_tick.setText("")
        self.write_new_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432 \u043d\u043e\u0432\u044b\u0439", None))
        self.select_txt_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.selected_xlsx_lbl.setText(QCoreApplication.translate("MainWindow", u"Excel \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.selected_txt_lbl.setText(QCoreApplication.translate("MainWindow", u"Txt \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
    # retranslateUi

