#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:fdm=marker:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2012, Kovid Goyal <kovid at kovidgoyal.net>'
__docformat__ = 'restructuredtext en'

from PyQt4.Qt import (QLabel, QVBoxLayout, QListWidget, QListWidgetItem, Qt)

from calibre.gui2.preferences import ConfigWidgetBase, test_widget

class ConfigWidget(ConfigWidgetBase):

    restart_critical = False

    def genesis(self, gui):
        self.gui = gui
        self.l = l = QVBoxLayout()
        self.setLayout(l)

        self.la = la = QLabel(_(
            'The list of devices that you have asked calibre to ignore. '
            'Uncheck a device to have calibre stop ignoring it.'))
        la.setWordWrap(True)
        l.addWidget(la)

        self.devices = f = QListWidget(self)
        l.addWidget(f)
        f.itemChanged.connect(self.changed_signal)
        f.itemDoubleClicked.connect(self.toggle_item)

    def toggle_item(self, item):
        item.setCheckState(Qt.Checked if item.checkState() == Qt.Unchecked else
                Qt.Unchecked)

    def initialize(self):
        self.devices.blockSignals(True)
        self.devices.clear()
        for dev in self.gui.device_manager.devices:
            for d, name in dev.get_user_blacklisted_devices().iteritems():
                item = QListWidgetItem('%s [%s]'%(name, d), self.devices)
                item.setData(Qt.UserRole, (dev, d))
                item.setFlags(Qt.ItemIsEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsSelectable)
                item.setCheckState(Qt.Checked)
        self.devices.blockSignals(False)

    def restore_defaults(self):
        if self.devices.count() > 0:
            self.devices.clear()

    def commit(self):
        devs = {}
        for i in xrange(0, self.devices.count()):
            e = self.devices.item(i)
            dev, uid = e.data(Qt.UserRole).toPyObject()
            if dev not in devs:
                devs[dev] = []
            if e.checkState() == Qt.Checked:
                devs[dev].append(uid)

        for dev, bl in devs.iteritems():
            dev.set_user_blacklisted_devices(bl)

        return True # Restart required

if __name__ == '__main__':
    from PyQt4.Qt import QApplication
    app = QApplication([])
    test_widget('Sharing', 'Ignored Devices')

