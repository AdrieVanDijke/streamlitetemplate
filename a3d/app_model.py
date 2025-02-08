import streamlit as st
import os
from a3d.app_functions import AppFunctions


class APPModel:
    def __init__(self):  
        self.functies = AppFunctions()        
        if 'app_init_done' not in st.session_state:
            st.session_state['app_init_done'] = True
        

