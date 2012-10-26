# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/store/config/chooser/adv_search_builder.ui'
#
# Created: Thu Oct 25 16:54:56 2012
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
        Dialog.resize(752, 472)
        Dialog.setWindowTitle(_("Advanced Search"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("search.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setText(_("&What kind of match to use:"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.matchkind = QtGui.QComboBox(Dialog)
        self.matchkind.setObjectName(_fromUtf8("matchkind"))
        self.matchkind.addItem(_fromUtf8(""))
        self.matchkind.setItemText(0, _("Contains: the word or phrase matches anywhere in the metadata field"))
        self.matchkind.addItem(_fromUtf8(""))
        self.matchkind.setItemText(1, _("Equals: the word or phrase must match the entire metadata field"))
        self.matchkind.addItem(_fromUtf8(""))
        self.matchkind.setItemText(2, _("Regular expression: the expression must match anywhere in the metadata field"))
        self.gridLayout_2.addWidget(self.matchkind, 0, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setTitle(_("Find entries that have..."))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(_("&All these words:"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.all = QtGui.QLineEdit(self.groupBox)
        self.all.setObjectName(_fromUtf8("all"))
        self.horizontalLayout.addWidget(self.all)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(_("This exact &phrase:"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.phrase = QtGui.QLineEdit(self.groupBox)
        self.phrase.setObjectName(_fromUtf8("phrase"))
        self.horizontalLayout_2.addWidget(self.phrase)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(_("&One or more of these words:"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.any = QtGui.QLineEdit(self.groupBox)
        self.any.setObjectName(_fromUtf8("any"))
        self.horizontalLayout_3.addWidget(self.any)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setTitle(_("But dont show entries that have..."))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setText(_("Any of these &unwanted words:"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.none = QtGui.QLineEdit(self.groupBox_2)
        self.none.setObjectName(_fromUtf8("none"))
        self.horizontalLayout_4.addWidget(self.none)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_6.setText(_("See the <a href=\"http://manual.calibre-ebook.com/gui.html#the-search-interface\">User Manual</a> for more help"))
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.tab)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setText(_("&Name:"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.name_box = EnLineEdit(self.tab_2)
        self.name_box.setToolTip(_("Enter the title."))
        self.name_box.setObjectName(_fromUtf8("name_box"))
        self.gridLayout.addWidget(self.name_box, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setText(_("&Description:"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.price_label = QtGui.QLabel(self.tab_2)
        self.price_label.setText(_("&Headquarters:"))
        self.price_label.setObjectName(_fromUtf8("price_label"))
        self.gridLayout.addWidget(self.price_label, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.clear_button = QtGui.QPushButton(self.tab_2)
        self.clear_button.setText(_("&Clear"))
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.horizontalLayout_6.addWidget(self.clear_button)
        self.tab_2_button_box = QtGui.QDialogButtonBox(self.tab_2)
        self.tab_2_button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.tab_2_button_box.setObjectName(_fromUtf8("tab_2_button_box"))
        self.horizontalLayout_6.addWidget(self.tab_2_button_box)
        self.gridLayout.addLayout(self.horizontalLayout_6, 9, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setText(_("Search only in specific fields:"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 2)
        self.description_box = EnLineEdit(self.tab_2)
        self.description_box.setObjectName(_fromUtf8("description_box"))
        self.gridLayout.addWidget(self.description_box, 2, 1, 1, 1)
        self.format_box = QtGui.QLineEdit(self.tab_2)
        self.format_box.setObjectName(_fromUtf8("format_box"))
        self.gridLayout.addWidget(self.format_box, 4, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setText(_("&Format:"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.headquarters_box = EnLineEdit(self.tab_2)
        self.headquarters_box.setObjectName(_fromUtf8("headquarters_box"))
        self.gridLayout.addWidget(self.headquarters_box, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setText(_("Enabled:"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setText(_("DRM:"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.enabled_combo = QtGui.QComboBox(self.tab_2)
        self.enabled_combo.setObjectName(_fromUtf8("enabled_combo"))
        self.enabled_combo.addItem(_fromUtf8(""))
        self.enabled_combo.setItemText(0, _fromUtf8(""))
        self.enabled_combo.addItem(_fromUtf8(""))
        self.enabled_combo.setItemText(1, _("true"))
        self.enabled_combo.addItem(_fromUtf8(""))
        self.enabled_combo.setItemText(2, _("false"))
        self.gridLayout.addWidget(self.enabled_combo, 5, 1, 1, 1)
        self.drm_combo = QtGui.QComboBox(self.tab_2)
        self.drm_combo.setObjectName(_fromUtf8("drm_combo"))
        self.drm_combo.addItem(_fromUtf8(""))
        self.drm_combo.setItemText(0, _fromUtf8(""))
        self.drm_combo.addItem(_fromUtf8(""))
        self.drm_combo.setItemText(1, _("true"))
        self.drm_combo.addItem(_fromUtf8(""))
        self.drm_combo.setItemText(2, _("false"))
        self.gridLayout.addWidget(self.drm_combo, 6, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setText(_("Affiliate:"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)
        self.affiliate_combo = QtGui.QComboBox(self.tab_2)
        self.affiliate_combo.setObjectName(_fromUtf8("affiliate_combo"))
        self.affiliate_combo.addItem(_fromUtf8(""))
        self.affiliate_combo.setItemText(0, _fromUtf8(""))
        self.affiliate_combo.addItem(_fromUtf8(""))
        self.affiliate_combo.setItemText(1, _("true"))
        self.affiliate_combo.addItem(_fromUtf8(""))
        self.affiliate_combo.setItemText(2, _("false"))
        self.gridLayout.addWidget(self.affiliate_combo, 7, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.label_5.setBuddy(self.matchkind)
        self.label.setBuddy(self.all)
        self.label_2.setBuddy(self.all)
        self.label_3.setBuddy(self.all)
        self.label_4.setBuddy(self.all)
        self.label_7.setBuddy(self.name_box)
        self.label_8.setBuddy(self.description_box)
        self.price_label.setBuddy(self.headquarters_box)
        self.label_10.setBuddy(self.format_box)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.all, self.phrase)
        Dialog.setTabOrder(self.phrase, self.any)
        Dialog.setTabOrder(self.any, self.none)
        Dialog.setTabOrder(self.none, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.name_box)
        Dialog.setTabOrder(self.name_box, self.description_box)
        Dialog.setTabOrder(self.description_box, self.headquarters_box)
        Dialog.setTabOrder(self.headquarters_box, self.format_box)
        Dialog.setTabOrder(self.format_box, self.clear_button)
        Dialog.setTabOrder(self.clear_button, self.tab_2_button_box)
        Dialog.setTabOrder(self.tab_2_button_box, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.matchkind)

    def retranslateUi(self, Dialog):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _("A&dvanced Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _("Nam&e/Description ..."))

from calibre.gui2.widgets import EnLineEdit

