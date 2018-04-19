# coding=utf-8

from pocounit.case import PocoTestCase
from pocounit.addons.poco.action_tracking import ActionTracker
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from airtest.core.api import connect_device, device as current_device


class AndroidAppCase(PocoTestCase):
    @classmethod
    def setUpClass(cls):
        super(AndroidAppCase, cls).setUpClass()
        if not current_device():
            connect_device('Android:///')

        dev = current_device()
        meta_info_emitter = cls.get_result_emitter('metaInfo')
        meta_info_emitter.snapshot_device_info(dev.serialno, dev.adb.get_device_info())

        cls.poco = AndroidUiautomationPoco(screenshot_each_action=False)

        action_tracker = ActionTracker(cls.poco)
        cls.register_addon(action_tracker)
