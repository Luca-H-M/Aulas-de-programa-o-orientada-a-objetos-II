from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorariosUI import ManterHorarioUI
from templates.manterproffisionaisUI import ManterProfissionaisUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.pefilprofissionaisUI import PerfilProfissionaisUI
from templates.agendarservicosUI import AgendarServicoUI
from templates.agendaPUI import AgendaPUI
from templates.cagendaPUI import CagendaPUI
from templates.agendaCUI import AgendaCUI
from templates.avprofissionais import AVProfissionais
from view import View
import streamlit as st

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes","Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionaisUI.main()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema","Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados","Agendar Serviço", "Meus serviços", "Avaliar Profissionais"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Meus serviços": AgendaCUI.main()
        if op == "Avaliar Profissionais" : AVProfissionais.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Minha Agenda", "Confirmar serviço"])
        if op == "Meus Dados": PerfilProfissionaisUI.main()
        if op == "Minha Agenda": AgendaPUI.main()
        if op == "Confirmar serviço": CagendaPUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state: IndexUI.menu_visitante()

        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])

            if admin: IndexUI.menu_admin()
            elif st.session_state["usuario_profissional"] == "true": IndexUI.menu_profissional()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()