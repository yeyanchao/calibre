# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/store/basic_config_widget.ui'
#
# Created: Thu Oct 25 16:54:55 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(460, 69)
        Form.setWindowTitle(_("Form"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setText(_("Added Tags:"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.tags = QtGui.QLineEdit(Form)
        self.tags.setObjectName(_fromUtf8("tags"))
        self.gridLayout.addWidget(self.tags, 1, 1, 1, 1)
        self.open_external = QtGui.QCheckBox(Form)
        self.open_external.setText(_("Open store in external web browswer"))
        self.open_external.setObjectName(_fromUtf8("open_external"))
        self.gridLayout.addWidget(self.open_external, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

