


class Equipement:
    
    def __init__(self):
        self.degatP = 0
        self.degatM = 0
        self.armure = 0
        self.prix = 0
        self.nom = ""


    def getDegatP(self):
        return self.degatP
    
    def setDegatP(self, DegatP):
        self.degatP = DegatP

    def getDegatM(self):
        return self.degatM

    def setDegatM(self, DegatM):
        self.degatM = DegatM

    def getArmure(self):
        return self.armure
    
    def setArmure(self, Armure):
        self.armure = Armure

    def getPrix(self):
        return self.prix

    def setPrix(self, Prix):
        self.prix = Prix

    def getNom(self):
        return self.nom
    
    def setNom(self, Nom):
        self.nom = Nom

class ArcLong(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 3
        self.degatM = 3
        self.armure = 0
        self.prix = 6
        self.nom = "Arc long"

class ArmureDeCuir(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 0
        self.degatM = 0
        self.armure = 3
        self.prix = 5
        self.nom = "Armure de cuir"

class ArmureDePlaque(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 0
        self.degatM = 0
        self.armure = 5
        self.prix = 10
        self.nom = "Armure de plaque"

class ArmureDeSoie(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 0
        self.degatM = 0
        self.armure = 1
        self.prix = 3
        self.nom = "Armure de soie"

class BatonDeMage(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 1
        self.degatM = 5
        self.armure = 0
        self.prix = 3
        self.nom = "Baton de magicien"

class CotteDeMaille(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 0
        self.degatM = 0
        self.armure = 5
        self.prix = 7
        self.nom = "Cotte de maille"

class CoupDePoing(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 2
        self.degatM = 5
        self.armure = 0
        self.prix = 0
        self.nom = "Poing"

class Dague(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 3
        self.degatM = 3
        self.armure = 0
        self.prix = 6
        self.nom = "Dague"

class EpeeADeuxMains(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 5
        self.degatM = 4
        self.armure = 0
        self.prix = 9
        self.nom = "Épée à deux mains"

class EpeeCourte(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 3
        self.degatM = 2
        self.armure = 0
        self.prix = 7
        self.nom = "Épée courte"

class EpeeLongue(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 4
        self.degatM = 3
        self.armure = 0
        self.prix = 8
        self.nom = "Épée longue"

class Gourdin(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 3
        self.degatM = 1
        self.armure = 0
        self.prix = 2
        self.nom = "Gourdin"

class HacheDouble(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 5
        self.degatM = 3
        self.armure = 0
        self.prix = 8
        self.nom = "Hache à deux mains"

class Lance(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 4
        self.degatM = 5
        self.armure = 0
        self.prix = 6
        self.nom = "Lance"

class Luth(Equipement):
    def __init__(self):
        super().__init__()
        self.degatP = 1
        self.degatM = 6
        self.armure = 0
        self.prix = 3
        self.nom = "Luth"

