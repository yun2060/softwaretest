# 2.	在医疗销售管理系统 http://127.0.0.1:8047/mgr/sign.html 中对异常登录进行测试。
# 要求：分别设计5个测试用例，包括：用户名为空、密码为空、用户名错误、密码错误、用户名和密码都错。
# 在excel文件中编写自己设计的测试用例（注意：测试用例要完整，既有测试数据，也要有预期结果），将其另存为csv格式的文档。
# 测试程序读取该文件，根据文件中的预期结果进行断言判断。
import codecs
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
data = csv.reader(codecs.open('20082108UI_10.csv', 'r', 'utf_8_sig'))
driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
driver.get("http://127.0.0.1:8047/mgr/sign.html")
for i in data:
    driver.find_element(By.CSS_SELECTOR, '#username').clear()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(i[0])
    driver.find_element(By.CSS_SELECTOR, '#password').clear()
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(i[1])
    driver.find_element(By.CSS_SELECTOR, '.btn').click()
    sleep(1)
    assert driver.switch_to.alert.text == i[2]
    driver.switch_to.alert.accept()
    sleep(1)
driver.quit()
