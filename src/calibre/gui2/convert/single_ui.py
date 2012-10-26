# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/convert/single.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1024, 700)
        Dialog.setWindowTitle(_("Dialog"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("convert.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.input_label = QtGui.QLabel(Dialog)
        self.input_label.setText(_("&Input format:"))
        self.input_label.setObjectName(_fromUtf8("input_label"))
        self.horizontalLayout.addWidget(self.input_label)
        self.input_formats = QtGui.QComboBox(Dialog)
        self.input_formats.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.input_formats.setMinimumContentsLength(5)
        self.input_formats.setObjectName(_fromUtf8("input_formats"))
        self.horizontalLayout.addWidget(self.input_formats)
        self.opt_individual_saved_settings = QtGui.QCheckBox(Dialog)
        self.opt_individual_saved_settings.setText(_("Use &saved conversion settings for individual books"))
        self.opt_individual_saved_settings.setObjectName(_fromUtf8("opt_individual_saved_settings"))
        self.horizontalLayout.addWidget(self.opt_individual_saved_settings)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setText(_("&Output format:"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.output_formats = QtGui.QComboBox(Dialog)
        self.output_formats.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.output_formats.setMinimumContentsLength(5)
        self.output_formats.setObjectName(_fromUtf8("output_formats"))
        self.horizontalLayout.addWidget(self.output_formats)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.groups = QtGui.QListView(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groups.sizePolicy().hasHeightForWidth())
        self.groups.setSizePolicy(sizePolicy)
        self.groups.setTabKeyNavigation(True)
        self.groups.setIconSize(QtCore.QSize(48, 48))
        self.groups.setSpacing(10)
        self.groups.setWordWrap(True)
        self.groups.setObjectName(_fromUtf8("groups"))
        self.gridLayout.addWidget(self.groups, 1, 0, 3, 1)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 810, 494))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.stack = QtGui.QStackedWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.stack.setObjectName(_fromUtf8("stack"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.stack.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stack.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stack)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)
        self.help = QtGui.QTextEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setMaximumSize(QtCore.QSize(16777215, 130))
        self.help.setObjectName(_fromUtf8("help"))
        self.gridLayout.addWidget(self.help, 2, 1, 1, 1)
        self.input_label.setBuddy(self.input_formats)
        self.label_2.setBuddy(self.output_formats)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass


