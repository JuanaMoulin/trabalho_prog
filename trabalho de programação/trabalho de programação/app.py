from config.Config import Config
from config.Database import Database
from dao.UsuarioDao import UsuarioDao
from model.Usuario import Usuario
from view.Table import Table

config = Config()
database = Database(config.config)
dao = UsuarioDao(database.conn)
lista = dao.selecionarUsuarios()
tela = Table(lista)

# teste teste, exemplo:
#usuario = Usuario()
#usuario.nome = 'Maria'
#usuario.email = 'email@teste.com.br'
#usuario.senha = 'senha'
print(dao.inserirUsuario(usuario))

#usuario = Usuario()
#usuario.id = 25
#usuario.nome = 'Larissa'
#usuario.email = 'email@teste.com.br'
#usuario.senha = '1234567'
#print(dao.alterarUsuario(usuario))

#usuario = Usuario()
#usuario.nome = 'Larissa'
#usuario.email = 'email@teste.com.br'
#usuario.senha = 'senha'
#print(dao.excluirUsuario(usuario))

#lista = dao.selecionarUsuarios()
#tela = Table(lista)