a = [["name","bought","Should Be Reduced"], 
     ["Dave",1,0], 
     ["Jim",1,1],
     ["Kim",1,0], 
     ["Mat",0,0],
     ["Bob",0,1]]

#Shift the names list to another array
b = []
for c in a:
    b.append(c[0])
print(b)

#Shift the names list of people who bought
b = []
for c in a:
    if c[1] == 1:
        b.append(c[0])

print(b)