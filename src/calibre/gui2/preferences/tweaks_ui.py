# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/preferences/tweaks.ui'
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
        Form.resize(756, 531)
        Form.setWindowTitle(_("Form"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_18 = QtGui.QLabel(Form)
        self.label_18.setText(_("Values for the tweaks are shown below. Edit them to change the behavior of calibre. Your changes will only take effect <b>after a restart</b> of calibre."))
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_4.addWidget(self.label_18)
        self.splitter = QtGui.QSplitter(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tweaks_view = QtGui.QListView(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tweaks_view.sizePolicy().hasHeightForWidth())
        self.tweaks_view.setSizePolicy(sizePolicy)
        self.tweaks_view.setMinimumSize(QtCore.QSize(300, 0))
        self.tweaks_view.setAlternatingRowColors(True)
        self.tweaks_view.setSpacing(5)
        self.tweaks_view.setUniformItemSizes(True)
        self.tweaks_view.setObjectName(_fromUtf8("tweaks_view"))
        self.verticalLayout_2.addWidget(self.tweaks_view)
        self.plugin_tweaks_button = QtGui.QPushButton(self.layoutWidget)
        self.plugin_tweaks_button.setToolTip(_("Edit tweaks for any custom plugins you have installed"))
        self.plugin_tweaks_button.setText(_("&Plugin tweaks"))
        self.plugin_tweaks_button.setObjectName(_fromUtf8("plugin_tweaks_button"))
        self.verticalLayout_2.addWidget(self.plugin_tweaks_button)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.layoutWidget1)
        self.groupBox.setTitle(_("Help"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.help = QtGui.QPlainTextEdit(self.groupBox)
        self.help.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.help.setReadOnly(True)
        self.help.setObjectName(_fromUtf8("help"))
        self.verticalLayout.addWidget(self.help)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 3)
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget1)
        self.groupBox_2.setTitle(_("Edit tweak"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.edit_tweak = QtGui.QPlainTextEdit(self.groupBox_2)
        self.edit_tweak.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.edit_tweak.setObjectName(_fromUtf8("edit_tweak"))
        self.gridLayout.addWidget(self.edit_tweak, 0, 0, 1, 2)
        self.restore_default_button = QtGui.QPushButton(self.groupBox_2)
        self.restore_default_button.setToolTip(_("Restore this tweak to its default value"))
        self.restore_default_button.setText(_("Restore &default"))
        self.restore_default_button.setObjectName(_fromUtf8("restore_default_button"))
        self.gridLayout.addWidget(self.restore_default_button, 1, 0, 1, 1)
        self.apply_button = QtGui.QPushButton(self.groupBox_2)
        self.apply_button.setToolTip(_("Apply any changes you made to this tweak"))
        self.apply_button.setText(_("&Apply"))
        self.apply_button.setObjectName(_fromUtf8("apply_button"))
        self.gridLayout.addWidget(self.apply_button, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 3)
        self.search = SearchBox2(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.search.setMinimumContentsLength(10)
        self.search.setObjectName(_fromUtf8("search"))
        self.gridLayout_3.addWidget(self.search, 0, 0, 1, 1)
        self.next_button = QtGui.QPushButton(self.layoutWidget1)
        self.next_button.setText(_("&Next"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-down.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.gridLayout_3.addWidget(self.next_button, 0, 1, 1, 1)
        self.previous_button = QtGui.QPushButton(self.layoutWidget1)
        self.previous_button.setText(_("&Previous"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-up.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_button.setIcon(icon1)
        self.previous_button.setObjectName(_fromUtf8("previous_button"))
        self.gridLayout_3.addWidget(self.previous_button, 0, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

from calibre.gui2.search_box import SearchBox2

