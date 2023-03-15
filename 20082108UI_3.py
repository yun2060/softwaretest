from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By
from time import sleep

# 3.	以管理员身份登录 http://127.0.0.1:8047/mgr/sign.html，用户名 ：byhy 密码： 88888888。
# 点击添加客户，输入客户名为“南京中医院”的客户，填写客户基本信息；
# 然后再点击编辑，修改客户名为：“南京省中医院”。
# 预期结果为：成功登录后，检查客户列表第一项结果中客户名、电话、地址信息都是正确的（修改后的结果）。
driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")  # 导入驱动
driver.get("http://127.0.0.1:8047/mgr/sign.html")
driver.find_element(By.ID, 'username').send_keys('byhy')
driver.find_element(By.ID, 'password').send_keys('88888888')
driver.find_element(By.CLASS_NAME, 'btn').click()
sleep(1)
list_input, list_output = ['南京中医院', '20082108', '南京雨花台'], []
driver.find_element(By.CLASS_NAME, 'btn-outlined').click()
table = driver.find_element(By.CLASS_NAME, 'col-md-8').find_elements(By.CLASS_NAME, 'form-control')
for i in range(len(table)):
    table[i].send_keys(list_input[i])
driver.find_element(By.CLASS_NAME, 'col-md-12').find_elements(By.CLASS_NAME, 'btn-xs')[0].click()
sleep(1)
driver.find_element(By.CLASS_NAME, 'btn-group').find_element(By.CLASS_NAME, 'btn-xs').click()
driver.find_element(By.CLASS_NAME, 'search-result-item').find_element(By.TAG_NAME, 'input').clear()
list_input[0] = '南京省中医院'
driver.find_element(By.CLASS_NAME, 'search-result-item').find_element(By.TAG_NAME, 'input').send_keys('南京省中医院')
driver.find_element(By.CLASS_NAME, 'search-result-item-actionbar').find_element(By.CLASS_NAME, 'btn-xs').click()
result = driver.find_element(By.CLASS_NAME, 'search-result-item').find_elements(By.TAG_NAME, 'span')[1::2]
for i in range(0, len(result)):
    list_output.append(result[i].text)
if list_input == list_output:
    print("正确")
else:
    print("错误")
driver.quit()
