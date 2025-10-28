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
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input("informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")


        if st.button("Inserir"):
            try:
                View.Profissionais_inserir(nome, especialidade, conselho, email, senha)
                st.success("Profissionais inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as error:
                st.error(error)

    def atualizar():
        Profissionais = View.Profissionais_listar()
        if len(Profissionais) == 0: st.write("Nenhum Profissionais cadastrado")

        else:
            op = st.selectbox("Atualização de Profissionais", Profissionais)
            nome = st.text_input("Novo nome", op.get_nome())
            especialidade = st.text_input("Nova especialidade", op.get_especialidade())
            conselho = st.text_input("Novo conselho", op.get_conselho())
            email = st.text_input("Novo conselho", op.get_email())
            senha =st.text_input("Nova senha", op.get_senha(),type="password")
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.Profissionais_atualizar(id, nome, especialidade, conselho, email, senha)
                    st.success("Profissionais atualizado com sucesso")
                except ValueError as error:
                    st.error(error)

    def excluir():
        Profissionais = View.Profissionais_listar()

        if len(Profissionais) == 0: st.write("Nenhum Profissionais cadastrado")

        else:
            op = st.selectbox("Exclusão de Profissionais", Profissionais)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.Profissionais_excluir(id)
                    st.success("Profissionais excluído com sucesso")
                except ValueError as error:
                    st.error(error)