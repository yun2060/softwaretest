# 3.	调用JS完成以下操作：在浏览器中访问百度网站，获取并输出当前网页的标题和地址；
# 弹出alert弹窗显示“你好！”再点击确定关闭；
# 设置搜索框输入字体颜色为蓝色加粗，value值为“selenium”，边框为绿色，删除搜索框元素的autocomplete属性；
# 执行搜索查询；在网页中拉动滚动条至右下角，再滑动到顶部。关闭浏览器。
# 整个过程适当添加等待时间，使相关步骤的操作可见。

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("J:\\softwaretest\\chromedriver.exe")
driver.get("https://www.baidu.com")
print(driver.execute_script("return document.title"))
print(driver.execute_script('return document.URL'))
driver.execute_script('window.alert("你好！")')
sleep(1)
driver.switch_to.alert.accept()
sleep(1)
driver.execute_script('''document.getElementById("kw").style="color: blue; font-weight: bold; border-color: green";
                      document.getElementById("kw").value="selenium";
                      document.getElementById("kw").removeAttribute("autocomplete");''')
driver.execute_script('document.getElementById("su").click()')
sleep(2)
driver.execute_script('window.scrollTo(0,document.body.clientHeight)')
sleep(2)
driver.execute_script('document.documentElement.scrollTop=0')
sleep(1)
driver.quit()
