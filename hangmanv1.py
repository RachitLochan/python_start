
#|----.
#|     |
#|     0
#|    /|\
#|     |
#|    /|\
#|    **
# lamao ded
import random
import string
live =8
words=["rachit","riwaz","gg","ama","baba","i","friend","relative"]
gameword=random.choice(words)
wordlist=gameword.split()
length = int(len(gameword))
print(length)
for i in  range(length):
   print("_", end=" ")
print("gess the word")
gess=(input("dal letter"))
for i in wordlist:
   while gess == i:
      
         print("right")
         length=length-1
         print(length)
         print("to go")
         if length==0:
            print("you won")
   while gess != i and live>-1:
      
      live = live-1
      print("galat fir dal")
      gess=(input("dal letter"))
      print(live)
      if live==1:
         print('''
         |----.
         |     |
         |     0
         |    /|\
         |     |
         |    /|\
              **
           lmao ded''')
         break
        
      if live==1:
         print('''
         |----.
         |     |
         |     0
         |    /|\\
         |     |
         |    /|\\
              **
         ''')
      if live==2:
         print('''
         |----.
         |     |
         |     0
         |    /|\
         |     |
         |    /|\
         ''')
      if live==3:
         print('''
         |----.
         |     
         |     0
         |    /|\
         |     |
         |    /|\
         ''')
      if live==4:
         print('''
         |
         |     
         |     0
         |    /|\
         |     |
         |     /\
         ''')
      if live==5:
         print('''
         
         |     
         |     0
         |    /|\
         |     |
         |    /|\
         ''')
      if live==6:
         print('''
         
               0
         |    /|\
         |     |
         |    /|\
         ''')
      if live==7:
         print('''
         
              
              0
             /|\
              |
             /|\
         ''')
      if live==8:
         print('''
         
              
              0
             /|\
              |
             /|\
            tf/*\ is this ''')
