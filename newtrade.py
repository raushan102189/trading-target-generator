from long import Long
from short import Short


run_again = "yes"
while run_again == "yes":
    current_price = float(input("current price: "))
    stoploss = float (input("stoploss: "))
    maxloss = float(input("maxloss: "))
    if  current_price > stoploss:
        a = Long(current_price, stoploss, maxloss)
    elif current_price < stoploss:
        a = Short(current_price, stoploss, maxloss)
    
    run_again = input("want to run again\nyes or no: ")
