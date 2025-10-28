import streamlit as st
from view import View
import time
class PerfilProfissionaisUI:
    def main():
        st.header("Meus Dados")

        op = View.Profissionais_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        especialidade = st.text_input("Informe o novo especialidade", op.get_especialidade())
        conselho = st.text_input("Informe o novo conselho", op.get_conselho())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        senha = st.text_input("Informe a nova senha", op.get_senha(),type="password")

        if st.button("Atualizar"):
            try:
                id = op.get_id()
                View.Profissionais_atualizar(id, nome, especialidade, conselho, email, senha)
                st.success("Profissionais atualizado com sucesso")
            except ValueError as error:
                st.error(error)