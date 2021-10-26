from neurone_struct import *

class Neurone_ReLu(Neurone):
    """docstring for Neurone_ReLu."""

    def __init__(self, nbEntrees):
        super().__init__(nbEntrees)

    def activation(self, valeur):
        val_r = valeur
        if valeur < 0:
            val_r = 0
        else:
            val_r = valeur
        return val_r
