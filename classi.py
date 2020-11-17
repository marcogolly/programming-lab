class Person:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    def __str__(self):
        return (self.nome+" "+self.cognome)
    pass

person = Person("marco", "golly")
print(person)
