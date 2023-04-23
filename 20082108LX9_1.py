from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 1.	打开https://cdn2.byhy.net/files/selenium/test4.html网页，窗口最大化，
# 分别点击alter按钮、confirm按钮及prompt按钮，检查是否存在对应的弹出对话框，不存在则打印“未弹出！”；
# 存在则打印对话框提示信息文本，并分别点击alter对话框中“确定”按钮、confirm对话框中“取消”按钮，
# 以及在prompt对话框的输入框内输入“python之selenium自动化测试”文本且点击“确定”按钮。
# 针对confirm对话框和prompt对话框的操作进行检查（这两个操作执行后页面中有相应文本提示）。
# 前面的每个操作后暂停3秒，方便观察。关闭浏览器。

driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
driver.get("https://cdn2.byhy.net/files/selenium/test4.html")
ac = ActionChains(driver)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '#b1').click()
if EC.alert_is_present():
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
else:
    print('未弹出！')
ac.pause(3).perform()
driver.find_element(By.CSS_SELECTOR, '#b2').click()
if EC.alert_is_present():
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.dismiss()
else:
    print('未弹出！')
ac.pause(3).perform()
driver.find_element(By.CSS_SELECTOR, '#b3').click()
if EC.alert_is_present():
    driver.switch_to.alert.send_keys('python之selenium自动化测试')
    driver.switch_to.alert.accept()
else:
    print('未弹出！')
ac.pause(3).perform()
Add = driver.find_elements(By.CSS_SELECTOR, 'li')
if Add[0].text == '取消操作':
    print("成功")
else:
    print("失败")
if Add[1].text == '你想学习:python之selenium自动化测试':
    print("成功")
else:
    print("失败")
driver.quit()
