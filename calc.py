# -*- coding: utf-8 -*-
import os
from time import sleep
import unittest
from appium import webdriver

from nose.tools import assert_equal, assert_not_equal
from nose_parameterized import parameterized

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestCalc(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'
        # desired_caps['deviceName'] = '73ffacfe'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = PATH('calc.apk')

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.orientation = 'PORTRAIT'

        self.arg1 = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("arg1")')
        self.arg2 = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("arg2")')
        self.add = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("addition")')
        self.sub = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("subtraction")')
        self.div = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("division")')
        self.mul = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("multiplication")')
        self.res = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("result")')

    @parameterized.expand([
        ('positive', '1', '2'),
        ('negative', '-3', '-4'),
        ('fraction', '5.6', '7.8'),
        ('long number', '11111111111111111111', '11111111111111111111'),
    ])
    def test_1_arguments_check(self, msg, argument1, argument2):
        assert_equal(self.arg1.get_attribute('text'), 'First argument')
        assert_equal(self.arg2.get_attribute('text'), 'Second argument')

        self.arg1.send_keys(argument1)
        self.arg2.send_keys(argument2)
        sleep(2)
        assert_equal(self.arg1.get_attribute('text'), argument1, msg)
        assert_equal(self.arg2.get_attribute('text'), argument2, msg)
        assert_equal(self.res.get_attribute('text'), 'Result', msg) \
 \
        @parameterized.expand([
            ('chars', 'a', 'B'),
            ('symbol', '#', '$'),
            # ('symbol cyr', 'Ж', 'й'),
        ])
    def test_1a_arguments_negativ(self, msg, argument1, argument2):
        self.arg1.send_keys(argument1)
        self.arg2.send_keys(argument2)
        # sleep(2)
        assert_equal(self.arg1.get_attribute('text'), 'First argument')
        assert_equal(self.arg2.get_attribute('text'), 'Second argument')


    @parameterized.expand([
        ('num num sub', '1', '1', 'sub', '0'),
        ('nul num sub', '', '1', 'sub', '-1'),
        ('num nul sub', '1', '', 'sub', '1'),
        ('nul nul sub', '', '', 'sub', 'Result'),
    ])
    def test_2_sub_operations(self, _, argument1, argument2, operation, result):
        self.arg1.send_keys(argument1)
        self.arg2.send_keys(argument2)
        self.sub.click()
        assert_equal(self.res.get_attribute('text'), result)

    @parameterized.expand([
        ('num num div', '1', '1', 'div', '1'),
        ('nul num div', '', '1', 'div', 'Error'),
        ('num nul div', '1', '', 'div', 'Error'),
        ('nul nul div', '', '', 'div', 'Error'),
        ('num 0 div', '1', '0', 'div', 'Error'),
    ])
    def test_3_div_operations(self, _, argument1, argument2, operation, result):
        self.arg1.send_keys(argument1)
        self.arg2.send_keys(argument2)
        self.div.click()
        assert_equal(self.res.get_attribute('text'), result)

    @parameterized.expand([
        ('positive result', 9, 2, '7'),
        ('negative result', 4, 7, '-3'),
        ('fraction result', '9.9', 3, '6.9'),
        ('subtract nill', 76, 0, '76'),
        ('subtract from nill', 0, 999, '-999'),
        ('sub from negativ number', -12, 4, '-16'),
        ('subtract negative number', 12, -4, '16'),
    ])
    def test_4_subtraction(self, _, argument1, argument2, result):
        self.arg1.send_keys(argument1)
        self.arg2.send_keys(argument2)
        self.sub.click()
        assert_equal(self.res.get_attribute('text'), result)

    @parameterized.expand([
        ('positive', 8, 4, '2'),
        ('2 digits', 33, 3, '11'),
        ('3 digits', 333, 3, '111'),
        ('fraction result', 9, 6, '1.5'),
        ('fraction argument1', '9.9', 3, '3.3'),
        ('negative argument1', -10, 2, '-5'),
        ('20 dig numbers', '11111111111111111111', 1, '11111111111111111111'),
    ])
    def test_5_division(self, _, argument1, argument2, result):
        self.arg1.send_keys(argument1)
        self.arg2.send_keys(argument2)
        self.div.click()

        assert_equal(self.res.get_attribute('text'), result)

    def test_6_rotation(self):
        self.driver.orientation = 'PORTRAIT'
        self.arg1.send_keys(1)
        self.arg2.send_keys(2)
        self.add.click()
        self.driver.orientation = 'LANDSCAPE'
        sleep(2)
        assert_equal(self.arg1.get_attribute('text'), '1')
        assert_equal(self.arg2.get_attribute('text'), '2')
        assert_equal(self.res.get_attribute('text'), '3')
        self.arg1.send_keys(1)
        self.arg2.send_keys(2)
        self.add.click()
        self.driver.orientation = 'LANDSCAPE'
        sleep(2)
        assert_equal(self.arg1.get_attribute('text'), '1')
        assert_equal(self.arg2.get_attribute('text'), '2')
        assert_equal(self.res.get_attribute('text'), '3')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalc)
    unittest.TextTestRunner(verbosity=2).run(suite)