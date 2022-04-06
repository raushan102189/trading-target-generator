import json
# trade_no = "raf" 
# trading_record = { "trade_no":trade_no}
# with open("trade.json", "w") as f:
#     json.dump(trading_record, f)
def try_to_save(short_long,entry,target,stoploss,quantity,net_profit,reason):
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        # print(data)
        for b in data:
            new_tradeNo = int(b)
            # print(type(new_tradeNo))
            
        print(new_tradeNo) 
        trade_no = new_tradeNo +1
        print(trade_no)
    except:
        trade_no = 1
    
    json_data = {trade_no:{
        "short_long": short_long,
        "entry":entry,
        "target":target,
        "stoploss":stoploss,
        "quantity":quantity,
        "net_profit":net_profit,
        "reason":reason}
        }    
    try:
        with open("data.json", "r") as f:
            newdata =json.load(f)
            newdata.update(json_data)
    except FileNotFoundError:
        with open("data.json", "w") as f:
            json.dump(json_data,f,indent=7)
    else:
        with open("data.json", "w") as f:
            json.dump(newdata, f, indent=7)
 

# try_to_save(2,2,3,4,5)


    

      

         



# print(b)
# def save_json(coinname = coinname, entry = entry, quantity = quantity):
#     json_data = {coinname:{
#         "coinname":coinname,
#         "entry":entry,
#         "quantity":quantity}
#     }
#     try:
#         with open("data.json", "r") as f:
#             newdata =json.load(f)
#             newdata.update(json_data)
#     except FileNotFoundError:
#         with open("data.json", "w") as f:
#             json.dump(json_data, f,indent=4)
#     else:
#         with open("data.json", "w") as f:
#             json.dump(newdata, f,indent=4)
# save_json()