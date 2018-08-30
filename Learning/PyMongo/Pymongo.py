import pymongo
from pymongo import MongoClient
myClient = MongoClient()

db = myClient.mydb

#mongo SQL table is called a collection

users = db.users

user1 = {"username": "nick", "pass": "123", "fav_num": "2", "hobbies":["games","python","moregames"]}

user_id = users.insert_one(user1).inserted_id

