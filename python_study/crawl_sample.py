# eclass.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="/Users/amgstation/Downloads/chromedriver")
url = 'https://lgcns.lglifecare.com/Home/Login'
driver.get(url)

driver.find_element_by_id('txtID').send_keys('###id###')
driver.find_element_by_id('txtPW').send_keys('###pw###')
driver.find_element_by_id('txtPW').send_keys(Keys.ENTER)
driver.implicitly_wait(5)


element = driver.find_elements_by_class_name('btnClosePop')


for i in element:
    driver.execute_script("arguments[0].click();", i)

driver.get('https://lgcns.lglifecare.com/OpenPage/6053')
html = driver.page_source # 페이지의 elements모두 가져오기
soup = BeautifulSoup(html, 'html.parser') # BeautifulSoup사용하기
print(soup)
notices = soup.select('#currPromotionArea > ul > li')
print(notices)
for n in notices:
    print(n.text.strip())
