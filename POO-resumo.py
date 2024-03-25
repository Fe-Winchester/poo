"""
POO- estilo de programação que enfatiza a modelagem computacional de objetos do mundo real para resolver um problema
"""
# classes-é uma representação do mundo real para objetos similares(mesmas características e comportamentos) - ex.:mamíferos
#objeto - um exemplo de determinada classe - exe: gato,cachorro,golfinho.
#atributos-características/ propriedades que definem obejetos similares(de uma mesma classe)
#métodos-ações que ajudam a definir uma classe com as quais os objetos interagem entre si.
#método construtor - método especial da classe usado para criar um objeto dessa classe(instanciar).

# modelando uma biblioteca computacional usando POO

# 1º passo:identificar as classes do universo do problema biblioteca
# usuário
# livro

# 2º passo: descrever/modelar as classes identificadas em Python
class Usuario:  # recomenda-se usar Letras maiúsculas no inicio do nome da classe.
    def __init__(self,nome,mat,cpf,uname,passwd,email,tel,dtn,livro=[]): # método construtor da classe - função
        # definir o molde do objeto que eu quero construir a partir da classe
        self.nome= nome # um atributo funciona como uma variável (espaço de memória que armazena um valor)
        self.matricula = mat
        self.cpf = cpf
        self.username = uname
        self.senha = passwd
        self.email = email
        self.fone = tel
        self.dt_nascimento = dtn
        self.livros_emprestados = livro
# o atributo recebe o que vem do parametros
# self/this é um atributo
# 3º passo: uma vez definida a classe,posso instanciar (criar/construir) um objeto (exemplo) dessa classe invocando seu método construtor
user1 = Usuario() # objeto instanciado da classe Usuario e chamado em user1
user2 = Usuario()
user3 = Usuario()
user4 = Usuario()
# Para acessar atributos de objetos em Python utilizou o seguinte padrão
# nome_do_objeto.nome_nome_do_atributo
#usuario_fernanda = Usuario(n,m,c,u,e,f,d,s)
#
#print(usuario_fernanda.email)

#user1 = Usuario("Vitor","32456985","021.365.852-74","")
#user3 = Usuario()
#user4 = Usuario()

#user1.nome
#print(user1.nome,user1.fone,user1.livros_emprestados)


