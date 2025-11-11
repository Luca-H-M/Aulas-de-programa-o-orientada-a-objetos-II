from view import View
import streamlit as st
import time
from datetime import datetime, date

class AVProfissionais:
    def main():
        st.header("Avaliar Profissionais")
        agendamentos_totais = View.horario_listar()
        agendamentos_passados = []
        for x in agendamentos_totais:
            if x.get_confirmado() == True and x.get_data() < datetime.today() and x.get_id_cliente() == st.session_state["usuario_id"]:
                # tendo certeza que x faz parte dos horarios confirmados que ja passaram
                agendamentos_passados.append(x)
        if len(agendamentos_passados) == 0: st.write("Nenhum Agendamento prévio")
        
        else:
            agendamento_avaliado = st.selectbox("Informe o agendamento a ser avaliado", agendamentos_passados)
            nota = st.text_input("Informe uma nota de 0 a 5")
            if st.button("Avaliar"):
                try:
                    View.nota_atualizar(nota, agendamento_avaliado.get_id_profissional())
                    View.horario_excluir(agendamento_avaliado.get_id())
                    st.success("Serviço inserido com sucesso")
                except ValueError as erro: st.error(erro)
                time.sleep(2)
                st.rerun()