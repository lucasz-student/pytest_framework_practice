import pytest 
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage_1 import HomePage

class TestEndToEndPurchase(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
