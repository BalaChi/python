# puriyala

class mygen():
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    def  __iter__(self):
        return self