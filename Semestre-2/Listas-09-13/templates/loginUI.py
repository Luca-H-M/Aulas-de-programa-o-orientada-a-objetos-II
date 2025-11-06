import streamlit as st
from view import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema como Cliente")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Entrar"): 
            c = View.cliente_autenticar(email, senha)
            if c == None:st.write("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["usuario_profissional"] = "false"
                st.rerun()


        st.header("Entrar no Sistema como Profissional")
        email = st.text_input("Informe o e-mail", key="prof")
        senha = st.text_input("Informe a senha", type="password", key="profpassword")
        if st.button("Entrar", key="profbutton"): 
            c = View.Profissionais_autenticar(email, senha)
            if c == None:st.write("E-mail ou senha inválidos")

            else:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["usuario_profissional"] = "true"
                st.rerun()