import random as r

class Neurone:
    """docstring for Neurone"""
    synapses=[]
    eta = .1
    tolerance= 1.e-2
    etat_interne = float('nan')

    def __init__(self, nbEntrees):
        self.synapses = []
        for i in range(nbEntrees+1):
            self.synapses.insert(i,r.random()*2.-1.)


    def activation(valeur):
        pass


    def sortie(s): return s.etat_interne

    def synapses(s): return s.synapses

    def neurone_injection(self, entrees):
        somme = self.synapses[len(self.synapses)-1]
        for i in range(len(self.synapses)-1):
            somme += entrees[i]*self.synapses[i]
        self.etat_interne = self.activation(somme)


    def apprentissage(self, entrees, resultats):
        drapeau = 0
        Echecs = 0
        while drapeau != len(entrees):
            drapeau = 0

            for i in range(len(entrees)):
                self.neurone_injection(entrees[i])
                difference = resultats[i] - self.sortie()

                if abs(difference) < self.tolerance:
                    drapeau += 1
                    continue
                else:
                    Echecs+=1

                    for k in range(len(self.synapses)-1):
                        self.synapses[k] += self.eta*entrees[i][k]*difference

                    else:
                        self.synapses[len(self.synapses)-1] += self.eta*difference

        return Echecs
