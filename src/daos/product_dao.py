"""
Product DAO (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
#from dotenv import load_dotenv
import mysql.connector
from models.user import User
from models.product import Product

class ProductDAO:
    def __init__(self):
        self.conn = None
        self.cursor = None
        try:
           # env_path = "../.env"
            #print(os.path.abspath(env_path))
            #load_dotenv(dotenv_path=env_path)
            db_host = os.getenv("MYSQL_HOST")
            db_name = os.getenv("MYSQL_DB_NAME")
            db_user = os.getenv("DB_USERNAME")  
            db_pass = os.getenv("DB_PASSWORD")     
            self.conn = mysql.connector.connect(host=db_host, user=db_user, password=db_pass, database=db_name)   
            self.cursor = self.conn.cursor()
        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))
            self.conn = None
            self.cursor = None

    def select_all(self):
        """ Sélectionne tous les produits depuis MySQL """
        if not self.cursor:
            print("Erreur : connexion à la base de données non disponible.")
            return []
        try:
            self.cursor.execute("SELECT id, name, brand, price FROM products")
            rows = self.cursor.fetchall()
            return [Product(*row) for row in rows]
        except Exception as e:
            print("Erreur lors de la sélection :", e)
            return []

    def insert(self, product):
        """ Insère le produit donné dans MySQL """
        if not self.cursor:
            print("Erreur : connexion à la base de données non disponible.")
            return None
        try:
            sql = "INSERT INTO products (name, brand, price) VALUES (%s, %s, %s)"
            values = (product.name, product.brand, product.price)
            self.cursor.execute(sql, values)
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print("Erreur lors de l'insertion :", e)

    def update(self, product):
        """ Met à jour le produit donné dans MySQL """
        if not self.cursor:
            print("Erreur : connexion à la base de données non disponible.")
            return
        try:
            sql = "UPDATE products SET name=%s, brand=%s, price=%s WHERE id=%s"
            values = (product.name, product.brand, product.price, product.id)
            self.cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Erreur lors de la mise à jour :", e)

    def delete(self, product_id):
        """ Supprime le produit de MySQL avec l'ID donné """
        if not self.cursor:
            print("Erreur : connexion à la base de données non disponible.")
            return
        try:
            sql = "DELETE FROM products WHERE id=%s"
            self.cursor.execute(sql, (product_id,))
            self.conn.commit()
        except Exception as e:
            print("Erreur lors de la suppression :", e)

    def delete_all(self): #optionnel
        """ Vide la table des produits dans MySQL """
        if not self.cursor:
            print("Erreur : connexion à la base de données non disponible.")
            return
        try:
            self.cursor.execute("DELETE FROM products")
            self.conn.commit()
        except Exception as e:
            print("Erreur lors du vidage de la table :", e)
        
    def close(self):
        self.cursor.close()
        self.conn.close()
