# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/wizard/send_email.ui'
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
        Form.resize(585, 238)
        Form.setWindowTitle(_("Form"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_15 = QtGui.QLabel(Form)
        self.label_15.setText(_("Send email &from:"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_9.addWidget(self.label_15)
        self.email_from = QtGui.QLineEdit(Form)
        self.email_from.setToolTip(_("<p>This is what will be present in the From: field of emails sent by calibre.<br> Set it to your email address"))
        self.email_from.setObjectName(_fromUtf8("email_from"))
        self.horizontalLayout_9.addWidget(self.email_from)
        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 0, 1, 2)
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setToolTip(_("<p>A mail server is useful if the service you are sending mail to only accepts email from well know mail services."))
        self.groupBox_5.setTitle(_("Mail &Server"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_16 = QtGui.QLabel(self.groupBox_5)
        self.label_16.setText(_("calibre can <b>optionally</b> use a server to send mail"))
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 4)
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setText(_("&Hostname:"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 1, 0, 1, 1)
        self.relay_host = QtGui.QLineEdit(self.groupBox_5)
        self.relay_host.setToolTip(_("The hostname of your mail server. For e.g. smtp.gmail.com"))
        self.relay_host.setObjectName(_fromUtf8("relay_host"))
        self.gridLayout_3.addWidget(self.relay_host, 1, 1, 1, 2)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_18 = QtGui.QLabel(self.groupBox_5)
        self.label_18.setText(_("&Port:"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_11.addWidget(self.label_18)
        self.relay_port = QtGui.QSpinBox(self.groupBox_5)
        self.relay_port.setToolTip(_("The port your mail server listens for connections on. The default is 25"))
        self.relay_port.setMinimum(1)
        self.relay_port.setMaximum(65555)
        self.relay_port.setProperty("value", 25)
        self.relay_port.setObjectName(_fromUtf8("relay_port"))
        self.horizontalLayout_11.addWidget(self.relay_port)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 1, 3, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_5)
        self.label_19.setText(_("&Username:"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_3.addWidget(self.label_19, 2, 0, 1, 1)
        self.relay_username = QtGui.QLineEdit(self.groupBox_5)
        self.relay_username.setToolTip(_("Your username on the mail server"))
        self.relay_username.setObjectName(_fromUtf8("relay_username"))
        self.gridLayout_3.addWidget(self.relay_username, 2, 1, 1, 2)
        self.label_20 = QtGui.QLabel(self.groupBox_5)
        self.label_20.setText(_("&Password:"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 3, 0, 1, 1)
        self.relay_password = QtGui.QLineEdit(self.groupBox_5)
        self.relay_password.setToolTip(_("Your password on the mail server"))
        self.relay_password.setEchoMode(QtGui.QLineEdit.Password)
        self.relay_password.setObjectName(_fromUtf8("relay_password"))
        self.gridLayout_3.addWidget(self.relay_password, 3, 1, 1, 2)
        self.relay_show_password = QtGui.QCheckBox(self.groupBox_5)
        self.relay_show_password.setText(_("&Show"))
        self.relay_show_password.setObjectName(_fromUtf8("relay_show_password"))
        self.gridLayout_3.addWidget(self.relay_show_password, 3, 3, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox_5)
        self.label_21.setText(_("&Encryption:"))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_3.addWidget(self.label_21, 4, 0, 1, 1)
        self.relay_tls = QtGui.QRadioButton(self.groupBox_5)
        self.relay_tls.setToolTip(_("Use TLS encryption when connecting to the mail server. This is the most common."))
        self.relay_tls.setText(_("&TLS"))
        self.relay_tls.setChecked(True)
        self.relay_tls.setObjectName(_fromUtf8("relay_tls"))
        self.gridLayout_3.addWidget(self.relay_tls, 4, 1, 1, 1)
        self.relay_ssl = QtGui.QRadioButton(self.groupBox_5)
        self.relay_ssl.setToolTip(_("Use SSL encryption when connecting to the mail server."))
        self.relay_ssl.setText(_("&SSL"))
        self.relay_ssl.setObjectName(_fromUtf8("relay_ssl"))
        self.gridLayout_3.addWidget(self.relay_ssl, 4, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 4, 1, 1)
        self.relay_none = QtGui.QRadioButton(self.groupBox_5)
        self.relay_none.setToolTip(_("WARNING: Using no encryption is highly insecure"))
        self.relay_none.setText(_("&None"))
        self.relay_none.setObjectName(_fromUtf8("relay_none"))
        self.gridLayout_3.addWidget(self.relay_none, 4, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.relay_use_gmail = QtGui.QToolButton(Form)
        self.relay_use_gmail.setText(_("Use Gmail"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("gmail_logo.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.relay_use_gmail.setIcon(icon)
        self.relay_use_gmail.setIconSize(QtCore.QSize(48, 48))
        self.relay_use_gmail.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.relay_use_gmail.setObjectName(_fromUtf8("relay_use_gmail"))
        self.verticalLayout_9.addWidget(self.relay_use_gmail)
        self.relay_use_hotmail = QtGui.QToolButton(Form)
        self.relay_use_hotmail.setText(_("Use Hotmail"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("hotmail.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.relay_use_hotmail.setIcon(icon1)
        self.relay_use_hotmail.setIconSize(QtCore.QSize(48, 48))
        self.relay_use_hotmail.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.relay_use_hotmail.setObjectName(_fromUtf8("relay_use_hotmail"))
        self.verticalLayout_9.addWidget(self.relay_use_hotmail)
        self.test_email_button = QtGui.QPushButton(Form)
        self.test_email_button.setText(_("&Test email"))
        self.test_email_button.setObjectName(_fromUtf8("test_email_button"))
        self.verticalLayout_9.addWidget(self.test_email_button)
        self.gridLayout.addLayout(self.verticalLayout_9, 1, 1, 1, 1)
        self.label_15.setBuddy(self.email_from)
        self.label_17.setBuddy(self.relay_host)
        self.label_18.setBuddy(self.relay_port)
        self.label_19.setBuddy(self.relay_username)
        self.label_20.setBuddy(self.relay_password)
        self.label_21.setBuddy(self.relay_tls)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass


