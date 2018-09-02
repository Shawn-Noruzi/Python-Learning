import pymongo
from pymongo import MongoClient
myClient = MongoClient()

db = myClient.mydb

#mongo SQL table is called a collection

#create table
users = db.users

#data to be put in
user1 = {"username": "josh", "pass": "123", "fav_num": "2", "hobbies":["games","python","moregames"]}

#how to put it in
user_id = users.insert_one(user1).inserted_id


#multi objects to insert
user_many = [{"username": "third", "password":"123"}, {"username2": "third", "password":"123"},{"username": "third", "password":"123"}]

#command is db.insert_many(obj)
users.insert_many(user_many)