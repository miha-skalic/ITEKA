# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adding_data.ui'
#
# Created: Fri May  8 13:32:06 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AddData(object):
    def setupUi(self, AddData):
        AddData.setObjectName(_fromUtf8("AddData"))
        AddData.resize(1079, 581)
        self.horizontalLayout = QtGui.QHBoxLayout(AddData)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(AddData)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.plainTextEdit = QtGui.QPlainTextEdit(AddData)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(AddData)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(AddData)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.verticalLayout_4.addWidget(self.plainTextEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_1 = QtGui.QVBoxLayout()
        self.verticalLayout_1.setObjectName(_fromUtf8("verticalLayout_1"))
        self.pushButton = QtGui.QPushButton(AddData)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_1.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(AddData)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_1.addWidget(self.pushButton_2)
        self.label_4 = QtGui.QLabel(AddData)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_1.addWidget(self.label_4)
        self.rep_count = QtGui.QLabel(AddData)
        self.rep_count.setIndent(4)
        self.rep_count.setObjectName(_fromUtf8("rep_count"))
        self.verticalLayout_1.addWidget(self.rep_count)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacerItem)
        self.CancelButton = QtGui.QPushButton(AddData)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.verticalLayout_1.addWidget(self.CancelButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_1)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(AddData)
        QtCore.QMetaObject.connectSlotsByName(AddData)

    def retranslateUi(self, AddData):
        AddData.setWindowTitle(_translate("AddData", "Dialog", None))
        self.label.setText(_translate("AddData", "Substrate concentrations:", None))
        self.label_2.setText(_translate("AddData", "Rates:", None))
        self.pushButton.setText(_translate("AddData", "Add replicate", None))
        self.pushButton_2.setText(_translate("AddData", "Done", None))
        self.label_4.setText(_translate("AddData", "Total number of replicates:", None))
        self.rep_count.setText(_translate("AddData", " 0", None))
        self.CancelButton.setText(_translate("AddData", "Cancel", None))

