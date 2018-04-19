# coding=utf-8

import time

# TODO: "from testflow.lib" should be renamed according to your actual package name
from testflow.lib.case.android_app import AndroidAppCase
from testflow.lib.utils.installation import install_android_app
from airtest.core.api import start_app, stop_app
from airtest.core.api import device as current_device


class CalculatorCase(AndroidAppCase):
    @classmethod
    def setUpClass(cls):
        super(CalculatorCase, cls).setUpClass()
        cls.package_name = 'com.google.android.calculator'
        apk_path = cls.R('res/app/com.google.android.calculator.apk')
        install_android_app(current_device().adb, apk_path)
        start_app(cls.package_name)

    @classmethod
    def tearDownClass(cls):
        stop_app(cls.package_name)
        super(CalculatorCase, cls).tearDownClass()

    def setUp(self):
        # clear previous result
        clr = self.poco('com.google.android.calculator:id/clr')
        if clr.exists():
            clr.click()


class CalculatorPlus(CalculatorCase):
    def runTest(self):
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/op_add').click()
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/eq').click()
        time.sleep(1)
        result = self.poco('com.google.android.calculator:id/formula').get_text()
        self.assertEqual(result, '2', '1+1=2 ^^')


class CalculatorMinus(CalculatorCase):
    def runTest(self):
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/op_sub').click()
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/eq').click()
        time.sleep(1)
        result = self.poco('com.google.android.calculator:id/formula').get_text()
        self.assertEqual(result, '0', '1-1=0 ^^')


if __name__ == '__main__':
    import pocounit
    pocounit.main()
