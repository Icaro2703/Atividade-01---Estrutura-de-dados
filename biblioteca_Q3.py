from livro import Livro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.lista_livros = []
        self.lista_usuarios = []
        self.teste = True
        
    def cadastrar_livro(self, livro: Livro):
        if len(self.lista_livros) == 0:
            self.lista_livros.append(livro)
            print("Livro cadastrado com sucesso")
        else:
            for i in self.lista_livros:
                if livro.titulo == i.titulo:
                    print("Este livro já está cadastrado")
                    self.teste = False
                    break
            if self.teste:
                self.lista_livros.append(livro)
                print("Livro cadastrado com sucesso")
            self.teste = True
                    
    def cadastrar_usuario(self, usuario: Usuario):
        if len(self.lista_usuarios) == 0:
            self.lista_usuarios.append(usuario)
            print("Usuário cadastrado com sucesso")
        else:
            for i in self.lista_usuarios:
                if usuario.ra == i.ra:
                    print("Ra indisponível")
                    self.teste = False
                    break
            if self.teste:
                self.lista_usuarios.append(usuario)
                print("Usuário cadastrado com sucesso")
            self.teste = True
        
    def realizar_emprestimo(self, ra: int, titulo_livro: str):
        if len(self.lista_livros) != 0:
            if len(self.lista_usuarios) != 0:
                livro = False
                usuario = False
                for i in self.lista_livros:
                    if i.titulo == titulo_livro:
                        livro = i
                        break
                for i in self.lista_usuarios:
                    if i.ra == ra:
                        usuario = i
                        break
                        
                if livro == False:
                    print("Livro não cadastrado")
                elif livro.disponivel == False:
                    print("Livro indisponivel")
                elif usuario == False:
                    print("Você não está cadastrado")
                else:
                    livro.emprestar()
                    usuario.emprestar_livro(livro)
                    print("Empréstimo realizado com sucesso")
            else:
                print("Você não está cadastrado")   
        else:
            print("Livro não cadastrado")
    
    def realizar_devolucao(self, ra, titulo_livro):
        if len(self.lista_livros) != 0:
            if len(self.lista_usuarios) != 0:
                livro = False
                usuario = False
                for i in self.lista_livros:
                    if i.titulo == titulo_livro:
                        livro = i
                        break
                for i in self.lista_usuarios:
                    if i.ra == ra:
                        usuario = i
                        break
                
                if livro == False:
                    print("Livro não cadastrado")
                elif usuario == False:
                    print("Você não está cadastrado")
                elif usuario.devolver_livro(livro):
                    livro.devolver()
                    print("Devolução realizada com sucesso")
                else:
                    print("Você não emprestou este livro")   
            else:
                print("Você não está cadastrado")
        else:
            print("Livro não cadastrado")
        
    def listar_livros_disponiveis(self):
        i = 0
        print("-" * 80)
        print("LISTA DE LIVROS DISPONÍVEIS")
        print()
        for livro in self.lista_livros:
            if livro.disponivel:
                i = 1
                print(livro)
        if i == 0:
            print("Não há livros disponíveis")
      
    def listar_livros_emprestados_usuario(self, ra: int):
        i = 0
        for usuario in self.lista_usuarios:
            if usuario.ra == ra:
                livros_emprestados = usuario
                i = 1
                break
        
        if i == 0:
            print("Você não está cadastrado")
        else:
            print("-" * 80)
            print(f"Lista de livros de {usuario.nome}")
            print()
            if len(livros_emprestados.listar_livros()) == 0:
                print("Você não possui livros emprestados")
            else:
                for livro in livros_emprestados.listar_livros():
                    print(livro)
