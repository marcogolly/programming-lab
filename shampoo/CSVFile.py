from matplotlib import pyplot
#modello generale
class Model:
    def fit(self, data):
        pass
    def predict(self):
        pass

#modello per shampoo
class IncrementModel(Model):
    def fit (self, data):
        pass    
    def predict (self, prec_months):
        incr= 0
        for i in range(len(prec_months) -1 ):
            incr += prec_months[i+1]- prec_months[i]
        return prec_months[len(prec_months)-1] + incr/len(prec_months)

class FittableIncrementModel(IncrementModel):
    def compute_avg_increment(self, prec_months):
        incr= 0
        for i in range(len(prec_months) -1 ):
            incr += prec_months[i+1]- prec_months[i]
        return incr/(len(prec_months)-1)

    def fit(self, data):
        self.global_avg_increment = self.compute_avg_increment(data)
        print("fit:",self.global_avg_increment)

    def predict(self, prec_months):
        predicted_increment = (( self.compute_avg_increment(prec_months) + self.global_avg_increment)/2)
        print( prec_months[-1], predicted_increment)
        prediction = prec_months[-1] + predicted_increment
        return prediction
    

#classe per leggere file csv
class CSVFile:
    def __init__(self, name):
        if type(name)!= str:
            raise Exception ("il nome non è una stringa")
        else:
            self.name = name
    
    def __str__(self):
        return "file CSV di nome {}.\n".format(self.name)
    
    #restituisce lista di dati float del file
    def get_data(self, start = None, end = None):
        try:
            file = open(self.name, "r")
        except:
            raise Exception ("impossibile aprire il file\n")
        data=[]
        i=start
        for line in file:
            tmp = line.split(",")
            try:
                data.append(float(tmp[1]))
            except Exception as e:
                #print('impossibile convertire in float, ti consiglio di cambiare corso\nerrore: "{}"\n'.format(e))

                pass

        file.close()

        try:
            print(data[start:end])
            return data[start:end]
        except Exception as e:
            print("start o end non validi, restituisco file intero")
            return data
def test(file, iniz=None, fine=None, result = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]):
    test_file= CSVFile(file)
    if (test_file.get_data(iniz, fine) != result):
        raise Exception("failed ciao, 4\n")

def add_pred(model, data):
    model.fit(data[:-3])
    pred = model.predict(data[-3:])
    return data + [pred]

mio_file = CSVFile("shampoo/shampoo_sales.csv")

#istanza del modello    
model = FittableIncrementModel()

#previsione per il prossimo mese
data = mio_file.get_data(end =-1)
data_plus_pred = data

for i in range(5):
    data_plus_pred = add_pred(model, data_plus_pred)


#model.fit([1,3,5,7])
#prediction = model.predict([9,11,13])



#pyplot.plot([1,5,3,9,7,13,11] + [prediction], color='tab:red')
#pyplot.plot([1,5,3,9,7,13,11], color='tab:blue')

pyplot.plot(data_plus_pred, color='tab:red')
pyplot.plot(data, color='tab:blue')

pyplot.show()

#test
"""try:
    print ("*******************")
    print ("test 1: file giusto")
    test(mio_file)

    print ("*******************")
    print ("test 2: nome inesistente")
    test("niente")

    print ("*******************")
    print ("test 3: ")
    test(mio_file, iniz = 6, fine=3)

except Exception as e:
    print(e)

try:
    test(mio_file)
    test(4)

except Exception as e:
    print(e)

"""