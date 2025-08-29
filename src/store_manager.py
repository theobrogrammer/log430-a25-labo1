"""
Application example - MVC avec 2 bases de données
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.user_view import UserView

if __name__ == '__main__':
    print("===== MAGASIN EXAMPLE =====")
    main_menu = UserView()
    main_menu.show_options()
