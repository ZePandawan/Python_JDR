import sys
sys.path.append('.')

import Histoire.Menu
import Commandes.Commandes as test
import Joueur.Joueur as joueur
import Equipements.Equipement as equip
import Classes.Classes as classes

class Main:
    
    def __init__(self):
        #Menu2 = Histoire.Menu.Menu()
        #print(type(Menu2))
        #Menu2.menuPrincipal()
        
        print("\n")
        
        #test.Commandes.lectureInt("->",5)
        #test.Commandes.nettoyerConsole()
        #test.Commandes.stopProgramme(self)
        #test.Commandes.afficherEntete(self,10,"test")

        #NewTest = test.Commandes()
        #NewTest.stopProgramme()
        #NewTest.afficherEntete(10,"test")
        #print('\n')
        
        #NewJoueur = joueur.Joueur("Test")
        #NewJoueur.choixClasse()

        NewEquip = equip.Equipement()
        Arc = equip.ArcLong()
        print(Arc.getDegatP())
        print(Arc.getNom())
        
        #Test = classes.Classes()
        

        
        
        
Main()