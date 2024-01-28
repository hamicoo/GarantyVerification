class Product:
    __numberOfItems = 0
    def __init__(self,_ID:int,_name:str,_start:str,_end:str,_date:str):
        self.iD = _ID
        self.name = _name
        self.start = _start
        self.end = _end
        self.date = _date

    def setName (self,_name):
        self.name = _name
        print(f"{_name} successfully Set !")
    def getName(self):
        return self.name

    def setStart(self, _start):
        self.start = _start
        print(f"{_start} successfully Set !")

    def getStart(self):
        return self.start

    def setEnd(self, _end):
        self.start = _end
        print(f"{_end} successfully Set !")

    def getEnd(self):
        return self.start

    def getDate(self):
        return self.date

