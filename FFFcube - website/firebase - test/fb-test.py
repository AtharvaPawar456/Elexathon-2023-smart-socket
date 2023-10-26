import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize the SDK with your project's service account key
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-name.firebaseio.com'
})

# Get a reference to the database service
ref = db.reference('')

# Write data to the database
ref.child('users').push({
    'name': 'John Doe',
    'email': 'johndoe@example.com'
})

# Read data from the database
users = ref.child('users').get()
print(users)
