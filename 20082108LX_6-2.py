# 2.	打开网易云音乐https://music.163.com/网站，
# 点击“排行榜”，在左侧菜单栏中点击“新歌榜”，在歌曲列表中找出排名上升最多和下降最多的歌曲名称及歌手，输出格式为：
# 排名上升最多：歌曲名：XXX   歌手：YYY（若有上升位次相同的换行列出）
# 排名下降最多：歌曲名：XXX   歌手：YYY（若有下降位次相同的换行列出）
# 将python测试用例程序命名为：学号+ LX_6-2.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("J:\softwaretest\chromedriver.exe")
driver.get("https://music.163.com/")
driver.find_element(By.CSS_SELECTOR, "#g_nav2 > div > ul > li:nth-child(2) > a").click()
driver.switch_to.frame('g_iframe')
driver.find_element(By.CSS_SELECTOR, '#toplist li:nth-child(2) a').click()

songs = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
max_up = {"song_name": "", "singer_name": "", "up": -1}
max_down = {"song_name": "", "singer_name": "", "down": -1}
for song in songs:
    song_name = song.find_element(By.CSS_SELECTOR, "td:nth-child(2) b").get_attribute('title')
    singer_name = song.find_element(By.CSS_SELECTOR, 'td:nth-child(4)>div').get_attribute('title')
    flag = song.find_element(By.CSS_SELECTOR, 'td:nth-child(1) div.rk span')
    if flag.get_attribute('class') == 'ico u-icn u-icn-73 s-fc9':  # 上升歌曲
        num = int(flag.text)
        if num == max_up["up"]:
            max_up["song_name"] += "\n" + song_name
            max_up["singer_name"] += "\n" + singer_name
        elif num > max_up["up"]:
            max_up["song_name"] = song_name
            max_up["singer_name"] = singer_name
            max_up["up"] = num
    elif flag.get_attribute('class') == 'ico u-icn u-icn-74 s-fc10':  # 下降歌曲
        num = int(flag.text)
        if num == max_down["down"]:
            max_down["song_name"] += "\n" + song_name
            max_down["singer_name"] += "\n" + singer_name
        elif num > max_down["down"]:
            max_down["song_name"] = song_name
            max_down["singer_name"] = singer_name
            max_down["down"] = num
print("排名上升最多：歌曲名：{}   歌手：{}".format(max_up['song_name'], max_up['singer_name']))
print("排名下降最多：歌曲名：{}   歌手：{}".format(max_down['song_name'], max_down['singer_name']))
driver.quit()
