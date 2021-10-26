from neurone_struct import *
from neurone_heavyside_struct import *
from neurone_ReLu_struct import *
from neurone_sigmoide_struct import *
import json
import os
import re
import sys

def learn(entrees, resultats,type_neurone, nom_table):
    #entrees = [[0,0],[0,1],[1,0],[1,1]]
    #resultats = [0,0,0,1]

    if type_neurone == "Neurone_Heavyside":
        neurone = Neurone_Heavyside(len(entrees[0]))
    elif type_neurone == "Neurone_ReLu":
        neurone = Neurone_ReLu(len(entrees[0]))
    elif type_neurone == "Neurone_Sigmoide":
        neurone = Neurone_Sigmoide(len(entrees[0]))
    else:
        return -1

    print("Apprentissage...")

    print("\nLa Table à bien été apprise !")

    print("Nombre d'itérations : " , neurone.apprentissage(entrees, resultats))


    for i in range(len(entrees)):
        entree=entrees[i]

        neurone.neurone_injection(entree)

        print("Entree",i,":", neurone.sortie())

    save_apprentissage_table(neurone, resultats,nom_table,entrees)
    sys.exit("\nLa table à bien été enregistrée !")

def save_apprentissage_table(neurone, resultats, nom_table, entrees):
    save = {
        "Type de neurone : " : type(neurone).__name__,
        "Nom de la table apprise : " : nom_table,
        "Table apprise : " : resultats,
        "Entrees utilisees : " : entrees,
        "Poids : " : neurone.synapses[:len(neurone.synapses)-1],
        "Biais :" : neurone.synapses[len(neurone.synapses)-1]
    }
    f=open("./Saves/sauvegarde_neurones_tables.json", "a")
    try:
        r=open("./Saves/sauvegarde_neurones_tables.json", "r")
        if r.read():
            f.write("/")
    finally:
        r.close()
    f.write(json.dumps(save))
    f.close()


def interface():
    print("""Choisir une option :
    1 - Reconnaissance d'entrées logiques
    2 - Reconnaissance d'images""")
    i = input("=>")
    if i == "1":
        os.system('cls')
        selection_neurone("table")
    elif i == "2":
        os.system('cls')
        print("Fonction indisponible\n")
        interface()
        #selection_neurone("img")
    else:
        os.system('cls')
        print("Entrée invalide.\n")
        interface()

def selection_neurone(selection):
    print("""Choisir un neurone à utiliser :
    1 - Neurone Heavyside ( Seuil )
    2 - Neurone ReLu
    3 - Neurone Sigmoïde""")
    i = input("=>")
    if i == "1":
        if selection == "img":
            pass
        else:
            os.system('cls')
            selection_methode(selection, "Neurone_Heavyside")
    elif i =="2":
        if selection == "img":
            pass
        else:
            os.system('cls')
            selection_methode(selection, "Neurone_ReLu")
    elif i =="3":
        if selection == "img":
            pass
        else:
            os.system('cls')
            selection_methode(selection, "Neurone_Sigmoide")
    else:
        os.system('cls')
        print("Entrée invalide.\n")
        selection_neurone(selection)

def selection_methode(selec, type_neurone):
    print("""Que voulez vous faire ?
    1 - Apprendre
    2 - Lire""")
    i = input("=>")
    if i == "1":
        if selec == "table":
            os.system('cls')
            learn_input_tables(type_neurone)
    elif i == "2":
        os.system('cls')
        print("Fonction indisponible\n")
        selection_methode(selec, type_neurone)
    else:
        os.system('cls')
        print("Entrée invalide.\n")
        selection_methode(selec, type_neurone)

def learn_input_tables(type_neurone):
    n = input("""Donnez un nom à la table :
=>""").upper()
    e = input("""\nDonnez les entrées ( ex : '0,0;0,1;1,0 ...') :
=>""")
    r = input("""\nDonnez les résultats attendus ( ex '0;1;1 ...' ) :
=>""")
    resultats = re.split(";" , r)
    e_lignes = re.split(";", e)
    entrees = []
    for l in e_lignes:
        entrees.append(re.split(",", l))
    if len(entrees) != len(resultats):
        os.system("cls")
        print("Il doit y avoir le même nombre d'entrées et de résultats\n")
        learn_input_tables(type_neurone)


    """ Intify entrees/resultats """
    for i in range(len(entrees)):
        if len(entrees[i]) != 2 or len(resultats[i]) != 1:
            os.system("cls")
            print("Les entrées doivent être de longueur 2 et les résultats de longueur 1.\n")
            learn_input_tables(type_neurone)

        for j in range(len(entrees[i])):
            try:
                entrees[i][j] = int(entrees[i][j])
            except Exception as e:
                os.system("cls")
                print("Les entrées doivent être numériques\n")
                learn_input_tables(type_neurone)
        try:
            resultats[i] = int(resultats[i])
        except Exception as e:
            os.system("cls")
            print("Les résultats doivent être numériques\n")
            learn_input_tables(type_neurone)

    """ Check si la table existe déjà ou si l'une d'elle possède le même nom """
    try:
        f=open("./Saves/sauvegarde_neurones_tables.json", 'r')
        contenue = f.read()
        if contenue:
            liste_objets = re.split("/",contenue)
            for obj_json in liste_objets:
                obj = json.loads(obj_json)
                if obj["Nom de la table apprise : "] == n:
                    os.system("cls")
                    print("Une table de nom :",obj["Nom de la table apprise : "]," existe déja.\nTable :\n\tNom : ",obj["Nom de la table apprise : "])
                    print("\tNeurone : ",obj["Type de neurone : "],"\n\tEntrées : ",obj["Entrees utilisees : "],"\n\tRésultats : ",obj["Table apprise : "],"\n")
                    learn_input_tables(type_neurone)
                elif obj["Entrees utilisees : "] == entrees and obj["Table apprise : "] == resultats and obj["Type de neurone : "] == type_neurone:
                    os.system("cls")
                    print("Une table de nom :",obj["Nom de la table apprise : "]," possède le même couple Entrées/Résultats et le même neurone.\nTable :\n\tNom : ",obj["Nom de la table apprise : "])
                    print("\tNeurone : ",obj["Type de neurone : "],"\n\tEntrées : ",obj["Entrees utilisees : "],"\n\tRésultats : ",obj["Table apprise : "],"\n")
                    learn_input_tables(type_neurone)
    finally:
        f.close()

    """ Affichage de la table et validation de l'utilisateur """
    print("\nNom de la table : ", n)
    print("Entrées : ", entrees)
    print("Résultats voulus : ", resultats)
    if input("""\nValidez votre choix ? o/n
=>""") == "o" :
        learn(entrees,resultats,type_neurone,n)
    else:
        os.system("cls")
        learn_input_tables(type_neurone)


print("Bienvenue sur le test d'IA python\n")
interface()
