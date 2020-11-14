#apro il file
f = open("demofile.txt", "r")

#appendo a "contenuto" ogni riga,separata da ,
contenuto=[]
for line in f:
    contenuto.append(line.split(","))

#chiudo
f.close()

#aggiungo i due punti dopo il primo valore
for el in contenuto:
    el[0]=el[0]+ ": "
#print (contenuto)

#aggiungo il contenuto a un nuovo file
f = open("newfile.txt", "w")
for line in contenuto:
    f.write(line[0]+line[1])
f.close()

#scrivo
f = open("newfile.txt", "r")
for l in f:
        print(l)
f.close()
