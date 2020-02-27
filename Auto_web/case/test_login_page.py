from selenium import webdriver
from page.login_page import LoginPage, login_url
import unittest

'''
1.输入admin，输入123456 点登录
2.输入admin，输入“”点登录
3.输入admin，输入123456，点记住登录按钮 点登录
4.点忘记密码
'''


class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.loginP = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginP.is_alert_exist()
        self.driver.delete_all_cookies()  # 去除所有登录信息
        self.driver.refresh()

    def test_01(self):
        '''输入admin，输入123456 点登录'''
        self.loginP.input_user("admin")
        self.loginP.input_pwd("123456")
        self.loginP.click_login_button()
        result = self.loginP.get_login_name()
        # 断言
        self.assertTrue(result == "admin")

    def test_02(self):
        '''输入admin，输入“”点登录'''
        self.loginP.input_user("admin")
        self.loginP.click_login_button()
        result = self.loginP.get_login_name()
        # 断言
        self.assertTrue(result == "")

    def test_03(self):
        '''输入admin，输入123456，点记住登录按钮 点登录'''
        self.loginP.input_user("admin")
        self.loginP.input_pwd("123456")
        self.loginP.click_keep_login()
        self.loginP.click_login_button()
        result = self.loginP.get_login_name()
        # 断言
        self.assertTrue(result == "admin")

    def test_04(self):
        '''点忘记密码'''
        self.loginP.click_forget_pwd()
        ret = self.loginP.is_refresh_exist()
        # 断言
        print()
        self.assertTrue(ret)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()