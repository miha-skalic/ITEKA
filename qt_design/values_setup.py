# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'values_setup.ui'
#
# Created: Wed May 20 10:19:33 2015
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

class Ui_ValueSetup(object):
    def setupUi(self, ValueSetup):
        ValueSetup.setObjectName(_fromUtf8("ValueSetup"))
        ValueSetup.resize(779, 402)
        self.verticalLayout = QtGui.QVBoxLayout(ValueSetup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(ValueSetup)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.line_3 = QtGui.QFrame(self.tab)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_3)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.Mestkm = QtGui.QDoubleSpinBox(self.tab)
        self.Mestkm.setDecimals(4)
        self.Mestkm.setMaximum(10000.0)
        self.Mestkm.setProperty("value", 1.0)
        self.Mestkm.setObjectName(_fromUtf8("Mestkm"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.Mestkm)
        self.Mestvmax = QtGui.QDoubleSpinBox(self.tab)
        self.Mestvmax.setDecimals(4)
        self.Mestvmax.setMaximum(1000.99)
        self.Mestvmax.setProperty("value", 1.0)
        self.Mestvmax.setObjectName(_fromUtf8("Mestvmax"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.Mestvmax)
        self.horizontalLayout_2.addLayout(self.formLayout_3)
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.line_4 = QtGui.QFrame(self.tab)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_4)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.Mminkm = QtGui.QDoubleSpinBox(self.tab)
        self.Mminkm.setDecimals(4)
        self.Mminkm.setObjectName(_fromUtf8("Mminkm"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.Mminkm)
        self.Mminvmax = QtGui.QDoubleSpinBox(self.tab)
        self.Mminvmax.setDecimals(4)
        self.Mminvmax.setObjectName(_fromUtf8("Mminvmax"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.Mminvmax)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.line_2 = QtGui.QFrame(self.tab)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_8)
        self.line_5 = QtGui.QFrame(self.tab)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_5)
        self.Mmaxkm = QtGui.QDoubleSpinBox(self.tab)
        self.Mmaxkm.setDecimals(4)
        self.Mmaxkm.setProperty("value", 99.99)
        self.Mmaxkm.setObjectName(_fromUtf8("Mmaxkm"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.Mmaxkm)
        self.Mmaxvmax = QtGui.QDoubleSpinBox(self.tab)
        self.Mmaxvmax.setDecimals(4)
        self.Mmaxvmax.setProperty("value", 99.99)
        self.Mmaxvmax.setObjectName(_fromUtf8("Mmaxvmax"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.Mmaxvmax)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_13)
        self.line_8 = QtGui.QFrame(self.tab_2)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_8)
        self.label_16 = QtGui.QLabel(self.tab_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_16)
        self.label_17 = QtGui.QLabel(self.tab_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_17)
        self.Hestkh = QtGui.QDoubleSpinBox(self.tab_2)
        self.Hestkh.setDecimals(4)
        self.Hestkh.setProperty("value", 1.0)
        self.Hestkh.setObjectName(_fromUtf8("Hestkh"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.Hestkh)
        self.Hestvmax = QtGui.QDoubleSpinBox(self.tab_2)
        self.Hestvmax.setDecimals(4)
        self.Hestvmax.setProperty("value", 1.0)
        self.Hestvmax.setObjectName(_fromUtf8("Hestvmax"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.Hestvmax)
        self.Hestn = QtGui.QDoubleSpinBox(self.tab_2)
        self.Hestn.setDecimals(4)
        self.Hestn.setProperty("value", 1.0)
        self.Hestn.setObjectName(_fromUtf8("Hestn"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.Hestn)
        self.horizontalLayout_4.addLayout(self.formLayout_4)
        self.line_7 = QtGui.QFrame(self.tab_2)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout_4.addWidget(self.line_7)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_14)
        self.line_9 = QtGui.QFrame(self.tab_2)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_9)
        self.label_18 = QtGui.QLabel(self.tab_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_18)
        self.label_19 = QtGui.QLabel(self.tab_2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_19)
        self.Hminkh = QtGui.QDoubleSpinBox(self.tab_2)
        self.Hminkh.setDecimals(4)
        self.Hminkh.setObjectName(_fromUtf8("Hminkh"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.Hminkh)
        self.HminVmax = QtGui.QDoubleSpinBox(self.tab_2)
        self.HminVmax.setDecimals(4)
        self.HminVmax.setObjectName(_fromUtf8("HminVmax"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.FieldRole, self.HminVmax)
        self.Hminn = QtGui.QDoubleSpinBox(self.tab_2)
        self.Hminn.setDecimals(4)
        self.Hminn.setMaximum(6.99)
        self.Hminn.setObjectName(_fromUtf8("Hminn"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.FieldRole, self.Hminn)
        self.horizontalLayout_4.addLayout(self.formLayout_6)
        self.line_6 = QtGui.QFrame(self.tab_2)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout_4.addWidget(self.line_6)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_15)
        self.label_20 = QtGui.QLabel(self.tab_2)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_20)
        self.Hmaxkh = QtGui.QDoubleSpinBox(self.tab_2)
        self.Hmaxkh.setDecimals(4)
        self.Hmaxkh.setProperty("value", 99.99)
        self.Hmaxkh.setObjectName(_fromUtf8("Hmaxkh"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.Hmaxkh)
        self.label_21 = QtGui.QLabel(self.tab_2)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_21)
        self.Hmaxvmax = QtGui.QDoubleSpinBox(self.tab_2)
        self.Hmaxvmax.setDecimals(4)
        self.Hmaxvmax.setProperty("value", 99.99)
        self.Hmaxvmax.setObjectName(_fromUtf8("Hmaxvmax"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.FieldRole, self.Hmaxvmax)
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_11)
        self.Hmaxn = QtGui.QDoubleSpinBox(self.tab_2)
        self.Hmaxn.setDecimals(4)
        self.Hmaxn.setMaximum(99.99)
        self.Hmaxn.setProperty("value", 80.99)
        self.Hmaxn.setObjectName(_fromUtf8("Hmaxn"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.Hmaxn)
        self.line_10 = QtGui.QFrame(self.tab_2)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_10)
        self.horizontalLayout_4.addLayout(self.formLayout_5)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(ValueSetup)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ValueSetup)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ValueSetup.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ValueSetup.reject)
        QtCore.QMetaObject.connectSlotsByName(ValueSetup)

    def retranslateUi(self, ValueSetup):
        ValueSetup.setWindowTitle(_translate("ValueSetup", "Dialog", None))
        self.label.setText(_translate("ValueSetup", "Initial estimate", None))
        self.label_4.setText(_translate("ValueSetup", "Km", None))
        self.label_5.setText(_translate("ValueSetup", "Vmax", None))
        self.label_2.setText(_translate("ValueSetup", "Minimum", None))
        self.label_6.setText(_translate("ValueSetup", "Km", None))
        self.label_7.setText(_translate("ValueSetup", "Vmax", None))
        self.label_3.setText(_translate("ValueSetup", "Maximum", None))
        self.label_8.setText(_translate("ValueSetup", "Km", None))
        self.label_9.setText(_translate("ValueSetup", "Vmax", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ValueSetup", "Michaelis–Menten kinetics", None))
        self.label_10.setText(_translate("ValueSetup", "Initial estimate", None))
        self.label_13.setText(_translate("ValueSetup", "Kh", None))
        self.label_16.setText(_translate("ValueSetup", "Vmax", None))
        self.label_17.setText(_translate("ValueSetup", "n", None))
        self.label_12.setText(_translate("ValueSetup", "Minimum", None))
        self.label_14.setText(_translate("ValueSetup", "Kh", None))
        self.label_18.setText(_translate("ValueSetup", "Vmax", None))
        self.label_19.setText(_translate("ValueSetup", "n", None))
        self.label_15.setText(_translate("ValueSetup", "Maximum", None))
        self.label_20.setText(_translate("ValueSetup", "Kh", None))
        self.label_21.setText(_translate("ValueSetup", "Vmax", None))
        self.label_11.setText(_translate("ValueSetup", "n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ValueSetup", "Hills kinetics", None))
