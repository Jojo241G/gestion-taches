from ajoute import ajouter_produit
from modi import modifier_produit
from supp import supprimer_produit

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Ajouter un produit")
        print("2. Modifier un produit")
        print("3. Supprimer un produit")
        print("4. Quitter")
        
        choix = input("Choix : ")

        if choix == "1":
            ajouter_produit()
        elif choix == "2":
            modifier_produit()
        elif choix == "3":
            supprimer_produit()
        elif choix == "4":
            print("Merci d'avoir utilisé le programme.")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    menu()
