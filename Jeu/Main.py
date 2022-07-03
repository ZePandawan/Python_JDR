import sys
sys.path.append('.')

import Histoire.Menu
import Commandes.Commandes as test

class Main:
    
    def __init__(self):
        Menu2 = Histoire.Menu.Menu()
        print(type(Menu2))
        Menu2.menuPrincipal()
        
        print("\n")
        
        #test.Commandes.lectureInt("->",5)
        #test.Commandes.nettoyerConsole()
        test.Commandes.stopProgramme()
        test.Commandes.afficherEntete(10,"test")
        
        
        
        
Main()