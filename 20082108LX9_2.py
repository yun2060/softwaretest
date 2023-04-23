from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 2.	在浏览器中访问百度网站并将窗口最大化，进行实操练习。
# 在百度搜索框中输入文本“Selenium”并搜索，点击“设置”菜单，打开“搜索设置”界面，在搜索语言范围中：设置“仅简体中文”，
# 在搜索结果显示条数中：设置搜索结果“每页50条”，点击保存设置。
# 此时应该会弹出alter类对话框，打印对话框内容，点击对话框中“确定”按钮，否则打印输出“未弹出！”。
# 检查搜索结果是否每页50条（注意：结果中有1条为“大家还在搜”，需把剔除此条记录），正确输出“每页显示50条设置通过！”，否则输出“设置失败！”。
# 重新打开“搜索设置”界面，点击“恢复默认”按钮，此时仍会弹出alter类对话框，打印对话框内容，点击对话框中“确定”按钮。
# 检查搜索结果是否每页10条，按上述过程输出测试结果。关闭浏览器。

driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
driver.get("https://www.baidu.com")
ac = ActionChains(driver)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, 'span #kw').send_keys('Selenium')
driver.find_element(By.CSS_SELECTOR, '.s_btn_wr').click()
driver.find_element(By.CSS_SELECTOR, '.pf').click()
driver.find_element(By.CSS_SELECTOR, '.setpref').click()
ac.pause(2).perform()
driver.find_element(By.CSS_SELECTOR, '#se-settting-2 input[value="1"]').click()
driver.find_element(By.CSS_SELECTOR, '#se-setting-3 input[value="50"]').click()
driver.find_element(By.CSS_SELECTOR, '#se-setting-7 .c-btn-primary').click()
if EC.alert_is_present():
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
else:
    print('未弹出！')
length1 = len(driver.find_elements(By.CSS_SELECTOR, 'div #content_left .result-op')) + len(
    driver.find_elements(By.CSS_SELECTOR, 'div #content_left .result'))
if length1 - 1 == 50:
    print('每页显示50条设置通过！')
else:
    print("设置失败！")
driver.find_element(By.CSS_SELECTOR, '.pf').click()
driver.find_element(By.CSS_SELECTOR, '.setpref').click()
driver.find_element(By.CSS_SELECTOR, '#se-setting-7 .c-gap-right-large').click()
if EC.alert_is_present():
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()
else:
    print('未弹出！')
length2 = len(driver.find_elements(By.CSS_SELECTOR, 'div #content_left .result-op')) + len(
    driver.find_elements(By.CSS_SELECTOR, 'div #content_left .result'))
if length2 - 1 == 10:
    print('每页显示10条设置通过！')
else:
    print("设置失败！")
driver.quit()
