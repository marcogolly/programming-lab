def sum (v):
    s=0
    for i in v:
        s =s +  i
    
    return s

print("inserisci dim: ")
dim = int (input("inserisci dim: "))
v =[]
for i in range(dim):
    v.append(int (input("inserisci numero: ")))

print(sum(v))