# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/dialogs/comments_dialog.ui'
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

class Ui_CommentsDialog(object):
    def setupUi(self, CommentsDialog):
        CommentsDialog.setObjectName(_fromUtf8("CommentsDialog"))
        CommentsDialog.resize(400, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CommentsDialog.sizePolicy().hasHeightForWidth())
        CommentsDialog.setSizePolicy(sizePolicy)
        CommentsDialog.setWindowTitle(_("Edit Comments"))
        self.verticalLayout = QtGui.QVBoxLayout(CommentsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textbox = Editor(CommentsDialog)
        self.textbox.setObjectName(_fromUtf8("textbox"))
        self.verticalLayout.addWidget(self.textbox)
        self.buttonBox = QtGui.QDialogButtonBox(CommentsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CommentsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CommentsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CommentsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CommentsDialog)

    def retranslateUi(self, CommentsDialog):
        pass

from calibre.gui2.comments_editor import Editor
