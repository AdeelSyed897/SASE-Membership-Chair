import streamlit as st

st.set_page_config()
homePage = st.Page(page="Homepage.py")
Create = st.Page(page="Pages/Create.py")
Merge = st.Page(page="Pages/Merge.py")
Visualize = st.Page(page="Pages/Visualize.py")
pg = st.navigation(pages=[homePage,Create,Merge,Visualize])
pg.run()


st.title("WPI SASE Membership Chair")
st.write("Welcome to the Membership Chair website for WPI’s Society of Asian Scientists and Engineers (SASE). This website streamlines the attendance tracking and gives valuable data on different events and demographics.")