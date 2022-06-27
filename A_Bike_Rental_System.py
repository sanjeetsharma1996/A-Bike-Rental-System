class bikeshop:
    def __init__(self,stock):
        self.stock=stock

# show totale bike in store
    def DisplayStock(self):
        print("Total Bike",self.stock) 

#how many bike given for rent    
    def rentForBike(self,quantity):
        if quantity<=0:
            print("Enter the positive value or greater then zero")
        elif quantity>self.stock:
            print("Enter the value(less then stock)")
        else:
            self.stock=self.stock-quantity
            print("Total price",quantity*100)
            print("Total bike ",self.stock)

while True:
    obj=bikeshop(100)
    uc=int(input('''
1 Display stock
2 Rent for bike
3 Exit
        '''))
    if uc==1:
        obj.DisplayStock()
    elif uc==2:
        n=int(input("Enter the qty: "))
        obj.rentForBike(n)
    else:
        break




