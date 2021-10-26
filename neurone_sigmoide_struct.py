from neurone_struct import *
from math import exp

class Neurone_Sigmoide(Neurone):
    """docstring for Neurone_Sigmoide."""

    def __init__(self, nbEntrees):
        super().__init__(nbEntrees)

    def activation(self, valeur):
        val_s = 1/(1+exp(-valeur))
        return val_s
