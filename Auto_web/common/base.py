from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Base(object):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self, locator):
        if not isinstance(locator, tuple):
            print("locator参数类型错误，必须传元组类型：loc=（'id','value'）")
        else:
            print("正在定位元素信息：定位方式-》%s,value值-》%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElementNew(self, locator):
        '''通过expected_conditions的presence_of_element_located类 获取元素'''
        if not isinstance(locator, tuple):
            print("locator参数类型错误，必须传元组类型：loc=（'id','value'）")
        else:
            print("正在定位元素信息：定位方式-》%s,value值-》%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele

    def findElements(self, locator):
        if not isinstance(locator, tuple):
            print("locator参数类型错误，必须传元组类型：loc=（'id','value'）")
        else:
            print("正在定位元素信息：定位方式-》%s,value值-》%s" % (locator[0], locator[1]))
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return eles

    def sendKeys(self, locator, value):
        self.findElement(locator).send_keys(value)

    def click(self, locator):
        self.findElement(locator).click()

    def clear(self, locator):
        self.findElement(locator).clear()

    def move_to_element(self, locator):
        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def isSelect(self, locator):
        '''判断元素是否被选中'''
        ele = self.findElement(locator)
        ret = ele.is_selected()
        return ret

    def isDisplay(self, locator):
        '''判断元素是否显示'''
        ele = self.findElement(locator)
        ret = ele.is_displayed()
        return ret

    def isElementExist(self, locator):
        try:
            self.findElement(locator)
        except:
            return False
        else:
            return True

    def isElementExist2(self, locator):
        eles = self.findElement(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            print("返回一个元素")
            return True
        else:
            print("返回元素个数%d" % n)
            return True

    def isTitle(self, title):
        '''返回bool，判断标题是否正确'''
        try:
            ret = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return ret
        except:
            return False

    def isTitleContains(self, title):
        '''返回bool,判断标题是否包含title参数的内容'''
        try:
            ret = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return ret
        except:
            return False

    def isTextInElement(self, locator, text):
        '''返回bool,判断标题是否包含title参数的内容'''
        try:
            ret = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator, text))
            return ret
        except:
            return False

    def isValueInElementValue(self, locator, value):
        '''返回bool,判断参数value是否是元素value值'''
        try:
            ret = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, value))
            return ret
        except:
            return False

    def isAlert(self):
        '''判断弹窗是否存在，存在返回弹窗，不存在返回False'''
        try:
            ret = WebDriverWait(self.driver, 3, self.t).until(EC.alert_is_present())
            return ret
        except:
            return False

    def get_text(self, locator):
        '''获取文本'''
        try:
            ret = self.findElement(locator).text
            return ret
        except:
            print("获取text失败，返回''")
            return ""

    def get_attribute(self, locator, name):
        '''获取属性'''
        try:
            ele = self.findElement(locator)
            return ele.get_attribute(name)
        except:
            print("获取属性失败，返回''")
            return ""

    def select_by_index(self, locator, index=0):
        '''通过索引选择，index是索引第几个元素，从0开始，默认第0个'''
        ele = self.findElement(locator)
        Select(ele).select_by_value(index)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        '''切换iframe'''
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.findElement(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print("iframe切换异常")

    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        ret = self.isAlert()
        if not ret:
            print("alert不存在")
        else:
            return ret

    def move_to_element(self, locator):
        '''移动到目标元素，鼠标悬停'''
        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def js_scroll_end(self, y=0):
        '''滚动到底部'''
        js_heig = "window.scrollTo(%s,document.body.scrollHeight)" % x
        self.driver.execute_script(js_heig)

    def js_scroll_top(self):
        '''回到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_focus(self, locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    zentao = Base(driver)

    loc1 = (By.ID, "account")
    loc2 = (By.NAME, "password")
    loc3 = (By.XPATH, "//*[@id='submit']")
    # zentao.findElement(loc1)
    # zentao.send_key("admin")

    zentao.sendKeys(loc1, "admin")
    zentao.sendKeys(loc2, "123456")
    zentao.click(loc3)

    driver.quit()
