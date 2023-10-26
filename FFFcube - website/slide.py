import streamlit as st
import pyrebase
import datetime
import pandas as pd


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

# DB Variables:
# portNumber = 

# info:-  Deviceid == "SmartDevice456" ,  DeviceKey == "123":
 
SubmitDeviceinfoParall = False

prevport1val,prevport2val,prevport3val,prevport4val = "OFF","OFF","OFF","OFF"

port1Num,port2Num,port3Num,port4Num = 0,0,0,0

def main(Deviceid,DeviceKey):
    global firebase, db, configdb, prevport1val,prevport2val,prevport3val,prevport4val
    now = datetime.datetime.now()
    cdate = now.strftime("%Y-%m-%d")
    ctime = now.strftime("%H:%M:%S")


    # -----------------------------------------------
    # Deviceid  = 12345


    titalVal = f'Deviceid : {Deviceid}'
    st.title(titalVal)

    p1Visibal,p2Visibal,p3Visibal,p4Visibal = "visible","visible","visible","visible"

    disabledP1,disabledP2,disabledP3,disabledP4 = False,False,False,False

    st.markdown('''<h3 style="color: aquamarine;">Control Port</h3>''', unsafe_allow_html=True)

    col1, col2,col3 = st.columns(3)

    with col1:
        st.header("Port 1")
        st.header("Port 2")
        st.header("Port 3")
        st.header("Port 4")

    with col2:
        port1val = st.radio(
            "",
            ["ON", "OFF"],
            key="visibility1",
            label_visibility=p1Visibal,
            disabled = disabledP1,
            horizontal=True,
        )
        port2val = st.radio(
            "",
            ["ON", "OFF"],
            key="visibility2",
            label_visibility=p2Visibal,
            disabled = disabledP2,
            horizontal=True,
        )
        port3val = st.radio(
            "",
            ["ON", "OFF"],
            key="visibility3",
            label_visibility=p3Visibal,
            disabled = disabledP3,
            horizontal=True,
        )
        port4val = st.radio(
            "",
            ["ON", "OFF"],
            key="visibility4",
            label_visibility=p4Visibal,
            disabled = disabledP4,
            horizontal=True,
        )
        
    def ONLabel(val):
        st.success(f'Status : {val}')

    def OFFLabel(val):
        st.error(f'Status : {val}')

    with col3:
        data = {
            "DeviceKey" : DeviceKey,
            "Deviceid"  : Deviceid,
            "Port1": {
                "status"    : "ON",
                "Time"      : "6:48",
                "TimeStatus": "True",
                "log"       : {
                    "info" : "10/11/2023 - ON",
                    }
                      },
            "Port2": {
                "status"    : "ON",
                "Time"      : "6:48",
                "TimeStatus": "True",
                "log"       : {
                    "info" : "10/11/2023 - ON",
                    }
                      },
            "Port3": {
                "status"    : "ON",
                "Time"      : "6:48",
                "TimeStatus": "True",
                "log"       : {
                    "info" : "10/11/2023 - ON",
                    }
                      },
            "Port4": {
                "status"    : "ON",
                "Time"      : "6:48",
                "TimeStatus": "True",
                "log"       : {
                    "info" : "10/11/2023- - ON",
                    }
                      }
        }

        # Send the data to Firebase
        # db.child("users").child("john").set(data)
        # db.child("Devices").child(Deviceid).set(data)

        if port1val == "ON":
            port1Num = 1
            ONLabel(port1val)
            db.child("Devices").child(Deviceid).child("Port1").child("status").set(port1Num)
            if port1val != prevport1val:
                if prevport1val == "ON":prevport1val = "OFF"
                else: prevport1val = "ON"
                # db.child("Devices").child(Deviceid).child("Port1").child("log").child("info").push(f'{cdate}-{ctime}-{port1Num}')
                # users = db.child("Devices").child(Deviceid).child("Port1").get()
                # st.write(users)



        if port1val == "OFF":
            port1Num = 0
            OFFLabel(port1val)
            db.child("Devices").child(Deviceid).child("Port1").child("status").set(port1Num)
            if port1val != prevport1val:
                if prevport1val == "ON":prevport1val = "OFF"
                else: prevport1val = "ON"
                # db.child("Devices").child(Deviceid).child("Port1").child("log").child("info").push(f'{cdate}-{ctime}-{port1Num}')



        if port2val == "ON":
            port2Num = 1
            ONLabel(port2val)
            db.child("Devices").child(Deviceid).child("Port2").child("status").set(port2Num)
            if port1val != prevport2val:
                if prevport2val == "ON":prevport2val = "OFF"
                else: prevport2val = "ON"
                # db.child("Devices").child(Deviceid).child("Port2").child("log").child("info").push(f'{cdate}-{ctime}-{port2Num}')


        if port2val == "OFF":
            port2Num = 0
            OFFLabel(port2val)
            db.child("Devices").child(Deviceid).child("Port2").child("status").set(port2Num)
            if port1val != prevport2val:
                if prevport2val == "ON":prevport2val = "OFF"
                else: prevport2val = "ON"
                # db.child("Devices").child(Deviceid).child("Port2").child("log").child("info").push(f'{cdate}-{ctime}-{port2Num}')



        if port3val == "ON":
            port3Num = 1
            ONLabel(port3val)
            db.child("Devices").child(Deviceid).child("Port3").child("status").set(port3Num)
            if port3val != prevport3val:
                if prevport3val == "ON":prevport3val = "OFF"
                else: prevport3val = "ON"
                # db.child("Devices").child(Deviceid).child("Port3").child("log").child("info").push(f'{cdate}-{ctime}-{port3Num}')


        if port3val == "OFF":
            port3Num = 0
            OFFLabel(port3val)
            db.child("Devices").child(Deviceid).child("Port3").child("status").set(port3Num)
            if port3val != prevport3val:
                if prevport3val == "ON":prevport3val = "OFF"
                else: prevport3val = "ON"
                # db.child("Devices").child(Deviceid).child("Port3").child("log").child("info").push(f'{cdate}-{ctime}-{port3Num}')



        if port4val == "ON":
            port4Num = 1
            ONLabel(port4val)
            db.child("Devices").child(Deviceid).child("Port4").child("status").set(port4Num)
            if port4val != prevport4val:
                if prevport4val == "ON":prevport4val = "OFF"
                else: prevport4val = "ON"
                # db.child("Devices").child(Deviceid).child("Port4").child("log").child("info").push(f'{cdate}-{ctime}-{port4Num}')
                


        if port4val == "OFF":
            port4Num = 0
            OFFLabel(port4val)
            db.child("Devices").child(Deviceid).child("Port4").child("status").set(port4Num)
            if port4val != prevport4val:
                if prevport4val == "ON":prevport4val = "OFF"
                else: prevport4val = "ON"
                # db.child("Devices").child(Deviceid).child("Port4").child("log").child("info").push(f'{cdate}-{ctime}-{port4Num}')




    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown('''<h3 style="color: aquamarine;">Set Smart Socket Schedule</h3>''', unsafe_allow_html=True)


    Timecol1, Timecol2,Timecol3, Timecol4 = st.columns(4)

    with Timecol1:
        st.header("Port 1")
        st.header("Port 2")
        st.header("Port 3")
        st.header("Port 4")

    with Timecol2:
        ScheduleHrP1 = st.number_input('Hour', 0, 23, key = "ScheduleHrP1Key")
        ScheduleHrP2 = st.number_input('Hour', 0, 23, key = "ScheduleHrP2Key")
        ScheduleHrP3 = st.number_input('Hour', 0, 23, key = "ScheduleHrP3Key")
        ScheduleHrP4 = st.number_input('Hour', 0, 23, key = "ScheduleHrP4Key")


    with Timecol3:
        ScheduleMnP1 = st.number_input('Minute', 0, 59, key = "ScheduleMnP1Key")
        ScheduleMnP2 = st.number_input('Minute', 0, 59, key = "ScheduleMnP2Key")
        ScheduleMnP3 = st.number_input('Minute', 0, 59, key = "ScheduleMnP3Key")
        ScheduleMnP4 = st.number_input('Minute', 0, 59, key = "ScheduleMnP4Key")


    with Timecol4:
        st.write("Schedule Time")
        UpdateTimeP1 = st.button('Update', key = "UpdateTimeP1Key")
        st.write("")
        st.write("")
        UpdateTimeP2 = st.button('Update', key = "UpdateTimeP2Key")
        st.write("")
        st.write("")
        UpdateTimeP3 = st.button('Update', key = "UpdateTimeP3Key")
        st.write("")
        st.write("")
        UpdateTimeP4 = st.button('Update', key = "UpdateTimeP4Key")

        if UpdateTimeP1:
            db.child(Deviceid).child(DeviceKey).child("Port1").child("Time").set(f'{ScheduleHrP1}:{ScheduleMnP1}')
            UpdateTimeP1 = False

        if UpdateTimeP2:
            db.child(Deviceid).child(DeviceKey).child("Port2").child("Time").set(f'{ScheduleHrP2}:{ScheduleMnP2}')
            UpdateTimeP2 = False

        if UpdateTimeP3:
            db.child(Deviceid).child(DeviceKey).child("Port3").child("Time").set(f'{ScheduleHrP3}:{ScheduleMnP3}')
            UpdateTimeP3 = False

        if UpdateTimeP4:
            db.child(Deviceid).child(DeviceKey).child("Port4").child("Time").set(f'{ScheduleHrP4}:{ScheduleMnP4}')
            UpdateTimeP4 = False

    data = pd.DataFrame({
    'Time': [1, 2, 3, 4, 5],
    'Power': [10, 5, 15, 12, 7]
    })

    # plot line chart
    st.line_chart(data) 


    # from datetime import datetime, time


    # st.button('Click me')
    # # st.experimental_data_editor('Edit data', data)
    # st.checkbox('I agree')
    # st.radio('Pick one', ['cats', 'dogs'])
    # st.selectbox('Pick one', ['cats', 'dogs'])
    # st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
    # st.slider('Pick a number', 0, 100)
    # st.select_slider('Pick a size', ['S', 'M', 'L'])
    # st.text_input('First name')
    # st.number_input('Pick a number', 0, 10)
    # st.text_area('Text to translate')
    # st.date_input('Your birthday')
    # st.time_input('Meeting time')
    # # st.file_uploader('Upload a CSV')
    # # st.download_button('Download file', data)
    # # st.camera_input("Take a picture")
    # st.color_picker('Pick a color')



    # togglep1 = st.checkbox("Toggle me", key="my_toggle", value=True, help="Click to toggle the button")
    # if togglep1 == True:disabledP1 = True
    # if togglep1 == False:disabledP1 = False

    # st.markdown("<h1 id='mytitle'>My Title</h1>", unsafe_allow_html=True)

    # st.markdown("Here is some content.")

    # st.markdown("[Jump to My Title](#mytitle)")

    # def home():
    #     st.write("Welcome to my app!")

    # def about():
    #     st.write("This is my about page.")


    # pages = {
    #     "Home": home,
    #     "About": about,
    # }

    # # Render the sidebar menu
    # st.sidebar.title("Navigation")
    # selection = st.radio("", list(pages.keys()))

    # # Render the selected page
    # page = pages[selection]
    # page()

    # if SubmitDeviceinfo == True or SubmitDeviceinfoParall == True:
    #     if Deviceid == "SmartDevice456" and DeviceKey == "123":
    #         page = main
    #         SubmitDeviceinfoParall = True
    #         page()





if __name__ == '__main__':
    st.set_page_config(page_title="Smart Socket",
                       page_icon=":socket:",
                       layout="wide")
    # st.title("Smart Socket")
    st.markdown('''<h1 style="font-family:courier;font-size:500%;color:blue;text-align:center;">Smart Socket</h1>''', unsafe_allow_html=True)

    # <h1 style="font-family:courier;font-size:300%;color:blue;">This is a heading</h1>

    Deviceid  = "SmartDevice456"
    DeviceKey =  "123"
    # Deviceid  = st.text_input('Device name', placeholder="enter device name")
    # DeviceKey = st.text_input('Device Secret Key', placeholder="enter device secret key")
    # SubmitDeviceinfo = st.button('Go')
    # if SubmitDeviceinfo == True or SubmitDeviceinfoParall == True:
    #     if Deviceid == "SmartDevice456" and DeviceKey == "123":
    #         SubmitDeviceinfoParall = True
    #         main(Deviceid,DeviceKey,SubmitDeviceinfo)
    main(Deviceid,DeviceKey)

# streamlit run slide.py


# Deviceid DeviceKey
# 


'''
                if users is not None and users.val() is not None:
                    port1_log = users.val().get("log")
                    if port1_log is not None:
                        # print("Port1 Log:")
                        st.write("Port1 Log:")

                        for key, value in port1_log.items():
                            # print(key, ":", value)
                            st.write(key, ":", value)

                            
Devices/SmartDevice456/Port1/status   = 1                           
Devices/SmartDevice456/Port1/status   = 0                          

'''