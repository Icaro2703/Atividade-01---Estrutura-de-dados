class Livro:
    def __init__(self, titulo: str, autor: str, disponivel: bool):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
        
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False
        
    def devolver(self):
        self.disponivel = True
    
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"    
        