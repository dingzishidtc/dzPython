#!/usr/bin/ruby -w
# -*- coding : utf-8 -*-


# require 'rubygems'

# require 'selenium-webdriver'
# # driver = webdriver.Chrome("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
# driver = Selenium::WebDriver.for :Chrome

# driver.navigate.to "http://baidu.com"

# sleep 3

# element = driver.find_element(:name, 'q')

# element.send_keys "Hello WebDriver!"

# element.submit

# puts driver.title

# driver.quit


# a=[1,3.22,2.3,12,5.55]
# b=[5,3.4,2.9,1.6,4]
# p a=a.sort
# p b=b.sort

# c=[]
# a.each{|a1|
# 	b.each{|b1|
# 		p a1,b1,c
# 		if a1<=b1
# 			c<<a1
# 			p "取a表第一"
# 		else
# 			c<<b1
# 			p "取b表第一"
# 		end
# 		p a1,b1,c
# 		p '--------------------------------'
# 		break
# 	}
# 	p a,b,a1
# 	p '出一次循环-------------------------'
# }

list_ = ['lll', 'lKK', 'wXy']
# def f(s):
    # return s[0:1].upper() + s[1:].lower()
# a = map(f, list_)
a=map(lambda x:x[0:1].upper()+x[1:].lower(), list_)

print(a)
print(list(a))