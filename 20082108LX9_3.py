from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import win32com.client as wc

# 3.	自己准备好两个png图片文件，仿照例题在https://tinypng.com网站中完成两种方式的文件上传。
# 先定位到该网页中可输入文件路径的input输入框，上传文件1，完成后截屏保存为sp1.png。
# 再利用pywin32库实现图片2的上传，完成后截屏保存为sp2.png。适当调整文件上传后的等待时间，使截屏图片能够反映成功上传后的完整信息。关闭浏览器。
pic1 = r"J:\first.jpg"
pic2 = r"J:\second.jpg"

driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
driver.get("https://tinypng.com")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(pic1)
driver.get_screenshot_as_file('sp1.png')
sleep(2)
driver.find_element(By.CSS_SELECTOR,'.target').click()
shell = wc.Dispatch("WScript.Shell")
sleep(10)
shell.Sendkeys(pic2 + '{ENTER}' + '\n')
sleep(2)
driver.get_screenshot_as_file('sp2.png')
driver.quit()
