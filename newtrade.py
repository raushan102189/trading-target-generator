from long import Long
from short import Short
# from fee import Fee

numbering = 1


run = "yes"
while run == "yes":

    current_price = float(input("current price: "))
    stoploss = float (input("stoploss: "))
    maxloss = float(input("maxloss: "))
    reason = input("reason: ")
    call = current_price >stoploss
    put = current_price < stoploss
    if  call:
        a = Long(current_price,stoploss,maxloss,reason)

    elif put:
        b = Short(current_price, stoploss, maxloss,reason)

 
        
    run= input("want to run again it\nyes or no: ")





    

    

