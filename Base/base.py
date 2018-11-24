from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # "在base类中封装常用的公共方法"
    def __init__(self,driver):
        self.driver = driver

    # "查找元素的方法封装"
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 点击元素 封装
    def base_click(self,loc):
        self.base_find_element(loc).click()
    #输入方法 封装
    def base_input(self,loc,text):
        # 调用查找元素
        el = self.base_find_element(loc)
        # 封装清除方法
        el.clear()
        # 封装发送数据方法
        el.send_keys(text)

