import streamlit as st

st.set_page_config(
    page_title='AI Portfolio',
    initial_sidebar_state='auto'
)

PAGES = {
    "Home": 0,
    "PyTorch": 1,
    "TensorFlow": 2,
    "Time-Series": 3
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
        st.write(page)

    st.sidebar.title("About")
    st.sidebar.info("Application under development")

if __name__ == "__main__":
    main()