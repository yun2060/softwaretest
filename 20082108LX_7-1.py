from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# 要求：每完成一项上述操作，输出选中的元素。python测试用例程序命名为：学号+LX_7-1.py
driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
driver.get("https://cdn2.byhy.net/files/selenium/test2.html")
# 在radio框中选择“小江老师”；
driver.find_element(By.CSS_SELECTOR, '#s_radio input[value="小江老师"]').click()
print('单选框选中了：'+driver.find_element(By.CSS_SELECTOR, '#s_radio input[name="teacher"]:checked').get_attribute('value'))
# 在checkbox框中选择“小江老师”和“小雷老师”；
elements = driver.find_elements(By.CSS_SELECTOR, '#s_checkbox input[name="teacher"]:checked')
for i in elements:
    i.click()
driver.find_element(By.CSS_SELECTOR, '#s_checkbox input[value="小江老师"]').click()
driver.find_element(By.CSS_SELECTOR, '#s_checkbox input[value="小雷老师"]').click()
print('多选框选中了：'+driver.find_element(By.CSS_SELECTOR, '#s_checkbox input[name="teacher"]:checked').get_attribute('value'))
# 在select框的单选下拉列表中选择“小雷老师” ；
select = Select(driver.find_element(By.CSS_SELECTOR, '#ss_single'))
select.select_by_visible_text("小雷老师")
print('单选下拉框选中了：'+select.first_selected_option.text)
# 多选列表中选择全部选项
multi = Select(driver.find_element(By.CSS_SELECTOR, '#ss_multi'))
multi.deselect_all()
for j in multi.options:
    j.click()
    print('多选下拉框选中了：' + j.text)
driver.quit()
