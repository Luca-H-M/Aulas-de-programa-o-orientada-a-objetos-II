from models.cliente import Cliente, ClienteDAO
from models.serviço import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from models.nota import Nota, NotaDAO
from datetime import datetime

class View:
    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key= lambda obj : obj.get_nome())
        return r
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    def cliente_inserir(nome, email, fone, senha):
        for x in View.cliente_listar():
            if x.get_email() == email or email == "admin": raise ValueError("Email já cadastrado")
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_atualizar(id, nome, email, fone, senha):
        for x in View.cliente_listar():
            if x.get_id() == id: pass
            elif x.get_email() == email or email == "admin": raise ValueError("Email já cadastrado")
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        for x in View.horario_listar():
            if x.get_id_cliente() == id:
                raise ValueError("cliente já possui serviço agendado: não é possível excluir")
        x = View.cliente_listar_id(id)
        cliente = Cliente(id, x.get_nome(), x.get_email(), x.get_fone(), x.get_senha())
        ClienteDAO.excluir(cliente)

    def Profissionais_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def Profissionais_listar_id(id):
        return ProfissionalDAO.listar_id(id)
    def Profissionais_inserir(nome, especialidade, conselho, email, senha):
        profissional = Profissional(0, nome, especialidade, conselho, email, senha)
        for x in View.Profissionais_listar():
            if x.get_email() == email or email == "admin": raise ValueError("Email já cadastrado")
        ProfissionalDAO.inserir(profissional)
        NotaDAO.calc_nota("", email)

    def Profissionais_atualizar(id, nome, especialidade, conselho, email, senha):
        for x in View.Profissionais_listar():
            if x.get_id() == id: pass
            elif x.get_email() == email or email == "admin": raise ValueError("Email já cadastrado")
        profissional = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(profissional)
    def Profissionais_excluir(id):
        for x in View.horario_listar():
            if x.get_id_profissional() == id:
                raise ValueError("Profissinal já possui serviço agendado: não é possível excluir")
        x = View.Profissionais_listar_id(id)
        profissional = Profissional(id, x.get_nome(), x.get_especialidade(), x.get_conselho(), x.get_email(), x.get_senha())
        ProfissionalDAO.excluir(profissional)

    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)
    def servico_inserir(descricao, valor):
        for obj in View.servico_listar():
            if obj.get_descricao() == descricao:raise ValueError("Serviço já cadastrado")
        c = Servico(0, descricao, valor)
        ServicoDAO.inserir(c)

    def servico_atualizar(id, descricao, valor):
        for x in View.servico_listar():
            if x.get_id() != id and x.get_descricao() == descricao:
                raise ValueError("Descriçao já cadastrada em outro serviço")
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    def servico_excluir(id):
        for x in View.horario_listar():
            if x.get_id_servico() == id:
                raise ValueError("Serviço já agendado: não é possível excluir")
        x = View.servico_listar_id(id)
        servico = Servico(id, x.get_descricao(), x.get_valor())
        ServicoDAO.excluir(servico)


    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        for x in View.horario_listar():
            if x.get_id_profissional() == id_profissional and x.get_data() == data: raise ValueError("Horario já cadastrado para este profissional")
        HorarioDAO.inserir(c)
    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        for x in View.horario_listar():
            if x.get_id_profissional() == id_profissional and x.get_data() == data: raise ValueError("Horario já cadastrado para este profissional")
        HorarioDAO.atualizar(c)
    def horario_excluir(id):
        c = Horario(id, None)
        for x in View.horario_listar_id(id):
            if x.get_id_cliente():
                raise ValueError("Horario já agendado por um cliente: não é possível excluir")
        HorarioDAO.excluir(c)
        
    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
            View.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return{"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    def Profissionais_autenticar(email, senha):
        for c in View.Profissionais_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return{"id": c.get_id(), "nome": c.get_nome()}
        return None