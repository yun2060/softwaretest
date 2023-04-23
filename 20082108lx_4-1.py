from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By

# 在https://cdn2.byhy.net/files/selenium/sample1.html 网页中，使用CSS Selector
# ①根据tag名选择此页中的输入框并输入“查看完毕！”，
# ②根据id属性选择此页面底部的版权信息并输出，
# ③选择此页中所有class属性值为plant的元素并依次输出。
driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")  # 导入驱动
driver.get("https://cdn2.byhy.net/files/selenium/sample1.html")
driver.find_element(By.CSS_SELECTOR, 'input').send_keys('查看完毕！')
print(driver.find_element(By.CSS_SELECTOR, '#bottom'))
plant=driver.find_elements(By.CSS_SELECTOR, '.plant')
for i in range(len(plant)):
    print(plant[i].text)