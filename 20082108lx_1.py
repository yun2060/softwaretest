from selenium import webdriver  # 导入selenium包


driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")  # 导入驱动

driver.get("http://127.0.0.1:8047/mgr/sign.html")  # 打开网页
# 实验一
# 获取当前页面的url：
driver.current_url
# 获取当前页面的title：
driver.title

# 窗口操作：
# 设置窗口大小
driver.set_window_size(1920, 1080)
# 窗口最小化
driver.minimize_window()
# 窗口最大化
driver.maximize_window()
# 全屏窗口
driver.fullscreen_window()

# 导航操作：
# 页面返回
driver.back()
# 页面前进
driver.forward()
# 页面刷新
driver.refresh()

# 窗口位置操作：
# 设置窗口位置坐标
driver.set_window_position(x=500, y=400)
# 设置窗口坐标及宽度和高度
driver.set_window_rect(x=30, y=30, width=450, height=450)
# 获取当前窗口位置坐标
driver.get_window_position()
# 获取当前窗口的长和宽
driver.get_window_size()

# 关闭窗口操作：
# 关闭当前窗口，或最后打开的窗口
driver.close()
# 关闭所有关联窗口，并且安全关闭session
driver.quit()


