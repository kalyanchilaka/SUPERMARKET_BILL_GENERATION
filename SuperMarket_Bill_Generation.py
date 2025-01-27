from datetime import datetime

print("----------------WELCOME TO KALYAN'S SUPERMARKET--------------------")
name=input("Enter Your Name: ")
lists='''

rice    Rs 60/kg
sugar   Rs 40/kg
salt    Rs 20/kg
oil     Rs 105/liter
maggi   Rs 10/each
biscuit Rs 40/each
powder  Rs 55/each
brush   Rs 12/each
'''

price = 0
totalprice = 0
finalprice = 0
pricelist = []
ilist = []
qlist = []
plist = []

items = {
    "rice": 60,
    "sugar": 40,
    "salt": 20,
    "oil": 105,
    "maggi": 10,
    "biscuit": 40,
    "powder": 55,
    "brush": 12
}

option = int(input("for in the list of items press-1: "))

if option == 1:
    print(lists)
    for i in range(len(items)):
        inp1 = int(input("if you want to buy press 1 or 2 for exist: "))
        if inp1 == 2:
            break
        if inp1 == 1:
            item = input("Enter Your Items: ")
            quantity = int(input("Enter Quatity: "))
            if item in items.keys():
                price = quantity * (items[item])
                pricelist.append((item, quantity, items, price))
                totalprice += price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                gst = (totalprice * 5) / 100
                finalamount = gst + totalprice
            else:
                print("your item is not available")
        else:
            print("you entered wrong number")
        inp = input("Can i  bill items yes or no: ")
        if inp == 'yes':
            pass
            if finalamount != 0:
                print(25 * "=", "KALYAN SUPERMARKET", 25 * "=")
                print(28 * " ", "NIRMAL")
                print("name:", name, 30 * " ", datetime.now())
                print("item", "quantity", "price")
                for i in range(len(ilist)):
                    print(ilist[i], qlist[i], plist[i])
                print("total price:", totalprice)
                print("gst:", gst)
                print("final amount:", finalamount)
        else:
            print("you entered wrong number")
else:
    print("you entered wrong number")
    
    
    
    
# Output:
# ----------------WELCOME TO KALYAN'S SUPERMARKET--------------------
# Enter Your Name: Kalyan
# for in the list of items press-1: 1

# rice    Rs 60/kg
# sugar   Rs 40/kg
# salt    Rs 20/kg
# oil     Rs 65/liter
# maggi   Rs 10/each
# biscuit Rs 40/each
# powder  Rs 55/each
# brush   Rs 12/each

# Example :

# if you want to buy press 1 or 2 for exist: 1
# Enter Your Items: rice
# Enter Quatity: 2
# Can i  bill items yes or no: yes
# ========================= KALYAN SUPERMARKET =========================
#                             NIRMAL
# name: Kalyan                              2021-09-26 16:34:25.549458
# item quantity price
# rice 2 120
# total price: 120
# gst: 6.0
# final amount: 126.0
# if you want to buy press 1 or 2 for exist: 2
# Process finished with exit code 0
