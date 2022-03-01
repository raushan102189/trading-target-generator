from long import Long
from short import Short
# from fee import Fee
import pickle

run_again = "yes"
while run_again == "yes":
    current_price = float(input("current price: "))
    stoploss = float (input("stoploss: "))
    maxloss = float(input("maxloss: "))
    if  current_price > stoploss:
        a = Long(current_price, stoploss, maxloss)
        # b = a
        # print(b)
        # with open("data.txt") as data:
        #     data.write(f"is it work")
    elif current_price < stoploss:
        a = Short(current_price, stoploss, maxloss)
        # with open("data.txt") as data:
        #     data.write(a)
    
    run_again = input("want to run again\nyes or no: ")
