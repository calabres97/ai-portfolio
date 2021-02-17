import streamlit as st
import streamlit.components.v1 as components

import src.tools.graphs.pyvis_helper as pyvish

def write():

    physics = st.sidebar.checkbox("Manual Physics Settings")

    pyvish.get_simple_graph(physics)
    HtmlFile = open("src/samples/sample.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height=900)