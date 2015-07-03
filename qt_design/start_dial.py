# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_dial.ui'
#
# Created: Wed Jun 17 14:13:17 2015
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

class Ui_start_dial(object):
    def setupUi(self, start_dial):
        start_dial.setObjectName(_fromUtf8("start_dial"))
        start_dial.resize(434, 293)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(start_dial)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(start_dial)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ProjectName = QtGui.QLineEdit(start_dial)
        self.ProjectName.setText(_fromUtf8(""))
        self.ProjectName.setObjectName(_fromUtf8("ProjectName"))
        self.horizontalLayout_2.addWidget(self.ProjectName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(start_dial)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.radioButton = QtGui.QRadioButton(start_dial)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.buttonGroup_2 = QtGui.QButtonGroup(start_dial)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(start_dial)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.buttonGroup_2.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.line = QtGui.QFrame(start_dial)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(start_dial)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(start_dial)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(start_dial)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.TimeVal = QtGui.QLineEdit(start_dial)
        self.TimeVal.setObjectName(_fromUtf8("TimeVal"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.TimeVal)
        self.ConcVal = QtGui.QLineEdit(start_dial)
        self.ConcVal.setObjectName(_fromUtf8("ConcVal"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.ConcVal)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(start_dial)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(start_dial)
        QtCore.QMetaObject.connectSlotsByName(start_dial)

    def retranslateUi(self, start_dial):
        start_dial.setWindowTitle(_translate("start_dial", "Dialog", None))
        self.label_2.setText(_translate("start_dial", "Project Name:", None))
        self.label.setText(_translate("start_dial", "Number of substrates:", None))
        self.radioButton.setText(_translate("start_dial", "1 substrate", None))
        self.radioButton_2.setText(_translate("start_dial", "2 substrates", None))
        self.label_3.setText(_translate("start_dial", "time:", None))
        self.label_4.setText(_translate("start_dial", "Concentration:", None))
        self.label_5.setText(_translate("start_dial", "Units", None))
        self.TimeVal.setText(_translate("start_dial", "s", None))
        self.ConcVal.setText(_translate("start_dial", "mM", None))

