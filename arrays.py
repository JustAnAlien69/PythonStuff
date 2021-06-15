a = [["price","bought","Should Be Reduced"], 
     [1500,1,0], 
     [2000,1,1],
     [2500,1,0], 
     [3000,0,0],
     [3500,0,1]]

#cancel out the first row
a.pop(0)
print(a)

#Calculating the second collum
e=0
for d in a:
    e=e+d[1]
print(e)

#to add all the prices
c=0
for b in a:
    print(b[0])
    c=c+b[0]

print(c)