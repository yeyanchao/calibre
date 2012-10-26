# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/convert/debug.ui'
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
        Form.resize(436, 382)
        Form.setWindowTitle(_("Form"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setText(_("Choose a folder to put the debug output into. If you specify a folder, calibre will place a lot of debug output into it. This will be useful in understanding the conversion process and figuring out the correct values for conversion parameters like Table of Contents and Chapter Detection."))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.opt_debug_pipeline = QtGui.QLineEdit(Form)
        self.opt_debug_pipeline.setReadOnly(True)
        self.opt_debug_pipeline.setObjectName(_fromUtf8("opt_debug_pipeline"))
        self.gridLayout.addWidget(self.opt_debug_pipeline, 1, 0, 1, 1)
        self.button_debug_dir = QtGui.QToolButton(Form)
        self.button_debug_dir.setToolTip(_("Choose debug folder"))
        self.button_debug_dir.setText(_("..."))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("document_open.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_debug_dir.setIcon(icon)
        self.button_debug_dir.setObjectName(_fromUtf8("button_debug_dir"))
        self.gridLayout.addWidget(self.button_debug_dir, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.button_clear = QtGui.QToolButton(Form)
        self.button_clear.setText(_("..."))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("clear_left.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_clear.setIcon(icon1)
        self.button_clear.setObjectName(_fromUtf8("button_clear"))
        self.gridLayout.addWidget(self.button_clear, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setText(_("The debug process outputs the intermediate HTML generated at various stages of the conversion process. This HTML can sometimes serve as a good starting point for hand editing a conversion."))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass


