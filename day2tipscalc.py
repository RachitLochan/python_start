print(type(123))
print(type(12.3))
#print(type(12,3))
print(type(True))
#print(type(true))
print(type("qwerty"))

bill =float(input("what is the bill ?"))
tip  =float(input("what is the tip percentage"))
pep=float(input("how many perple are there bro ?"))
tip = bill*(tip/100)
bill = bill+tip
final = bill/pep
print ("each one will pay")
print(final)

