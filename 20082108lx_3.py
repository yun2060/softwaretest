from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")  # 导入驱动
# 1.	在https://www.51job.com/网站中，点击搜索栏中的添加工作地点的元素，将会弹出选择地区的新界面，
# 在此界面中，检查是否有已被选中的地区，如果有，依次进行删除操作，然后点击“上海”，确定选择。使用qiut()关闭浏览器。
driver.get("https://www.51job.com/")
driver.find_element(By.ID, 'work_position_input').click()
sleep(1)
ele = driver.find_elements(By.CLASS_NAME, "ttag")
while len(ele) != 0:
    driver.find_element(By.CLASS_NAME, "ttag").click()
driver.find_element(By.ID, 'work_position_click_center_right_list_category_000000_020000').click()
driver.find_element(By.ID, 'work_position_click_bottom_save').click()
# 2.	在上个操作步骤的关闭浏览器之前，添加：获取网站显示语言的元素的文本内容，
# 如果为“简”则输出：“本网站现以简体中文版显示”，如果为“EN”需输出：“本网站现以英文版显示”。
if driver.find_element(By.ID, 'languagelist').get_attribute('innerText')[0] == '简':
    print("本网站现以简体中文版显示")
elif driver.find_element(By.ID, 'languagelist').get_attribute('innerText')[0] == 'E':
    print("本网站现以英文版显示")
# 3.	在上个操作步骤的关闭浏览器之前，添加：清空搜索输入框，再向输入框中传入“python”文本。
driver.find_element(By.ID, 'kwdselectid').clear()
driver.find_element(By.ID, 'kwdselectid').send_keys("python")
# 4.	在上个操作步骤的关闭浏览器之前，添加：
# ①获取并输出“扫码登录”的二维码资源（src）信息；
pic = driver.find_element(By.ID, 'qrimg').get_attribute("src")
print(pic)
# ②获取输入框中的文本信息，判定是否为“python”，并输出检查结果；
sleep(3)
content = driver.find_element(By.ID, 'kwdselectid').get_attribute("preval")
if content == 'python':
    print("匹配")
else:
    print("不匹配")
# ③点击搜索按钮，将搜索到的第一条信息对应的全部HTML文本内容抓取并输出；
driver.find_element(By.CLASS_NAME, 'top_wrap').find_element(By.TAG_NAME, 'button').click()
sleep(3)
print(driver.find_element(By.CLASS_NAME, 'sensors_exposure').get_attribute("textContent"))
# ④点击“最新优先”选项卡，将此时搜索到的第一条信息对应的可见文本内容抓取并输出。
ch_list = driver.find_element(By.CLASS_NAME, 'tleft').find_elements(By.CLASS_NAME, "ss")
ch_list[1].click()
sleep(3)
print(driver.find_element(By.CLASS_NAME, 'sensors_exposure').get_attribute("textContent"))
# ⑤点击“薪资优先”选项卡，将此时搜索到的第一条信息对应的所有文本内容抓取并输出。
ch_list[2].click()
sleep(3)
print(driver.find_element(By.CLASS_NAME, 'sensors_exposure').get_attribute("textContent"))
driver.quit()
