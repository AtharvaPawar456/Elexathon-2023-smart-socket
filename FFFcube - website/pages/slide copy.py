import streamlit as st
import pyrebase
import datetime


Deviceid  = st.text_input('Device name', placeholder="enter device name")
DeviceKey = st.text_input('Device Secret Key', placeholder="enter device secret key")
SubmitDeviceinfo = st.button('Go')


# def DevicePage():
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
    if port1val == "ON":ONLabel(port1val)
    if port1val == "OFF":OFFLabel(port1val)

    if port2val == "ON":ONLabel(port2val)
    if port2val == "OFF":OFFLabel(port2val)

    if port3val == "ON":ONLabel(port3val)
    if port3val == "OFF":OFFLabel(port3val)

    if port4val == "ON":ONLabel(port4val)
    if port4val == "OFF":OFFLabel(port4val)


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

# if SubmitDeviceinfo == True:
#     page = DevicePage
#     page()
