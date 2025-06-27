import streamlit as st

st.title("My Streamlit App with Tabs")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Overview", "Details", "Settings"])

# Tab content
with tab1:
    st.header("Overview Tab")
    st.write("This is the overview section.")

with tab2:
    st.header("Details Tab")
    st.write("This tab contains detailed information.")

with tab3:
    st.header("Settings Tab")
    st.write("This tab lets you tweak settings.")
