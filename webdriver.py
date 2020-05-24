from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(30) # 隐性等待，最长等30秒  
driver.get("http://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/")
elem4 = driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td[2]/a")
elem4.click()
a = input("please input any key to quit")
driver.quit()