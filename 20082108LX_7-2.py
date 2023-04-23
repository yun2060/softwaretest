# 按照自己的性别、爱好进行单选、多选（至少选择两项）按钮选择；
# 对于目标城市选择框，先清除全部选项，再分别使用value属性值、可见文本、排列次序三种方法各选择一个城市，
# 然后使用排列次序去除的方法去掉用value属性值选中的选项；最后打印输出选中的性别、爱好及目标城市中选中的第一个选项。
# 将python测试用例程序命名为：学号+ LX_7-2.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
driver.get("J:\softwaretest\selector.html")
driver.find_element(By.CSS_SELECTOR, '#sexual input[value="男"]').click()
driver.find_element(By.CSS_SELECTOR, '#hobby input[value="C"]').click()
driver.find_element(By.CSS_SELECTOR, '#hobby input[value="Java"]').click()
city = Select(driver.find_element(By.CSS_SELECTOR, '#citys'))
city.deselect_all()
city.select_by_value("北京")
city.select_by_visible_text("上海")
city.select_by_index(2)
city.deselect_by_index(0)
print(driver.find_element(By.CSS_SELECTOR, '#sexual input[name="sexform"]:checked').get_attribute('value'))
hobbies = driver.find_elements(By.CSS_SELECTOR, '#hobby input[name="programform"]:checked')
for i in hobbies:
    print(i.get_attribute('value'))
print(city.first_selected_option.text)
driver.quit()
