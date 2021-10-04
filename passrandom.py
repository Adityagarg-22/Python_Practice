import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSRTUVWXYZ"
numbers="123456789"

all=lower+upper+numbers
length=16
password="".join(random.sample(all,length))
print(password)
