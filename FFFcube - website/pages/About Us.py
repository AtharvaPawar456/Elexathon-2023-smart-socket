import streamlit as st

st.set_page_config(page_title="Fcube",
                    page_icon=":fish:",
                    layout="wide")
st.title("Smart Fish Food Feeder")

col1, col2 = st.columns(2)
with col1:
    st.image('images\_fishlogo.png',width=140)
with col2:
    st.markdown('<p style="color: green;"># This text is blue</p>', unsafe_allow_html=True)


st.markdown("""
# About Our Product

The smart fish food feeder described above is an advanced device that uses technology to provide the right amount of food to fish, based on various factors such as the type and number of fish, and their size. This helps to prevent overfeeding, which can be harmful to the fish and the aquatic environment.

One of the key features of this product is its dynamic functionality, which allows users to schedule feeding times for up to a month in advance, using the food container attached to the device. This means that fish owners can be confident that their fish are getting the right amount of food, even when they are away from home.

At our company, we are committed to developing innovative products that help fish owners to care for their pets more easily and effectively. Our smart fish food feeder is the result of years of research and development, and we are proud to offer a product that is not only practical but also affordable and user-friendly.

Our team of experts includes experienced engineers, designers, and fish enthusiasts who are passionate about improving the lives of both fish and their owners. We believe that our smart fish food feeder is just the beginning of a new generation of smart aquarium products that will revolutionize the way people care for their aquatic pets.

With our focus on innovation, quality, and customer satisfaction, we are confident that our products will continue to meet the needs of fish owners around the world, and we look forward to being a part of your fish-keeping journey.



This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).

""")

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
