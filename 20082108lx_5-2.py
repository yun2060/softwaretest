from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By

# 2.	在浏览器中打开：京东商城网页https://www.jd.com/，
# 应用按照次序选择元素的方法去检查页面左侧导航栏中是否有如下菜单：
# “家用电器|电脑 / 办公|男装 / 女装 / 童装 / 内衣|女鞋 / 箱包 / 钟表 / 珠宝|房产 / 汽车 / 汽车用品|食品 / 酒类 / 生鲜 / 特产|医药保健 / 计生情趣|机票 / 酒店 / 旅游 / 生活|安装 / 维修 / 清洗 / 二手”，
# 再使用兄弟节点选择方法定位页面头部导航栏中“京东超市”后三项菜单是否为“秒杀”、“便宜包邮”、“京东生鲜”，输出检查结果。
# 关闭浏览器。将python测试用例程序命名为：学号+lx_5-2.py
driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")  # 导入驱动
driver.get("https://www.jd.com/")
menu = '家用电器|电脑 / 办公|男装 / 女装 / 童装 / 内衣|女鞋 / 箱包 / 钟表 / 珠宝|房产 / 汽车 / 汽车用品|食品 / 酒类 / 生鲜 / 特产|医药保健 / 计生情趣|机票 / 酒店 / 旅游 / 生活|安装 / 维修 / 清洗 / 二手'
menu_test = ''
text = driver.find_elements(By.CSS_SELECTOR, '.cate_menu_item:nth-of-type(odd)')
for i in text:
    menu_test = menu_test + i.text + '|'
if menu == menu_test[:-1]:
    print('正确')
else:
    print("错误")
top, top_test = ["秒杀", "便宜包邮", "京东生鲜"], []
bro = driver.find_elements(By.CSS_SELECTOR, '#navitems-group1 li~li')
for i in bro:
    top_test.append(i.text)
if top == top_test:
    print("正确")
else:
    print("错误")
driver.quit()
