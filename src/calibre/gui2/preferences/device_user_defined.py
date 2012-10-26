#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import with_statement

__license__   = 'GPL v3'
__copyright__ = '2009, Kovid Goyal <kovid@kovidgoyal.net>'
__docformat__ = 'restructuredtext en'


from PyQt4.Qt import QDialog, QVBoxLayout, QPlainTextEdit, QTimer, \
    QDialogButtonBox, QPushButton, QApplication, QIcon, QMessageBox

from calibre.constants import iswindows

def step_dialog(parent, title, msg, det_msg=''):
    d = QMessageBox(parent)
    d.setWindowTitle(title)
    d.setText(msg)
    d.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return d.exec_() & QMessageBox.Cancel


class UserDefinedDevice(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self._layout = QVBoxLayout(self)
        self.setLayout(self._layout)
        self.log = QPlainTextEdit(self)
        self._layout.addWidget(self.log)
        self.log.setPlainText(_('Getting device information')+'...')
        self.copy = QPushButton(_('Copy to &clipboard'))
        self.copy.setDefault(True)
        self.setWindowTitle(_('User-defined device information'))
        self.setWindowIcon(QIcon(I('debug.png')))
        self.copy.clicked.connect(self.copy_to_clipboard)
        self.ok = QPushButton('&OK')
        self.ok.setAutoDefault(False)
        self.ok.clicked.connect(self.accept)
        self.bbox = QDialogButtonBox(self)
        self.bbox.addButton(self.copy, QDialogButtonBox.ActionRole)
        self.bbox.addButton(self.ok, QDialogButtonBox.AcceptRole)
        self._layout.addWidget(self.bbox)
        self.resize(750, 500)
        self.bbox.setEnabled(False)
        QTimer.singleShot(1000, self.device_info)

    def device_info(self):
        try:
            from calibre.devices import device_info
            r = step_dialog(self.parent(), _('Device Detection'),
                        _('Ensure your device is disconnected, then press OK'))
            if r:
                self.close()
                return
            before = device_info()
            r = step_dialog(self.parent(), _('Device Detection'),
                        _('Ensure your device is connected, then press OK'))
            if r:
                self.close()
                return
            after = device_info()
            new_drives = after['drive_set'] - before['drive_set']
            new_devices = after['device_set'] - before['device_set']
            res = ''
            if (not iswindows or len(new_drives)) and len(new_devices) == 1:
                for d in new_devices:
                    res =  _('USB Vendor ID (in hex)') + ': 0x' + \
                            after['device_details'][d][0] + '\n'
                    res += _('USB Product ID (in hex)') + ': 0x' + \
                            after['device_details'][d][1] + '\n'
                    res += _('USB Revision ID (in hex)') + ': 0x' + \
                            after['device_details'][d][2] + '\n'
                if iswindows:
                    # sort the drives by the order number
                    for i,d in enumerate(sorted(new_drives,
                                    key=lambda x: after['drive_details'][x][0])):
                        if i == 0:
                            res +=  _('Windows main memory vendor string') + ': ' + \
                                    after['drive_details'][d][1] + '\n'
                            res += _('Windows main memory ID string') + ': ' + \
                                    after['drive_details'][d][2] + '\n'
                        else:
                            res +=  _('Windows card A vendor string') + ': ' + \
                                    after['drive_details'][d][1] + '\n'
                            res += _('Windows card A ID string') + ': ' + \
                                    after['drive_details'][d][2] + '\n'
            trailer = _(
                    'Copy these values to the clipboard, paste them into an '
                    'editor, then enter them into the USER_DEVICE by '
                    'customizing the device plugin in Preferences->Plugins. '
                    'Remember to also enter the folders where you want the books to '
                    'be put. You must restart calibre for your changes '
                    'to take effect.\n')
            self.log.setPlainText(res + '\n\n' + trailer)
        finally:
            self.bbox.setEnabled(True)

    def copy_to_clipboard(self):
        QApplication.clipboard().setText(self.log.toPlainText())

if __name__ == '__main__':
    app = QApplication([])
    d = UserDefinedDevice()
    d.exec_()
