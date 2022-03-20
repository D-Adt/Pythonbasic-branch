#Take User input and process

a=int(input("enter a no."))
b=int(input("enter a no."))
c=int(input("enter a no."))
d=int(input("enter a no."))
e=int(input("enter a no."))

list=[a,b,c,d,e]
for a in list:
    if a<9:
        list.remove(a)
for b in list:
    if b<9:
        list.remove(b)
for c in list:
    if c<9:
        list.remove(c)
for d in list:
    if d<9:
        list.remove(d)
for e in list:
    if e<9:
        list.remove(e)

print(sum(list))
        
