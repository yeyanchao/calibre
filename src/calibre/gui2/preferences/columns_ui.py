# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/preferences/columns.ui'
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
        Form.resize(504, 399)
        Form.setWindowTitle(_("Form"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setText(_("Here you can re-arrange the layout of the columns in the calibre library book list. You can hide columns by unchecking them. You can also create your own, custom columns."))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.opt_columns = QtGui.QListWidget(Form)
        self.opt_columns.setAlternatingRowColors(True)
        self.opt_columns.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.opt_columns.setObjectName(_fromUtf8("opt_columns"))
        self.gridLayout.addWidget(self.opt_columns, 1, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.column_up = QtGui.QToolButton(Form)
        self.column_up.setToolTip(_("Move column up"))
        self.column_up.setText(_("..."))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-up.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.column_up.setIcon(icon)
        self.column_up.setIconSize(QtCore.QSize(32, 32))
        self.column_up.setObjectName(_fromUtf8("column_up"))
        self.verticalLayout_3.addWidget(self.column_up)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.del_custcol_button = QtGui.QToolButton(Form)
        self.del_custcol_button.setToolTip(_("Remove a user-defined column"))
        self.del_custcol_button.setText(_("..."))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("trash.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_custcol_button.setIcon(icon1)
        self.del_custcol_button.setIconSize(QtCore.QSize(32, 32))
        self.del_custcol_button.setObjectName(_fromUtf8("del_custcol_button"))
        self.verticalLayout_3.addWidget(self.del_custcol_button)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.add_custcol_button = QtGui.QToolButton(Form)
        self.add_custcol_button.setToolTip(_("Add a user-defined column"))
        self.add_custcol_button.setText(_("..."))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(I("plus.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_custcol_button.setIcon(icon2)
        self.add_custcol_button.setIconSize(QtCore.QSize(32, 32))
        self.add_custcol_button.setObjectName(_fromUtf8("add_custcol_button"))
        self.verticalLayout_3.addWidget(self.add_custcol_button)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.edit_custcol_button = QtGui.QToolButton(Form)
        self.edit_custcol_button.setToolTip(_("Edit settings of a user-defined column"))
        self.edit_custcol_button.setText(_("..."))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(I("edit_input.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_custcol_button.setIcon(icon3)
        self.edit_custcol_button.setIconSize(QtCore.QSize(32, 32))
        self.edit_custcol_button.setObjectName(_fromUtf8("edit_custcol_button"))
        self.verticalLayout_3.addWidget(self.edit_custcol_button)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.column_down = QtGui.QToolButton(Form)
        self.column_down.setToolTip(_("Move column down"))
        self.column_down.setText(_("..."))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-down.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.column_down.setIcon(icon4)
        self.column_down.setIconSize(QtCore.QSize(32, 32))
        self.column_down.setObjectName(_fromUtf8("column_down"))
        self.verticalLayout_3.addWidget(self.column_down)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.add_col_button = QtGui.QPushButton(Form)
        self.add_col_button.setText(_("Add &custom column"))
        self.add_col_button.setObjectName(_fromUtf8("add_col_button"))
        self.gridLayout.addWidget(self.add_col_button, 2, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass


