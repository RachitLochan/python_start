import random
draw ='y'
sumpc=0
sumplayer=0
cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
pc1=random.choice(cards)
pc2=random.choice(cards)
player1=random.choice(cards)
player2=random.choice(cards)
pclist=[pc1,pc2]
print(f"pc top card is {pc1}")
print(f"your cards are {player1,player2}")
playerlist=[player1,player2]

while draw == 'y':
    
    draw=input("hit or miss? y/n")
    if draw == 'y':
        player2=random.choice(cards)
        playerlist.append(player2)
        print(f"you got {player2} now total is {sum(playerlist)}")
        
        if sum(playerlist)==21:
            print(f"you win t0tal is {sum(playerlist)} ")
            draw = 'n'
            exit()
        if sum(playerlist)>21:
            print(f"you lose  {sum(playerlist)}>21 ")
            draw = 'n'
            exit()


print(f"pc cards are {pc1} and {pc2} sum is {sum(pclist)}")


while sum(pclist)<=21:
    new_pc_card = random.choice(cards)
    pclist.append(new_pc_card)
    print(f"PC draws {new_pc_card}, total now {sum(pclist)}")

          
    if sum(pclist)==21:
        print(f"never mind house won lol we got {pc2}so total is 21 ")
        draw = 'n'
        exit()

    elif sum(pclist) > 21:
        print(f"PC stackoverflow with {sum(pclist)}! lol You win!") #lil gpt help not gon lie 
        exit()

if sum(playerlist)>sum(pclist) and sum(playerlist)<=21:
        print(f"you win t0tal is {sum(playerlist)} more than pc {sum(pclist)} ")
        draw = 'n'
if sum(playerlist)<sum(pclist) and sum(pclist)<=21:
      print(f"you lost pc got {pc2} so total is {sum(pclist)} more than your  {sum(playerlist)} lol  ")
      draw = 'n'
if sum(playerlist)>21 and sum(pclist)>21 :
     print("automatic house won dude as both more than 21 ")
     print(f"your {sum(playerlist)}and house got {sum(pclist)}")
     

   
