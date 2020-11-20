class Pagina:
	def __init__ (self, num, cap, text):
		self.num = num
		self.cap = cap
		self.text = text

class PaginaSinistra(Pagina):
    def posizione_numero(self):
        return 'sinistra'
    pass
class PaginaDestra(Pagina):
    def posizione_numero(self):
        return 'destra'
    pass

n_pag = input("inserisci num pagina: ")
n_cap = input("inserisci num capitolo: ")
testo = input("inserisci testo: ")

pag = PaginaSinistra(n_pag, n_cap, testo)


pag2 = PaginaDestra(2, 1, "ciao, questa è la seconda pagina")

libro = []
libro.append(pag)
libro.append(pag2)

print("\n")
for p in libro:
    print("cap {}, pagina {}: {}".format(p.cap, p.num, p.text))