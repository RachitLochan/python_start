import random
hangman_stages = [
    """
 ------
 |    |
 |    O
 |   /|\\
 |   / \\
 |    |
 |   ..
------
    """,
    """
 ------
 |    |
 |    O
 |   /|\\
 |   / \\
 |   
 |   
------
    """,
    """
 ------
 |    |
 |    O
 |   /|\\
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
 |    fasi ready
 |   
 |   
 |   
 |   
------
    """,
    """
 ------
 |    
 |    
 |   
 |   
 |   
 |   
------
    """
]

print("""
_________        .__  .__                          .____    .__  _____               .__         
\_   ___ \  ____ |  | |  | _____     ____   ____   |    |   |__|/ ____\____     _____|__| _____  
/    \  \/ /  _ \|  | |  | \__  \   / ___\_/ __ \  |    |   |  \   __\/ __ \   /  ___/  |/     \ 
\     \___(  <_> )  |_|  |__/ __ \_/ /_/  >  ___/  |    |___|  ||  | \  ___/   \___ \|  |  Y Y  \\
 \______  /\____/|____/____(____  /\___  / \___  > |_______ \__||__|  \___  > /____  >__|__|_|  /
        \/                      \//_____/      \/          \/             \/       \/         \/ 
""")



live = 7
words=["rachit","riwaz","gg","ama","baba","i","friend","relative"]
gameword=random.choice(words)
gameover=False
list=[]
for i in gameword:
        print(" _ ", end=" ")
while gameover is False:
    print("")
    gess=input("\nenter you letter - ").lower()#all print wrong as () forgot in llower
    gamestring=""
    length=len(gameword)
    count=0
    if gess in list:
          print("back lagi koi na phir try")
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
          print(f"hogaya? {7-live} sem khatam dost")

    print(gamestring)

    print(hangman_stages[live])

    if "_"not in gamestring:
          gameover=True
          print("bro you won in life man")
    if live==0:
          gameover=True
          print(f"letter tha {gameword}")
          print("lamao ded bhai ; 3-) ")
          print("hogaya bro collage life khatam")
