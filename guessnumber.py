import random
num=random.randint(1,20)
i=0
while i<5:
    ans=int(input("number?"))
    if ans==num:
        print("yes")
        print("guess times:",i+1)
        break
    elif ans>num:
        print("no")
        print("too big")
    else:
        print("no")
        print("too small")
        
        
    i=i+1