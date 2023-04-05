# 3.	以管理员身份登录 http://127.0.0.1:8047/mgr/sign.html，用户名 ：byhy 密码： 88888888。
# 点击页脚处 链接 白月黑羽教学使用，点击访问官网；
# 然后在新打开的 白月黑羽教学网页，获取页眉导航菜单中所有教程类目（可以调用webdriver对象的maximize_window()方法最大化窗口，以便显示所有菜单 ）；
# 随后再回到 白月SMS系统网页，点击退出登录。
# 预期结果为：成功登录后，完成上述操作，验证导航菜单名，依次为：Python基础、Python进阶、Qt图形界面、Django、自动化测试、性能测试、HTML/CSS、JS语言、JS Web。
# 验证回到登录界面（可以根据webdriver对象的current_url属性判断是否进入登录页面）。
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
sign_url = 'http://127.0.0.1:8047/mgr/sign.html'
driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")
driver.get(sign_url)
driver.find_element(By.CSS_SELECTOR, '#username').send_keys('byhy')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('88888888')
driver.find_element(By.CSS_SELECTOR, '.btn').click()
sleep(1)
mainWindow = driver.current_window_handle
driver.find_element(By.CSS_SELECTOR, 'div.hidden-xs').click()
driver.switch_to.window(driver.window_handles[1])
course = driver.find_element(By.CSS_SELECTOR, '.d-md-inline-flex').text.replace('\n', '、')
sample = 'Python基础、Python进阶、Qt图形界面、Django、自动化测试、性能测试、HTML/CSS、JS语言、JS Web'
if sample == course:
    print('抓取成功！')
else:
    print('抓取错误！')
driver.switch_to.window(mainWindow)
driver.find_element(By.CSS_SELECTOR, '.user-menu>a').click()
driver.find_element(By.CSS_SELECTOR, '.dropdown-menu div.pull-right a').click()
sleep(1)
if driver.current_url == sign_url:
    print('已返回登陆页面！')
else:
    print('未返回登陆页面！')
driver.quit()
