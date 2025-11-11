import streamlit as st
import time
from view import View

class CagendaPUI:
    def main():
        Profissionais = View.Profissionais_listar_id(st.session_state["usuario_id"])
        if Profissionais == None: st.write("Nenhum Profissionais cadastrado"); return

        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horario cadastrado"); return

        horarios_profissional = [h for h in horarios if h.get_id_profissional() == Profissionais.get_id() and h.get_id_cliente() is not None]
        if len(horarios_profissional) == 0: st.write("Você não possui horários agendados com clientes."); return

        x = st.selectbox("Informe o horário", horarios_profissional, format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')} - {h.get_confirmado()}")
        
        cliente = View.cliente_listar_id(x.get_id_cliente())
        clientes_op = []
        if cliente is not None:
            clientes_op.append(cliente)

        cliente_selecionado = st.selectbox("Cliente", clientes_op, format_func=lambda c: f"{c.get_id()} - {c.get_nome()} - {c.get_email()} - {c.get_fone()}")

        if st.button("Confirmar"):
                View.horario_atualizar(x.get_id(), x.get_data(), True,  x.get_id_cliente(), x.get_id_servico(), x.get_id_profissional())
                
                st.success("Serviço confirmado com sucesso!")
                time.sleep(2)
                st.rerun()