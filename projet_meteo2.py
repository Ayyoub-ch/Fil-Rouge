import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

try:
    df = pd.read_csv("Fil rouge donnees2.csv", sep=";", na_values=["mq"], parse_dates=["date"])
    print("Donnees chargees avec succes")
except FileNotFoundError:
    print("Fichier Non Trouve")
    print("Veuillez verifier l'existence du fichier Fil rouge donnees2.csv ou redemarrer le script main")

# Étape 1 — Évolution de la température

def temperature_celsius():
    """
    Nom: temperature_celsius
    But: Fonction permettant d'afficher et enregistrer un graphique de la température en Celcius en fonction de la date
    
    Aucun paramètre
    
    Ne renvoit rien mais affiche un graphique nommé temperature_celsius.png
    """
    ax = df.plot(x="date", y="t_celsius")
    ax = df.set_index("date")["t_celsius"].plot()
    ax.set_ylabel("Température (°C)")
    ax.set_xlabel("Période d'une année (2023 - 2024)")
    plt.xticks(rotation=45) 
    plt.savefig("images/temperature_celsius.png", dpi=150, bbox_inches="tight")
    plt.show()
    return

def temperature_celsius_moyenne_mensuelle():
    """
    Nom: temperature_celsius_moyenne_mensuelle
    But: Fonction permettant d'afficher et enregistrer un graphique de la température en Celcius en fonction de la moyenne mensuelle
        
    Aucun paramètre
        
    Ne renvoit rien mais affiche un graphique nommé temperature_celsius_moyenne_mensuelle.png
    """
    df["mois"] = df["date"].dt.month
    df_moyenne = df.groupby("mois")["t_celsius"].mean()
    ax = df_moyenne.plot()
    ax.set_xlabel("Année par mois (Moyenne mensuelle)")
    ax.set_ylabel("Température (°C)")
    plt.xticks(rotation=45) 
    plt.savefig("images/temperature_celsius_moyenne_mensuelle.png", dpi=150, bbox_inches="tight")
    plt.show()
    return



# Le premier graphique montre les températures relevés au fil du temps
# A travers le cours de l'année avec plus de détail comme les pics et creux 

# Tandis que le deuxième montre la tendance des température certes de manière plus lisible
# Mais moins détaillée, étant basé sur la moyenne mensuelle, il ne montre pas les variations quotidiennes.

# Les valeurs manquantes ne sont pas visibles sur le graphique
# car on utilise un dataframe nettoyé issu du fil rouge n° 2 qui enlève les valeurs manquantes et rend le graphique plus clair.


# Étape 2 — Précipitations

def affichage_infos_rr1_rr3():
    """
    Nom: affichage_infos_rr1_rr3
    But: Fonction permettant d'afficher les informations sur le minimum, maximum et la moyenne des précipitations
    sur 1h et 3h
            
    Aucun paramètre
            
    Ne renvoit rien 
    """
    print("Minimum sur 1h : ", df["rr1"].min())
    print("Maximum sur 1h : ", df["rr1"].max())
    print("Moyenne sur 1h : ", df["rr1"].mean())
    print("\n")
    print("Minimum sur 3h : ", df["rr3"].min())
    print("Maximum sur 3h : ", df["rr3"].max())
    print("Moyenne sur 3h : ", df["rr3"].mean())
    print("\n")
    return


# Les 0 représentent l'absence de précipitation mesurable
# Les valeurs négatives comme -0.1 représentent une quantité trop faible de précipitation pour être mesurée
# On peut garder les valeurs initiales du csv2 (générée par projet_meteo.py)
# Car étant nettoyées au préalable et sont cohérentes


# On peut prendre un histogramme pour savoir la répartion des précipitations sur 3 heures

def hist_rr3():
    """
    Nom: hist_rr3
    But: Fonction permettant d'afficher et enregistrer un histogramme avec la fréquence des précipitations sur 3H
    
    Aucun paramètre
    
    Ne renvoit rien
    """
    hx= df["rr3"].plot(kind="hist", bins=5)
    hx.set_xlabel("Précipitations sur 3h")
    hx.set_ylabel("Fréquence")
    plt.savefig("images/hist_rr3.png", dpi=150, bbox_inches="tight")
    plt.show()
    return

def mois_pluvieux():
    """
    Nom: mois_pluvieux
    But: Fonction permettant d'afficher et enregistrer un histogramme avec la fréquence des précipitations sur 3H, mais sur une moyenne mensuelle
        
    Aucun paramètre
        
    Ne renvoit rien
    """
    df["mois"] = df["date"].dt.month
    df.groupby("mois")["rr3"].mean().plot(kind="bar")
    plt.xticks(rotation=0)
    plt.savefig("images/hist_rr3_mois.png", dpi=150, bbox_inches="tight")
    plt.show()
    


# Le mois le plus pluvieux est le 11e mois de l'année


# Étape 3 — Relations entre variables

def correlation():
    """
    Nom: correlation
    
    But: Affiche la correlation entre la température en celsius, l'humidité, la vitesse du vent et la pression
    
    Aucun paramètre 
    
    Ne renvoit rien
    """
    print("Lien de correlation entre la température en celsius, l'humidité, la vitesse du vent et la pression : ",
          "\n", 
          df[["t_celsius", "u", "ff", "pres"]].corr())
    print("\n")



# Parmi les variables on peut prendre ff qui est la vitesse du vent, qui se corrèle à la température

def nuage_point_ff():
    """
    Nom: nuage_point_ff
    But: Fonction permettant de créer un graphique représentant la témpérature de Lille-Lesquin en fonction de la vitesse du vent.
    
    Aucun paramètre
    
    Ne renvoit rien 
    """
    ux = df.plot.scatter(x="ff", y="t_celsius")
    ux.set_title("Température à Lille-Lesquin en fonction de la vitesse du vent")
    plt.savefig("images/relation_extrait_ff.png", dpi=150, bbox_inches="tight")
    plt.show()

def nuage_point_pres():
    """
    Nom: nuage_point_pres
    But: Fonction permettant de créer un graphique représentant la témpérature de Lille-Lesquin en fonction de la pression.
        
    Aucun paramètre
        
    Ne renvoit rien 
    """
    ux = df.plot.scatter(x="pres", y="t_celsius")
    ux.set_title("Température à Lille-Lesquin en fonction de la pression")
    plt.savefig("images/relation_extrait_pres.png", dpi=150, bbox_inches="tight")
    plt.show()

def nuage_point_hum():
    """
    Nom: nuage_point_hum
    But: Fonction permettant de créer un graphique représentant la témpérature de Lille-Lesquin en fonction de l'humidité'.
        
    Aucun paramètre
        
    Ne renvoit rien 
    """
    ux = df.plot.scatter(x="u", y="t_celsius")
    ux.set_title("Température à Lille-Lesquin en fonction de l'humidité'")
    plt.savefig("images/relation_extrait_hum.png", dpi=150, bbox_inches="tight")
    plt.show()



# On peut définir l'humidité comme la plus liée à la température
# Tandis que le vent et la pression ont une faible corrélation en raison des valeurs concentrées sur une partie précise
# Alors que l’humidité (u) est de loin la plus liée à la température : le nuage de points montre une tendance nettement décroissante,


# Étape 4 — Enregistrement des figures

# Le fichier s'appelle images et contient tous les graphiques effectuées lors du tp 3

# Étape 5 — Restructuration en fonctions

# Chaque script dépend de données qui sont propres à la demande du programme 
# La température, la pression ou encore la date pour exemple sont commune à chaque programme
# Chaque fonction reçoit ce qu'elle a besoin

# Exemple si on veut le moyenne mensuelle alors on l'inscrira au début du programme pour ne pas avoir de perturbation

# Elle ne modifie pas le Dataframe, il garde sa constance et sa cohérence issu du Fil Rouge 2
# Dans ce même travail précédent, on a nettoyé le DataFrame pour qu'aucune donnée ne soit bloquée ou rendu inutile

# Étape 6 — Gestion minimale des erreurs



# Étape 7 — Vérification finale

# Le script ne dépend que d'un fichier généré grâce à projet_meteo uniquement

def main():
    """
    Fonction appelant toutes les autres fonctions afin de les déclencher en une seule fois
    
    Ne renvoit rien
    """
    affichage_infos_rr1_rr3()

    hist_rr3()
    mois_pluvieux()
    
    temperature_celsius()
    temperature_celsius_moyenne_mensuelle()
    correlation()
    nuage_point_pres()
    nuage_point_ff()
    nuage_point_hum()
    
    print("Execution effectuee avec succes !")
    
    
    
if __name__ == "__main__":
    print("\n")
    print("Execution du script du Fil Rouge n 3")
    print("\n")
    main()
    