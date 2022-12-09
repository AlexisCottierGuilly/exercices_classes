"""
Fait par Alexis Cottier-Guilly du 13 octobre au 7 novembre 2022
Code pour créer divers classes et pour s'entrainer
à programmer avec l'orienté objet.
"""

from math import pi
import random
from dataclasses import dataclass


class StringFoo:
    """
    Prend un message en argument et permet de
    l'afficher à l'écran en majuscules et de
    le changer.
    """

    def __init__(self, message):
        """
        Prend le message en argument et se l'affecte
        en tant qu'attribut.
        :params message: le message
        :return: None
        """
        self.message = message

    def set_string(self, string):
        """
        Prend un message et change l'attribut 'message'
        de l'instance de la classe.
        :params string: le message
        :return: None
        """
        self.message = string

    def print_string(self):
        """
        Permet d'afficher le message de l'instance de
        la classe en majuscules.
        :params: None
        :return: None
        """
        print(self.message.upper())


class Rectangle:
    """
    Cette classe permet de créer un rectanges avec
    une largeur et une longueur et permet d'accéder
    à son aire et à ses informations.
    """

    def __init__(self, largeur, longueur):
        """
        Prend la largeur et la longueur et s'affecte
        ceux-ci en tant qu'attribut.
        """
        self.largeur = largeur
        self.longueur = longueur

    def calculer_aire(self):
        """
        Fonctions qui retourne l'aire du rectangle.
        :params: None
        :return: aire du rectange
        """
        return self.largeur * self.longueur

    def afficher_infos(self):
        """
        Fonction qui permet d'afficher la largeur
        et la longueur du rectange.
        :params: None
        :return: None
        """
        print(f'Largeur : {self.largeur}')
        print(f'Longueur : {self.longueur}')


class Cercle:
    """
    Permet de créer un cercle avec son rayon, et
    de calculer son aire et sa circonférence.
    """

    def __init__(self, rayon):
        """
        Prend le rayon et crée un attribut 'rayon'
        avec la valeur.
        :params rayon: la valeur du rayon
        :return: None
        """
        self.rayon = rayon

    def calcul_aire(self):
        """
        Calcule la valeur de l'aire du cercle.
        :params: None
        :return: l'aire du cercle
        """
        return pi * self.rayon ** 2

    def calcul_circonference(self):
        """
        Calcule la circonférence du cercle.
        :params: None
        :return: la circonférence du cercle
        """
        return 2 * pi * self.rayon


@dataclass
class StatistiquesHero:
    """
    Permet de rassembler les valeurs de divers
    attribut d'un héro.
    """
    force: int = random.randint(1, 20)
    dexterite: int = random.randint(1, 20)
    constitution: int = random.randint(1, 20)
    intelligence: int = random.randint(1, 20)
    sagesse: int = random.randint(1, 20)
    charisme: int = random.randint(1, 20)


class Hero:
    """
    Crée un héro qui peut attaquer, recevoir des
    dommages et dire si il est vivant.
    """

    def __init__(self, nom):
        """
        Reçois le nom en argument et le reste des attributs
        du héro sont aléatoires.
        :params nom: le nom du héro
        :return: None
        """
        self.nom = nom
        self.nombre_vies = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defense = random.randint(1, 6)
        self.statistiques = StatistiquesHero()

    def attaque(self):
        """
        Fonction pour attaquer.
        :params: None
        :return: la force de l'attaque
        """
        return random.randint(1, 6) + self.force_attaque

    def recevoir_dommages(self, dommages):
        """
        Permet de recevoir des dommages d'une attaque
        et les enlever à ses vies.
        :params: les dommages
        :return: None
        """
        self.nombre_vies -= dommages - self.force_defense

    def est_vivant(self):
        """
        Fonction pour savoir si le héro est vivant ou pas.
        :params: None
        :return: True si le joueur est en vie, sinon False
        """
        return True if self.nombre_vies > 0 else False
