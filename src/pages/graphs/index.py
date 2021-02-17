import streamlit as st

import src.pages.graphs.pyvis_playground as pyvis_playground

PAGES = {
    "PyVis Playground": pyvis_playground
}

def write():
    st.title("Graphs Examples And Exercises")
    st.sidebar.title("Graphs Menu")
    
    selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner("Loading %s ..." % (selection)):
        page.write()
