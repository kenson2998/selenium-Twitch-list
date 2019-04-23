from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

sys.path.append("/usr/local/bin/chromedriver")

d = webdriver.Chrome()

d.get("http://webdatacommons.org/webtables/")

element_a = d.find_element_by_xpath('//*[@id="toccontent"]/table[1]/tbody')
element_b = d.find_elements_by_tag_name('tr')
trs = {}
t = 0
for i in element_b:
    tds = []
    keynames = i.find_element_by_tag_name('th').text
    element_b_child = i.find_elements_by_tag_name('td')
    for ii in element_b_child:
        tds.append(ii.text)
    trs[keynames] = tds
    t += 1
x = []
for k, v in trs.items():
    x.append(k)


# selecta = input('1.{} 2.{} 3.{} 4.{}'.format(x[1], x[2], x[3], x[4]))
# print('your choose {} : {}'.format(selecta, trs[selecta]))


element_c = d.find_element_by_xpath('/html/body/div[5]/div[2]/table[1]')
element_c_th = element_c.find_elements_by_tag_name('th')
element_c_td = element_c.find_elements_by_tag_name('td')

for i in element_c_th:
    print(i.text)
for i in element_c_td:
    print(i.text)
d.close()