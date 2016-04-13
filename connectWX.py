from selenium import webdriver
b = webdriver.Firefox();
b.get('https://wx.qq.com');
e = b.find_element_by_class('img');
print(e);
