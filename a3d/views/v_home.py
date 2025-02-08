import streamlit as st
from a3d.views.v_base import BaseView
from a3d.controlers.c_home import HomeControler


class HomeView(BaseView):
    
    def __init__(self): 
        super().__init__()

        if 'controler' not in st.session_state or not isinstance(st.session_state['controler'], HomeControler):
            st.session_state['controler'] = HomeControler()

        self.buildView()

    # VIEWS =========================================
    def buildView(self):
        st.subheader("Home")


