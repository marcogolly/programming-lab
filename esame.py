#questa classe serve a calcolare la media mobile
class MovingAverage:
    #costruttore
    def __init__(self, window):
        try:
            
            assert(window >=1)
            assert(isinstance(window, int))
        except:
            raise ExamException("non valido")
        self.window= window
    #calcolo vero e proprio
    def compute(self, vals):
        #tests
        try:
            #testo che vals sia una lista
            assert(isinstance(vals, list))
            #testo che ogni val in vals sia int o float
            for val in vals:
                assert(isinstance(val, (int, float)))
        except:
            raise ExamException("formato lista non corretto")
        try:
            #testo che la lista non sia vuota o più piccola della len di finestra
            assert(len(vals) >= self.window)
        except:
            raise ExamException("lista troppo piccola")
        #definisco la lista delle medie
        avg=[]
        #per ogni finestra...
        for i in range(len(vals) - self.window +1):
            #... calcolo la media e la aggiungo alla lista
            avg.append(sum(vals[i:i+self.window])/self.window)
        #ritorno la lista di medie
        return avg
    pass
#classe per eccezioni personalizzate
class ExamException(Exception):
        pass

#instanzio MovingAverage
'''moving_average = MovingAverage(2)
test = [[2,4,8,16],[], [1,2,3], [1.2, 2.3, 4.5, 6.3, 4.6], "ciao", 10, [1,2,3,[4,5]], ["1","2", "3", "4"], [1,2, True]]

for t in test:
    try:
        result = moving_average.compute(t)
        print(result)
    except ExamException as e:
        print(e)'''
