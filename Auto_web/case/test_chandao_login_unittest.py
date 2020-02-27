from selenium import webdriver
import time
import unittest


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://127.0.0.1:81/zentao/my/")
        # time.sleep(2)
        # self.driver.implicitly_wait(3)
        self.is_alert_exit()
        self.driver.delete_all_cookies()  # 去除所有登录信息
        self.driver.refresh()

    def tearDown(self):
        # self.is_alert_exit()
        self.driver.delete_all_cookies()  # 去除所有登录信息
        self.driver.refresh()

    def get_login_ret(self):
        # 判断是否登陆成功
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text
        except:
            return ""
        else:
            return t

    def is_alert_exist(self):
        # 判断登录弹窗是否存在
        time.sleep(2)
        try:
            alert = self.driver.switch_to.alert
            t = alert.text
        except:
            return ""
        else:
            alert.accept()
            return t

    def login(self, user, pwd):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(pwd)
        self.driver.find_element_by_id("submit").click()
        time.sleep(3)  # 等待页面切换

    def test_01(self):
        '''登陆成功的案例'''
        self.login("admin", "123456")

        # 判断是否登陆成功
        t = self.get_login_ret()
        print("登录成功，获取的结果:%s" % t)
        # 断言
        self.assertTrue(t == "admin")

    def test_02(self):
        '''登陆失败的案例'''
        self.login("admin12233", "123456")

        # 判断是否登陆成功
        t = self.get_login_ret()
        print("登录失败，获取的结果:%s" % t)
        # 断言
        self.assertTrue(t == "")
        # self.assertTrue(t == "1")  # 故意断言失败，触发截图


if __name__ == '__main__':
    unittest.main()
