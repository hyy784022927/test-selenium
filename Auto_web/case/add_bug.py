from selenium import webdriver
from common.base import Base
import time


class ZenTaoBug(Base):
    # 定位登录
    loc_user = ("id", "account")
    loc_pwd = ("css selector", "[name='password']")
    loc_btn = ("xpath", "//*[@id='submit']")

    # 添加bug
    loc_test = ("link text", "测试")
    loc_bug = ("link text", "Bug")
    loc_addbug = ("xpath", "//*[@id='createActionMenu']/a")
    loc_truck = ("xpath", "//*[@id='openedBuild_chosen']/ul")
    loc_truck_add = ("xpath", "//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id", "title")
    # 需要先切换iframe
    loc_input_body = ("class name", "article-content")
    loc_avse = ("css selector", "#submit")

    # 新增的列表
    loc_new = ("xpath", "//*[@id='bugList']/tbody/tr[1]/td[4]/a")
    ".// *[ @ id = 'bugList'] / tbody / tr[1] / td[4] / a"

    # def __init__(self,driver):
    #     self.driver=driver
    #     self.zentao=Base(self.driver)

    def login(self, user="admin", pwd="123456"):
        self.driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
        self.sendKeys(self.loc_user, user)
        self.sendKeys(self.loc_pwd, pwd)
        self.click(self.loc_btn)

    def add_bug(self, title):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)
        self.sendKeys(self.loc_input_title, title)

        # 切换到iframe
        self.driver.switch_to.frame(0)
        body = '''[步骤]XXXX
        [结果]XXXX
        [期望]XXXX
        '''
        self.sendKeys(self.loc_input_body, body)
        self.driver.switch_to.default_content()

        self.click(self.loc_avse)

    def is_add_bug_sucess(self, title):
        return self.isTextInElement(self.loc_new, title)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    bug = ZenTaoBug(driver)
    bug.login()
    time_str = time.strftime("%Y-%m-%D-%H-%M-%S")
    title = "测试提交Bug" + time_str
    bug.add_bug(title)
    result = bug.is_add_bug_sucess(title)
    driver.quit()
    print(result)
