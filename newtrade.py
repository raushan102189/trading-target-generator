from long import Long
from short import Short
# from fee import Fee
import pickle
numbering = 1


save = "no"
while save != "yes":

    current_price = float(input("current price: "))
    stoploss = float (input("stoploss: "))
    maxloss = float(input("maxloss: "))
    call = current_price >stoploss
    put = current_price < stoploss
    if  call:
        a = Long(current_price,stoploss,maxloss)
        e=a.longo()
        call_data = {numbering + 1:e}
        
     
        #
    elif put:
        b = Short(current_price, stoploss, maxloss)
        e = b.shorto()
        put_data = {numbering + 1:e}

 
        
    save = input("want to save it\nyes or no: ")
while save == "yes":
    if call:
        with open("long_data.txt","ab") as datas:
                trb = pickle.dump(call_data, datas)
    if put:
        with open("short_data.txt","ab") as datas:
                trb = pickle.dump(put_data,datas)
    break
        



write_remarks = input("write the cause: ")
with open("long_data.txt" ,"rb") as read_data:
    c =pickle.load(read_data)
    
print(c)
    

