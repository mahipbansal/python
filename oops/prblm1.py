class calculator:

    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"square is {self.n * self.n}")
    
    def cube(self):
        print(f"square is {self.n * self.n * self.n}")
    
    def squareroot(self):
        print(f"square is {self.n ** (1/2)}")

calc = calculator(4)
calc.square()
calc.cube()
calc.squareroot()