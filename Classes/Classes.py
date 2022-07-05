import random
import sys
sys.path.append('.')
import Equipements.Equipement as Equip

class Classes:
    def __init__(self):
        self.physique = 0
        self.social = 0
        self.mental = 0
        
        self.sante = 0
        self.mana = 0
        
        self.argent = 0
        
        self.arme = Equip
        self.armure = Equip
        
        self.description = ""
        
        self.attaquesPhysiques = []
        self.attaquesMagiques = []
        #print(self.equipement.getNom())
        
    def getPhysique(self):
        return self.physique
    
    def getSocial(self):
        return self.social
    
    def getMental(self):
        return self.mental
    
    def getSante(self):
        return self.sante
    
    def getMana(self):
        return self.mana
    
    def getDescription(self):
        return self.description
    
    def getArmeDegatsP(self):
        return self.arme.getDegatP()
    
    def getArmeDegatsM(self):
        return self.arme.getDegatM()
    
    def getArmure(self):
        return self.armure.getArmure()
    
    def getArme(self):
        return self.arme
    
    def getClasseDegats(self):
        return random.randint(1,10)
    
    def getAttaquesPhysiques(self):
        return self.attaquesPhysiques
    
    def getAttaquesMagiques(self):
        return self.attaquesMagiques
    

class Archer(Classes):
    
    def __init__(self):
        super().__init__()
        self.physique = 65
        self.social = 50
        self.mental = 55
        self.sante = 14
        self.mana = 6
        
        self.arme = Equip.ArcLong
        self.armure = Equip.ArmureDeCuir
        
        self.description = "L'archer utilise principalement le tir à distance, il est souvent équipé d'un arc ou d'une arbalète, lui permettant d'effectuer de lourds dégâts perforants"
        
        
    
    