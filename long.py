from fee import Fee
import pandas as pd
from save_json import try_to_save
class Long():
    def __init__(self,current,stoploss,maxloss,reason):
        self.current = current
        self.stoploss = stoploss
        self.maxloss = maxloss
        self.reason = reason

        b = self.longo()
        print(b)

    def longo(self):
        risk_on_1_share = self.current - self.stoploss
        quantity = (self.maxloss / risk_on_1_share)

    
        entry_price = self.current * quantity
        target = risk_on_1_share *2
        target_price = target + self.current
        target_percentage = (target_price / self.current)
        exit_price = target_percentage * entry_price
        stoploss_hit_percentage = self.stoploss /self.current
        stoploss_hit_price = stoploss_hit_percentage * entry_price
        fee = Fee(entry_price,exit_price)
        total_fee = fee.run()
        fee_for_calc =fee.all_calc()
        net_profit = exit_price -(fee_for_calc +entry_price)
        try_to_save("long",self.current,target,self.stoploss,quantity,net_profit,self.reason)
       

       
    
       
        return (f"\nquantity ={quantity}\ntarget = {target_price}\nentry price"
        f"{entry_price}\nif right ={exit_price}and{100*target_percentage -100}"
        f"\nif wrong{stoploss_hit_price}and{100 - 100*stoploss_hit_percentage} "
        f"\n{ total_fee}"
        f"\nnet profit:{ exit_price -(fee_for_calc +entry_price)} ")



