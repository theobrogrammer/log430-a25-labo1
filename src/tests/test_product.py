from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    # au minimum, aucune contrainte de seed ici, vérifier que ça retourne une liste
    assert isinstance(product_list, list)

def test_product_insert():
    product = Product(None, 'ThinkPad X1', 'Lenovo', 1999.99)
    dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names

def test_product_update():
    product = Product(None, 'MacBook Air', 'Apple', 1499.0)
    assigned_id = dao.insert(product)

    new_price = 1399.0
    product.id = assigned_id
    product.price = new_price

    dao.update(product)

    product_list = dao.select_all()
    updated = [p for p in product_list if p.id == assigned_id]
    assert any(abs(p.price - new_price) < 1e-6 for p in updated)

def test_product_delete():
    product = Product(None, 'Surface Laptop', 'Microsoft', 1299.0)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)

    product_list = dao.select_all()
    ids = [p.id for p in product_list]
    assert assigned_id not in ids