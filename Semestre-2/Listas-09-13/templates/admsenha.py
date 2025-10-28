import streamlit as st
import time
from view import View

class Admsenha:
    def main():
        st.header("Alterar senha (Admin)")


        adm = View.cliente_listar_id(st.session_state["usuario_id"])
        if adm == 0 or adm.get_email() != "admin": st.warning("Pagina de administradores"); return

        st.text_input("Nome", adm.get_nome(), disabled=True)
        st.text_input("E-mail (não pode ser alterado)", adm.get_email(), disabled=True)

        senha = st.text_input("Informe a nova senha", type="password")

        if st.button("Alterar Senha"):
            if senha.strip() == "":
                st.error("Por favor, informe uma senha válida.")
            else:
                View.cliente_atualizar(adm.get_id(), adm.get_nome(), adm.get_email(), adm.get_fone(), senha)
                
                st.success("Senha alterada com sucesso!")
                time.sleep(2)
                st.rerun()