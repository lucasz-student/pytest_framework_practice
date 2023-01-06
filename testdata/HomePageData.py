import json

class HomePageData():

    @staticmethod
    def getData():
        with open(r"C:\Users\lucas\OneDrive\Desktop\complete_pytest_framework\TestData\vegetables.json", "r") as f:
            vdict = json.load(f)
            return[vdict]
            
