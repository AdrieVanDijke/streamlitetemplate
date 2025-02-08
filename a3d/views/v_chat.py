import streamlit as st
from a3d.views.v_base import BaseView
from a3d.controlers.c_chat import ChatControler


class ChatView(BaseView):
    
    def __init__(self): 
        super().__init__()
        if 'controler' not in st.session_state or not isinstance(st.session_state['controler'], ChatControler):
            st.session_state['controler'] = ChatControler()    
        self.buildView()

    # VIEWS =========================================
    def buildView(self):
        st.subheader("AI Chatbot")

    # WORKERS =======================================