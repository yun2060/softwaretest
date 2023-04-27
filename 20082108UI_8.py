# 1.	修改UI_7程序，要求在执行所有操作前，先确定系统中没有订单、客户和药品，如果有，点击删除按钮删除掉。
# 注意：订单数据依赖于客户和药品，必须先删除订单，然后方可删除客户和药品。
# 修改部分的元素选择过程用XPath方法实现。预期结果仍为：成功登录后，添加订单成功。
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


def login(a):  # 登录
    a.get("http://127.0.0.1:8047/mgr/sign.html")
    a.find_element(By.XPATH, '//*[@id="username"]').send_keys('byhy')
    a.find_element(By.XPATH, '//*[@id="password"]').send_keys('88888888')
    a.find_element(By.XPATH, '//*[@class="btn btn-primary btn-block btn-flat"]').click()
    sleep(1)


def del_list(a):  # 删除各个记录
    list_ele = a.find_elements(By.XPATH, '//*[@class="search-result-item"]')
    list_del = a.find_elements(By.XPATH, '//div//label[last()]')
    if len(list_ele) != 0:
        for i in list_del:
            i.click()
            if EC.alert_is_present():
                a.switch_to.alert.accept()
    else:
        print('null!')


def page_check(a):  # 检查多页情况并执行单页多页操作
    page = a.find_elements(By.XPATH, '//ul[@class="pagination"]/li')
    if not page:
        del_list(a)
    else:
        for i in range(0, len(page) - 3):
            del_list(a)
            sleep(1)


def clear(a):  # 删除整合
    a.find_element(By.XPATH, '//*[@class="fa fa-paperclip"]').click()  # 删除订单
    sleep(1)
    page_check(a)
    a.find_element(By.XPATH, '//*[@class="fa fa-user"]').click()  # 删除客户
    sleep(1)
    page_check(a)
    a.find_element(By.XPATH, '//*[@class="fa fa-plus"]').click()  # 删除药品
    sleep(1)
    page_check(a)


def add(a, b):  # 添加记录
    for i in b:
        a.find_element(By.XPATH, '//button/span').click()
        for j in range(0, len(i)):
            a.find_elements(By.XPATH, '//div[@class="col-lg-8 col-md-8 col-sm-8"]//div/*')[j].send_keys(i[j])
        a.find_element(By.XPATH, '//button[@class="btn btn-green btn-outlined btn-xs"]').click()


def add_order(a, b):  # 增加订单
    c = 0
    a.find_element(By.XPATH, '//button/span').click()
    a.find_elements(By.XPATH, '//input')[0].send_keys(b[0])
    customer = Select(a.find_elements(By.XPATH, '//select')[0])
    customer.select_by_visible_text(b[1])
    drug = Select(a.find_elements(By.XPATH, '//select')[1])
    for i in b[2::2]:
        drug.select_by_visible_text(i)
    for j in b[3::2]:
        a.find_elements(By.XPATH, '//div[@class="col-lg-8 col-md-8 col-sm-8"]/div[3]/div/input')[c].send_keys(j)
        c = c + 1
    a.find_element(By.XPATH, '//button[@class="btn btn-green btn-outlined btn-xs"]').click()


def add_all(a):  # 增加整合
    a.find_element(By.XPATH, '//*[@class="fa fa-plus"]').click()
    sleep(1)
    add(a, drugs)
    a.find_element(By.XPATH, '//*[@class="fa fa-user"]').click()
    sleep(1)
    add(a, customers)
    a.find_element(By.XPATH, '//*[@class="fa fa-paperclip"]').click()
    sleep(1)
    add_order(a, orders)


def check_order():
    order = []
    o = driver.find_elements(By.XPATH, '//*[@id="root"]/div/section[2]/div[3]/div/*[2]')
    for i in range(0, len(o)):
        temp = o[i].text.split()
        if len(temp) == 1:
            order.append(''.join(temp))
        elif len(temp) > 2:
            for j in temp[::3]:
                temp.remove('*')
            for k in temp:
                order.append(k)
    sleep(1)
    if order == orders:
        print('订单添加成功！')
    else:
        print(order)


# 药品添加标准[名称，编号，描述]
drugs = [['头孢盒装1', 'YP-20023524', '头孢他啶注射液，每支15ml，10支装'], ['头孢盒装2', 'YP-20023525', '头孢他啶注射液，每支15ml，20支装'],
         ['头孢盒装3', 'YP-20023526', '头孢他啶注射液，每支15ml，30支装']]
# 客户添加标准[名称，联系方式，地址]
customers = [['南京鼓楼区中医院1', '2583426507', '江苏省-南京市-鼓楼区-中山北路-253'], ['南京鼓楼区中医院2', '2583426508', '江苏省-南京市-鼓楼区-中山北路-254'],
             ['南京鼓楼区中医院3', '2583426509', '江苏省-南京市-鼓楼区-中山北路-255']]
# 订单添加标准[订单名称，客户，药品1，数量，药品2，数量，药品3，数量...]
orders = ['南京鼓楼中院头孢', '南京鼓楼区中医院2', '头孢盒装1', '100', '头孢盒装2', '100']
driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
login(driver)
clear(driver)
add_all(driver)
sleep(1)
check_order()
driver.quit()
