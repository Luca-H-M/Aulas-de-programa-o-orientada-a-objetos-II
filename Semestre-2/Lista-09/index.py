from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
import streamlit as st

class IndexUI:
    def main():
        tab1, tab2 = st.tabs(["Cliente", "Serviço"])
        with tab1: ManterClienteUI.main()
        with tab2: ManterServicoUI.main()


        IndexUI.main()