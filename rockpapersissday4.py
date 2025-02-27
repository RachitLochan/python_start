import random
user=int(input("1 fro rck and 2 paper and 3 sissor   :---  "))

if(user==1):
    print('''  
   _____
  /     \
 /       \
 \       /
  \_____/
 ''')
    print("rock")

elif(user==2):
    print('''  
 _______________
|               |
|               |
|    PAPER      |
|               |
|_______________|

 ''')
    print("paper")
elif(user==3):
    print('''   
   __    __
  /  \  /  \
 /    \/    \
 \    /\    /
  \__/  \__/
     ||
     ||
     ||
     ||
     ||

''')
    print("sissors")

pc=random.randint(0,2)
if(pc==0):
    print('''  
   _____
  /     \
 /       \
 \       /
  \_____/
 ''')
    print("rock")

elif(pc==1):
    print('''  
 _______________
|               |
|               |
|    PAPER      |
|               |
|_______________|

 ''')
    print("paper")
elif(pc==2):
    print('''   
   __    __
  /  \  /  \
 /    \/    \
 \    /\    /
  \__/  \__/
     ||
     ||
     ||
     ||
     ||

''')
    print("sissors")

if(user==1 and pc==0 ):
    print("tie")
elif(user==2 and pc==1 ):
    print("tie")

elif(user==3 and pc==2 ):
    print("tie")

elif(user==1 and pc==2 ):
    print("you won agints random ness")

elif(user==1 and pc==1 ):
    print("i win the random race haha")

elif(user==2 and pc==0 ):
    print("you won randomly bro")
elif(user==2 and pc==2 ):
    print("you lost randomly bro")
elif(user==3 and pc==0 ):
    print("you lost randomly bro")
elif(user==3 and pc==1 ):
    print("you won randomly bro")



# people=["rachit","gg","amit","chigga"]
# choose=random.randint(0,3)
# print(people[choose])