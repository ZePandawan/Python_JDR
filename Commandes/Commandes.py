from xml.sax.handler import EntityResolver
import os

class Commandes:
    def __init__(self) -> None:
        pass
    
    def lectureInt(choix, choixUtilisateur):
        entree = -1
        
        
        while(entree < 1 or entree > choixUtilisateur):
            try : 
                entree = int(input(choix + " "))
            except:
                entree = -1;
                print("Veuillez rentrer une valeur entière !")
        
        return entree
    
    def nettoyerConsole():
        os.system('cls')
        
    def afficherSeparateur(n):
        sepa = ""
        for i in range(n):
            sepa += "-"
        print(sepa, end='')
        
    def afficherEntete(nombre, texte):
        Commandes.afficherSeparateur(nombre)
        print(texte, end='')
        Commandes.afficherSeparateur(nombre)
    
    def stopProgramme():
        input("Appuyez sur Entrée pour continuer : ")   
        
    def debugScanner():
        input()
        
        