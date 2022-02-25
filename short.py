class Short():
    def __init__(self,current,stoploss,maxloss):
        self.current = current
        self.stoploss = stoploss
        self.maxloss = maxloss

        b = self.shorto(current,stoploss,maxloss)
        print(b)

    def shorto(self,current,stoploss,maxloss):
        risk_on_1_share =  stoploss - current 
        quantity = (maxloss / risk_on_1_share)

    
        entry_price = current * quantity
        target = risk_on_1_share *2
        target_price = current - target 
        target_percentage = (current/ target_price)
        exit_price = target_percentage * entry_price
        stoploss_hit_percentage = current / stoploss 
        stoploss_hit_price = stoploss_hit_percentage * entry_price
    
        return (f"quantity ={quantity}\ntarget = {target_price}\nentry price"
        f"{entry_price}\nif right ={exit_price }and { 100*target_percentage - 100}"
        f"\nif wrong{stoploss_hit_price } and { 100 - 100*stoploss_hit_percentage} ")



