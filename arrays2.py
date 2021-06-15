a = [["price","bought","Should Be Reduced"], 
     [1500,1,0], 
     [2000,1,1],
     [2500,1,0], 
     [3000,0,0],
     [3500,0,1]]

#shift the prices list (first column) into another array

b = []
for c in a:
    b.append(c[0])
print(b)

#shift the third column into another array

d = []
for e in a:
    d.append(e[2])
print(d)