import streamlit as st

def home():
    st.write("Welcome to my app!")

def about():
    st.write("This is my about page.")

def app():
    st.set_page_config(page_title="My App")
    
    # Define the URL routing
    pages = {
        "Home": home,
        "About": about,
    }

    # Render the sidebar menu
    st.title("Navigation")
    selection = st.radio("", list(pages.keys()))

    # Render the selected page
    page = pages[selection]
    page()

if __name__ == "__main__":
    app()

# streamlit run routMain.py