from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from time import sleep

# 1.	在浏览器中访问百度网站，将窗口最大化，鼠标置于顶部“地图”菜单项，右键单击，暂停3秒查看界面状态，
# 使用move_by_offset函数将鼠标移动到界面中任何一个热搜超链接上（调试找到适合的偏移量），进行点击，等待5秒，
# 在新打开网页中，应用鼠标滚轮使页面底部的“相关搜索”出现在屏幕中，等待5秒。关闭浏览器。
driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")
ac = ActionChains(driver)
driver.get("https://www.baidu.com")
driver.maximize_window()
Map = driver.find_element(By.CSS_SELECTOR, '#s-top-left :nth-child(3)')
ac.move_to_element(Map).context_click().pause(3).perform()
ActionBuilder(driver).clear_actions()
ac.move_by_offset(400, 320).click().perform()
sleep(5)
ActionBuilder(driver).clear_actions()
driver.switch_to.window(driver.window_handles[1])
relevant = driver.find_element(By.CSS_SELECTOR, 'div .rs-label_ihUhK')
ac.scroll_to_element(relevant).perform()
sleep(5)
driver.quit()
