import random

a="abcdefghijklmnopqrstuvwxyz"
b="QWERTYUIOPASDFGHJKLZXCVBNM"
c="0123456789"
d="!@#$&*"

length=16
all=a+b+c+d

pas="".join(random.sample(all,length))
print(pas)
