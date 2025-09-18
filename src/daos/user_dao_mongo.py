"""
User DAO (Data Access Object) - MongoDB
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from models.user import User


class UserDAOMongo:
    """Implémentation de la DAO User avec MongoDB (pymongo)."""

    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None
        try:
            host = os.getenv("MONGODB_HOST")
            db_name = os.getenv("MONGODB_DB_NAME")  
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")
            
            uri = f"mongodb://{db_user}:{db_pass}@{host}:27017/?authSource=admin"
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            self.collection = self.db["users"]
        except Exception as e:
            print("Erreur de connexion MongoDB:", e)
            self.client = None
            self.db = None
            self.collection = None

    def select_all(self):
        """Sélectionne tous les utilisateurs depuis MongoDB."""
        if not self.collection:
            print("Erreur : connexion à la base de données non disponible.")
            return []
        try:
            docs = list(self.collection.find({}, {"name": 1, "email": 1}))
            return [User(str(doc.get("_id")), doc.get("name"), doc.get("email")) for doc in docs]
        except Exception as e:
            print("Erreur lors de la sélection :", e)
            return []

    def insert(self, user):
        """Insère l'utilisateur donné dans MongoDB."""
        if not self.collection:
            print("Erreur : connexion à la base de données non disponible.")
            return None
        try:
            res = self.collection.insert_one({"name": user.name, "email": user.email})
            return str(res.inserted_id)
        except Exception as e:
            print("Erreur lors de l'insertion :", e)
            return None

    def update(self, user):
        """Met à jour l'utilisateur donné dans MongoDB."""
        if not self.collection:
            print("Erreur : connexion à la base de données non disponible.")
            return
        try:
            if not user.id:
                print("Erreur : user.id manquant pour la mise à jour.")
                return
            self.collection.update_one(
                {"_id": ObjectId(user.id)},
                {"$set": {"name": user.name, "email": user.email}},
            )
        except Exception as e:
            print("Erreur lors de la mise à jour :", e)

    def delete(self, user_id):
        """Supprime l'utilisateur de MongoDB avec l'ID donné."""
        if not self.collection:
            print("Erreur : connexion à la base de données non disponible.")
            return
        try:
            self.collection.delete_one({"_id": ObjectId(user_id)})
        except Exception as e:
            print("Erreur lors de la suppression :", e)

    def delete_all(self):  # optionnel
        """Vide la collection users dans MongoDB."""
        if not self.collection:
            print("Erreur : connexion à la base de données non disponible.")
            return
        try:
            self.collection.delete_many({})
        except Exception as e:
            print("Erreur lors du vidage de la collection :", e)

    def close(self):
        if self.client:
            self.client.close()


# Alias facultatif pour compatibilité si du code attend encore `UserDAO`
UserDAO = UserDAOMongo
