class CSVFile():
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "file CSV di nome {}.\n".format(self.name)
    
    def get_data(self):
        file = open(self.name, "r")
        data=[]
        for line in file:
            tmp = line.split(",")
            if tmp[0] != 'Date':
                data.append(float(tmp[1]))
        file.close()
        return data

mio_file = CSVFile("shampoo_sales.csv")
print(mio_file)