import streamlit as st

st.set_page_config(page_title="Fcube",
                    page_icon="🧊",
                    layout="wide")
st.title("Smart Fish Food Feeder")

col1, col2 = st.columns(2)
with col1:
    st.image('images\_fishlogo.png',width=140)
with col2:
    st.markdown('<p style="color: green;"># This text is blue</p>', unsafe_allow_html=True)


st.header("Developers:")
st.write(" ")
st.write(" ")
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Atharva Pawar")
   st.image("images\Developers\_app.png",width=200)
   st.write("Software Developer")
   st.markdown('''
   
   [Github     ](link)
   [Instagram  ](link) 
   [LinkedIn   ](link)
   [Facebook   ](link)

   ''')

with col2:
   st.header("Sahil Baikar")
   st.image("images\Developers\_baikar.png",width=200)
   st.write("Hardware Developer")
   st.markdown('''
   
   [Github     ](link)
   [Instagram  ](link) 
   [LinkedIn   ](link)
   [Facebook   ](link)

   ''')

with col3:
   st.header("Eshank Pawar")
   st.image("images\Developers\_pawar.png",width=200)
   st.write("Mechanical Developer")
   st.markdown('''
   
   [Github     ](link)
   [Instagram  ](link) 
   [LinkedIn   ](link)
   [Facebook   ](link)

   ''')
