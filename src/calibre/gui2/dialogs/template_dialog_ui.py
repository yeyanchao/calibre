# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/dialogs/template_dialog.ui'
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

class Ui_TemplateDialog(object):
    def setupUi(self, TemplateDialog):
        TemplateDialog.setObjectName(_fromUtf8("TemplateDialog"))
        TemplateDialog.resize(588, 546)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TemplateDialog.sizePolicy().hasHeightForWidth())
        TemplateDialog.setSizePolicy(sizePolicy)
        TemplateDialog.setWindowTitle(_("Edit Comments"))
        self.verticalLayout = QtGui.QVBoxLayout(TemplateDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.colored_field_label = QtGui.QLabel(TemplateDialog)
        self.colored_field_label.setText(_("Set the color of the column:"))
        self.colored_field_label.setObjectName(_fromUtf8("colored_field_label"))
        self.gridlayout.addWidget(self.colored_field_label, 0, 0, 1, 1)
        self.colored_field = QtGui.QComboBox(TemplateDialog)
        self.colored_field.setObjectName(_fromUtf8("colored_field"))
        self.gridlayout.addWidget(self.colored_field, 0, 1, 1, 1)
        self.color_chooser_label = QtGui.QLabel(TemplateDialog)
        self.color_chooser_label.setText(_("Copy a color name to the clipboard:"))
        self.color_chooser_label.setObjectName(_fromUtf8("color_chooser_label"))
        self.gridlayout.addWidget(self.color_chooser_label, 1, 0, 1, 1)
        self.color_name = QtGui.QComboBox(TemplateDialog)
        self.color_name.setObjectName(_fromUtf8("color_name"))
        self.gridlayout.addWidget(self.color_name, 1, 1, 1, 1)
        self.color_copy_button = QtGui.QToolButton(TemplateDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("edit-copy.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.color_copy_button.setIcon(icon)
        self.color_copy_button.setToolTip(_("Copy the selected color name to the clipboard"))
        self.color_copy_button.setObjectName(_fromUtf8("color_copy_button"))
        self.gridlayout.addWidget(self.color_copy_button, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.textbox = QtGui.QPlainTextEdit(TemplateDialog)
        self.textbox.setObjectName(_fromUtf8("textbox"))
        self.verticalLayout.addWidget(self.textbox)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(TemplateDialog)
        self.label.setText(_("Template value:"))
        self.label.setToolTip(_("The value of the template using the current book in the library view"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.template_value = QtGui.QLineEdit(TemplateDialog)
        self.template_value.setReadOnly(True)
        self.template_value.setObjectName(_fromUtf8("template_value"))
        self.gridLayout.addWidget(self.template_value, 5, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TemplateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 1, 1, 1)
        self.label1 = QtGui.QLabel(TemplateDialog)
        self.label1.setText(_("Function &name:"))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.gridLayout.addWidget(self.label1, 6, 0, 1, 1)
        self.function = QtGui.QComboBox(TemplateDialog)
        self.function.setObjectName(_fromUtf8("function"))
        self.gridLayout.addWidget(self.function, 7, 1, 1, 1)
        self.label_2 = QtGui.QLabel(TemplateDialog)
        self.label_2.setText(_("&Documentation:"))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 1)
        self.label_3 = QtGui.QLabel(TemplateDialog)
        self.label_3.setText(_("Python &code:"))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)
        self.documentation = QtGui.QPlainTextEdit(TemplateDialog)
        self.documentation.setMaximumSize(QtCore.QSize(16777215, 75))
        self.documentation.setObjectName(_fromUtf8("documentation"))
        self.gridLayout.addWidget(self.documentation, 8, 1, 1, 1)
        self.source_code = QtGui.QPlainTextEdit(TemplateDialog)
        self.source_code.setObjectName(_fromUtf8("source_code"))
        self.gridLayout.addWidget(self.source_code, 9, 1, 1, 1)
        self.template_tutorial = QtGui.QLabel(TemplateDialog)
        self.template_tutorial.setOpenExternalLinks(True)
        self.template_tutorial.setObjectName(_fromUtf8("template_tutorial"))
        self.gridLayout.addWidget(self.template_tutorial, 10, 1, 1, 1)
        self.template_func_reference = QtGui.QLabel(TemplateDialog)
        self.template_func_reference.setOpenExternalLinks(True)
        self.template_func_reference.setObjectName(_fromUtf8("template_func_reference"))
        self.gridLayout.addWidget(self.template_func_reference, 11, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.colored_field_label.setBuddy(self.colored_field)
        self.color_chooser_label.setBuddy(self.color_name)
        self.label.setBuddy(self.template_value)
        self.label1.setBuddy(self.function)
        self.label_2.setBuddy(self.documentation)
        self.label_3.setBuddy(self.source_code)

        self.retranslateUi(TemplateDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TemplateDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TemplateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TemplateDialog)

    def retranslateUi(self, TemplateDialog):
        pass

