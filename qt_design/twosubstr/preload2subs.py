# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preload2subs.ui'
#
# Created: Fri May 29 16:34:25 2015
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

class Ui_PreloadTwoSubs(object):
    def setupUi(self, PreloadTwoSubs):
        PreloadTwoSubs.setObjectName(_fromUtf8("PreloadTwoSubs"))
        PreloadTwoSubs.resize(415, 259)
        self.verticalLayout = QtGui.QVBoxLayout(PreloadTwoSubs)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(PreloadTwoSubs)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(PreloadTwoSubs)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.SetAName = QtGui.QLineEdit(PreloadTwoSubs)
        self.SetAName.setObjectName(_fromUtf8("SetAName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.SetAName)
        self.SetBName = QtGui.QLineEdit(PreloadTwoSubs)
        self.SetBName.setObjectName(_fromUtf8("SetBName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.SetBName)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.line = QtGui.QFrame(PreloadTwoSubs)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.IsITC = QtGui.QCheckBox(PreloadTwoSubs)
        self.IsITC.setChecked(True)
        self.IsITC.setObjectName(_fromUtf8("IsITC"))
        self.verticalLayout_2.addWidget(self.IsITC)
        self.ITCSettings = QtGui.QWidget(PreloadTwoSubs)
        self.ITCSettings.setObjectName(_fromUtf8("ITCSettings"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.ITCSettings)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.ITCSettings)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ASpBox = QtGui.QDoubleSpinBox(self.ITCSettings)
        self.ASpBox.setProperty("value", 1.0)
        self.ASpBox.setObjectName(_fromUtf8("ASpBox"))
        self.horizontalLayout.addWidget(self.ASpBox)
        self.SubALab = QtGui.QLabel(self.ITCSettings)
        self.SubALab.setObjectName(_fromUtf8("SubALab"))
        self.horizontalLayout.addWidget(self.SubALab)
        self.label_6 = QtGui.QLabel(self.ITCSettings)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.BSpBox = QtGui.QDoubleSpinBox(self.ITCSettings)
        self.BSpBox.setProperty("value", 1.0)
        self.BSpBox.setObjectName(_fromUtf8("BSpBox"))
        self.horizontalLayout.addWidget(self.BSpBox)
        self.SubBLab = QtGui.QLabel(self.ITCSettings)
        self.SubBLab.setObjectName(_fromUtf8("SubBLab"))
        self.horizontalLayout.addWidget(self.SubBLab)
        self.label_4 = QtGui.QLabel(self.ITCSettings)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.ITCSettings)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line_2 = QtGui.QFrame(PreloadTwoSubs)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(PreloadTwoSubs)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PreloadTwoSubs)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PreloadTwoSubs.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PreloadTwoSubs.reject)
        QtCore.QMetaObject.connectSlotsByName(PreloadTwoSubs)

    def retranslateUi(self, PreloadTwoSubs):
        PreloadTwoSubs.setWindowTitle(_translate("PreloadTwoSubs", "Dialog", None))
        self.label.setText(_translate("PreloadTwoSubs", "Substrate A name:", None))
        self.label_2.setText(_translate("PreloadTwoSubs", "Substrate B name:", None))
        self.SetAName.setText(_translate("PreloadTwoSubs", "SubsA", None))
        self.SetBName.setText(_translate("PreloadTwoSubs", "SubsB", None))
        self.IsITC.setText(_translate("PreloadTwoSubs", "ITC project", None))
        self.label_3.setText(_translate("PreloadTwoSubs", "Reaction stoichiometry:", None))
        self.SubALab.setText(_translate("PreloadTwoSubs", "SubsA", None))
        self.label_6.setText(_translate("PreloadTwoSubs", "+", None))
        self.SubBLab.setText(_translate("PreloadTwoSubs", "SubsB", None))
        self.label_4.setText(_translate("PreloadTwoSubs", "= Products", None))

