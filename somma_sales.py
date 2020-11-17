file = open("shampoo_sales.csv", "r")
somma=0
for line in file:
    a = line.split(",")
    if a[0] != "Date":
        somma += float(a[1])

print(somma)