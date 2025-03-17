import random
#its legs are broken after your 3  misses(i gess) bug or feture lol right?! 
hangman_stages = [
    """
 ------
 |    |
 |    O
 |   /|\
 |   / \
 |   |
 |   
------
    """,
    """
 ------
 |    |
 |    O
 |   /|\
 |   / 
 |   
 |   
------
    """,
    """
 ------
 |    |
 |    O
 |   /|\
 |   
 |   
 |   
------
    """,
    """
 ------
 |    |
 |    O
 |   /|\
 |   
 |   
 |   
------
    """,
    """
 ------
 |    |
 |    O
 |   /|
 |   
 |   
 |   
------
    """,
    """
 ------
 |    |
 |    O
 |    |
 |   
 |   
 |   
------
    """,
    """
 ------
 |    |
 |    O
 |   
 |   
 |   
 |   
------
    """,
    """
 ------
 |    |
 |    
 |   
 |   
 |   
 |   
------
    """
]





live =7
words=["rachit","riwaz","gg","ama","baba","i","friend","relative"]
gameword=random.choice(words)
gameover=False
list=[]
for i in gameword:
        print("_", end=" ")
while gameover is False:
    
    gess=input("\nenter you letter - ").lower()#all print wrong as () forgot in llower
    gamestring=""
    length=len(gameword)
    count=0

    for letter in gameword:
            if gess==letter:
                gamestring+=gess
                list.append(letter)
            elif letter in list:
                  gamestring+=letter
            else:
                gamestring+="_"
    if gess not in gameword:
          live=live-1

    print(gamestring)

    print(hangman_stages[live])

    if "_"not in gamestring:
          gameover=True
          print("bro you won in life man")
    if live==0:
          gameover=True
          print("hogaya bro collage life khatam")



   

