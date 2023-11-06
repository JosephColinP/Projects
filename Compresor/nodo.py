class Nodo:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.freq < otro.freq