# 3.	在医疗销售管理系统中先运行学号+UI_8测试用例，保证系统中有数据。
# 再完成以下测试过程的编写：正常登录http://127.0.0.1:8047/mgr/sign.html 后，点击药品按钮，依次获取已有药品信息，
# 将药品名称中的“头孢”替换为 “阿奇霉素”；编号改为“H20010556 ”（另外两个末位为5和4），描述信息改为“阿奇霉素注射液，每支2ml，10支装” （另外两个为20支和30支装）。
# 改好的信息保存至medicine.csv文件中，再从文件中读取信息完成新药品的添加操作。
import codecs
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def login(a):  # 登录
    a.get("http://127.0.0.1:8047/mgr/sign.html")
    a.find_element(By.XPATH, '//*[@id="username"]').send_keys('byhy')
    a.find_element(By.XPATH, '//*[@id="password"]').send_keys('88888888')
    a.find_element(By.XPATH, '//*[@class="btn btn-primary btn-block btn-flat"]').click()
    sleep(1)


def get_info(a):  # 获取已有药品信息
    a.find_element(By.CSS_SELECTOR, '.fa-plus').click()
    sleep(1)
    med_info = []
    tables = a.find_elements(By.XPATH, '//*[@id="root"]/div/section[2]/div[@class="search-result-item"]')
    for i in tables:
        result = []
        field = i.find_elements(By.CSS_SELECTOR, 'span:nth-child(2)')
        for j in field:
            result.append(j.text)
        med_info.append(result)
    return med_info


def chinfo(a):  # 修改药品信息
    n, m = 6, 10
    for i in a:
        i[0] = i[0].replace('头孢', '阿奇霉素')
        i[1] = 'H2001055' + str(n)
        i[2] = "阿奇霉素注射液，每支2ml，" + str(m) + "支装"
        n = n - 1
        m = m + 10


def save_to_csv(a):  # 保存到csv中
    with codecs.open('20082108UI_11.csv', 'w', 'utf_8_sig') as f:
        csv.writer(f).writerows(a)
    data = csv.reader(codecs.open('20082108UI_11.csv', 'r', 'utf_8_sig'))
    return data


def add(a, b):  # 添加药品记录
    a.find_element(By.XPATH, '//*[@class="fa fa-plus"]').click()
    sleep(1)
    for data in b:
        a.find_element(By.XPATH, '//button/span').click()
        for i in range(0, len(data)):
            a.find_elements(By.XPATH, '//div[@class="col-lg-8 col-md-8 col-sm-8"]//div/*')[i].send_keys(data[i])
        a.find_element(By.XPATH, '//button[@class="btn btn-green btn-outlined btn-xs"]').click()


# def main():
driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
login(driver)
med_infos = get_info(driver)
chinfo(med_infos)
csv_data = save_to_csv(med_infos)
add(driver, csv_data)
driver.quit()


# main()
