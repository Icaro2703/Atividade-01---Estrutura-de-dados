from livro import Livro

class Usuario:
    def __init__(self, ra: int, nome: str, lista_livros_emprestados: list):
        self.ra = ra
        self.nome = nome
        self.lista_livros_emprestados = lista_livros_emprestados
    
    def emprestar_livro(self, livro: Livro):
        self.lista_livros_emprestados.append(livro)
        
    def devolver_livro(self, livro: Livro):
        if livro in self.lista_livros_emprestados:
            self.lista_livros_emprestados.remove(livro)
            return True
        return False
    
    def listar_livros(self):
        return self.lista_livros_emprestados
    