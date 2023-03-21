from selenium import webdriver  # 导入selenium包
from selenium.webdriver.common.by import By

# 2.	打开2345天气王网站https://tianqi.2345.com/，获取网页中当前城市名称，
# 查看今天以及之后一周内的天气情况，输出当前城市一周内的最高气温和最低气温，输出格式为：
# AAA（当前城市名称）一周内最高气温为XX摄氏度，最低气温为YY摄氏度。
# 将python测试用例程序命名为：学号+lx_4-2.py
driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")  # 导入驱动
driver.get("https://tianqi.2345.com/")
city_n = driver.find_element(By.CSS_SELECTOR, '.banner .banner-city-change span').text
tem = driver.find_elements(By.CSS_SELECTOR, '.banner-right-con-list-temp')
tem_low, tem_high = [], []
for i in range(7):
    tem_low.append(int(tem[i+1].text[:-1].split('~')[0]))
    tem_high.append(int(tem[i+1].text[:-1].split('~')[1]))
tem_low.sort()
tem_high.sort()
print('{}一周内最高气温为{}摄氏度，最低气温为{}摄氏度。'.format(city_n, tem_high[-1], tem_low[0]))
