import streamlit as st
import numpy as np
import pyrebase
import time
import PIL
from PIL import Image
import datetime


configdb = {
  "apiKey"              : "AIzaSyDZlUy8Iv20U1mhq23SM7xkRWqpOKRMNxQ",
  "authDomain"          : "smart-socket-elex.firebaseapp.com",
  "databaseURL"         : "https://smart-socket-elex-default-rtdb.firebaseio.com",
  "projectId"           : "smart-socket-elex",
  "storageBucket"       : "smart-socket-elex.appspot.com",
  "messagingSenderId"   : "844785896968",
  "appId"               : "1:844785896968:web:0ea4dc571818e8b4534bbd",
  "measurementId"       : "G-RLR2LLJLP2"
}


firebase = pyrebase.initialize_app(configdb)
db = firebase.database()
register_Stat = False
login_status = False
loged_in_account_username = ""
count = 0


def main():
    global register_Stat,loged_in_account_username
    # add_selectbox = st.sidebar.selectbox(
    #     "How would you like to be contacted?",
    #     ("Email", "Home phone", "Mobile phone")
    # )
    # st.sidebar.image('images\_fishlogo.png')
    # selectbox = st.empty()
    # add_selectbox1 = selectbox.sidebar.selectbox(
    #     "Login / Register",
    #     (" ","Login", "Register")
    # )

    # st.sidebar.write(add_selectbox1)

    # if add_selectbox1 == "Login":
    #     loginFun()
    #     add_selectbox1.selectbox(" ")


    # elif add_selectbox1 == "Register":
    #     registerFun()
    #     add_selectbox1.selectbox(" ")


    # selectbox = st.empty()
    add_selectbox1 = st.sidebar.selectbox(
        "Login / Register",
        ("Select an option","Login", "Register"),key="select_box"
    )

    st.sidebar.write(add_selectbox1)

    if add_selectbox1 == "Login":
        loginFun()

    elif add_selectbox1 == "Register":
        registerFun()


    if register_Stat == True:
        st.success("Register Done !!!")
    

    fishRxData()
    st.sidebar.write("Account: ", loged_in_account_username)


    
    # st.header("A cat")
    # st.image("https://static.streamlit.io/examples/cat.jpg")

    # with col2:
    # st.header("A dog")
    # st.image("https://static.streamlit.io/examples/dog.jpg")

    # with col3:
    # st.header("An owl")
    # st.image("https://static.streamlit.io/examples/owl.jpg")


# '''
# details about Goldfish
# details about Angelfish
# details about Guppy
# details about Catfish
# details about Tetra
# details about Molly
# details about Knife
# details about Plecostomus
# details about Shark
# details about Gourami

# '''




def fishRxData():
    global loged_in_account_username
    username_for_db = st.text_input("Enter Username: ")
    fishselected = st.multiselect('Select type of fish you have in Tank', ["Goldfish", "Angelfish", "Guppy", "Catfish", "Tetra", "Molly", "Knife Fish", "Plecostomus", "Shark", "Gourami"])

    st.write(f'Selected Types of fishs: {fishselected}')

    col1, col2 = st.columns(2)
    col1.write(" ")
    col2.write(" ")

    # num_items = st.number_input('How many  do you want to add?', min_value=1, max_value=10)

    # # Create an empty list to store items
    items = []
    databasetx = []
    # Loop through the range of user input value and add items to the list
    with col1:
        for i in range(len(fishselected)):
            st.write(f'Fish type {i+1} ({fishselected[i]}):')
            inputNo = st.number_input('Fish Count:', 0, 10, key=f'input_{i}')
            for j in range(inputNo):
                fishsize = st.select_slider(f'Pick a size ({fishselected[i]},Fish Type{i+1} ---  Fish {j+1})', ['S', 'M', 'L'], key=f'size_{i}_{j}')
                item = {'fish_type': fishselected[i], 'fish_count': j, 'fish_size': fishsize}
                databasetx.append(item)

    # st.write(databasetx)
    # print("----------------------------------------------------------------------------------------------------------")
    # databasetxAcc = 
    # print(databasetx)

    fish_account_data = {loged_in_account_username: databasetx}
    # item = st.text_input(f'Fish type {i+1} ({fishselected[i]}):')
    # items.append(item)

    # Display the list of items
    # st.write(f'Items: {items}')
    if st.button("Upload Data"):
        data = {"username": loged_in_account_username, "FishData": databasetx}

        # db.child("Account_db").child(loged_in_account_username).push(fish_account_data)
        db.child("Account_db").set(data)

        # for i in databasetx:
        #     account_data = databasetx[abc]
        #     db.child("Account_db").child(loged_in_account_username).push(account_data)
        #     abc += 1
        st.success("Data Uploaded successfully !!!")

        #Backend Ml
        # st.write(databasetx)
        # abcd = 0
        # for item in databasetx:
        #     st.write(f'databasetx-index {abcd} :  {databasetx[abcd]["fish_type"]}')
        #     abcd += 1
        delayValue = Backend_Ml(databasetx)
        send_delayData = {"a":delayValue}
        db.child("test").set(send_delayData)


    with col2:
        pass
        # for i in range(len(fishselected)):
        #     # inputNo = st.number_input('Pick a number', 0, 10)
        #     item = st.number_input(f'Fish {i+1} ({fishselected[i]}):')
        #     items.append(item)

def Backend_Ml(databasetx):
    # fish food in grams [S,M,L] for different size where eg: goldfish[ [flakes], [pellets] ]
    # fd_goldfish =      [ [0.5,1,2],    [0.75,1.5,3] ]
    # fd_angelfish=      [ [0.5,1,2],    [0.75,1.5,3] ]
    # fd_guppy =         [ [0.5,1,2],    [0.75,1.5,3] ] 
    # fd_catfish =       [ [0.5,1,2],    [0.75,1.5,3] ]
    # fd_tetra =         [ [0.5,1,2],    [0.75,1.5,3] ]
    # fd_molly =         [ [0.5,1,2],    [0.75,1.5,3] ]
    # fd_knifefish =     [ [0.5,1,2],    [0.75,1.5,3] ]
    # fd_plecostomus =   [ [0.5,1,2],    [0.75,1.5,3] ]
    # fd_shark =         [ [0.5,1,2],    [0.75,1.5,3] ]
    # fd_gourami =       [ [0.5,1,2],    [0.75,1.5,3] ] 

    fd_fish =     [     [ [0.5,1,2],    [0.75,1.5,3] ],
                        [ [0.5,1,2],    [0.75,1.5,3] ],
                        [ [0.5,1,2],    [0.75,1.5,3] ], 
                        [ [0.5,1,2],    [0.75,1.5,3] ],
                        [ [0.5,1,2],    [0.75,1.5,3] ],
                        [ [0.5,1,2],    [0.75,1.5,3] ],
                        [ [0.5,1,2],    [0.75,1.5,3] ],
                        [ [0.5,1,2],    [0.75,1.5,3] ],
                        [ [0.5,1,2],    [0.75,1.5,3] ],
                        [ [0.5,1,2],    [0.75,1.5,3] ] ]

    mydelay = 0
    # ["Goldfish", "Angelfish", "Guppy", "Catfish", "Tetra", "Molly", "Knife", "Plecostomus", "Shark", "Gourami"]
    count = [0,0,0,0,0,0,0,0,0,0]
    size = ["S","M","L"]
    
    # for i in range(len(databasetx)):
    #     fishName = ["Goldfish", "Angelfish", "Guppy", "Catfish", "Tetra", "Molly", "Knife", "Plecostomus", "Shark", "Gourami"]
    #     for fishes in range(len(fishName)):
    #         if databasetx[i]["fish_type"] == fishName[fishes]:
    #             for j in range(3):
    #                 if databasetx[i]["fish_size"] == size[j]:
    #                     mydelay += fd_fish[i][0][j]
    #                     st.write(f'{fishName[fishes]} : {fd_fish[i][0][j]}')
    # st.write("mydelay: ",mydelay)

    for i in range(len(databasetx)):
        fishName = ["Goldfish", "Angelfish", "Guppy", "Catfish", "Tetra", "Molly", "Knife", "Plecostomus", "Shark", "Gourami"]
        for fishes in range(len(fishName)):
            if databasetx[i]["fish_type"] == fishName[fishes]:
                for j in range(len(size)):
                    if databasetx[i]["fish_size"] == size[j]:
                        mydelay += fd_fish[fishes][0][j]
                        # st.write(f'{fishName[fishes]} : {fd_fish[fishes][0][j]}')
    st.write("Total food in gram : ",mydelay)
    return mydelay


# ["Goldfish", "Angelfish", "Guppy", "Catfish", "Tetra", "Molly", "Knife", "Plecostomus", "Shark", "Gourami"]

# [
# 0:{
# "fish_type":"Angelfish"
# "fish_count":0
# "fish_size":"S"
# }
# 1:{
# "fish_type":"Angelfish"
# "fish_count":1
# "fish_size":"S"
# }
# 2:{
# "fish_type":"Guppy"
# "fish_count":0
# "fish_size":"S"



def loginFun():
    global login_status,loged_in_account_username,count

    # data = {"username": "pawar", "password": "1254gy@"}

    # st.write("Account Login")
    # with st.form(key='my_form1'):
    #     username = st.text_input('Username')
    #     password = st.text_input('Password')
    #     value1 = st.form_submit_button('Login')
    #     st.write(value1)
    #     if value1 == True:
    #         st.write("loged - in")

    # with st.container():
    #     st.write("This is inside the container")
    #     st.bar_chart(np.random.randn(50, 3))
    #     st.write("This is outside the container")



    # Create the login form using the st.form context manager
    with st.sidebar.form(key="login_form"):
    # with st.form(key="login_form"):
        # Add input fields for username and password
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        # Add a submit button
        submitted = st.form_submit_button("Submit")
        # st.write(submitted)

        # Check if the form has been submitted
        if submitted:
            # check account in dB
            # users = db.child("registerlog").get()
            # for user in users.each():
            #     print(user.key(), user.val("name"),user.val("password"))

            users = db.child("registerlog").get()
            # accountsListUsername = []
            # accountsListPassword = []
            for user in users.each():
                nameR = user.val()["username"]
                passwordR = user.val()["password"]
                print("Name: {}, Password: {}".format(nameR, passwordR))
                print(username,nameR)
                print(password,passwordR)
                if username == nameR and password == passwordR:
                    login_status = True
                    print("ture")

        # Display login status
        if login_status:
            st.sidebar.success("Login successful!")
            st.write(f'Hello {username}')
            loginLogFun(username)
            if count == 0:
                loged_in_account_username = username
                count = 1
                st.write("Account Name: ",loged_in_account_username)

            
        else:
            st.sidebar.warning("Login failed. Please try again.")
    # if count == 1:
    #     fishRxData()
    # return loged_in_account_username



def registerFun():
    global register_Stat
    with st.sidebar.form(key='my_form2'):
        name = st.text_input('Name')
        surname = st.text_input('Surname')
        username = st.text_input('Username')
        password = st.text_input('Enter Password')
        Repassword = st.text_input('Reenter Password')
        data = {"name": name,"surname": surname,"username": username, "password": password}
        datalist = [name,surname,username,password,Repassword]
        value2 = st.form_submit_button('Resigter')
        register_Stat = value2
        # if value2:
        #     st.sidebar.success("Login successful!")
        # else:
        #     st.sidebar.warning("Login failed. Please try again.")

        if value2 == True:
            list_empty = False
            for item in datalist:
                if not item:
                    list_empty = True
                    break

            if list_empty:
                st.sidebar.warning("Fill all the details")

            else:
                # st.write(value2)
                if password == Repassword:
                    db.child("registerlog").push(data)
                    st.sidebar.success("Registered successful!")

                    register_Stat = True
                else:
                    st.sidebar.warning("Wrong Username Or Password")


def loginLogFun(username):
    now = datetime.datetime.now()
    currenttime = now.strftime("%d-%m-%Y %H:%M:%S")
    # print("Current date and time: ",currenttime)

    data = {"username": username, "time": currenttime}
    db.child("loginlogs").push(data)


if __name__ == '__main__':
    st.set_page_config(page_title="Fcube",
                       page_icon=":fish:",
                       layout="wide")
    st.title("Smart Fish Food Feeder")
    main()

# streamlit run app.py

# name
# :
# "gta"
# password
# :
# "123"
# surname
# :
# "pawar"
# username
# :
# "tim"


# ['account1' : {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'M'}, {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'M'}, {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Guppy', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Guppy', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Knife Fish', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Tetra', 'fish_count': 1, 'fish_size': 'M'}, {'fish_type': 'Tetra', 'fish_count': 1, 'fish_size': 'L'},
# 'account2' : {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'M'}, {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'M'}, {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Guppy', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Guppy', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Knife Fish', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'L'}, {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Tetra', 'fish_count': 1, 'fish_size': 'M'}, {'fish_type': 'Tetra', 'fish_count': 1, 'fish_size': 'L'}
# ]

# db.child("Account_db").push(data)

# give code that uploads the above json to goolg firebase as Account_db

# // Set the data
# var data = {
#   'account1' : {
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'M'}, 
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'M'}, 
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Guppy', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Guppy', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Knife Fish', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Tetra', 'fish_count': 1, 'fish_size': 'M'}, 
#     {'fish_type': 'Tetra', 'fish_count': 1, 'fish_size': 'L'},
#   },
#   'account2' : {
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'M'}, 
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'M'}, 
#     {'fish_type': 'Goldfish', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Guppy', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Guppy', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Knife Fish', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'L'}, 
#     {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'S'}, 
#     {'fish_type': 'Tetra', 'fish_count': 1, 'fish_size': 'M'}, 
#     {'fish_type': 'Tetra', 'fish_count': 1, 'fish_size': 'L'}
#   }
# }

# // Get a reference to the database service
# var database = firebase.database();

# // Push the data to the database
# database.ref('Account_db').push(data);

# data
# [{'fish_type': 'Angelfish', 'fish_count': 0, 'fish_size': 'M'}, {'fish_type': 'Angelfish', 'fish_count': 1, 'fish_size': 'M'}, {'fish_type': 'Angelfish', 'fish_count': 2, 'fish_size': 'S'}, {'fish_type': 'Angelfish', 'fish_count': 3, 'fish_size': 'S'}, {'fish_type': 'Molly', 'fish_count': 0, 'fish_size': 'S'}, {'fish_type': 'Molly', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Molly', 'fish_count': 2, 'fish_size': 'S'}, {'fish_type': 'Catfish', 'fish_count': 0, 'fish_size': 'S'}, {'fish_type': 'Catfish', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Guppy', 'fish_count': 0, 'fish_size': 'S'}, {'fish_type': 'Guppy', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Plecostomus', 'fish_count': 0, 'fish_size': 'S'}, {'fish_type': 'Plecostomus', 'fish_count': 1, 'fish_size': 'S'}, {'fish_type': 'Plecostomus', 'fish_count': 2, 'fish_size': 'S'}, {'fish_type': 'Plecostomus', 'fish_count': 3, 'fish_size': 'S'}, {'fish_type': 'Plecostomus', 'fish_count': 4, 'fish_size': 'S'}, {'fish_type': 'Knife Fish', 'fish_count': 0, 'fish_size': 'S'}, {'fish_type': 'Knife Fish', 'fish_count': 1, 'fish_size': 'S'}]