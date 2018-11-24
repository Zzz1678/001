import os,sys
sys.path.append(os.getcwd())

import pytest
from Base.get_driver import get_driver
from Page.Page_Login import PageLogin


class testlogin():
    # 初始化方法
    def setup_class(self):
        self.driver = get_driver()
        self.login = PageLogin(self.driver)
    # 结束放啊
    def teardown(self):
        # 关闭驱动
        self.driver.quit()
    # 测试方法
    def test_login(self,username="18600001111",pwd="123456"):
        # 输入用户名
        self.login.page_input_username(username)
        #输入密码
        self.login.page_input_pwd(pwd)
        #点击登录
        self.login.page_click_login_btn()
if __name__ == '__main__':
    pytest.main("-s test.login.py")


