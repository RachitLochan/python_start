alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#in 40 mins done while looking but
def encode(word,number):
    i=0
    prin=""
    for f in word:#f has no meaingman f is kuch be just dhunne use kiya if trrue or false if true then for will run
        go=alpha.index(f)+number#python malually checks caracter by carcter if it exist in the abube alpha list or not
        go=go%len(alpha)#basically like doing a hashfuntion bro kush nai 51%52=51 but zada hua toh 52%52=1 or 53%52=2
        prin+=alpha[go]#adding the value to the strinng prine = prine+alpga[go] []is use for string index eg [0]is first position
    print(f"lu tero encodede {prin}")
def decode(word,number):
    i=0
    prin=""
    for f in word:
        go=alpha.index(f)-number
        if go<0:
            go=go+len(alpha)#kud socha hehe can do go-len for encode too super proud 
        prin+=alpha[go]
    print(f"le tera decoaded {prin}")
logic=str(input("e to encode d to decode"))
sabd =str(input("enter word"))
key = int(input("enter key"))
if logic == 'e':
    encode(sabd,key)
elif logic == 'd':
    decode(sabd,key)
else:
    print(f"sahi dal {logic} nai chaelga ")


