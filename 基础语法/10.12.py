from random import randint

print("Guess what I think?")
num=randint(1,100)

Offon=False
while Offon==False:
    name=input()
    if name>num:
        print("too big")
        
    if name<num:
        print("too small")
        
    if name==num:
        print("very good")
        Offon=True
    
    

