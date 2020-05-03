#encoding=utf8
#!/usr/bin/python3
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r'https://wenku.baidu.com/view/c5d88d850408763231126edb6f1aff00bed570ea.html')
time.sleep(1)
js = "window.scrollTo(0,3500)"
driver.execute_script(js)
time.sleep(1)
ele=driver.find_element_by_xpath("//p[@class='down-arrow goBtn']")
ele.click()
time.sleep(1)
for i in range(1,11):
	js = "window.scrollBy(0,500)"
	driver.execute_script(js)
	elem=driver.find_element_by_id("pageNo-"+str(i))
	print (elem.text,1111111111111111111111111111111111111111111111111111111111111111111)


