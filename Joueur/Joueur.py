import Joueur.Personnage as perso

class Joueur(perso.Personnage):
    
    def __init__(self, Name):
        self.classes = ["Archer", "Barbare", "Barde", "Guerrier", "Lutteur", "Mage", "Rodeur"]
        self.numeroClasse = 0
        self.races = ["Elfe", "Ent", "Gobelin", "Hobbit", "Humain", "Maiar", "Nain", "Orque"]
        self.numeroRace = 0

        self.classeValide = False
        self.raceValide = False

        super().__init__()
        self.name = Name
        
        #exp = new Experience()

        #choixRace()
        #self.choixClasse()
        #recapitulatif()

    def choixClasse(self):
        self.Com.nettoyerConsole()
        self.Com.afficherSeparateur(122)

        print("\nAragorn : Quel est votre classe de prédilection "+ self.name + " ?!\n")
        for i in range(len(self.classes)):
            print("[" + str(i+1) + "] " + self.classes[i])
        
        self.Com.afficherSeparateur(122)
        print('\n')
        self.choixClasse = self.Com.lectureInt("->",len(self.classes))
        self.Com.nettoyerConsole()

        #if (self.choixClasse == 1):

