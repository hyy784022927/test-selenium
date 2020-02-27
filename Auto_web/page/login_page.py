from selenium import webdriver
from common.base import Base
import time

login_url = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"


class LoginPage(Base):
    # 定位登录
    loc_user = ("id", "account")
    loc_pwd = ("css selector", "[name='password']")
    loc_btn = ("xpath", "//*[@id='submit']")
    loc_keep = ("id", "keepLoginon")
    loc_forget_pwd = ("link text", "忘记密码")

    # 登录后，跳转的页面里的元素
    loc_get_user = ("css selector", "#userMenu>a")

    # 点忘记密码后，跳转的页面里的元素
    loc_forget_pwd_page = ("xpath", "html/body/div[1]/div/div[2]/p/a")

    def input_user(self, text=""):
        self.sendKeys(self.loc_user, text)

    def input_pwd(self, text=""):
        self.sendKeys(self.loc_pwd, text)

    def click_login_button(self):
        self.click(self.loc_btn)

    def click_keep_login(self):
        self.click(self.loc_keep)

    def click_forget_pwd(self):
        self.click(self.loc_forget_pwd)

    def login(self, user="admin", pwd="123456", keep_login=False):
        '''登录流程'''
        self.driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
        self.loginP.input_user(user)
        self.loginP.input_pwd(pwd)

        if keep_login:
            self.click_keep_login()

        self.loginP.click_login_button()

    def get_login_name(self):
        user = self.get_text(self.loc_get_user)
        return user

    def is_alert_exist(self):
        # 判断登录弹窗是否存在
        a = self.isAlert()
        if a:
            print(a.text)
            a.accept()

    def is_refresh_exist(self):
        '''判断忘记密码页面，刷新按钮是否存在'''
        ret = self.isElementExist(self.loc_forget_pwd_page)
        return ret
