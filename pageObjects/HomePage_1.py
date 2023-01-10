
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class HomePage: 

    def __init__(self, driver):
        self.driver = driver

    def searchBarSend(self, keys): 
        """Finds and types keys into searchbar"""
        search = self.driver.find_element_by_xpath("//input[@type='search']")
        search.send_keys(Keys.CONTROL, 'a')
        search.send_keys(keys)
        time.sleep(1.5)

    def addToCart(self):
        """Adds item to cart"""
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[3]/button").click()
        time.sleep(1)
    
    def cartNumber(self):
        """Returns number of vegetables in the cart"""
        number = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/div[1]/table/tbody/tr[1]/td[3]/strong")
        return number.text
