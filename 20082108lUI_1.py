from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")  # 导入驱动
sample, test = ['客户', '药品', '订单'], []
driver.get("http://127.0.0.1:8047/mgr/sign.html")
driver.find_element(By.ID, 'username').send_keys('byhy')
driver.find_element(By.ID, 'password').send_keys('88888888')
driver.find_element(By.CLASS_NAME, 'btn').click()
sleep(1)
k = driver.find_elements_by_xpath('//*[@id="root"]/aside/section/ul/li')
for ele in k:
    test.append(ele.text)
if test[1:4] == sample:
    print("测试通过")
else:
    print("测试不通过")
driver.quit()
