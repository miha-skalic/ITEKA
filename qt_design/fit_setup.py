# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fit_setup.ui'
#
# Created: Tue Jun 16 11:18:25 2015
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

class Ui_FitSetup(object):
    def setupUi(self, FitSetup):
        FitSetup.setObjectName(_fromUtf8("FitSetup"))
        FitSetup.resize(778, 349)
        self.verticalLayout = QtGui.QVBoxLayout(FitSetup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lab13 = QtGui.QLabel(FitSetup)
        self.lab13.setObjectName(_fromUtf8("lab13"))
        self.gridLayout_2.addWidget(self.lab13, 4, 0, 1, 1)
        self.SB11 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB11.setDecimals(4)
        self.SB11.setMaximum(9999999.99)
        self.SB11.setProperty("value", 1.0)
        self.SB11.setObjectName(_fromUtf8("SB11"))
        self.gridLayout_2.addWidget(self.SB11, 2, 1, 1, 1)
        self.lab15 = QtGui.QLabel(FitSetup)
        self.lab15.setObjectName(_fromUtf8("lab15"))
        self.gridLayout_2.addWidget(self.lab15, 6, 0, 1, 1)
        self.lab14 = QtGui.QLabel(FitSetup)
        self.lab14.setObjectName(_fromUtf8("lab14"))
        self.gridLayout_2.addWidget(self.lab14, 5, 0, 1, 1)
        self.lab12 = QtGui.QLabel(FitSetup)
        self.lab12.setObjectName(_fromUtf8("lab12"))
        self.gridLayout_2.addWidget(self.lab12, 3, 0, 1, 1)
        self.SB14 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB14.setDecimals(4)
        self.SB14.setMaximum(9999999.99)
        self.SB14.setProperty("value", 1.0)
        self.SB14.setObjectName(_fromUtf8("SB14"))
        self.gridLayout_2.addWidget(self.SB14, 5, 1, 1, 1)
        self.SB12 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB12.setDecimals(4)
        self.SB12.setMaximum(9999999.99)
        self.SB12.setProperty("value", 1.0)
        self.SB12.setObjectName(_fromUtf8("SB12"))
        self.gridLayout_2.addWidget(self.SB12, 3, 1, 1, 1)
        self.SB13 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB13.setDecimals(4)
        self.SB13.setMaximum(9999999.99)
        self.SB13.setProperty("value", 1.0)
        self.SB13.setObjectName(_fromUtf8("SB13"))
        self.gridLayout_2.addWidget(self.SB13, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 3, 1, 1)
        self.label = QtGui.QLabel(FitSetup)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.line_3 = QtGui.QFrame(FitSetup)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 1, 1, 1, 1)
        self.lab11 = QtGui.QLabel(FitSetup)
        self.lab11.setObjectName(_fromUtf8("lab11"))
        self.gridLayout_2.addWidget(self.lab11, 2, 0, 1, 1)
        self.lab16 = QtGui.QLabel(FitSetup)
        self.lab16.setObjectName(_fromUtf8("lab16"))
        self.gridLayout_2.addWidget(self.lab16, 7, 0, 1, 1)
        self.SB15 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB15.setDecimals(4)
        self.SB15.setMaximum(9999999.99)
        self.SB15.setProperty("value", 1.0)
        self.SB15.setObjectName(_fromUtf8("SB15"))
        self.gridLayout_2.addWidget(self.SB15, 6, 1, 1, 1)
        self.SB16 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB16.setDecimals(4)
        self.SB16.setMaximum(9999999.99)
        self.SB16.setProperty("value", 1.0)
        self.SB16.setObjectName(_fromUtf8("SB16"))
        self.gridLayout_2.addWidget(self.SB16, 7, 1, 1, 1)
        self.CB2 = QtGui.QCheckBox(FitSetup)
        self.CB2.setObjectName(_fromUtf8("CB2"))
        self.gridLayout_2.addWidget(self.CB2, 3, 2, 1, 1)
        self.CB1 = QtGui.QCheckBox(FitSetup)
        self.CB1.setObjectName(_fromUtf8("CB1"))
        self.gridLayout_2.addWidget(self.CB1, 2, 2, 1, 1)
        self.CB3 = QtGui.QCheckBox(FitSetup)
        self.CB3.setObjectName(_fromUtf8("CB3"))
        self.gridLayout_2.addWidget(self.CB3, 4, 2, 1, 1)
        self.CB4 = QtGui.QCheckBox(FitSetup)
        self.CB4.setObjectName(_fromUtf8("CB4"))
        self.gridLayout_2.addWidget(self.CB4, 5, 2, 1, 1)
        self.CB5 = QtGui.QCheckBox(FitSetup)
        self.CB5.setObjectName(_fromUtf8("CB5"))
        self.gridLayout_2.addWidget(self.CB5, 6, 2, 1, 1)
        self.CB6 = QtGui.QCheckBox(FitSetup)
        self.CB6.setObjectName(_fromUtf8("CB6"))
        self.gridLayout_2.addWidget(self.CB6, 7, 2, 1, 1)
        self.line_5 = QtGui.QFrame(FitSetup)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout_2.addWidget(self.line_5, 1, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.line = QtGui.QFrame(FitSetup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lab25 = QtGui.QLabel(FitSetup)
        self.lab25.setObjectName(_fromUtf8("lab25"))
        self.gridLayout_4.addWidget(self.lab25, 6, 0, 1, 1)
        self.lab23 = QtGui.QLabel(FitSetup)
        self.lab23.setObjectName(_fromUtf8("lab23"))
        self.gridLayout_4.addWidget(self.lab23, 4, 0, 1, 1)
        self.lab24 = QtGui.QLabel(FitSetup)
        self.lab24.setObjectName(_fromUtf8("lab24"))
        self.gridLayout_4.addWidget(self.lab24, 5, 0, 1, 1)
        self.SB23 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB23.setDecimals(4)
        self.SB23.setMaximum(9999999.99)
        self.SB23.setObjectName(_fromUtf8("SB23"))
        self.gridLayout_4.addWidget(self.SB23, 4, 1, 1, 1)
        self.SB22 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB22.setDecimals(4)
        self.SB22.setMaximum(9999999.99)
        self.SB22.setObjectName(_fromUtf8("SB22"))
        self.gridLayout_4.addWidget(self.SB22, 3, 1, 1, 1)
        self.SB24 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB24.setDecimals(4)
        self.SB24.setMaximum(9999999.99)
        self.SB24.setObjectName(_fromUtf8("SB24"))
        self.gridLayout_4.addWidget(self.SB24, 5, 1, 1, 1)
        self.line_4 = QtGui.QFrame(FitSetup)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_4.addWidget(self.line_4, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(FitSetup)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.LBSet = QtGui.QCheckBox(FitSetup)
        self.LBSet.setChecked(True)
        self.LBSet.setObjectName(_fromUtf8("LBSet"))
        self.gridLayout_4.addWidget(self.LBSet, 0, 1, 1, 1)
        self.lab21 = QtGui.QLabel(FitSetup)
        self.lab21.setObjectName(_fromUtf8("lab21"))
        self.gridLayout_4.addWidget(self.lab21, 2, 0, 1, 1)
        self.SB25 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB25.setDecimals(4)
        self.SB25.setMaximum(9999999.99)
        self.SB25.setObjectName(_fromUtf8("SB25"))
        self.gridLayout_4.addWidget(self.SB25, 6, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 3, 2, 1, 1)
        self.SB21 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB21.setDecimals(4)
        self.SB21.setMaximum(9999999.99)
        self.SB21.setObjectName(_fromUtf8("SB21"))
        self.gridLayout_4.addWidget(self.SB21, 2, 1, 1, 1)
        self.lab22 = QtGui.QLabel(FitSetup)
        self.lab22.setObjectName(_fromUtf8("lab22"))
        self.gridLayout_4.addWidget(self.lab22, 3, 0, 1, 1)
        self.lab26 = QtGui.QLabel(FitSetup)
        self.lab26.setObjectName(_fromUtf8("lab26"))
        self.gridLayout_4.addWidget(self.lab26, 7, 0, 1, 1)
        self.SB26 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB26.setDecimals(4)
        self.SB26.setMaximum(9999999.99)
        self.SB26.setObjectName(_fromUtf8("SB26"))
        self.gridLayout_4.addWidget(self.SB26, 7, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_4)
        self.line_2 = QtGui.QFrame(FitSetup)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.line_7 = QtGui.QFrame(FitSetup)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout_3.addWidget(self.line_7, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 3, 2, 1, 1)
        self.lab35 = QtGui.QLabel(FitSetup)
        self.lab35.setObjectName(_fromUtf8("lab35"))
        self.gridLayout_3.addWidget(self.lab35, 6, 0, 1, 1)
        self.SB35 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB35.setDecimals(4)
        self.SB35.setMaximum(9999999.99)
        self.SB35.setProperty("value", 99.0)
        self.SB35.setObjectName(_fromUtf8("SB35"))
        self.gridLayout_3.addWidget(self.SB35, 6, 1, 1, 1)
        self.UBSet = QtGui.QCheckBox(FitSetup)
        self.UBSet.setChecked(True)
        self.UBSet.setObjectName(_fromUtf8("UBSet"))
        self.gridLayout_3.addWidget(self.UBSet, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(FitSetup)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.lab31 = QtGui.QLabel(FitSetup)
        self.lab31.setObjectName(_fromUtf8("lab31"))
        self.gridLayout_3.addWidget(self.lab31, 2, 0, 1, 1)
        self.SB32 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB32.setDecimals(4)
        self.SB32.setMaximum(9999999.99)
        self.SB32.setProperty("value", 99.99)
        self.SB32.setObjectName(_fromUtf8("SB32"))
        self.gridLayout_3.addWidget(self.SB32, 3, 1, 1, 1)
        self.SB34 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB34.setDecimals(4)
        self.SB34.setMaximum(9999999.99)
        self.SB34.setProperty("value", 99.0)
        self.SB34.setObjectName(_fromUtf8("SB34"))
        self.gridLayout_3.addWidget(self.SB34, 5, 1, 1, 1)
        self.lab34 = QtGui.QLabel(FitSetup)
        self.lab34.setObjectName(_fromUtf8("lab34"))
        self.gridLayout_3.addWidget(self.lab34, 5, 0, 1, 1)
        self.lab32 = QtGui.QLabel(FitSetup)
        self.lab32.setObjectName(_fromUtf8("lab32"))
        self.gridLayout_3.addWidget(self.lab32, 3, 0, 1, 1)
        self.lab33 = QtGui.QLabel(FitSetup)
        self.lab33.setObjectName(_fromUtf8("lab33"))
        self.gridLayout_3.addWidget(self.lab33, 4, 0, 1, 1)
        self.SB31 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB31.setDecimals(4)
        self.SB31.setMaximum(9999999.99)
        self.SB31.setProperty("value", 99.99)
        self.SB31.setObjectName(_fromUtf8("SB31"))
        self.gridLayout_3.addWidget(self.SB31, 2, 1, 1, 1)
        self.SB33 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB33.setDecimals(4)
        self.SB33.setMaximum(9999999.99)
        self.SB33.setProperty("value", 99.0)
        self.SB33.setObjectName(_fromUtf8("SB33"))
        self.gridLayout_3.addWidget(self.SB33, 4, 1, 1, 1)
        self.lab36 = QtGui.QLabel(FitSetup)
        self.lab36.setObjectName(_fromUtf8("lab36"))
        self.gridLayout_3.addWidget(self.lab36, 7, 0, 1, 1)
        self.SB36 = QtGui.QDoubleSpinBox(FitSetup)
        self.SB36.setDecimals(4)
        self.SB36.setMaximum(9999999.99)
        self.SB36.setProperty("value", 99.0)
        self.SB36.setObjectName(_fromUtf8("SB36"))
        self.gridLayout_3.addWidget(self.SB36, 7, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_6 = QtGui.QFrame(FitSetup)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(FitSetup)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.InicN = QtGui.QSpinBox(FitSetup)
        self.InicN.setMinimum(0)
        self.InicN.setMaximum(9999)
        self.InicN.setProperty("value", 0)
        self.InicN.setObjectName(_fromUtf8("InicN"))
        self.gridLayout.addWidget(self.InicN, 1, 1, 1, 1)
        self.InclRand = QtGui.QCheckBox(FitSetup)
        self.InclRand.setEnabled(True)
        self.InclRand.setChecked(False)
        self.InclRand.setObjectName(_fromUtf8("InclRand"))
        self.gridLayout.addWidget(self.InclRand, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(FitSetup)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FitSetup)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FitSetup.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FitSetup.reject)
        QtCore.QMetaObject.connectSlotsByName(FitSetup)

    def retranslateUi(self, FitSetup):
        FitSetup.setWindowTitle(_translate("FitSetup", "Dialog", None))
        self.lab13.setText(_translate("FitSetup", "TextLabel", None))
        self.lab15.setText(_translate("FitSetup", "TextLabel", None))
        self.lab14.setText(_translate("FitSetup", "TextLabel", None))
        self.lab12.setText(_translate("FitSetup", "Vmax", None))
        self.label.setText(_translate("FitSetup", "Initial estimate", None))
        self.lab11.setText(_translate("FitSetup", "Km", None))
        self.lab16.setText(_translate("FitSetup", "TextLabel", None))
        self.CB2.setText(_translate("FitSetup", "Lock Value", None))
        self.CB1.setText(_translate("FitSetup", "Lock Value", None))
        self.CB3.setText(_translate("FitSetup", "Lock Value", None))
        self.CB4.setText(_translate("FitSetup", "Lock Value", None))
        self.CB5.setText(_translate("FitSetup", "Lock Value", None))
        self.CB6.setText(_translate("FitSetup", "Lock Value", None))
        self.lab25.setText(_translate("FitSetup", "TextLabel", None))
        self.lab23.setText(_translate("FitSetup", "TextLabel", None))
        self.lab24.setText(_translate("FitSetup", "TextLabel", None))
        self.label_2.setText(_translate("FitSetup", "Minimum", None))
        self.LBSet.setText(_translate("FitSetup", "Use lower bounds", None))
        self.lab21.setText(_translate("FitSetup", "Km", None))
        self.lab22.setText(_translate("FitSetup", "Vmax", None))
        self.lab26.setText(_translate("FitSetup", "TextLabel", None))
        self.lab35.setText(_translate("FitSetup", "TextLabel", None))
        self.UBSet.setText(_translate("FitSetup", "Use upper bounds", None))
        self.label_3.setText(_translate("FitSetup", "Maximum", None))
        self.lab31.setText(_translate("FitSetup", "Km", None))
        self.lab34.setText(_translate("FitSetup", "TextLabel", None))
        self.lab32.setText(_translate("FitSetup", "Vmax", None))
        self.lab33.setText(_translate("FitSetup", "TextLabel", None))
        self.lab36.setText(_translate("FitSetup", "TextLabel", None))
        self.label_4.setText(_translate("FitSetup", "Number of Inicializations:", None))
        self.InclRand.setText(_translate("FitSetup", "Include random inicialization", None))

