# coding=utf-8

import time

# TODO: "from testflow.lib" should be renamed according to your actual package name
from testflow.lib.case.android_app import AndroidAppCase
from testflow.lib.utils.installation import install_android_app
from airtest.core.api import start_app, stop_app, Template, exists
from airtest.core.api import device as current_device


class CalculatorPlus(AndroidAppCase):
    @classmethod
    def name(cls):
        return 'CalculatorPlus (customized name)'

    @classmethod
    def getMetaInfo(cls):
        return {
            "author": 'author name',
            "remark": 'any data',
            'any-keys': 'any-values',
        }

    def setUp(self):
        self.package_name = 'com.google.android.calculator'
        apk_path = self.R('res/app/com.google.android.calculator.apk')
        install_android_app(current_device().adb, apk_path)
        start_app(self.package_name)

    def runTest(self):
        keyboard = Template(self.R('res/img/keyboard-digits.png'))
        keyboard_landscape = Template(self.R('res/img/keyboard-digits-landscape.png'))
        self.assertTrue(exists(keyboard) or exists(keyboard_landscape), 'App started.')

        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/op_add').click()
        self.poco('com.google.android.calculator:id/digit_1').click()
        self.poco('com.google.android.calculator:id/eq').click()
        time.sleep(1)
        result = self.poco('com.google.android.calculator:id/formula').get_text()
        self.site_capturer.snapshot('check-point-1')
        self.assertEqual(result, '2', '1+1=2 ^^')

    def tearDown(self):
        stop_app(self.package_name)


if __name__ == '__main__':
    import pocounit
    pocounit.main()
