import streamlit as st


def card(id,title,context):
    return f'''
            <div class="card" style="width: 18rem;">
            <img class="card-img-top" src="/images/_fishlogo.png" alt="Card image cap">
            <div class="card-body">
                <h2 class="card-title">{id}</h2>
                <h5 class="card-title">{title}</h5>
                <p class="card-text ">{context}</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
            </div>


            <div class="card text-white bg-info mb-3" style="max-width: 18rem;">
                <div class="card-header">{id}</div>
                <div class="card-body">
                    <h5 class="card-title">{title}</h5>
                    <p class="card-text">{context}</p>
                </div>
            </div>
    
        
    
    '''


if __name__ == '__main__':
    st.set_page_config(page_title="BS : Card",
                       page_icon=":socket:",
                       layout="wide")
    # st.title("Smart Socket")
    st.markdown("""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">

        """, unsafe_allow_html=True
        )

    st.markdown('''<h1 style="font-family:courier;font-size:500%;color:blue;text-align:center;">BS : Card</h1>''', unsafe_allow_html=True)
    st.markdown(card(1,"BLOG","This is a sample blog"), unsafe_allow_html=True)
# streamlit run test-card.py
