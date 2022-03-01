class Fee():
       
        
    def __init__(self,entry_price,exit_price):
        self.MAKER_FEE = 0.0002
        self.TAKER_FEE = 0.0004
        self.entry_price = entry_price
        self.exit_price = exit_price
        self.run()
        # all_cost = self.entry_fee() + self.exit_fee()
        # print(all_cost)
    def run(self):
        all_cost = self.entry_fee() + self.exit_fee()
        return f"fee: {all_cost}"
 
       
    def entry_fee(self):
        entry_fees =self.entry_price * self.MAKER_FEE          
        # print(entry_fees)
        return entry_fees
    def exit_fee(self):
        exit_fees = self.exit_price * self.TAKER_FEE
        # print(exit_fees)
        return exit_fees

    
    # def all_fees(self):
    #     entry_charges = entry_fee(entr)
    #     exit_charges = exit_fee()
    #     calculate = entry_charges + exit_charges
    #     return calculate
     
  

a = Fee(100,102)
b = a.run()
print(b)


# entryfee =a.entry_fee()
# exitfee= a.exit_fee()
# c = entryfee+exitfee
# print(c)
# # a.exit_fee()

