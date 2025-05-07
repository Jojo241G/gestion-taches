from ajout import produits

def modifier_produit():
    if not produits:
        print("Aucun produit disponible à modifier.")
        return

    for i, produit in enumerate(produits):
        print(f"{i + 1}. {produit}")

    try:
        choix = int(input("Numéro du produit à modifier : ")) - 1
        if 0 <= choix < len(produits):
            nouveau_nom = input("Nouveau nom du produit : ")
            produits[choix] = nouveau_nom
            print("Produit modifié avec succès.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")
