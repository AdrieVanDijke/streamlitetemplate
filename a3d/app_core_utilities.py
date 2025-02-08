import streamlit as st
import importlib


class AppCoreUtilities:
    def __init__(self):        
        # App Staat zetten als deze nog niet bestaat
        if "appState" not in st.session_state:
            self.setAppState("Home")    
        if "controler" not in st.session_state:
            st.session_state['controler'] = None

    # App Staat zetten
    def setAppState( self, state ):
        if 'controler' in st.session_state and st.session_state['controler'] is not None:
            st.session_state['controler'].reset()
        st.session_state['appState'] = state

    # Dynamisch modules laden 
    def loadModule( self, module_name, class_name=None ):
        # Class terug als class naam is opgegeven
        if class_name is not None:
            module = importlib.import_module(module_name)
            klass = getattr(module, class_name)
            return klass
        # Module terug als class naam niet is opgegeven
        else:
            return importlib.import_module(module_name)
        
