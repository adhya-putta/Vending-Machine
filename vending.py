# Author   : Adhya Reddy Putta
# Email    : aputta@umass.edu
# Spire ID : 34219968

class VendingMachine:
    def __init__(self):
        self.inventory={}
        self.customer_balance=0.0
        self.purchases=[]
        self.sales_history2=[]

    def add_item(self, name, price, quantity):
        if name not in self.inventory:
            self.inventory.update({name:{'name':name,'price':price,'quantity':quantity}})
        else:
            self.inventory[name]['price']=price
            self.inventory[name]['quantity']+=quantity
        print (f"{quantity} {name}(s) added to inventory")
    def get_item_price(self,name):
        if name in self.inventory:
            return self.inventory.get(name).get('price')
        else:
            print("Invalid item")
            return None
    def get_item_quantity(self, name):
        if name in self.inventory:
            return self.inventory.get(name).get('quantity')
        else:
            print("Invalid item")
            return None
    def list_items(self):
        if not self.inventory:
            print ("No items in the vending machine")
        else:
            Keys=list(self.inventory.keys())
            Keys.sort()
            print("Available items:")
            for x in Keys:
                print(f"{x} (${self.inventory[x]['price']}): {self.inventory[x]['quantity']} available")
    def insert_money(self, dollar_amount:float):
        if dollar_amount==1.0 or dollar_amount==2.0 or dollar_amount==5.0:
            self.customer_balance+=dollar_amount
            self.customer_balance=self.customer_balance
            print (f"Balance: {round(self.customer_balance,2)}")
        else:
            print ("Invalid amount")
    def purchase(self, name):
            if name not in self.inventory:
                print("Invalid item")
            elif self.inventory[name]['quantity']==0:
                print(f"Sorry {self.inventory[name]['name']} is out of stock")
            elif self.customer_balance<=self.inventory[name]['price']:
                print(f"Insufficient balance. Price of {self.inventory[name]['name']} is {self.inventory[name]['price']}")
            else:
                self.inventory[name]['quantity']-=1
                self.customer_balance=self.customer_balance-self.inventory[name]['price']
                print(f"Purchased {name}\nBalance: {round(self.customer_balance,2)}")
                self.purchases.append(self.inventory[name]['price'])
                self.sales_history2.append([self.inventory[name]['name'],self.inventory[name]['price'],self.inventory[name]['quantity']])
    def output_change(self):
        if self.customer_balance>0:
            print (f"Change: {self.customer_balance}")
            self.customer_balance=0.0
        else:
            print ("No change")
    def remove_item (self, name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"{name} removed from inventory")
        else:
            print("Invalid item")
    def empty_inventory(self):
        self.inventory.clear()
        print ("Inventory cleared")
    def get_total_sales(self):
        total_sales=sum(self.purchases)
        return round(float(total_sales),2)
    def stats(self,N):
        if len(self.sales_history2)<N:
            N=len(self.sales_history2)
        if self.sales_history2==[]:
            print ("No sale history in the vending machine")
        else:
            num_of_sales=self.sales_history2[::-1]
            num_of_sales=num_of_sales[:N]
            sorted_history=sorted(num_of_sales)
            diction={}
            for i in sorted_history:
                if i[0] not in diction:
                    diction.update({i[0]:{'name':i[0],'spent':i[1],'numBought':1}})
                else:
                    diction[i[0]]['spent']+=i[1]
                    diction[i[0]]['numBought']+=1
            print(f"Sale history for the most recent {N} purchase(s):")
            for x in diction:
                print(f"{diction[x]['name']}: ${round(diction[x]['spent'], 2)} for {diction[x]['numBought']} purchase(s)")


