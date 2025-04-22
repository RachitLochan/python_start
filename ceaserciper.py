def encode(x,y):
    i=0
    while i<len(x):
         ascii=ord(x[i])
         ascii=ascii+y
         caracter= chr(ascii)
         print(caracter,end="")
         i=i+1
def decode(x,y):
    i=0
    while i<len(x):
         ascii=ord(x[i])
         ascii=ascii-y
         caracter= chr(ascii)
         print(caracter,end="")
         i=i+1
#include<stdio.h>
#display all  words in one line use end = ""
go=str(input("enter encode to encode and decode to decode :- "))
enterword=str(input("put word -"))
num=int(input("enter your key - "))
if go == "encode":
    encode(enterword,num)
elif go == "decode":
    decode(enterword,num)
else:
    print(f"enter valid sattemaent bo not {enterword}" )

