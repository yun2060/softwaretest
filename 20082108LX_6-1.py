from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By

# 练习1：登录 https://cdn2.byhy.net/files/selenium/sample2.html，
# ①切换进入iframe框架，在其中选择所有动物类型并输出动物名称，
# ②切换回外层默认部分，点击“外部按钮”，
# ③输出网页中新出现的“你点击了外部按钮”文本信息。
# 练习2：在练习1主要操作过程和关闭浏览器操作之间，添加以下操控步骤：
# ①登录 https://cdn2.byhy.net/files/selenium/sample3.html，
# ②输出当前窗口的标题栏文本，点击打开新窗口的链接，
# ③切换到新窗口并输出新窗口的标题栏文本，
# ④返回原窗口，点击“功能按钮”，输出网页中新出现的“你点击了外部按钮”。
# 关闭浏览器
driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")  # 导入驱动
driver.get("https://cdn2.byhy.net/files/selenium/sample2.html")

driver.switch_to.frame('frame1')
animals = driver.find_elements(By.CSS_SELECTOR, '.animal')
for i in animals:
    print(i.text)
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, '#outerbutton').click()
print(driver.find_element(By.CSS_SELECTOR, '#add').text)
driver.get("https://cdn2.byhy.net/files/selenium/sample3.html")
print(driver.title)
mainWindow = driver.current_window_handle
driver.find_element(By.CSS_SELECTOR, 'a').click()

driver.switch_to.window(driver.window_handles[1])
print(driver.title)

driver.switch_to.window(mainWindow)
driver.find_element(By.CSS_SELECTOR,'#outerbutton').click()
print(driver.find_element(By.CSS_SELECTOR, '#add').text)

driver.quit()
