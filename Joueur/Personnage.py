from sys import implementation


import sys
sys.path.append('.')

import Commandes.Commandes as newCom

class Personnage:
    
    #protected Experience exp
    #protected Race race
    #protected Classe classe
    
    
    #protected Inventaire inventaire = new Inventaire()
    
    def __init__(self):
        self.Com = newCom.Commandes()
        self.maxHp, self.hp, self.mana, self.maxMana, self.argent = 0
        self.attaques = []
    
    def getManaMax(self):
        return self.maxMana
    
    def setManaMax(self,MaxMana):
        self.maxMana = MaxMana
        
    def getMana(self):
        return self.mana
    
    def setMana(self, Mana):
        if(Mana + self.mana > self.maxMana):
            self.mana = self.maxMana
        else:
            self.mana += Mana
            
    def getMaxHp(self):
        return self.maxHp
    
    def setMaxHp(self, MaxHp):
        self.maxHp = MaxHp
        
    def getHp(self):
        self.hp
    
    def setHp(self, HP):
        if(self.hp + HP > self.getHp):
            self.hp = self.maxHp
        else:
            self.hp += HP
            
        
        
    
    
    
    