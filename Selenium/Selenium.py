from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get("http://www.google.com")
sleep(30)