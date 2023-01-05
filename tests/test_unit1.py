from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass

class TestHomepage(BaseClass): 
    def test_addtocart(self, getData):
        # Use getData for dictionary
        log = self.getLogger()

        for i in range(1, 11):
            search = self.driver.find_element_by_xpath("//input[@type='search']").sendkeys(getData[f"vegetable{i}"])
            addToCart = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[3]/button").click()
        
        cartNumber = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div[3]/div[1]/table/tbody/tr[1]/td[3]/strong")
        
        assert cartNumber.text == "10"
        


    @pytest.fixture(params=HomePageData.getData())
    def getData(request):
        return request.param 

