class Prodotto():
    buon_prodotto = True                             # Variabile / Attributo di classe

    def __init__(self, nome, tipo, qty, prezzo_unitario):
        self.nome = nome
        self.tipo = tipo
        self.qty = qty
        self.prezzo_unitario = prezzo_unitario
        self.prezzo_complessivo = self.prezzo_unitario * self.qty


prodotto1 = Prodotto("Blaster", "Detersivo", 5, 2.1)
print(prodotto1)
print(prodotto1.qty)
print(prodotto1.prezzo_unitario)
print(prodotto1.prezzo_complessivo)
print(prodotto1.buon_prodotto)
print(prodotto1.__class__.buon_prodotto)
