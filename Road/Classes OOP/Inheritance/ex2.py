class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def showdata(self):
        print('Nome: ' + self.nome)
        print('Sobrenome: ' + self.sobrenome)
        print('Idade: ' + str(self.idade))

    def space(self):
        print('-'*30)

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, idade, turno, curso):
        #super().__init__(self, nome, sobrenome, idade)
        Pessoa.__init__(self, nome, sobrenome, idade)
        self.turno = turno
        self.curso = curso

    def alldata(self):
        self.showdata()
        print('Turno: ' + self.turno)
        print('Curso: ' + self.curso)

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, idade, funcao, cracha):
        Pessoa.__init__(self, nome, sobrenome, idade)
        self.funcao = funcao
        self.cracha = cracha

    def alldata(self):
        self.showdata()
        print('Funcao : ' + self.funcao)
        print('N° Cracha : ' + str(self.cracha))

aluno1 = Aluno('Harry', 'Potter', 25, 'Integral', 'Propriedades da Magia')
aluno2 = Aluno('Frank', 'Matt', 27, 'Matutino', 'Web programming')

func1 = Funcionario('Snape', 'Boow', 39, 'Professor', '5073')
func2 = Funcionario('Dexter', 'Morgan', 40, 'Zelador', '668')

aluno1.space()
aluno1.alldata()
aluno1.space()
aluno2.alldata()
aluno2.space()
func1.alldata()
func1.space()
func2.alldata()
func2.space()


