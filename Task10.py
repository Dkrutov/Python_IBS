from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


s = Service('chromedriver.exe')
drv = webdriver.Chrome(service=s)
drv.get('http://google.com/ncr')
assert 'Google' in drv.title
elm = drv.find_element('name', 'q')
elm.send_keys('selenide')
elm.send_keys(Keys.RETURN)
assert 'selenide.org' in drv.find_element('tag name', 'cite').text
elm = drv.find_element('link text', 'Images')
elm.click()
assert 'selenide.org' in drv.find_element('xpath', '//*[@id="islrg"]/div[1]/div[1]/a[2]/div').text
elm = drv.find_element('xpath', '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]')
elm.click()
assert 'selenide.org' in drv.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/cite').text
drv.close()




