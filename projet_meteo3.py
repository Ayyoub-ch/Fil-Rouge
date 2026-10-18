import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


try:
    df = pd.read_csv("Fil rouge donnees2.csv", sep=";", na_values=["mq"], parse_dates=["date"])
    print("Donnees chargees avec succes")
except FileNotFoundError:
    print("Fichier Non Trouve")
    print("Veuillez verifier l'existence du fichier Fil rouge donnees2.csv ou redemarrer le script main")

# Étape 1 — Définir le problème

# La cible est la température en celsius en lien avec la pression, la vitesse du vent et l'humidité

# Les variables explicatives qu'on utilisera la pression, la vitesse du vent et l'humidité

# Les variables issus de la date qu'on peut construire sont jour, mois et heure
# Pour pouvoir mettre en relation de manière linéaire les changements de températures en fonction 
# de l'heure ou du mois

# Étape 2 — Préparer X et y
print("Désolé je n'ai pas su comprendre et réaliser le numero 4 à temps")