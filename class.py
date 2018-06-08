class SquaringNumbers:
    def _init_(self, squaring,printSquare):
        self.inputNumber = " "
    def squaring(self):
        self.inputNumber = int(raw_input())
    def printSquare(self):
        print(self.inputNumber ** 2)
    def cubing(self):
        self.inputNumber = self.inputNumber ** 3
    def printCube(self):
        print(self.inputNumber)
while True:
    n = SquaringNumbers()
    n.squaring()
    print("This is the square of that number.")
    n.printSquare()
    n.cubing()
    print("This is the cube of that number.")
    n.printCube()
    

        
        




        
    
        
    
    
    



    

        
        
        

