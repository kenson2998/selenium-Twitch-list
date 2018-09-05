### selenium + Chrome 爬取Twitch 實況列表

一開始想說用bfsoup4 ,但是Twitch沒這麼好撈，所以要動用到瀏覽器來模擬操作。<br>
往下滾動捲軸才會繼續動態載入更多玩家實況列表。<br>
這邊就不使用無窗模式了，因為版本更新問題，就把無窗口指令先槓掉，之後可以參考。<br>
開啟LOL實況的頁面，然後在做捲軸下來動作之前，必須仿真的先點擊一下頁面，<br>
所以我這邊選擇了頁面上的某一個小標題，當作我載入時等待頁面正確載入和點擊作用。<br>
如果10秒未找到該元素就會timeout錯誤，也可以自行加個判斷refresh頁面。<br>

```python
start_text='/html/body/div[1]/div/div/div[2]/div/main/div/div[3]/div/div/div/div[2]/div/div[4]/h4'
element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,start_text)))
driver.find_element_by_xpath(start_text).click()
```

設定約120個迴圈來查詢頁面，可自行再改次數。<br>
1.向下滾頁面一次
```python
ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
```
2.等待5秒給他載入標題。
```python
element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,title_xpath)))
```
3.把標題和url給變數d和e
```python
d=driver.find_element_by_xpath(title_xpath)
e=driver.find_element_by_xpath(url_xpath)
```
4.print出實況的玩家列表

```python
1: wake up https://www.twitch.tv/c9sneaky
2: element - no energy drinks today https://www.twitch.tv/elementlolz
3: stream original recuse imitações https://www.twitch.tv/yetz
4: madrugratis - https://www.twitch.tv/gratis150ml
#...
#中間省略
#...
20: ヘアーの虎 https://www.twitch.tv/haretti
21: 人生悔しいことだらけ https://www.twitch.tv/nagisatty
22: xD !sliver !mythicleague twitter.com/iiPolen https://www.twitch.tv/polen
23: FG jaimito duo coscu // dia 5 en argentina https://www.twitch.tv/lolwingz
#...略...
```