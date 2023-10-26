# from pyrebase import pyrebase
from firebase import Firebase

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


# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()

fire = Firebase(configdb)
db = fire.database()
print(db)

# date = {"name" : "atharva","surname" : "pawar","username" : "GTA","password" : "456"}

# email = 'test@gmail.com'
# password = '123456'

# user = auth.create_user_with_email_and_password(email,password)
# print(user)
# # --------------------------------------------------------------------
# # create data

# # database.push(date)














