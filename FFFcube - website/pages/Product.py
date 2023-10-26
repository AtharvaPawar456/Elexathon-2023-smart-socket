import streamlit as st

# Get user input value
# num_items = st.number_input('How many  do you want to add?', min_value=1, max_value=10)

# # Create an empty list to store items
# items = []

# # Loop through the range of user input value and add items to the list
# for i in range(num_items):
#     item = st.text_input(f'Enter item {i+1}:')
#     items.append(item)

# # Display the list of items
# st.write(f'Items: {items}')

# st.write(
#     '<style>button[title="View fullscreen"], h4 a {display: none !important} hello world img {border: 1px solid #D6D6D9; border-radius: 3px; height: 200px; object-fit: cover; width: 100%} .block-container img:hover {}</style> hello gta',
#     unsafe_allow_html=True,
# )



col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg",width=60)

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg",width=60)

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg",width=60)




col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

# Three different columns:
col1, col2, col3 = st.columns([3, 1, 1])
# col1 is larger.

with col1:
    st.radio('Select one:', [1, 2])

fishselected = st.multiselect('Select type of fish you have in Tank', ["Goldfish", "Angelfish", "Guppy", "Catfish", "Tetra", "Molly", "Knife Fish", "Plecostomus", "Shark", "Gourami"])

st.write(fishselected)

col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


tab11,tab12,tab13 = st.tabs(["Small","Medium","Large"])

with tab11:
    st.selectbox('Select one:', [1, 2],key='selectbox_1')

with tab12:
    st.selectbox('Select one:', [1, 2],key='selectbox_2')

with tab13:
    st.selectbox('Select one:', [1, 2],key='selectbox_3')

st.selectbox('Pick one', ['cats', 'dogs'])



# database

# const char *fish[10] = {"Goldfish", "Angelfish", "Guppy", "Catfish", "Tetra", "Molly", "Knife Fish", "Plecostomus", "Shark", "Gourami"};
# const char *food[2] = {"Flakes", "Pellets"};
# const char *size[3] = {"Small", "Medium", "Big"};
# int data[3] = {0, 0, 0}; // fishIndex foodIndex sizeIndex

# float food_value[2][3] = {{0.5, 1, 2}, {0.75, 1.5, 3}};

# float weight = 0.0;
# float dataarray[10][2][3]=
# {
#   {{0.5, 1, 2}, {0.75, 1.5, 3}}, // Goldfish
#   {{0.5, 1, 2}, {0.75, 1.5, 3}}, // Angelfish
#   {{0.5, 1, 2}, {0.75, 1.5, 3}}, // Guppy
#   {{0.5, 1, 2}, {0.75, 1.5, 3}}, // Catfish
#   {{0.5, 1, 2}, {0.75, 1.5, 3}}, // Tetra
#   {{0.5, 1, 2}, {0.75, 1.5, 3}}, // Molly
#   {{0.5, 1, 2}, {0.75, 1.5, 3}}, // Knife Fish
#   {{0.5, 1, 2}, {0.75, 1.5, 3}}, // Plecostomus
#   {{0.5, 1, 2}, {0.75, 1.5, 3}}, // Shark
#   {{0.5, 1, 2}, {0.75, 1.5, 3}} // Gourami
# };