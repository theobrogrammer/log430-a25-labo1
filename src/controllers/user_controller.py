"""
User controller
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from daos.user_dao import UserDAO
from models.user import User
from views.user_view import UserView

class UserController:
    def __init__(self):
        self.dao = UserDAO()

    def list_users(self):
        """ List all users """
        users = self.dao.select_all()
        UserView.show_users(users)

    def create_user(self):
        """ Create a new user based on user inputs """
        name, email = UserView.get_inputs()
        user = User(None, name, email)
        self.dao.insert(user)

    def shutdown(self):
        """ Close database connection """
        self.dao.close()
