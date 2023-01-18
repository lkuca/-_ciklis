from random import *
from math import *
try:
    n=int(input("vali 1-9 numbrist et panda nii palju rebasi"))
    if n<1 or n>9:
        print("vale")
except:
      print("vale")
x=0
for x in range(4):
    for e in range(n):
        if x==0:
            print(" ^---^ ",end="")
        elif x== 1:
            print("( o o )",end="")
        elif x==2:
            print("! = !/)",end="")
    print("")


nch=int(input("sissestage arv"))
st=int(input("sissestage aste"))
nch1 = 1
st1 =1
for i in range(1,nch+1):
    stn=nch1**st
    print(nch1,"^",st,"=",stn)
    nch1 +=1
    st1 +=1

bruh =randint(1,5)
õpilaste = randint(1,16)
if bruh<2:
    print(f"minimaalne hinne {bruh}")
elif bruh>4:
    print(f"maksimaalne hinne{bruh}")
