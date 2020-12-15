file = open("shampoo_sales.csv", "r")
somma=0
for line in file:
    a = line.split(",")
    try:
        somma += float(a[1])
    except Exception as e:
        print ("\n errore \n {}".format(e))

print(somma)