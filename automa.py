import random
class Automa:
    biancheria = None
    calzini =None
    maglia = None
    pantaloni =None
    calzatura=None
    def Biancheria(self):
        rand = random.randint(0,4)
        if not rand:
            raise Exception ("fatal error: automa cannot dress")
        if self.biancheria == True:
            print("già indossato")
            return 0
        else:
            self.biancheria= True
            print("biancheria indossata")
            return 1
    
    def Calzini(self):
        rand = random.randint(0,4)
        if not rand:
            raise Exception ("fatal error: automa cannot dress")            
        if self.calzini == True:
            print("già indossato")
            return 0
        else:
            self.calzini= True
            print("calzini indossati")
            return 1
    def Maglia(self):
        rand = random.randint(0,4)
        if not rand:
            raise Exception ("fatal error: automa cannot dress")
        if self.maglia == True:
            print("già indossato")
            return 0
        else:
            self.maglia= True
            print("maglia indossata")
            return 1
    def Pantaloni(self):
        if self.biancheria ==None:
            raise Exception ("non hai le mutande!!")
        rand = random.randint(0,4)
        if not rand:
            raise Exception ("fatal error: automa cannot dress")
        if self.pantaloni == True:
            print("già indossato")
            return 0
        else:
            self.pantaloni= True
            print("pantaloni indossati")
            return 1
    def Calzatura(self):
        if self.calzini ==None or self.pantaloni ==None:
            raise Exception ("non hai i calzini e/o i pantaloni!")
        rand = random.randint(0,4)
        if not rand:
            raise Exception ("fatal error: automa cannot dress")
        if self.calzatura== True:
            print("già indossato")
            return 0
        else:
            self.calzatura= True
            print("calzatura indossata")
            return 1
def esegui(automa, capo):
    res =False
    if (capo =="Biancheria"):
        res=automa.Biancheria()
    elif(capo == "Calzini"):
        res=automa.Calzini()
    elif(capo == "Calzatura"):
        res=automa.Calzatura()
    elif(capo == "Pantaloni"):
        res=automa.Pantaloni()
    elif(capo == "Maglia"):
        res=automa.Maglia()
    else:
        raise Exception("impossibile vestirsi")
    return res

automa = Automa()
capi_vestiario= ["Biancheria", "Calzatura", "Calzini", "Maglia", "Pantaloni"]
capi_indossati =[]
vestito = False
while (not vestito):
    try:
        capo_rand = random.choice(capi_vestiario)
        res= esegui(automa, capo_rand)
        if res:
            capi_indossati += [capo_rand]
        if len(capi_indossati) >=5:
            vestito=True
    except Exception as e:
        print(e)
print(capi_indossati)
print("androide vestito")