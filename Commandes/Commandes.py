from xml.sax.handler import EntityResolver
import os

class Commandes:
    def __init__(self) -> None:
        pass
    
    def lectureInt(self,choix, choixUtilisateur):
        entree = -1
        
        
        while(entree < 1 or entree > choixUtilisateur):
            try : 
                entree = int(input(choix + " "))
            except:
                entree = -1;
                print("Veuillez rentrer une valeur entière !")
        
        return entree
    
    def nettoyerConsole(self):
        #os.system('cls')
        for i in range (10):
            print('\n')
        
    def afficherSeparateur(self,n):
        sepa = ""
        for i in range(n):
            sepa += "-"
        print(sepa, end='')
        
    def afficherEntete(self, nombre, texte):
        Commandes.afficherSeparateur(self, nombre)
        print(texte, end='')
        Commandes.afficherSeparateur(self, nombre)
    
    def stopProgramme(self):
        input("Appuyez sur Entrée pour continuer : ")   
        
    def debugScanner(self):
        input()
        
        