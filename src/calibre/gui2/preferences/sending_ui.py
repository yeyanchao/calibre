# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/preferences/sending.ui'
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
        Form.resize(807, 331)
        Form.setWindowTitle(_("Form"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mm_label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mm_label.sizePolicy().hasHeightForWidth())
        self.mm_label.setSizePolicy(sizePolicy)
        self.mm_label.setText(_("Metadata &management:"))
        self.mm_label.setObjectName(_fromUtf8("mm_label"))
        self.gridLayout.addWidget(self.mm_label, 0, 0, 1, 1)
        self.opt_manage_device_metadata = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_manage_device_metadata.sizePolicy().hasHeightForWidth())
        self.opt_manage_device_metadata.setSizePolicy(sizePolicy)
        self.opt_manage_device_metadata.setObjectName(_fromUtf8("opt_manage_device_metadata"))
        self.opt_manage_device_metadata.addItem(_fromUtf8(""))
        self.opt_manage_device_metadata.setItemText(0, _("Manual management"))
        self.opt_manage_device_metadata.addItem(_fromUtf8(""))
        self.opt_manage_device_metadata.setItemText(1, _("Only on send"))
        self.opt_manage_device_metadata.addItem(_fromUtf8(""))
        self.opt_manage_device_metadata.setItemText(2, _("Automatic management"))
        self.gridLayout.addWidget(self.opt_manage_device_metadata, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(457, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label_41 = QtGui.QLabel(Form)
        self.label_41.setText(_("<li><b>Manual management</b>: Calibre updates the metadata and adds collections only when a book is sent. With this option, calibre will never remove a collection.</li>\n"
"<li><b>Only on send</b>: Calibre updates metadata and adds/removes collections for a book only when it is sent to the device. </li>\n"
"<li><b>Automatic management</b>: Calibre automatically keeps metadata on the device in sync with the calibre library, on every connect</li></ul>"))
        self.label_41.setWordWrap(True)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout.addWidget(self.label_41, 1, 0, 1, 3)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setText(_("Format &dates as:"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.opt_send_timefmt = QtGui.QLineEdit(Form)
        self.opt_send_timefmt.setObjectName(_fromUtf8("opt_send_timefmt"))
        self.gridLayout.addWidget(self.opt_send_timefmt, 2, 1, 1, 1)
        self.label_43 = QtGui.QLabel(Form)
        self.label_43.setText(_("Here you can control how calibre will save your books when you click the Send to Device button. This setting can be overriden for individual devices by customizing the device interface plugins in Preferences->Advanced->Plugins"))
        self.label_43.setWordWrap(True)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout.addWidget(self.label_43, 3, 0, 1, 3)
        self.send_template = SaveTemplate(Form)
        self.send_template.setObjectName(_fromUtf8("send_template"))
        self.gridLayout.addWidget(self.send_template, 4, 0, 1, 3)
        self.mm_label.setBuddy(self.opt_manage_device_metadata)
        self.label_2.setBuddy(self.opt_send_timefmt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

from calibre.gui2.preferences.save_template import SaveTemplate
