import random

l="abcdefghijklmnopqrstuvwxyz"
u="QWERTYUIOPASDFGHJKLZXCVBNM"
n="0123456789"
s="!@#$&*"

length=16
all=l+u+n+s

pas="".join(random.sample(all,length))
print(pas)
