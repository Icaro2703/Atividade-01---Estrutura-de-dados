from livro_Q3 import Livro
from usuario_Q3 import Usuario
from biblioteca_Q3 import Biblioteca

print("MENU DE OPÇÕES\n\n 1. Cadastrar livro\n 2. Cadastrar usuário\n 3. Realizar empréstimo\n 4. Realizar devolução \n 5. Listar livros disponíveis\n 6. Listar livros emprestados ao usuário\n 7. Finalizar")
print()
opcao = int(input("Escolha uma das opções do menu: "))
print()
biblioteca = Biblioteca()

while opcao != 7:
    if opcao == 1:
        titulo = input("Informe o título do livro: ")
        autor = input("Informe o autor do livro: ")
        disponivel = True
        livro = Livro(titulo, autor, disponivel)
        biblioteca.cadastrar_livro(livro)
    
    elif opcao == 2:
        nome = input("Informe o nome do usuário a ser cadastrado: ")
        ra = int(input("Informe o RA desejado: "))
        lista_livros_emprestados = []
        usuario = Usuario(ra, nome, lista_livros_emprestados)
        biblioteca.cadastrar_usuario(usuario)
    
    elif opcao == 3:
        ra = int(input("Informe seu RA: "))
        titulo_livro = input("Informe o título do livro que você deseja encontrar: ")
        biblioteca.realizar_emprestimo(ra, titulo_livro)
    
    elif opcao == 4:
        ra = int(input("Informe seu RA: "))
        titulo_livro = input("Informe o título do livro que deseja devolver: ")
        biblioteca.realizar_devolucao(ra, titulo_livro)
        
    elif opcao == 5:
        biblioteca.listar_livros_disponiveis()
    
    elif opcao == 6:
        ra = int(input("Informe o seu RA: "))
        biblioteca.listar_livros_emprestados_usuario(ra)
        
    elif opcao != 7:
        print("OPÇÃO INVÁLIDA")
    
    print("-" * 80)
    opcao = int(input("Escolha uma das opções do menu: "))

print("PROGRAMA FINALIZADO")
