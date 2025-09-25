import streamlit as st
import pandas as pd
import time
from view import View

class ManterProfissionaisUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir","Atualizar", "Excluir"])
        with tab1: ManterProfissionaisUI.listar()
        with tab2: ManterProfissionaisUI.inserir()
        with tab3: ManterProfissionaisUI.atualizar()
        with tab4: ManterProfissionaisUI.excluir()
    
    def listar():
        Profissionais = View.Profissionais_listar()
        if len(Profissionais) == 0: st.write("Nenhum Profissionais cadastrado")
        else:
            list_dic = []
            for obj in Profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")

        if st.button("Inserir"):
            View.Profissionais_inserir(nome, email, fone)
            st.success("Profissionais inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        Profissionais = View.Profissionais_listar()
        if len(Profissionais) == 0: st.write("Nenhum Profissionais cadastrado")

        else:
            op = st.selectbox("Atualização de Profissionais", Profissionais)
            nome = st.text_input("Novo nome", op.get_nome())
            email = st.text_input("Novo e-mail", op.get_email())
            fone = st.text_input("Novo fone", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                View.Profissionais_atualizar(id, nome, email, fone)
                st.success("Profissionais atualizado com sucesso")

    def excluir():
        Profissionais = View.Profissionais_listar()

        if len(Profissionais) == 0: st.write("Nenhum Profissionais cadastrado")

        else:
            op = st.selectbox("Exclusão de Profissionais", Profissionais)
            if st.button("Excluir"):
                id = op.get_id()
                View.Profissionais_excluir(id)
                st.success("Profissionais excluído com sucesso")