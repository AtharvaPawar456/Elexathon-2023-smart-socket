def DeviceForm():
    with st.form(key='my_form'):
        username = st.text_input('Device Name',placeholder="enter device name")
        password = st.text_input('Device Secret Key',placeholder="enter device secret key")
        subVal = st.form_submit_button('Login')
        #    if subVal == True:
        #        if username == "" or password == "":
        #         st.info("Hello", "This is a notification!")

    st.write(subVal)
    if subVal:
        page = DevicePage
        page()
pages = {
    "Login": DeviceForm,
    "About": DevicePage,
}

# Render the sidebar menu
st.title("Navigation")
selection = st.radio("", list(pages.keys()),horizontal=True)

# Render the selected page
page = pages[selection]
page()


# fb.db:
Deviceid = Device456

db.child(Deviceid).child(DeviceKey).child("Port1").child("Status").set("True")
db.child(Deviceid).child(DeviceKey).child("Port1").child("Time").set("6:48")
db.child(Deviceid).child(DeviceKey).child("Port1").child("ScheduleStatus").set("True")
db.child(Deviceid).child(DeviceKey).child("Port1").child("Logs").child("datatime").push("10/11/2023-11:06")
db.child(Deviceid).child(DeviceKey).child("Port1").child("Logs").child("status").push("True")


db.child("Devices").child(Deviceid).child("Port1").child("Logs").child("status").push("True")


db.child("Devices").child(Deviceid).child("Port1").child("status").set("True")





db.child("Device_Name").child("DeviceKey").child("Port1").child("Logs").child("status").push("True")


data = {"username": loged_in_account_username, "FishData": databasetx}
db.child("Account_db").set(data)

send_delayData = {"a":delayValue}
db.child("test").set(send_delayData)

db.child("registerlog").push(data)

users = db.child("registerlog").get()

