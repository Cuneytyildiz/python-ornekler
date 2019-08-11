#-*- coding: utf-8-*-
#3x-09-google.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def gogol(keyword):
    # google ile keyword araması yap
    profile = webdriver.FirefoxProfile()
    profile.native_events_enabled=True

    driver = webdriver.Firefox(profile)
    searchEngineUrl = "http://www.google.com"

    # firefox sayfasını aç ve google sitesine bağlan
    driver.get(searchEngineUrl)

    # Adı q olan html elemanını bul (arama kutusu)
    inputElement = driver.find_element_by_name("q")

    # keyword bilgisini arama kutusuna gir ve Return tuşuna tıkla
    inputElement.send_keys(keyword+Keys.RETURN)

    # Dikkat ! İncelemen bittiğinde sayfayı kapatmayı unutma
    # Bu kod, sayfayı otomatik kapatmaz
    # Otomatik kapanmasını isterseniz aşağıdaki iki satırın başındaki ifadeleri kaldırın

    # time.sleep(30) # 30 saniye bekle
    # driver.quit()  # sayfayı kapat


keyword = "Python Selenium"
gogol(keyword)