import pyrebase

configdb = {
  "apiKey"              : "AIzaSyDgz34RIMvnV95tfI0QVL0yLF_3IlN8nvU",
  "authDomain"          : "firewebtest-acd85.firebaseapp.com",
  "projectId"           : "firewebtest-acd85",
  "databaseURL"         : "https://firewebtest-acd85-default-rtdb.firebaseio.com",
  "storageBucket"       : "firewebtest-acd85.appspot.com",
  "messagingSenderId"   : "355676175409",
  "appId"               : "1:355676175409:web:9d207ac8d11828c1382910",
  "measurementId"       : "G-6Z60DDCB8Y"
}

firebase = pyrebase.initialize_app(configdb)

# get a reference to the database
db = firebase.database()

# write data to the database
data = {"username": "pawar", "password": "1254gy@"}
# db.child("users").push(data)
db.child("registerlog").push(data)



# read data from the database
users = db.child("users").get()
for user in users.each():
    print(user.key(), user.val())



# ---------------------------------------------------------------


import pyrebase

configdb = {
  "apiKey"              : "AIzaSyDgz34RIMvnV95tfI0QVL0yLF_3IlN8nvU",
  "authDomain"          : "firewebtest-acd85.firebaseapp.com",
  "projectId"           : "firewebtest-acd85",
  "databaseURL"         : "https://firewebtest-acd85-default-rtdb.firebaseio.com",
  "storageBucket"       : "firewebtest-acd85.appspot.com",
  "messagingSenderId"   : "355676175409",
  "appId"               : "1:355676175409:web:9d207ac8d11828c1382910",
  "measurementId"       : "G-6Z60DDCB8Y"
}

firebase = pyrebase.initialize_app(configdb)

# get a reference to the database
db = firebase.database()

# write data to the database
data = {"username": "pawar", "password": "1254gy@"}
# db.child("users").push(data)
db.child("Account_db").push(data)



# read data from the database
users = db.child("users").get()
for user in users.each():
    print(user.key(), user.val())












# auth = firebase.auth()

# email = 'test@gmail.com'
# password = '123456'
# def register():
#     try:
#         auth.create_user_create_user_with_email_and_password(email,password)
#         print("register ok")

#     except Exception as e:
#         print(e)
#         print("failed")

# register()






# auth = firebase.auth()

# email = 'test@gmail.com'
# password = '123456'
# def register():
#     try:
#         auth.create_user_create_user_with_email_and_password(email,password)
#         print("register ok")

#     except Exception as e:
#         print(e)
#         print("failed")

# register()
