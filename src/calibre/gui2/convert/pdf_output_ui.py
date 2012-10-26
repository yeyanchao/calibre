# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/convert/pdf_output.ui'
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
        Form.resize(590, 395)
        Form.setWindowTitle(_("Form"))
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setText(_("&Paper Size:"))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.opt_paper_size = QtGui.QComboBox(Form)
        self.opt_paper_size.setObjectName(_fromUtf8("opt_paper_size"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.opt_paper_size)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setText(_("&Orientation:"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.opt_orientation = QtGui.QComboBox(Form)
        self.opt_orientation.setObjectName(_fromUtf8("opt_orientation"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.opt_orientation)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setText(_("&Custom size:"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.opt_custom_size = QtGui.QLineEdit(Form)
        self.opt_custom_size.setObjectName(_fromUtf8("opt_custom_size"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.opt_custom_size)
        self.opt_preserve_cover_aspect_ratio = QtGui.QCheckBox(Form)
        self.opt_preserve_cover_aspect_ratio.setText(_("Preserve &aspect ratio of cover"))
        self.opt_preserve_cover_aspect_ratio.setObjectName(_fromUtf8("opt_preserve_cover_aspect_ratio"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.opt_preserve_cover_aspect_ratio)
        spacerItem = QtGui.QSpacerItem(20, 213, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtGui.QFormLayout.LabelRole, spacerItem)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setText(_("Se&rif family:"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.opt_pdf_serif_family = QtGui.QFontComboBox(Form)
        self.opt_pdf_serif_family.setObjectName(_fromUtf8("opt_pdf_serif_family"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.opt_pdf_serif_family)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setText(_("&Sans family:"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.opt_pdf_sans_family = QtGui.QFontComboBox(Form)
        self.opt_pdf_sans_family.setObjectName(_fromUtf8("opt_pdf_sans_family"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.opt_pdf_sans_family)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setText(_("&Monospace family:"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_6)
        self.opt_pdf_mono_family = QtGui.QFontComboBox(Form)
        self.opt_pdf_mono_family.setObjectName(_fromUtf8("opt_pdf_mono_family"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.opt_pdf_mono_family)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setText(_("S&tandard font:"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_7)
        self.opt_pdf_standard_font = QtGui.QComboBox(Form)
        self.opt_pdf_standard_font.setObjectName(_fromUtf8("opt_pdf_standard_font"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.opt_pdf_standard_font)
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setText(_("Default font si&ze:"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_8)
        self.opt_pdf_default_font_size = QtGui.QSpinBox(Form)
        self.opt_pdf_default_font_size.setSuffix(_(" px"))
        self.opt_pdf_default_font_size.setObjectName(_fromUtf8("opt_pdf_default_font_size"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.opt_pdf_default_font_size)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setText(_("Monospace &font size:"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_9)
        self.opt_pdf_mono_font_size = QtGui.QSpinBox(Form)
        self.opt_pdf_mono_font_size.setSuffix(_(" px"))
        self.opt_pdf_mono_font_size.setObjectName(_fromUtf8("opt_pdf_mono_font_size"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.opt_pdf_mono_font_size)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setText(_("<b>Note:</b> The paper size settings below only take effect if you have set the output profile to the default output profile. Otherwise the output profile will override these settings."))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_10)
        self.label.setBuddy(self.opt_paper_size)
        self.label_2.setBuddy(self.opt_orientation)
        self.label_3.setBuddy(self.opt_custom_size)
        self.label_4.setBuddy(self.opt_pdf_serif_family)
        self.label_5.setBuddy(self.opt_pdf_sans_family)
        self.label_6.setBuddy(self.opt_pdf_mono_family)
        self.label_7.setBuddy(self.opt_pdf_standard_font)
        self.label_8.setBuddy(self.opt_pdf_default_font_size)
        self.label_9.setBuddy(self.opt_pdf_mono_font_size)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

