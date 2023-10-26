import streamlit as st



# Initialization
# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'

# # Session State also supports attribute based syntax
# if 'key' not in st.session_state:
#     st.session_state.key = 'value'

def main():
    # with st.form("my_form"):
    #     st.write("Inside the form")
    #     slider_val = st.slider("Form slider")
    #     checkbox_val = st.checkbox("Form checkbox")

    #     # Every form must have a submit button.
    #     submitted = st.form_submit_button("Submit")
    #     if submitted:
    #         st.write("slider", slider_val, "checkbox", checkbox_val)
    #         # if 'formsubmitbtn' not in st.session_state:
    #         #     st.session_state['formsubmitbtn'] = submitted


    # st.write("Outside the form")
    # # With magic:
    # st.write(st.session_state)
    # formVal = st.session_state['FormSubmitter:my_form-Submit']
    # st.write(f"form value: {formVal}")
    # global preFormVal
    # if formVal:
    #     preFormVal = formVal
    # if preFormVal:
    #     st.slider("Formslider",0,10,key="formSlider")
    # st.write(preFormVal)
    def lbs_2_kg():
        st.session_state.kg = st.session_state.lbs/2.2046
    def kg_2_lbs():
        st.session_state.lbs = st.session_state.kg*2.2046
    
    col1,buff,col2 = st.columns([2,1,2])
    with col1:
        pounds = st.number_input("Pounds", key="lbs",on_change=lbs_2_kg)

    with col2:
        kilograms = st.number_input("Kilograms", key="kg",on_change=kg_2_lbs)
    if pounds > 200:
        st.warning("hello pounds")
        pounds.disabled(True)
    if kilograms < 200:
        st.warning("no kilograms")
        # kilograms.disabled(True)


if __name__ == '__main__':
    
    st.set_page_config(page_title="BS : Card",
                       layout="wide")
    preFormVal = False
    # st.title("Smart Socket")
    st.title("Session state Basics")

    "st.session_state object:", st.session_state
    main()

# streamlit run form-test.py
