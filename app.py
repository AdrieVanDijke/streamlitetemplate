import streamlit as st
from a3d.app_core_utilities import AppCoreUtilities


st.set_page_config(
    page_title="Streamlit App",
    page_icon=":material/support_agent:",
    layout="wide"
)

def main():
    appcore = AppCoreUtilities()
    # Laad het Model maar een keer (alleen st.session_state vars in Model)
    if 'app_init_done' not in st.session_state:
        klass = appcore.loadModule("a3d.app_model", "APPModel")
        klass()

    # Laad de sidebar
    klass = appcore.loadModule("a3d.views.parts.vp_side_menu", "SideMenuView")
    klass()
    # Load the huidige/gekozen view
    if st.session_state['appState'] == "Home":
        klass = appcore.loadModule("a3d.views.v_home", "HomeView")
        klass() 
    elif st.session_state['appState'] == "Agents":
        klass = appcore.loadModule("a3d.views.v_agents", "AgentsView")
        klass()
    elif st.session_state['appState'] == "Chat":
        klass = appcore.loadModule("a3d.views.v_chat", "ChatView")
        klass()
    elif st.session_state['appState'] == "Developing":
        klass = appcore.loadModule("a3d.views.v_developing", "DevelopingView")
        klass()
    elif st.session_state['appState'] == "Help":
        klass = appcore.loadModule("a3d.views.v_help", "HelpView")
        klass()

if __name__ == "__main__":
    main()

    