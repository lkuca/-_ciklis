from random import *
from statistics import mean
s=int(input("viberite skolko lis hotite"))
for n in range(s):
    if s<=10:
        print(" ^---^")
        print("( o o )")
        print(" ! = !/)")
        print("")
        print("")
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
bruh =randint(0,6)
õpilaste = randint(1,16)
print(f"keskmine hinne õpilastel={bruh+õpilas"),
format(mean(int(print(f'hinne:{bruh} '))))
print(f' õpilase arv:{õpilaste} ')