#apro il file
f = open("demofile.txt", "r")

#leggo
contenuto=[]
for line in f:
    contenuto.append(line.split(","))


#scrivo
for l in contenuto:
    for p in l:
        print(p)

#chiudo
f.close()
