import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': 'YOUR_EMULATOR_VERSION',
            'deviceName': 'YOUR_EMULATOR_NAME',
            'appPackage': 'com.google.android.calculator',
            'appActivity': 'com.android.calculator2.Calculator',
            'automationName': 'UiAutomator2'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def find_element(self, locator):
        return self.driver.find_element(MobileBy.XPATH, locator)

    def perform_calculation(self, first, operation, second, result):
        self.find_element(f"//android.widget.Button[@text='{first}']").click()
        self.find_element(f"//android.widget.Button[@content-desc='{operation}']").click()
        self.find_element(f"//android.widget.Button[@text='{second}']").click()
        self.find_element("//android.widget.Button[@content-desc='equals']").click()
        sleep(1)
        output = self.find_element("//android.widget.TextView[@resource-id='com.google.android.calculator:id/result_final']")
        self.assertEqual(output.text, result)

    def test_addition(self):
        self.perform_calculation('5', 'plus', '3', '8')

    def test_subtraction(self):
        self.perform_calculation('9', 'minus', '4', '5')

    def test_multiplication(self):
        self.perform_calculation('7', 'multiply', '6', '42')

    def test_division(self):
        self.perform_calculation('8', 'divide', '2', '4')

    def test_complex_calculation(self):
        self.perform_calculation('1', 'plus', '2', '3')
        self.perform_calculation('3', 'multiply', '3', '9')

if __name__ == '__main__':
    unittest.main()