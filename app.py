import streamlit as st

import src.pages.home as home_page
import src.pages.pytorch as pytorch_page
import src.pages.tensorflow as tensorflow_page
import src.pages.timeseries as timeseries_page
import src.pages.graphs.index as graphs_page

st.set_page_config(
    page_title='AI Portfolio',
    initial_sidebar_state='auto'
)

PAGES = {
    "Home": home_page,
    "PyTorch": pytorch_page,
    "TensorFlow": tensorflow_page,
    "Time-Series": timeseries_page,
    "Graphs": graphs_page
}

def main():
    """
        Main function of the app
    """

    st.sidebar.title("Main Menu")

    selection = st.sidebar.selectbox(
        "Select Navigation Option",
        list(PAGES.keys())
    )

    page = PAGES[selection]

    with st.spinner("Loading %s ..." % (selection)):
        page.write()

    st.sidebar.title("About")
    st.sidebar.info("Application under development")

if __name__ == "__main__":
    main()