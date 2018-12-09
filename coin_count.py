################################################################################################
## Program to count the coins for the given ruppee. Available coins are 10,5,2,1              ##
## Author Harish Bhat M.                                                                      ##
## Email harish.bhat.m@gmail.com                                                              ##
################################################################################################
class CoinCount():

    def __init__(self, rupee_amount):
        self.rupee_amount = rupee_amount
        self.COINS = (10,5,2,1)
        self.dct = {}
        self.count = 0
        self.__calculate()
        
    def __str__(self):
        st=""
        #print "Entered rupee is %d"%(self.rupee_amount)
        for i in self.COINS:
            if self.dct.has_key(i):
                st +=  "Count of Coin denomination %s is %s\n"%(str(i),str(self.dct[i]))
        return st
    
    def __dictify(self, coin):
        if self.dct.has_key(coin):
            self.dct[coin] += 1
        else:
            self.dct[coin] = 1

    def __calculate(self):
        while True:
            if self.count == self.rupee_amount:
                break
            for i in range(len(self.COINS)):
                while (self.count+self.COINS[i]) <= self.rupee_amount:
                        self.count += self.COINS[i]
                        self.__dictify(self.COINS[i])

if __name__ == "__main__":
    rupees = input("Enter the ruppes: ")
    print(CoinCount(rupees))
        
