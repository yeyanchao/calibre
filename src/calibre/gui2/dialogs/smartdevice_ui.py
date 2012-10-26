# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/dialogs/smartdevice.ui'
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
        Dialog.resize(612, 226)
        Dialog.setWindowTitle(_("Smart device control"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("devices/tablet.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridlayout = QtGui.QGridLayout(Dialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.msg = QtGui.QLabel(Dialog)
        self.msg.setMinimumSize(QtCore.QSize(600, 0))
        self.msg.setStyleSheet(_fromUtf8("QLabel { margin-bottom: 1ex; }"))
        self.msg.setText(_("<p>Start wireless device connections. Currently used only\n"
"       by <a href=\"http://www.multipie.co.uk/calibre-companion/\">Calibre Companion</a>.\n"
"       <p>You may see some messages from your computer\'s firewall or anti-virus manager asking you if it is OK for calibre to connect to the network. <b>Please answer yes</b>. If you do not, wireless connections will not work."))
        self.msg.setWordWrap(True)
        self.msg.setOpenExternalLinks(True)
        self.msg.setObjectName(_fromUtf8("msg"))
        self.gridlayout.addWidget(self.msg, 0, 0, 1, 3)
        self.label_23 = QtGui.QLabel(Dialog)
        self.label_23.setText(_("Calibre IP addresses:"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridlayout.addWidget(self.label_23, 1, 0, 1, 1)
        self.ip_addresses = QtGui.QLabel(Dialog)
        self.ip_addresses.setText(_("Possibe IP addresses:"))
        self.ip_addresses.setWordWrap(True)
        self.ip_addresses.setObjectName(_fromUtf8("ip_addresses"))
        self.gridlayout.addWidget(self.ip_addresses, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setText(_("Optional &password:"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.password_box = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_box.sizePolicy().hasHeightForWidth())
        self.password_box.setSizePolicy(sizePolicy)
        self.password_box.setEchoMode(QtGui.QLineEdit.Password)
        self.password_box.setPlaceholderText(_("Optional password for security"))
        self.password_box.setObjectName(_fromUtf8("password_box"))
        self.gridlayout.addWidget(self.password_box, 2, 1, 1, 1)
        self.show_password = QtGui.QCheckBox(Dialog)
        self.show_password.setText(_("&Show password"))
        self.show_password.setObjectName(_fromUtf8("show_password"))
        self.gridlayout.addWidget(self.show_password, 2, 2, 1, 1)
        self.label_21 = QtGui.QLabel(Dialog)
        self.label_21.setText(_("Optional &fixed port:"))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridlayout.addWidget(self.label_21, 4, 0, 1, 1)
        self.fixed_port = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixed_port.sizePolicy().hasHeightForWidth())
        self.fixed_port.setSizePolicy(sizePolicy)
        self.fixed_port.setPlaceholderText(_("Optional port number"))
        self.fixed_port.setObjectName(_fromUtf8("fixed_port"))
        self.gridlayout.addWidget(self.fixed_port, 4, 1, 1, 1)
        self.use_fixed_port = QtGui.QCheckBox(Dialog)
        self.use_fixed_port.setText(_("&Use a fixed port"))
        self.use_fixed_port.setObjectName(_fromUtf8("use_fixed_port"))
        self.gridlayout.addWidget(self.use_fixed_port, 4, 2, 1, 1)
        self.autostart_box = QtGui.QCheckBox(Dialog)
        self.autostart_box.setText(_("&Automatically allow connections at calibre startup"))
        self.autostart_box.setObjectName(_fromUtf8("autostart_box"))
        self.gridlayout.addWidget(self.autostart_box, 6, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 10, 0, 1, 3)
        self.label_2.setBuddy(self.password_box)
        self.label_21.setBuddy(self.fixed_port)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass


