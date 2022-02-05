class Led:
    def __init__(self, color, status):
        self.color = color
        self.status = status
        
    def getcolor(self):
        return(self.color)
    
    def setStatus(self, status):
        self.status = status
        
    def getStatus(self):
        return(self.status)
    
led01 = Led("Red", False)
print(Led.getStatus(led01))
Led.setStatus(led01, True)
print(Led.getStatus(led01))