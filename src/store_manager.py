"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.user_view import UserView
from views.product_view import ProductView

if __name__ == '__main__':
    print("=" * 40)
    print("=         LE MAGASIN DU COIN         =")
    print("=" * 40)

    user_menu = UserView()
    product_menu = ProductView()

    q1 = "Désirez-vous gérer les utilisateurs (1), les produits (2) ou quitter (3) ?"
    print()
    print(q1)

    choice = input("Choisissez une option : ").strip()
    if choice == '1':
        user_menu.show_options()
    elif choice == '2':
        product_menu.show_options()
    elif choice == '3':
        print("Au revoir!")
    else:
        print("Cette option n'existe pas.")
        print(q1)

