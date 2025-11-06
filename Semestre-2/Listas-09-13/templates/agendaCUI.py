import streamlit as st
import pandas as pd
from view import View

class AgendaCUI:
    def main():
        cliente = []
        cliente.append(View.cliente_listar_id(st.session_state["usuario_id"]))
        if len(cliente) == 0: st.write("Nenhum cliente cadastrado"); return
        horarios = []
        horarios.append(View.horario_listar())
        if len(horarios) == 0: st.write("Nenhum horario cadastrado"); return

        horarios_cliente = [h for h in horarios[0] if h.get_id_cliente() == cliente[0].get_id()]
        if len(horarios_cliente) == 0: st.write("Você ainda não possui serviços cadastrados."); return

        list = []
        for x in horarios_cliente:
            servico = View.servico_listar_id(x.get_id_servico())
            profissional = View.Profissionais_listar_id(x.get_id_Profissional())

            list.append({"id": x.get_id(),"data": x.get_data(),"confirmado": x.get_confirmado(),"serviço": servico.get_descricao() if servico else None, "profissional": profissional.get_nome() if profissional else None})

        df = pd.DataFrame(list)
        st.dataframe(df)