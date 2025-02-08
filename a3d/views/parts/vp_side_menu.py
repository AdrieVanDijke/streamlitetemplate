import streamlit as st
from a3d.app_core_utilities import AppCoreUtilities


class SideMenuView:
    def __init__( self ): 
        self.appcore = AppCoreUtilities()
        self.buildView()

    # VIEWS =========================================
    def buildView( self ):
        st.markdown(
            """
            <style>
                section[data-testid="stSidebar"] {
                    width: 250px !important;
                }              
            </style>
            """,
            unsafe_allow_html=True  
        )
        with st.sidebar:
            if st.session_state['appState'] == "Home":
                st.button("**:red[Home]** 🔸", type="secondary", use_container_width=True, icon="🏡")
            else:
                st.button("Home", type="secondary", use_container_width=True, on_click = self.appcore.setAppState, args={"Home"}, icon="🏡")
            if st.session_state['appState'] == "Agents":
                st.button("**:red[AI Agents]** 🔸", type="secondary", use_container_width=True, icon="🤖")
            else:
                st.button("AI Agents", type="secondary", use_container_width=True, on_click = self.appcore.setAppState, args={"Agents"}, icon="🤖")
            if st.session_state['appState'] == "Chat":
                st.button("**:red[AI Chatbot]** 🔸", type="secondary", use_container_width=True, icon="🗨️")
            else:
                st.button("AI Chatbot", type="secondary", use_container_width=True, on_click = self.appcore.setAppState, args={"Chat"}, icon="🗨️")
            if st.session_state['appState'] == "Developing":
                st.button("**:red[Developing]** 🔸", type="secondary", use_container_width=True, icon="🧑‍💻")
            else:
                st.button("Developing", type="secondary", use_container_width=True, on_click = self.appcore.setAppState, args={"Developing"}, icon="🧑‍💻")
            if st.session_state['appState'] == "Help":
                st.button("**:red[Help]** 🔸", type="secondary", use_container_width=True, icon="ℹ️")
            else:
                st.button("Help", type="secondary", use_container_width=True, on_click = self.appcore.setAppState, args={"Help"}, icon="ℹ️")
    

 

