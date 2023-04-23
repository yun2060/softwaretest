# 3.	应用选择语法的联合使用方法编写测试用例：
# 以管理员身份登录 http://127.0.0.1:8047/mgr/sign.html，用户名 ：byhy 密码： 88888888。
# 点击添加药品，输入正确格式的药品名、编号和描述，点击创建。
# 预期结果为：成功登录后，检查药品列表第一项结果中 药品名、编号和描述都是正确的。
# python测试用例程序命名为：学号+UI_5。
from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")  # 导入驱动
driver.get("http://127.0.0.1:8047/mgr/sign.html")
driver.find_element(By.CSS_SELECTOR, '#username').send_keys('byhy')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('88888888')
driver.find_element(By.CSS_SELECTOR, '.btn').click()
sleep(1)
sample, test = ['阿莫西林', '001', '阿莫西林胶囊'], []
driver.find_element(By.CSS_SELECTOR, 'section>ul>li:nth-child(3)').click()
driver.find_element(By.CSS_SELECTOR, 'button>span').click()
driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(1) .form-control').send_keys('阿莫西林')
driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(2) .form-control').send_keys('001')
driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(3) .form-control').send_keys('阿莫西林胶囊')
driver.find_element(By.CSS_SELECTOR, '.col-lg-12 .btn-xs').click()
result = driver.find_elements(By.CSS_SELECTOR, '.search-result-item span:nth-of-type(even)')
for i in result[:3]:
    test.append(i.text)
if test == sample:
    print('正确')
else:
    print('错误')
driver.quit()
