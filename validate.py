"""
A validating to ensure the database acces is from the super user.
@:param String Username, Password
@:return None
"""
from pymongo import MongoClient
import bcrypt

# TODO: Remember to connect to Earthify Atlas cluster
client = MongoClient('mongodb://db:27017')
db = client.EarthifyDB
users = db['Users']


def validateUser(username, password):
    if users.find({
        'username': username}).count() != 1:
        return False
    hashed_pw = users.find({
        'username': username})[0]['password']

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    return False
