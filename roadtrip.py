import numpy as np
from matplotlib import pyplot
import math
# Dati della tabella
data = np.array([[833. ,  37. ],
                 [987. ,  41.6],
                 [883. ,  37.2],
                 [378. ,  15.2],
                 [ 84. ,   3.4],
                 [483. ,  19.6],
                 [835. ,  35.1],
                 [646. ,  28.9],
                 [508. ,  22.6],
                 [ 90. ,   3.7]])

#------------------------
# definizione del modello
#------------------------
class LinearModel:
  def __init__(self):
    self.angular_coeff =None
    self.intercept=None
    self.train_data=None

  def fit(self,train_data):
    # controllo che train_data sia della forma giusta
    try:
      assert(len(train_data.shape)==2)
      assert(train_data.shape[1]==2)
      assert(len(train_data[:,0]) == len(train_data[:,1]))
    except:
      raise Exception("Bad train_data shape! {} should be (*,2)".format(train_data.shape))
  
	  # ricavo le x e le y da train_data
    x = train_data[:,0]
    y = train_data[:,1]

    #calcolo la media delle x e delle y
    avg_x = sum(x)/len(x)
    avg_y = sum(y)/len(y)

    #calcolo il coefficiente di correlazione (calcolo prima le tre sommatorie)
    sum_diff_xy = np.sum((x - avg_x) * (y - avg_y))
    sum_pow_x = np.sum((x-avg_x)**2)
    sum_pow_y = np.sum((y-avg_y)**2)
    
    coeff_P = sum_diff_xy / math.sqrt(sum_pow_x * sum_pow_y)
    dev_std_x = math.sqrt(sum_pow_x /(len(x)-1))
    dev_std_y = math.sqrt(sum_pow_y /(len(y)-1))

    #coefficiente angolare:
    self.angular_coeff = coeff_P * (dev_std_y / dev_std_x)
    self.intercept = avg_y - self.angular_coeff * avg_x

    self.train_data =train_data

  def predict(self,xs):
    
    if self.angular_coeff is None or self.intercept is None:
        raise Exception ("coefficiente angolare e/o intercetta non calcolati ")
    
    return xs*self.angular_coeff + self.intercept

#-------------------------
# applicazione del modello
#-------------------------
def plot_regression(model):
    xs= np.array([0,100,200,2000,2500])
    ys = model.predict(xs)
    pyplot.plot(xs,ys, "blue")
try:
    linMod = LinearModel()
    linMod.fit(data)

    plot_regression(linMod)
    km_tragitto = 2500

    litri_tragitto = linMod.predict(km_tragitto)

    prezzo_benzina = 1.4

    tot_costo = litri_tragitto*prezzo_benzina
    quota_individuale = tot_costo/3

    #Stampa i risultati a schermo 
    print("Litri di benzina totali:{}lt\nQuota individuale:{}€".format(litri_tragitto,quota_individuale))
    pyplot.plot(data[:,0],data[:,1],'go')
    pyplot.plot(km_tragitto, litri_tragitto, 'ro')
    pyplot.show()
except Exception as e:  
    print(e) 