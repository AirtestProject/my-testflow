# coding=utf-8

import time
from lib.case.android_app import AndroidAppCase
from airtest.core.api import install, start_app


class TestCalculatorPlus(AndroidAppCase):
    def setUp(self):
        assets_mgr = self.get_assets_manager()
        print(assets_mgr)
        apk_path = assets_mgr.get_abspath('res/app/com.google.android.calculator.apk')
        install(apk_path)
        start_app('com.google.android.calculator')

    def runTest(self):
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/op_add').click()
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/eq').click()
        time.sleep(1)
        result = self.poco('com.google.android.calculator:id/result').get_text()
        self.assertEqual(result, '2', '1+1=2 ^^')


if __name__ == '__main__':
    import pocounit
    pocounit.main()
