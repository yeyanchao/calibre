# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/convert/look_and_feel.ui'
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
        Form.resize(655, 522)
        Form.setWindowTitle(_("Form"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.opt_disable_font_rescaling = QtGui.QCheckBox(Form)
        self.opt_disable_font_rescaling.setText(_("&Disable font size rescaling"))
        self.opt_disable_font_rescaling.setObjectName(_fromUtf8("opt_disable_font_rescaling"))
        self.gridLayout.addWidget(self.opt_disable_font_rescaling, 0, 0, 1, 1)
        self.label_18 = QtGui.QLabel(Form)
        self.label_18.setText(_("Base &font size:"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 1, 0, 1, 1)
        self.opt_base_font_size = QtGui.QDoubleSpinBox(Form)
        self.opt_base_font_size.setSuffix(_(" pt"))
        self.opt_base_font_size.setDecimals(1)
        self.opt_base_font_size.setMinimum(0.0)
        self.opt_base_font_size.setMaximum(50.0)
        self.opt_base_font_size.setSingleStep(1.0)
        self.opt_base_font_size.setProperty("value", 15.0)
        self.opt_base_font_size.setObjectName(_fromUtf8("opt_base_font_size"))
        self.gridLayout.addWidget(self.opt_base_font_size, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setText(_("Font size &key:"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.opt_font_size_mapping = QtGui.QLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_font_size_mapping.sizePolicy().hasHeightForWidth())
        self.opt_font_size_mapping.setSizePolicy(sizePolicy)
        self.opt_font_size_mapping.setObjectName(_fromUtf8("opt_font_size_mapping"))
        self.horizontalLayout.addWidget(self.opt_font_size_mapping)
        self.button_font_key = QtGui.QToolButton(Form)
        self.button_font_key.setToolTip(_("Wizard to help you choose an appropriate font size key"))
        self.button_font_key.setText(_("..."))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("wizard.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_font_key.setIcon(icon)
        self.button_font_key.setIconSize(QtCore.QSize(32, 32))
        self.button_font_key.setObjectName(_fromUtf8("button_font_key"))
        self.horizontalLayout.addWidget(self.button_font_key)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 3)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setText(_("Minimum &line height:"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.opt_minimum_line_height = QtGui.QDoubleSpinBox(Form)
        self.opt_minimum_line_height.setSuffix(_(" %"))
        self.opt_minimum_line_height.setDecimals(1)
        self.opt_minimum_line_height.setMaximum(900.0)
        self.opt_minimum_line_height.setObjectName(_fromUtf8("opt_minimum_line_height"))
        self.gridLayout.addWidget(self.opt_minimum_line_height, 3, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setText(_("Line &height:"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.opt_line_height = QtGui.QDoubleSpinBox(Form)
        self.opt_line_height.setSuffix(_(" pt"))
        self.opt_line_height.setDecimals(1)
        self.opt_line_height.setObjectName(_fromUtf8("opt_line_height"))
        self.gridLayout.addWidget(self.opt_line_height, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setText(_("Input character &encoding:"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.opt_input_encoding = EncodingComboBox(Form)
        self.opt_input_encoding.setEditable(True)
        self.opt_input_encoding.setObjectName(_fromUtf8("opt_input_encoding"))
        self.gridLayout.addWidget(self.opt_input_encoding, 5, 1, 1, 2)
        self.opt_remove_paragraph_spacing = QtGui.QCheckBox(Form)
        self.opt_remove_paragraph_spacing.setText(_("Remove &spacing between paragraphs"))
        self.opt_remove_paragraph_spacing.setObjectName(_fromUtf8("opt_remove_paragraph_spacing"))
        self.gridLayout.addWidget(self.opt_remove_paragraph_spacing, 6, 0, 1, 2)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setText(_("&Indent size:"))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 6, 3, 1, 1)
        self.opt_remove_paragraph_spacing_indent_size = QtGui.QDoubleSpinBox(Form)
        self.opt_remove_paragraph_spacing_indent_size.setToolTip(_("<p>When calibre removes inter paragraph spacing, it automatically sets a paragraph indent, to ensure that paragraphs can be easily distinguished. This option controls the width of that indent."))
        self.opt_remove_paragraph_spacing_indent_size.setSpecialValueText(_("No change"))
        self.opt_remove_paragraph_spacing_indent_size.setSuffix(_(" em"))
        self.opt_remove_paragraph_spacing_indent_size.setDecimals(1)
        self.opt_remove_paragraph_spacing_indent_size.setMinimum(-0.1)
        self.opt_remove_paragraph_spacing_indent_size.setSingleStep(0.1)
        self.opt_remove_paragraph_spacing_indent_size.setObjectName(_fromUtf8("opt_remove_paragraph_spacing_indent_size"))
        self.gridLayout.addWidget(self.opt_remove_paragraph_spacing_indent_size, 6, 4, 1, 1)
        self.opt_insert_blank_line = QtGui.QCheckBox(Form)
        self.opt_insert_blank_line.setText(_("Insert &blank line between paragraphs"))
        self.opt_insert_blank_line.setObjectName(_fromUtf8("opt_insert_blank_line"))
        self.gridLayout.addWidget(self.opt_insert_blank_line, 7, 0, 1, 2)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setText(_("&Line size:"))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 3, 1, 1)
        self.opt_insert_blank_line_size = QtGui.QDoubleSpinBox(Form)
        self.opt_insert_blank_line_size.setSuffix(_(" em"))
        self.opt_insert_blank_line_size.setDecimals(1)
        self.opt_insert_blank_line_size.setObjectName(_fromUtf8("opt_insert_blank_line_size"))
        self.gridLayout.addWidget(self.opt_insert_blank_line_size, 7, 4, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setText(_("Text &justification:"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.opt_change_justification = QtGui.QComboBox(Form)
        self.opt_change_justification.setObjectName(_fromUtf8("opt_change_justification"))
        self.gridLayout.addWidget(self.opt_change_justification, 8, 2, 1, 3)
        self.opt_smarten_punctuation = QtGui.QCheckBox(Form)
        self.opt_smarten_punctuation.setText(_("Smarten &punctuation"))
        self.opt_smarten_punctuation.setObjectName(_fromUtf8("opt_smarten_punctuation"))
        self.gridLayout.addWidget(self.opt_smarten_punctuation, 9, 0, 1, 1)
        self.opt_asciiize = QtGui.QCheckBox(Form)
        self.opt_asciiize.setText(_("&Transliterate unicode characters to ASCII"))
        self.opt_asciiize.setObjectName(_fromUtf8("opt_asciiize"))
        self.gridLayout.addWidget(self.opt_asciiize, 9, 1, 1, 4)
        self.opt_unsmarten_punctuation = QtGui.QCheckBox(Form)
        self.opt_unsmarten_punctuation.setText(_("&UnSmarten punctuation"))
        self.opt_unsmarten_punctuation.setObjectName(_fromUtf8("opt_unsmarten_punctuation"))
        self.gridLayout.addWidget(self.opt_unsmarten_punctuation, 10, 0, 1, 1)
        self.opt_keep_ligatures = QtGui.QCheckBox(Form)
        self.opt_keep_ligatures.setText(_("Keep &ligatures"))
        self.opt_keep_ligatures.setObjectName(_fromUtf8("opt_keep_ligatures"))
        self.gridLayout.addWidget(self.opt_keep_ligatures, 10, 1, 1, 2)
        self.opt_linearize_tables = QtGui.QCheckBox(Form)
        self.opt_linearize_tables.setText(_("&Linearize tables"))
        self.opt_linearize_tables.setObjectName(_fromUtf8("opt_linearize_tables"))
        self.gridLayout.addWidget(self.opt_linearize_tables, 10, 3, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.extra_css_tab = QtGui.QWidget()
        self.extra_css_tab.setObjectName(_fromUtf8("extra_css_tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.extra_css_tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.opt_extra_css = QtGui.QTextEdit(self.extra_css_tab)
        self.opt_extra_css.setObjectName(_fromUtf8("opt_extra_css"))
        self.gridLayout_2.addWidget(self.opt_extra_css, 0, 0, 1, 1)
        self.tabWidget.addTab(self.extra_css_tab, _fromUtf8(""))
        self.opt_filter_css = QtGui.QWidget()
        self.opt_filter_css.setObjectName(_fromUtf8("opt_filter_css"))
        self.gridLayout_3 = QtGui.QGridLayout(self.opt_filter_css)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_8 = QtGui.QLabel(self.opt_filter_css)
        self.label_8.setText(_("Select what style information you want completely removed:"))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 5)
        self.filter_css_fonts = QtGui.QCheckBox(self.opt_filter_css)
        self.filter_css_fonts.setToolTip(_("Removes the font-family CSS property"))
        self.filter_css_fonts.setText(_("&Fonts"))
        self.filter_css_fonts.setObjectName(_fromUtf8("filter_css_fonts"))
        self.gridLayout_3.addWidget(self.filter_css_fonts, 1, 0, 1, 1)
        self.filter_css_margins = QtGui.QCheckBox(self.opt_filter_css)
        self.filter_css_margins.setToolTip(_("Removes the margin CSS properties. Note that page margins are not affected by this setting."))
        self.filter_css_margins.setText(_("&Margins"))
        self.filter_css_margins.setObjectName(_fromUtf8("filter_css_margins"))
        self.gridLayout_3.addWidget(self.filter_css_margins, 1, 1, 1, 1)
        self.filter_css_padding = QtGui.QCheckBox(self.opt_filter_css)
        self.filter_css_padding.setToolTip(_("Removes the padding CSS properties"))
        self.filter_css_padding.setText(_("&Padding"))
        self.filter_css_padding.setObjectName(_fromUtf8("filter_css_padding"))
        self.gridLayout_3.addWidget(self.filter_css_padding, 1, 2, 1, 1)
        self.filter_css_floats = QtGui.QCheckBox(self.opt_filter_css)
        self.filter_css_floats.setToolTip(_("Convert floating images/text into static images/text"))
        self.filter_css_floats.setText(_("F&loats"))
        self.filter_css_floats.setObjectName(_fromUtf8("filter_css_floats"))
        self.gridLayout_3.addWidget(self.filter_css_floats, 1, 3, 1, 1)
        self.filter_css_colors = QtGui.QCheckBox(self.opt_filter_css)
        self.filter_css_colors.setToolTip(_("Removes foreground and background colors"))
        self.filter_css_colors.setText(_("&Colors"))
        self.filter_css_colors.setObjectName(_fromUtf8("filter_css_colors"))
        self.gridLayout_3.addWidget(self.filter_css_colors, 1, 4, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_9 = QtGui.QLabel(self.opt_filter_css)
        self.label_9.setText(_("&Other CSS Properties:"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        self.filter_css_others = QtGui.QLineEdit(self.opt_filter_css)
        self.filter_css_others.setToolTip(_("Comma separated list of CSS properties to remove. For example: display, color, font-family"))
        self.filter_css_others.setObjectName(_fromUtf8("filter_css_others"))
        self.horizontalLayout_2.addWidget(self.filter_css_others)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 5)
        self.tabWidget.addTab(self.opt_filter_css, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 11, 0, 1, 5)
        self.label_18.setBuddy(self.opt_base_font_size)
        self.label_2.setBuddy(self.opt_font_size_mapping)
        self.label_6.setBuddy(self.opt_minimum_line_height)
        self.label.setBuddy(self.opt_line_height)
        self.label_3.setBuddy(self.opt_input_encoding)
        self.label_4.setBuddy(self.opt_remove_paragraph_spacing_indent_size)
        self.label_7.setBuddy(self.opt_insert_blank_line_size)
        self.label_5.setBuddy(self.opt_change_justification)
        self.label_9.setBuddy(self.filter_css_others)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.opt_disable_font_rescaling, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.opt_base_font_size.setDisabled)
        QtCore.QObject.connect(self.opt_disable_font_rescaling, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.opt_font_size_mapping.setDisabled)
        QtCore.QObject.connect(self.opt_remove_paragraph_spacing, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_4.setEnabled)
        QtCore.QObject.connect(self.opt_remove_paragraph_spacing, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.opt_remove_paragraph_spacing_indent_size.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extra_css_tab), _("&Extra CSS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.opt_filter_css), _("&Filter Style Information"))

from calibre.gui2.widgets import EncodingComboBox


