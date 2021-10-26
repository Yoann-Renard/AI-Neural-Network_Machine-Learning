from neurone_struct import *

class Neurone_Heavyside(Neurone):
    """docstring for Neurone_Heavyside."""

    def __init__(self, nbEntrees):
        super().__init__(nbEntrees)

    def activation(self, valeur):
        val_h = valeur
        if valeur > 0:
            val_h = 1
        else:
            val_h = 0
        return val_h
