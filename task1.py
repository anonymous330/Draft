
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time,os

import requests, bs4
import pickle,pprint
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os






# wait.until(ExpectedConditions.elementToBeClickable(element));

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)





def save_cookie(driver,location):
    pickle.dump(driver.get_cookies(),open(location,'wb'))

def load_cookies(driver,location,url=None):
    cookies=pickle.load(open(location,'rb'))
    driver.delete_all_cookies()
    url='https://www.google.com' if url is None else url
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)

def delete_cookie(driver,domains=None):
    cookies=driver.get_cookies()
    for cookie in cookies:
        if domains is not None:
            if str(cookie['domain']) in domains:
                cookies.remove(cookie)
        else:
            driver.delete_all_cookies()
            return


    driver.delete_all_cookies()

    for cookie in cookies:
        driver.add_cookie(cookie)


def get_data():
    url="https://dbt.mpdage.org/Agri_Index.aspx    "
    driver.get(url)
    print("Page title was '{}'".format(driver.title))
    # time.sleep(100)
    driver.find_element_by_xpath('//*[@id="AlertDiv"]/div[2]/div/div[1]/button').click()


    # .click()
    time.sleep(2)
    driver.quit()
    driver.find_element_by_link_text('लॉगिन').click()
    time.sleep(5)
    user=driver.find_element_by_name('ucLogin$txtUserName').send_keys(46998)
    passw=driver.find_element_by_id('ucLogin_txtPassword').send_keys('123')
    element = driver.find_element_by_xpath('//*[@id="ucLogin_form11"]/div[2]/div/div[5]/div[1]/div/img').screenshot('00.png') # find part of the page you want image of


    im = Image.open("00.png") # the second one
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save('01.png')
    text = pytesseract.image_to_string(Image.open('01.png'))
    print(text)
    text=text.replace(' ','')
    text=text.lower()
    print(text)
    captcha=driver.find_element_by_id('ucLogin_txtCaptcha').send_keys(text)

    sign=driver.find_element_by_name('ucLogin$imgLogin').click()
    time.sleep(5)
# save_cookie(driver,'/Users/rohittiwari/Documents/python codes/cookieReva.txt')

    try:
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_lbl_manufac').text
        save_cookie(driver,'/Users/rohittiwari/Documents/python codes/cookieP.txt')
        driver.quit()
    except NoSuchElementException:
        print('exception')
        get_data()


if __name__=='__main__':
    get_data()







