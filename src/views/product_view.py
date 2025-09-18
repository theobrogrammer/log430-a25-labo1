"""
Product view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.product import Product
from controllers.product_controller import ProductController


class MenuPrinter:
	"""Affiche les options du menu Produits."""

	@staticmethod
	def print_menu():
		print("\n1. Montrer la liste d'items")
		print("2. Ajouter un item")
		print("3. Supprimer un item")
		print("4. Retour")


class ProductView:
	@staticmethod
	def show_options():
		"""Affiche le menu Produits et traite les choix utilisateur."""
		controller = ProductController()
		while True:
			MenuPrinter.print_menu()
			choice = input("Choisissez une option : ").strip()

			if choice == '1':
				products = controller.list_products()
				ProductView.show_products(products)
			elif choice == '2':
				name, brand, price = ProductView.get_inputs()
				if name is None:
					# entrée invalide déjà signalée
					continue
				product = Product(None, name, brand, price)
				controller.create_product(product)
			elif choice == '3':
				pid = input("ID du produit à supprimer : ").strip()
				if not pid.isdigit():
					print("ID invalide. Veuillez entrer un entier.")
					continue
				controller.delete_product(int(pid))
			elif choice == '4':
				controller.shutdown()
				break
			else:
				print("Cette option n'existe pas.")

	@staticmethod
	def show_products(products):
		"""Affiche la liste des produits."""
		if not products:
			print("(Aucun item)")
			return
		print("\n".join(f"{p.id}: {p.name} [{p.brand}] - {p.price:.2f}$" for p in products))

	@staticmethod
	def get_inputs():
		"""Demande les informations pour ajouter un produit."""
		name = input("Nom de l'item : ").strip()
		brand = input("Marque : ").strip()
		price_str = input("Prix : ").strip()
		if not name or not brand or not price_str:
			print("Entrées manquantes. Opération annulée.")
			return None, None, None
		try:
			price = float(price_str)
		except ValueError:
			print("Prix invalide. Veuillez entrer un nombre.")
			return None, None, None
		return name, brand, price

