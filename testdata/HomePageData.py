import json

class HomePageData():

    @staticmethod
    def getData():
        with open("vegetables.json") as f:
            vdict = json.load(f)
            return vdict
