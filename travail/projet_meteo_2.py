import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

# Étape 1 — Chargement du fichier complet

df = pd.read_csv("Fil rouge donnees.csv", sep=";", na_values=["mq"])

print(df.dtypes)

# La cause du fait que tend et cod_tend sont des entiers mais représentés 
# en tant que float est que dans le fichier CSV, 
# certaines valeurs sont manquantes (représentées par "mq"). 
# Lorsque pandas lit le fichier, 
# il convertit automatiquement les colonnes contenant des valeurs manquantes 
# en type float pour pouvoir représenter les NaN (Not a Number) 
# qui sont utilisés pour indiquer les valeurs manquantes.

# Étape 2 — Sélection des colonnes utiles

# Colonnes utiles :
# date (date)
# pres (pression), pmer (pression en mer)
# t (en kelvin), celsius=t-273.15 (temperature en celsius)
# ff (vent), dd (direction du vent), raf10 (rafale de vent)
# u(humidité), 
# rr1 (précipitations sur 1h), rr3 (précipitations sur 3h), rr6 (précipitations sur 6h)
# rr12 (précipitations sur 12h), rr24 (précipitations sur 24h)

# Étape 3 — Conversion et plausibilité des valeurs

# Pour créer une nouvelle colonne "t_celsius" à partir de la colonne "t" (température en kelvin),
df["t_celsius"]=df["t"] - 273.15

print(df["t_celsius"])

print("Minimum : ", df["t_celsius"].min())
print("Maximum : ", df["t_celsius"].max())

# Étape 4 — Gestion des valeurs manquantes

print("Nombre de valeurs manquantes par colonne :")
print(df.isnull().sum())

# Pour les colonnes comme nnuage4  où les valeurs manquantes sont trop fréquentes
# on va provilégier la suppresion totale de la colonne via dropna
# Autrement pour ceux comme tend ou cod_tend qui n'ont qu'une seule valeur manquante
#  On peut simplement remplacer la valeur par la moyenne, étant donnée 
# qu'elle se trouve également au milieu de sa plage de valeurs.

# implace applique la modification directement sur le DataFrame
df["tend"].fillna(df.mean(numeric_only=True), inplace=True)
df["cod_tend"].fillna(df.mean(numeric_only=True), inplace=True)


df.drop(columns=["ssfrai"], inplace=True)
df.drop(columns=["perssfrai"], inplace=True)
df.drop(columns=["sw"], inplace=True)
df.drop(columns=["tw"], inplace=True)
df.drop(columns=["tx24"], inplace=True)
df.drop(columns=["tx12"], inplace=True)
df.drop(columns=["tn12"], inplace=True)
df.drop(columns=["tn24"], inplace=True)
df.drop(columns=["niv_bar"], inplace=True)
df.drop(columns=["geop"], inplace=True)
df.drop(columns=["ch"], inplace=True)
df.drop(columns=["cm"], inplace=True)
df.drop(columns=["cl"], inplace=True)
df.drop(columns=["w1"], inplace=True)
df.drop(columns=["w2"], inplace=True)
df.drop(columns=["phenspe1"], inplace=True)
df.drop(columns=["phenspe2"], inplace=True)
df.drop(columns=["phenspe3"], inplace=True)
df.drop(columns=["phenspe4"], inplace=True)
df.drop(columns=["ctype1"], inplace=True)
df.drop(columns=["ctype2"], inplace=True)
df.drop(columns=["ctype3"], inplace=True)
df.drop(columns=["ctype4"], inplace=True)
df.drop(columns=["nnuage2"], inplace=True)
df.drop(columns=["hnuage3"], inplace=True)
df.drop(columns=["nnuage4"], inplace=True)
df.drop(columns=["hnuage4"], inplace=True)
df.drop(columns=["Unnamed: 59"], inplace=True)


# Étape 5 — Extraction du mois et première agrégation

# 1.
df["date"] = pd.to_datetime(df["date"], format="%Y%m%d%H%M%S")
print(df["date"])

# 2.
df["mois"] = df["date"].dt.month
print(df["mois"])

# 3.
print(df.groupby("mois")["t_celsius"].min())
print(df.groupby("mois")["t_celsius"].max())
print(df.groupby("mois")["t_celsius"].mean())

# Étape 6 — Consolidation du checkpoint

# Applique les changements et sauvegarde le DataFrame modifié dans un nouveau fichier CSV
df.to_csv("Fil rouge donnees2.csv", sep=";", index=False)