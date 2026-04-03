from datetime import date

class Studente:
    nome: str
    cognome: str

    data_nascita: date
    luogo_nascita: str

    def __init__(self, nome: str = "", cognome: str = ""):
        self.nome = nome
        self.cognome = cognome

        self.data_nascita = date(1970, 1, 1)
        self.luogo_nascita = ""

    def calcola_eta(self):
        return date.today() - self.data_nascita
