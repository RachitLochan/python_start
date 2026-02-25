MENU = {
    "e": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "l": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "c": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def sorce(list):
    """find resorce availabe put same list of same number of variables as resourece """
    for saman in list:
        if list[saman] > resources[saman]: #if resources[item] < ingredients[item]:

            print(f"sorry not enough {saman}")
            return False
        
    return True

def usecoffeemachine(list):
    for item in list:
        resources[item]=resources[item]-list[item] #reduce stuff from resources
cook = True
profit=0.0
while cook == True:
    cup=input("watchu drinkin ? espresso latte or cappachino ?")
    
    if cup=='off':
        cook = False

    elif cup=='report':
            print(f"water : {resources['water']}")
            print(f"milk : {resources['milk']}")
            print(f"coffee : {resources['coffee']}")
            print(f"profit : {profit}")

    else:
        drink=MENU[cup] #from big list we took abstration of smaller list (just took 1 list out of 3 (e/l/c))
        
        if sorce(drink["ingredients"])== False:#very imp to take only the ingredient list cause original has cost also
            print(" ")
        elif cup not in MENU:
            print("Invalid selection.")

        else:    
            p = int(input("enter pennies"))*0.01
            n = int(input("enter nickel"))*0.05
            d = int(input("enter dimes"))*0.1
            q = int(input("enter quater"))*0.25
            money = p+n+d+q
            if money < MENU[cup]['cost']:#only comparing cost nothing more nothing less
                print(f"get out you poor duckf you need more funds take your {money}back")
            else:
                usecoffeemachine(drink["ingredients"])
                change=round(money-MENU[cup]['cost'],2)
                print(f"here is you change back { change }")
                profit=(profit+MENU[cup]['cost'])
                
