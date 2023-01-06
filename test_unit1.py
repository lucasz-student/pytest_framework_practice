from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestHomepage(BaseClass): 
    def test_addtocart(self, getData):
        # Use getData for dictionary
        log = self.getLogger()

        for i in range(1, 11):
            
            self.driver.implicitly_wait(10)
            search = self.driver.find_element_by_xpath("//input[@type='search']").send_keys(Keys.CONTROL, 'a')
            search.send_keys(getData[f"vegetable{i}"])
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div[3]/button")))
            addToCart = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[3]/button").click()
        

        cartNumber = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/div[1]/table/tbody/tr[1]/td[3]/strong")
        
        assert cartNumber.text == "10"
        


    @pytest.fixture(params=HomePageData.getData())
    def getData(self, request):
        return request.param 

