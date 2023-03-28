from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By

# 1.	在浏览器中打开百度新闻https://news.baidu.com/网站，
# 选择“热点要闻”栏目中的class名 为 focuslistnews 和 hotnews的元素，计算满足此条件的元素共有多少项，输出：“热点要闻栏目中有XX项焦点列表和热点新闻项”。
# 使用qiut()关闭浏览器。
driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")  # 导入驱动
driver.get("https://news.baidu.com/")
news = driver.find_elements(By.CSS_SELECTOR, '#left-col-wrapper .hotnews,#left-col-wrapper .focuslistnews')
print("热点要闻栏目中有{}项焦点列表和热点新闻项".format(len(news)))
# 2.	在上个操作步骤的关闭浏览器之前，
# 添加：按照次序选择子节点的任意两种不同的方式，完成对“热点要闻”栏目中的class名hotnews的元素中的第四个新闻标题的获取，
# 并输出显示文本信息。
forth_1 = driver.find_element(By.CSS_SELECTOR, '#left-col-wrapper .hotnews :nth-child(4)')
forth_2 = driver.find_element(By.CSS_SELECTOR, '#left-col-wrapper .hotnews :nth-of-type(4)')
print(forth_1, forth_2)
# 3.	在上个操作步骤的关闭浏览器之前，
# 添加：按照兄弟节点选择方式，完成对“热点要闻”栏目中的class名hotnews的元素的兄弟节点的选择，
# 并输出兄弟节点的全部可见文本。
print(driver.find_element(By.CSS_SELECTOR, '#left-col-wrapper .hotnews+ul').text)
driver.quit()
