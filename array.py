l = [] # empty list

while 100:
    num =input('enter some numbers:-  ') #string
    if num== "":
        break
    l.append(int(num)) #string convert into int then store in l
print(l)

a=len(l)
print(f'the length of string is {a}  ')

b=sum(l)
print(f'the sum of lise is {b} ')

