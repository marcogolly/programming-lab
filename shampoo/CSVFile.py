#per visualizzare grafici
from matplotlib import pyplot

#classe modello generale
class Model:
    def fit(self, data):
        pass
    def predict(self):
        pass

#classe modello per shampoo (no fit)
class IncrementModel(Model):
    #questa funzione calcola l'incremento medio da un dataset di mesi
    def compute_avg_increment(self, prec_months):
        incr= 0
        #sommo gli incrementi
        for i in range(len(prec_months) -1 ):
            incr += prec_months[i+1]- prec_months[i]
        #ritorno la media degli incrementi
        return incr/(len(prec_months)-1)

    def fit (self, data):
        pass

    #predice il valore del mese successivo a quelli passati come parametro nella lista
    def predict (self, prec_months):
        return prec_months[len(prec_months)-1] + self.compute_avg_increment(prec_months) 

class FittableIncrementModel(IncrementModel):
    #assegna ad una variabile globale l'incremento medio del dataset di mesi passato 
    def fit(self, data):
        self.global_avg_increment = self.compute_avg_increment(data)
    
    #predice, a partire dal dataset degli ultimi mesi (di solito 3), le vendite del mese successivo tenendo conto del fit
    def predict(self, prec_months):
        #predicted_increment = media della media degli incrementi del fit e della media di questi ultimi mesi 
        predicted_increment = (( self.compute_avg_increment(prec_months) + self.global_avg_increment)/2)
        
        #ritorno le vendite dell'ultimo mese + previsione incremento
        return prec_months[-1] + predicted_increment
    

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
        #nel file CSV ogni riga è scritta in questo modo: "data, valore float"
        for line in file:
            tmp = line.split(",")
            try:
                data.append(float(tmp[1]))
            except Exception as e:
                print("impossible to convert {} to float".format(tmp[1]))
        file.close()

        try:
            print(data[start:end])
            return data[start:end]
        except:
            print("start o end non validi, restituisco file intero")
            return data

#test brutti scritti male
def test(file, iniz=None, fine=None, result = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]):
    test_file= CSVFile(file)
    if (test_file.get_data(iniz, fine) != result):
        raise Exception("failed\n")

#fitta con più dati possibile e predice con gli ultimi 3 mesi
def add_pred(model, data):
    model.fit(data[:-3])
    pred = model.predict(data[-3:])
    #ritorna la lista + la previsione
    return data + [pred]

#fitta 24 mesi e testa l'affidabilità del modello sui successivi 12 mesi
def test_model(model, data,color ="orange"):
    diff=[]
    pred=[]
    model.fit(data[:24])
    #voglio predirre dal mese 24 al mese 36
    for i in range(24,36):
        #predico sui precedenti 3 mesi
        this_pred = model.predict(data[i-4:i-1])
        
        #calcolo la differenza tra previsione e dato effettivo
        this_diff = abs(this_pred - data[i])
        
        #appendo entrambi i risultati in 2 liste
        diff.append(this_diff)
        pred.append(this_pred)
    #printo la differenza media tra previsione e dato effettivo
    print("errore medio:",sum(diff)/12)
    
    #plotto sul grafico shiftando di 24 posizioni per allinearlo col grafico
    pyplot.plot( ([None] * 24) +pred, 'bo', color="tab:{}".format(color))
    

#apro il CSV
mio_file = CSVFile("shampoo/shampoo_sales.csv")

#leggo i dati del file
data = mio_file.get_data()

#istanzio 2 modelli, il primo fittable e il secondo non fittable
model = FittableIncrementModel()
model2 = IncrementModel()

#creo le previsioni (col primo modello) dei prossimi 2 mesi
data_plus_pred = data
data_plus_pred = add_pred(model, data_plus_pred)
data_plus_pred = add_pred(model, data_plus_pred)

#testo i 2 modelli calcolando l'errore medio 
err1 = test_model(model, data)
err2 = test_model(model2, data, "green")

#plotto il dataset
pyplot.plot(data_plus_pred, color='tab:red')
pyplot.plot(data, color='tab:blue')

#visualizzo il grafico
pyplot.show()

#test
''' try:
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

'''