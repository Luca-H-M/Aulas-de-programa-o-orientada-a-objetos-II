import streamlit as st
import pandas as pd
from view import View
import time
from datetime import datetime, timedelta

class AgendaPUI:
    def main():
        st.header("Agenda")
        tab1, tab2 = st.tabs(["Listar", "Inserir"])
        with tab1: AgendaPUI.listar()
        with tab2: AgendaPUI.inserir()
    
    def listar():
        Profissionais = View.Profissionais_listar_id(st.session_state["usuario_id"])
        if Profissionais == None: st.write("Nenhum Profissionais cadastrado"); return

        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horario cadastrado"); return

        horarios_profissional = [h for h in horarios if h.get_id_profissional() == Profissionais.get_id()]
        if len(horarios_profissional) == 0: st.write("Você ainda não abriu horários na sua agenda."); return

        list = []
        for x in horarios_profissional:
            cliente = View.cliente_listar_id(x.get_id_cliente())
            servico = View.servico_listar_id(x.get_id_servico())

            list.append({"id": x.get_id(),"data": x.get_data(),"confirmado": x.get_confirmado(),"cliente": cliente.get_nome() if cliente else None,"serviço": servico.get_descricao() if servico else None})

        df = pd.DataFrame(list)
        st.dataframe(df)
    
    def inserir():
        profissional_id = st.session_state.get("usuario id")

        data = st.date_input("Informe o dia do atendimento")
        comeco_consulta = st.time_input("Informe a hora de inicio da consulta")
        fim_consulta = st.time_input("Informe a hora de final da consulta")
        intervalo = st.number_input("Informe o intervalo entere horarios")

        if st.button("Inserir"):
            try:
                inicio = datetime.combine(data, comeco_consulta)
                fim = datetime.combine(data, fim_consulta)
                list = []
                while fim > inicio:
                    View.horario_inserir(inicio, False, None, None, profissional_id)
                    list.append(inicio.strftime("%H:%M"))
                    inicio += timedelta(minutes=intervalo)
                st.success("Horarios inseridos com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as error:
                st.error(error)