# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataview.ui'
#
# Created: Tue Jun 16 16:51:52 2015
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

class Ui_PointsView(object):
    def setupUi(self, PointsView):
        PointsView.setObjectName(_fromUtf8("PointsView"))
        PointsView.resize(1078, 763)
        self.verticalLayout_2 = QtGui.QVBoxLayout(PointsView)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(PointsView)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(PointsView)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(PointsView)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.VarBox = QtGui.QComboBox(PointsView)
        self.VarBox.setObjectName(_fromUtf8("VarBox"))
        self.gridLayout.addWidget(self.VarBox, 0, 1, 1, 1)
        self.SetBox = QtGui.QComboBox(PointsView)
        self.SetBox.setObjectName(_fromUtf8("SetBox"))
        self.gridLayout.addWidget(self.SetBox, 1, 1, 1, 1)
        self.RepBox = QtGui.QComboBox(PointsView)
        self.RepBox.setObjectName(_fromUtf8("RepBox"))
        self.gridLayout.addWidget(self.RepBox, 2, 1, 1, 1)
        self.DelBut = QtGui.QPushButton(PointsView)
        self.DelBut.setObjectName(_fromUtf8("DelBut"))
        self.gridLayout.addWidget(self.DelBut, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(1600, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(PointsView)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(PointsView)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PointsView.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PointsView.reject)
        QtCore.QMetaObject.connectSlotsByName(PointsView)

    def retranslateUi(self, PointsView):
        PointsView.setWindowTitle(_translate("PointsView", "Dialog", None))
        self.label_2.setText(_translate("PointsView", "Set", None))
        self.label.setText(_translate("PointsView", "Variable substrate", None))
        self.label_3.setText(_translate("PointsView", "Replicate", None))
        self.DelBut.setText(_translate("PointsView", "Delete replicate", None))

