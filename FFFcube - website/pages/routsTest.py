# Working
import streamlit as st

query_params = st.experimental_get_query_params()
device_id = query_params.get("device_id", b"")
if device_id:
    device_id = device_id[0]
    st.set_page_config(page_title=f"Device {device_id} - My Streamlit App")
    st.write(f"Device ID: {device_id}")
    st.write("Here is some content.")

else:
    device_id = ""

# streamlit run routsTest.py
# http://localhost:8502/?device_id=1234
# http://localhost:8502/routsTest?device_id=123878

# streamlit run routsTest.py