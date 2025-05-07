from ajout import produits

def supprimer_produit():
    if not produits:
        print("Aucun produit disponible à supprimer.")
        return

    for i, produit in enumerate(produits):
        print(f"{i + 1}. {produit}")

    try:
        choix = int(input("Numéro du produit à supprimer : ")) - 1
        if 0 <= choix < len(produits):
            produit_supprime = produits.pop(choix)
            print(f"Produit '{produit_supprime}' supprimé avec succès.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")
