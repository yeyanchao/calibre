# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yc/code/calibre/calibre/src/calibre/gui2/lrf_renderer/main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(601, 701)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle(_("LRF Viewer"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("viewer.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.central_widget = QtGui.QWidget(MainWindow)
        self.central_widget.setObjectName(_fromUtf8("central_widget"))
        self.vboxlayout = QtGui.QVBoxLayout(self.central_widget)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.stack = QtGui.QStackedWidget(self.central_widget)
        self.stack.setObjectName(_fromUtf8("stack"))
        self.viewer_page = QtGui.QWidget()
        self.viewer_page.setObjectName(_fromUtf8("viewer_page"))
        self.gridlayout = QtGui.QGridLayout(self.viewer_page)
        self.gridlayout.setMargin(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.graphics_view = BookView(self.viewer_page)
        self.graphics_view.setMouseTracking(True)
        self.graphics_view.setObjectName(_fromUtf8("graphics_view"))
        self.gridlayout.addWidget(self.graphics_view, 0, 0, 1, 1)
        self.stack.addWidget(self.viewer_page)
        self.bar_page = QtGui.QWidget()
        self.bar_page.setObjectName(_fromUtf8("bar_page"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.bar_page)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.frame_2 = QtGui.QFrame(self.bar_page)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.frame_2)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.progress_bar = QtGui.QProgressBar(self.frame_2)
        self.progress_bar.setMaximum(0)
        self.progress_bar.setProperty("value", -1)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.vboxlayout2.addWidget(self.progress_bar)
        self.progress_label = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.progress_label.setFont(font)
        self.progress_label.setText(_("Parsing LRF file"))
        self.progress_label.setObjectName(_fromUtf8("progress_label"))
        self.vboxlayout2.addWidget(self.progress_label)
        self.vboxlayout1.addWidget(self.frame_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem1)
        self.stack.addWidget(self.bar_page)
        self.vboxlayout.addWidget(self.stack)
        MainWindow.setCentralWidget(self.central_widget)
        self.tool_bar = QtGui.QToolBar(MainWindow)
        self.tool_bar.setWindowTitle(_("LRF Viewer toolbar"))
        self.tool_bar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.tool_bar.setObjectName(_fromUtf8("tool_bar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.tool_bar)
        self.action_next_page = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("next.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_next_page.setIcon(icon1)
        self.action_next_page.setText(_("Next Page"))
        self.action_next_page.setObjectName(_fromUtf8("action_next_page"))
        self.action_previous_page = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(I("previous.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_previous_page.setIcon(icon2)
        self.action_previous_page.setText(_("Previous Page"))
        self.action_previous_page.setObjectName(_fromUtf8("action_previous_page"))
        self.action_back = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(I("back.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_back.setIcon(icon3)
        self.action_back.setText(_("Back"))
        self.action_back.setObjectName(_fromUtf8("action_back"))
        self.action_forward = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(I("forward.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_forward.setIcon(icon4)
        self.action_forward.setText(_("Forward"))
        self.action_forward.setObjectName(_fromUtf8("action_forward"))
        self.action_next_match = QtGui.QAction(MainWindow)
        self.action_next_match.setText(_("Next match"))
        self.action_next_match.setObjectName(_fromUtf8("action_next_match"))
        self.action_open_ebook = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(I("document_open.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_ebook.setIcon(icon5)
        self.action_open_ebook.setText(_("Open ebook"))
        self.action_open_ebook.setObjectName(_fromUtf8("action_open_ebook"))
        self.action_configure = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(I("config.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_configure.setIcon(icon6)
        self.action_configure.setText(_("Configure"))
        self.action_configure.setObjectName(_fromUtf8("action_configure"))
        self.tool_bar.addAction(self.action_back)
        self.tool_bar.addAction(self.action_forward)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.action_open_ebook)
        self.tool_bar.addAction(self.action_configure)
        self.tool_bar.addSeparator()
        self.tool_bar.addAction(self.action_previous_page)
        self.tool_bar.addAction(self.action_next_page)
        self.tool_bar.addSeparator()

        self.retranslateUi(MainWindow)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

from bookview import BookView

