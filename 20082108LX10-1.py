# 2.	在https://www.byhy.net/_files/stock1.html 网页中
# 修改“股票名称”输入框的边框为“3px solid red”，删除输入框的提示输入内容placeholder属性；
# “一句话建议”输入框的提示输入内容placeholder属性改为“说说哪个股票最优”，输入文本颜色为“绿色”、14px、加粗且居中；
# 查询结果第一条的背景色为黄色。在“一句话建议”输入框中输入“不好说”。
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
driver.get("https://www.byhy.net/_files/stock1.html")
driver.execute_script('''document.getElementById('kw').style='3px solid red';
document.getElementById('kw').removeAttribute('placeholder');''')
driver.execute_script('''document.getElementById('suggestion').placeholder='说说哪个股票最优';
document.getElementById('suggestion').style='color: green; font-size: 14px; text-align: center; font-weight: bold';''')
driver.execute_script("document.getElementById('1').style='background: yellow'")
driver.find_element(By.ID, 'suggestion').send_keys('不好说')
sleep(1)
driver.quit()
