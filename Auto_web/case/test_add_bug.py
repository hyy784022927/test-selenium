import unittest
from selenium import webdriver
from page.add_bug_page import AddBugPage
from page.login_page import LoginPage
import time

url = "http://127.0.0.1:81/zentao/my/"


class AddBugCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.log = LoginPage(cls.driver)
        cls.bug = AddBugPage(cls.driver)
        log = LoginPage(cls.driver)
        log.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        '''使每个用例都回到同一个起点'''
        self.driver.get(url)

    def test_add_bug(self):
        '''添加bug '''
        time_str = time.strftime("%Y-%m-%D-%H-%M-%S")
        title = "测试提交Bug" + time_str
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_sucess(title)
        print(result)
        self.assertTrue(result)

    def test_add_bugXXX(self):
        '''添加bug '''
        time_str = time.strftime("%Y-%m-%D-%H-%M-%S")
        title = "测试提交Bug" + time_str
        self.bug.add_bug(title)
        result = self.bug.is_add_bug_sucess(title)
        print(result)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()