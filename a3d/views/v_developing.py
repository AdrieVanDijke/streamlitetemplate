import streamlit as st
from a3d.views.v_base import BaseView
from a3d.controlers.c_developing import DevelopingControler


class DevelopingView(BaseView):

    def __init__(self): 
        super().__init__()

        if 'controler' not in st.session_state or not isinstance(st.session_state['controler'], DevelopingControler):
            st.session_state['controler'] = DevelopingControler()

        self.buildView()

    # VIEWS =========================================
    def buildView(self):
        st.subheader("Developing")

    # WORKERS =======================================