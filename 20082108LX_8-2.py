from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

# 2.	在浏览器中访问百度网站，将窗口最大化，鼠标悬停在顶部“设置”菜单项，暂停3秒，单击“关闭热搜”，查看界面状态变化；
# 打开新网页“http://sahitest.com/demo/dragDropMooTools.htm” ，拖拽“drag me”方块到“Item 3”上，查看是否出现了“dropped”文本，
# 出现则测试通过，否则失败。关闭浏览器。
driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")
ac = ActionChains(driver)
driver.get("https://www.baidu.com")
driver.maximize_window()
option = driver.find_element(By.CSS_SELECTOR, 'div #s-usersetting-top')
off = driver.find_element(By.CSS_SELECTOR, 'div .s-set-hotsearch')
ac.move_to_element(option).pause(3).move_to_element(off).click().perform()
ActionBuilder(driver).clear_actions()
driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
drag = driver.find_element(By.CSS_SELECTOR, '.drag')
Item = driver.find_elements(By.CSS_SELECTOR, 'div.item')[2]
ac.drag_and_drop(drag, Item).perform()
change = driver.find_element(By.CSS_SELECTOR, 'div.dropped')
if change.text == 'dropped':
    print('测试通过')
else:
    print('失败')
driver.quit()
