# from selenium.webdriver.remote.webelement import *

# ele = WebElement(None, "")

# i = 0
# for m in dir(WebElement) :
#     if m[0] == '_': continue
#     i += 1

#     print("方法 %d : ele.%s" % (i, m) )
#     print("     ")
#     f = getattr(ele, m, None)
#     print(f.__doc__)
#     print("     ")
#     print("======================================================")
#     print("     ")

a=[1,3,2,1,5]
b=[5,3,2,1,4]
a=a.sort
b=b.sort
c=[]
a.each{|a1|
 c<<a1
}
print c
