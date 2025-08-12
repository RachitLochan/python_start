auction = {}
bid="yes"
max=0
while bid == "yes":
    name=input("enter your name \n")
    amount=int(input("enter your amount \n"))
    auction[name]=amount
    bid=input("more bids? yes / no")
    print("\n "* 60)
for key in auction:
    if auction[key]>max:
        max=auction[key]
        winner=key
print(winner )
print("wins with ")
print(max)    
