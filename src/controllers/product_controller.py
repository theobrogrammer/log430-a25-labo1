"""
User controller
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from daos.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self.dao = ProductDAO()

    def list_products(self):
        """ Liste tous les produits """
        return self.dao.select_all()
        
    def create_product(self, product):
        """ Crée un nouveau produit à partir des entrées utilisateur """
        self.dao.insert(product)

    def delete_product(self, product_id: int):
        """ Supprime un produit par ID """
        self.dao.delete(product_id)

    def shutdown(self):
        """ Close database connection """
        self.dao.close()
