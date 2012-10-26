# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/dialogs/search_item.ui'
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
        Form.resize(400, 39)
        Form.setWindowTitle(_("Form"))
        self.hboxlayout = QtGui.QHBoxLayout(Form)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.field = QtGui.QComboBox(Form)
        self.field.setObjectName(_fromUtf8("field"))
        self.hboxlayout.addWidget(self.field)
        self.label = QtGui.QLabel(Form)
        self.label.setText(_("contains"))
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.text = QtGui.QLineEdit(Form)
        self.text.setToolTip(_("The text to search for. It is interpreted as a regular expression."))
        self.text.setObjectName(_fromUtf8("text"))
        self.hboxlayout.addWidget(self.text)
        self.negate = QtGui.QCheckBox(Form)
        self.negate.setToolTip(_("<p>Negate this match. That is, only return results that <b>do not</b> match this query."))
        self.negate.setText(_("Negate"))
        self.negate.setObjectName(_fromUtf8("negate"))
        self.hboxlayout.addWidget(self.negate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

