# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
import unittest
from appium import webdriver


class AppiumBaseTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '6.0',
                        'deviceName': 'b892ad4d',
                        'appPackage': 'com.example.svenweng.uiwidgettest',
                        'appActivity': '.MainActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
