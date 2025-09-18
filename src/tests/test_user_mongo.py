import os, sys


from daos.user_dao_mongo import UserDAOMongo as UserDAO
from models.user import User

dao = UserDAO()

def test_user_mongo_select():
	user_list = dao.select_all()
	# Pas d'hypothèse de seed côté Mongo; vérifier que ça retourne une liste
	assert isinstance(user_list, list)

def test_user_mongo_insert():
	user = User(None, 'Grace Hopper', 'hopper@example.com')
	dao.insert(user)
	user_list = dao.select_all()
	emails = [u.email for u in user_list]
	assert user.email in emails

def test_user_mongo_update():
	user = User(None, 'Katherine Johnson', 'kjohnson@example.com')
	assigned_id = dao.insert(user)

	corrected_email = 'katherine.johnson@example.com'
	user.id = assigned_id
	user.email = corrected_email

	dao.update(user)

	user_list = dao.select_all()
	emails = [u.email for u in user_list]
	assert corrected_email in emails

def test_user_mongo_delete():
	user = User(None, 'Tim Berners-Lee', 'tbl@example.com')
	assigned_id = dao.insert(user)
	dao.delete(assigned_id)

	user_list = dao.select_all()
	ids = [u.id for u in user_list]
	assert str(assigned_id) not in ids
