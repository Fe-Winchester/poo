class Usuario:
    def __init__(self,nome,mat,cpf,uname,email,dtn,passwd=[],livro=[]):
        self.nome= nome
        self.mat = mat
        self.cpf = cpf
        self.username = uname
        self.senha = passwd
        self.email = email
        self.dtn = dtn
        self.livros_eptd = livro
    def cadastrar_livro(self, titulo,autor,ano_publicacao,genero):

user = input("Digite o seu nome: ")
nome = input("Digite seu nome de usuário: ")
matri = input("Digite a matrícula do usuário: ")
cpf = input("Digite o cpf do usuário: ")
email = input("Digite o E-MAIL do usuário: ")
fone = input("Digite o celular do usuário: ")
data_nascimento = input("Digite a data de nascimento do usuário: ")
senha = input("Digite a senha do usuário: ")

user1 = Usuario("Minho","32456985","021.365.852-74","Relâmpago_Marquinhos","minhomelhorcorredor@clareiros.labirinto.com.br","10/07/2004","eusoulindo")
user2 = Usuario()
user3 = Usuario()
user4 = Usuario()

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero,exemplares,qtd):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publicacao
        self.genero = genero
        self.num_exemplares = exemplares
        self.qtd_emprestados = qtd

        if.

titulo = input("Qual título do livro?")
autor = input("Qual nome do autor?")
ano_publicacao = input("Qual gênero do livro?")
categoria = input("Quantos exemplares tem do livro?")

livro1 =
livro2 =
livro3 =
