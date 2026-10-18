import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Étape 1 — Définir le problème

# La cible est la température en celsius en lien avec la pression, la vitesse du vent et l'humidité

# Les variables explicatives qu'on utilisera la pression, la vitesse du vent et l'humidité

# Les variables issus de la date qu'on peut construire sont jour, mois et heure
# Pour pouvoir mettre en relation de manière linéaire les changements de températures en fonction 
# de l'heure ou du mois

# Étape 2 — Préparer X et y

# Les colonnes pres, t_celsius, rr1 à rr12, ff et u doivent contenir aucune valeur manquante
# Autrement les valeurs seront incohérentes ou juste incorrectes

def prep_x_y():
    try:
        df = pd.read_csv("Fil rouge donnees2.csv", sep=";", na_values=["mq"],parse_dates=["date"],usecols=["date", "pres", "u", "ff", "t_celsius","rr1","rr3"])
    except FileNotFoundError:
        print("Fichier Non Trouve")
        print("Veuillez verifier l'existence du fichier Fil rouge donnees2.csv ou redemarrer le script main")
        quit()
    try:
        df["mois"] = df["date"].dt.month
        df["heure"] = df["date"].dt.hour
        variables = ["pres", "u", "ff", "mois", "heure","rr1","rr3"]
        cible = "t_celsius"
        donnees = df[variables + [cible]].dropna()
        X = donnees[variables]
        y = donnees[cible]
        print("Taille du DataFrame : ",len(df),"\n","Taille des donnees : ", len(donnees))
        return X,y
    except KeyError:
        print("Colonne non existante")

prep_x_y()

# Étape 3 — Séparer entraînement et test

