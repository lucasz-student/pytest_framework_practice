from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from pageObjects.HomePage_1 import HomePage

class TestHomepage(BaseClass): 
    def test_addtocart(self, getData):
        # Use getData for dictionary
        log = self.getLogger()
        Homepage = HomePage(self.driver)

        for i in range(1, 11):
            
            self.waitTime(10)
            Homepage.searchBarSend(getData[f"vegetable{i}"])
            log.info(f"Adding vegetable {i} to bag")
            self.waitPresenceByXPATH("/html/body/div[1]/div/div[1]/div/div/div[3]/button")
            Homepage.addToCart()
        
        assert Homepage.cartNumber() == "10"
        


    @pytest.fixture(params=HomePageData.getData())
    def getData(self, request):
        return request.param 

