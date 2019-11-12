# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sqliteeditor.ui',
# licensing of 'sqliteeditor.ui' applies.
#
# Created: Mon Nov 11 12:28:34 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_current_file = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_current_file.sizePolicy().hasHeightForWidth())
        self.label_current_file.setSizePolicy(sizePolicy)
        self.label_current_file.setObjectName("label_current_file")
        self.horizontalLayout.addWidget(self.label_current_file)
        self.button_change_file = QtWidgets.QPushButton(self.frame)
        self.button_change_file.setObjectName("button_change_file")
        self.horizontalLayout.addWidget(self.button_change_file)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_current_table = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_current_table.sizePolicy().hasHeightForWidth())
        self.label_current_table.setSizePolicy(sizePolicy)
        self.label_current_table.setObjectName("label_current_table")
        self.horizontalLayout.addWidget(self.label_current_table)
        self.combo_table_select = QtWidgets.QComboBox(self.frame)
        self.combo_table_select.setObjectName("combo_table_select")
        self.horizontalLayout.addWidget(self.combo_table_select)
        self.verticalLayout.addWidget(self.frame)
        self.table_view = QtWidgets.QTableView(self.centralwidget)
        self.table_view.setObjectName("table_view")
        self.verticalLayout.addWidget(self.table_view)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_current_file.setText(QtWidgets.QApplication.translate("MainWindow", "No File Selected", None, -1))
        self.button_change_file.setText(QtWidgets.QApplication.translate("MainWindow", "Change File", None, -1))
        self.label_current_table.setText(QtWidgets.QApplication.translate("MainWindow", "Current Table:", None, -1))

