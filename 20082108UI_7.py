# 3.	以管理员身份登录 http://127.0.0.1:8047/mgr/sign.html，用户名 ：byhy 密码： 88888888。
# 在系统中添加3种药品，依次为：‘头孢盒装1’,‘YP-20023524’,‘头孢他啶注射液，每支15ml，10支装’； ‘头孢盒装2’,‘YP-20023525’,‘头孢他啶注射液，每支15ml，20支装’； ‘头孢盒装3’,‘YP-20023526’,‘头孢他啶注射液，每支15ml，30支装’；。
# 在系统中添加3个客户，依次为：‘南京鼓楼区中医院1’,‘2583426507’,‘江苏省-南京市-鼓楼区-中山北路-253’； ‘南京鼓楼区中医院2’,‘2583426508’,‘江苏省-南京市-鼓楼区-中山北路-254’； ‘南京鼓楼区中医院3’,‘2583426509’,‘江苏省-南京市-鼓楼区-中山北路-255’ 。
# 进入订单管理界面，添加一个订单，具体内容为：订单名称为 南京鼓楼中院头孢；客户选择 南京鼓楼区中医院2；药品选择头孢盒装1和头孢盒装2；每种药品数量填入 100盒。
# 预期结果为：成功登录后，添加订单成功。 python测试用例程序命名为：学号+UI_7.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")
driver.get("http://127.0.0.1:8047/mgr/sign.html")
driver.find_element(By.CSS_SELECTOR, '#username').send_keys('byhy')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('88888888')
driver.find_element(By.CSS_SELECTOR, '.btn').click()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '.fa-plus').click()
drugs = [['头孢盒装1', 'YP-20023524', '头孢他啶注射液，每支15ml，10支装'], ['头孢盒装2', 'YP-20023525', '头孢他啶注射液，每支15ml，20支装'],
         ['头孢盒装3', 'YP-20023526', '头孢他啶注射液，每支15ml，30支装']]
for i in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button>span').click()
    driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(1) .form-control').send_keys(drugs[i][0])
    driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(2) .form-control').send_keys(drugs[i][1])
    driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(3) .form-control').send_keys(drugs[i][2])
    driver.find_element(By.CSS_SELECTOR, '.col-lg-12 .btn-xs').click()
driver.find_element(By.CSS_SELECTOR, '.fa-user').click()
customers = [['南京鼓楼区中医院1', '2583426507', '江苏省-南京市-鼓楼区-中山北路-253'], ['南京鼓楼区中医院2', '2583426508', '江苏省-南京市-鼓楼区-中山北路-254'],
             ['南京鼓楼区中医院3', '2583426509', '江苏省-南京市-鼓楼区-中山北路-255']]
for j in range(3):
    driver.find_element(By.CSS_SELECTOR, 'button>span').click()
    driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(1) .form-control').send_keys(customers[j][0])
    driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(2) .form-control').send_keys(customers[j][1])
    driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(3) .form-control').send_keys(customers[j][2])
    driver.find_element(By.CSS_SELECTOR, '.col-lg-12 .btn-xs').click()
sample, test = ['南京鼓楼中院头孢', '南京鼓楼区中医院2', '头孢盒装1 * 100 头孢盒装2 * 100'], []
driver.find_element(By.CSS_SELECTOR, '.fa-paperclip').click()
driver.find_element(By.CSS_SELECTOR, '.glyphicon-plus').click()
driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(1) .form-control').send_keys('南京鼓楼中院头孢')
customer = Select(driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(2) select'))
customer.select_by_visible_text("南京鼓楼区中医院2")
drug = Select(driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(3) select'))
drug.select_by_visible_text('头孢盒装1')
drug.select_by_visible_text('头孢盒装2')
driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(3) div:nth-child(1) > input').send_keys('100')
driver.find_element(By.CSS_SELECTOR, '.col-lg-8 :nth-child(3) div:nth-child(2) > input').send_keys('100')
driver.find_element(By.CSS_SELECTOR, '.col-lg-12 .btn-xs').click()
order = driver.find_elements(By.CSS_SELECTOR, '.search-result-item-field :nth-child(2)')
test.append(order[0].text)
test.append(order[2].text)
test.append(order[3].text)
if sample == test:
    print('成功！')
else:
    print('失败！')
driver.quit()
