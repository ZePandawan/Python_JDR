import random
import sys
sys.path.append('.')

import Classes.Classes as classe
import Joueur.Joueur as joueur

class Attaque:
    def __init__(self):
        
        
        self.nom = ""
        self.description = ""
        self.degats = 0
        self.type = ""
        
        self.classe = classe
        self.joueur = joueur
        
        
        