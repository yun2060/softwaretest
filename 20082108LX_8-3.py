# 3.	在浏览器中访问百度网站，使用模拟键盘控制：
# 在搜索输入框中输入大写的“S”，然后输入小写的“elenium!”，对当前输入框内容进行全选、复制操作。
# 打开新网页“https://www.sogou.com”进入搜狗网站，在其搜索输入框中先执行粘贴，再输入“!”，暂停3秒，然后删除两个字符，执行回车操作，
# 检查是否出现查询结果，是查询结果页测试通过，否则测试失败。关闭浏览器。

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
ac = ActionChains(driver)
driver.get("https://www.baidu.com")
Input_b = driver.find_element(By.CSS_SELECTOR, 'span #kw')
ac.key_down(Keys.SHIFT).send_keys_to_element(Input_b, 's').key_up(Keys.SHIFT).send_keys_to_element(Input_b,
                                                                                                   'elenium!').perform()
ac.key_down(Keys.CONTROL).send_keys('a').send_keys('c').perform()
driver.get("https://www.sogou.com")
Input_s = driver.find_element(By.CSS_SELECTOR, '.sec-input')
ac.key_down(Keys.CONTROL).send_keys_to_element(Input_s, 'v').key_up(Keys.CONTROL).send_keys('!').pause(3).key_down(
    Keys.BACKSPACE).key_down(Keys.BACKSPACE).key_down(Keys.ENTER).perform()
sleep(1)
test_url = 'https://www.sogou.com/web?query=Selenium&'
if driver.current_url[:41] == test_url:
    print('测试通过')
else:
    print('失败')
driver.quit()
