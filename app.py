import streamlit as st

pg = st.navigation([st.Page("Homepage.py"),st.Page("Create.py"), st.Page("Merge.py"), st.Page("Visualize.py")])
pg.run()
