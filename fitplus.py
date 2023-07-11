## Variáveis globais:
alunos_db = []
treinos_db = []
exercicios = ["Abdominal","Agachamento","Flexão de braço","Flexão de pernas","Polichinelo","Prancha","Pular corda","Remada","Tríceps mergulho","Zumba"]
## Classes:
class Aluno:  # Recebe Nome, CPF, Peso, Altura e Indice
    def __init__(self,n,c,p,a,i,s=False):
        self.nome = n
        self.cpf = f'{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}'  # Formata CPF
        self.peso = p
        self.peso_inicial = p
        self.altura = a
        self.indice = i
        self.status = s
        treinos_db.append([])  # Gera a instancia dos treinos
        self.treinos = []
        imc = int(float(float(p)/(float(a)*float(a)))*10000)
        self.imc = f'IMC: {imc} Kg/m²'
    def detalhes(self):
        return print(f'''
        Nome: {self.nome}
        CPF: {self.cpf}
        Peso: {self.peso}Kg (variou {int(self.peso)-int(self.peso_inicial)}Kg)
        Altura: {self.altura}cm
        {self.imc}
        Treinos: {[i.nome for i in treinos_db[self.indice]]}
        Status: {self.status}
        ''')
class Treino:  # Recebe Nome, Repetições e Peso
    def __init__(self,n,r,p):
        self.nome = n
        self.repeticoes = r
        self.peso = p
## Funções
def main():  # Menu Principal
    limpar_tela()
    print(f'''{"*"*40}\n Fit+   Menu Principal\n{"*"*40}
    1 - Iniciar novo cadastro
    2 - Gerenciar treinos
    3 - Consultar alunos
    4 - Atualizar cadastros
    5 - Excluir registros
    6 - Relatório geral
    ''')
    user_in = input('Digite uma opção: ')
    if user_in == '1':  # Cadastrar aluno
        limpar_tela()
        n = input(f'{"*"*40}\n Cadastrando novo aluno:\n{"*"*40}\n\nDigite o nome: ')
        # Verifica CPF e formata para string
        c = str([i for i in input('Número do CPF: ') if i.isdigit()])[1:-1].replace("'","").replace(',','').replace(' ','')
        p = int(input('Peso: '))
        a = int(input('Altura (cm): '))
        i = len(alunos_db)
        alunos_db.append(Aluno(n,c,p,a,i))
    elif user_in == '2':  # Gerenciar treino
        menu_treino(consulta_aluno())
    elif user_in == '3':  # Consultar aluno
        escolha = consulta_aluno()
        limpar_tela()
        alunos_db[escolha].detalhes()
        sair()
    elif user_in == '4':  # Atualizar cadastro
        aluno = alunos_db[consulta_aluno()]
        limpar_tela()
        escolha = input(f'''{"*"*40}\n O que deseja fazer?:\n{"*"*40}
        1 - Editar nome ({aluno.nome})
        2 - Número do CPF ({aluno.cpf})
        3 - Peso atual ({aluno.peso}Kg)
        4 - Corrigir altura ({aluno.altura}cm)
        x - Sair
        \nOpção: ''')
        limpar_tela()
        if escolha == 'x': return main()
        elif int(escolha) > 4:
            print('Opção inválida!')
            return sair()
        elif escolha == '1': aluno.nome = input('Digite o nome: ')
        elif escolha == '2': aluno.cpf = input('Digite o novo CPF: ')
        elif escolha == '3': aluno.peso = input('Digite o novo peso: ')
        elif escolha == '4': aluno.altura = input('Digite a altura: ')
        limpar_tela()
        print('Editado com sucesso!\n')
        return sair()
    elif user_in == '5':  # Excluir aluno
        aluno_id = consulta_aluno()
        if input(f"Deseja remover {alunos_db[aluno_id].nome}? (S/n) ").lower() == 's':
            alunos_db.pop(aluno_id)
            limpar_tela()
            print("Aluno removido com sucesso! \n")
            sair()
        else: main()
    elif user_in == '6':  # Relatório de alunos
        limpar_tela()
        print(f'{"*"*40}\n Listagem completa de alunos:\n{"*"*40}\n')
        for i in range(len(alunos_db)):
            print(f"Índice {alunos_db[i].indice}:",end='')
            alunos_db[i].detalhes()
        sair()
    else: main()
def menu_treino(aluno_id):  # Operações relacionadas a treinos
    aluno = alunos_db[aluno_id]
    treinos_aluno = treinos_db[aluno_id]
    limpar_tela()
    user_in = input(f'''{"*"*40}\n Editar treinos de {aluno.nome}\n{"*"*40}
    1 - Incluir novo item
    2 - Modificar treinos do aluno
    3 - Excluir exercício
    4 - Apagar tudo
    x - Sair    \n\n Digite uma opção: ''')
    if user_in == 'x': main()
    elif user_in == '1':  # Incluir novo exercício
        limpar_tela()
        print(f'{"*"*40}\n Selecione o treino a incluir:\n{"*"*40}')
        for i in enumerate(exercicios):
            print(f"    {i[0]} -",i[1])
        escolha = int(input("\nOpção: "))
        for treino in treinos_aluno:  # Verifica se já existe
            if treino.nome == exercicios[escolha]:
                print(f"O aluno já possui {exercicios[escolha]} \n")
                sair()
        if len(treinos_aluno) >= 10:  # Quantidade de treinos?
            print("O aluno excedeu o limite de treinos \n")
            sair()
        reps = input("Quantas repetições? ")
        peso = input("Qual é o peso (em Kg)? ")
        # Adiciona o treino
        treinos_db[aluno_id].append(Treino(exercicios[escolha],reps,peso))
        alunos_db[aluno_id].status = True  # Atualiza status
        limpar_tela()
        print("Treino adicionado com sucesso! \n")
        sair()
    elif user_in == '2':  # Alterar um exercício
        limpar_tela()
        if len(treinos_aluno) == 0:  # Possui treinos?
            print("O aluno não possui nenhum treino! \n")
            sair()
        print(f'{"*"*40}\n Escolha o treino para modificar:\n{"*"*40}')
        escolha = listar_treinos(aluno_id)
        print(f'''{"*"*40}\n O que deseja alterar?\n{"*"*40}
        1 - Nome ({treinos_db[aluno_id][int(escolha)].nome})
        2 - Repetições ({treinos_db[aluno_id][int(escolha)].repeticoes} vezes)
        3 - Peso ({treinos_db[aluno_id][int(escolha)].peso}Kg)
            ''')
        sub_escolha = input("Opção: ")
        if sub_escolha == '1': treinos_db[aluno_id][int(escolha)].nome = input('Digite o novo nome: ')
        elif sub_escolha == '2': treinos_db[aluno_id][int(escolha)].repeticoes = input('Quantas repetições? ')
        elif sub_escolha == '3': treinos_db[aluno_id][int(escolha)].peso = input('Novo peso (Kg): ')
        sair()
    elif user_in == '3':  # Excluir exercício
        limpar_tela()
        print(f'{"*"*40}\n Escolha o treino para excluir:\n{"*"*40}')
        treinos_db[aluno_id].pop(listar_treinos(aluno_id))
        if len(treinos_db[aluno_id]) == 0:  # Treino vazio?
            alunos_db[aluno_id].status = False
        print('Exercício excluido com sucesso! \n')
        sair()
    elif user_in == '4':  # Excluir tudo
        limpar_tela()
        if input(f'{"*"*40}\n APAGAR TODOS OS TREINOS? (S/n) \n{"*"*40}\n\nOpção: ').lower() == 's':
            treinos_db[aluno_id] = []
            alunos_db[aluno_id].status = False
            limpar_tela()
            print('Treinos excluídos com sucesso! \n')
            sair()
        else: sair()
def limpar_tela():  # Limpa o terminal
    return print(chr(27) + "[2J")
def sair():  # Voltar para o menu principal
    input('Digite qualquer valor para sair... ')
    return main()
def popular_db():  # Gera alunos e treinos para testar o programa
    alunos_db.append(Aluno('João da Silva','12345678910',70,175,0))
    alunos_db.append(Aluno('Fabiana Oliveira','44433322211',50,165,1))
    alunos_db.append(Aluno('Marcos Souza','32132132100',100,190,2))
    for i in range(3):  # Add um treino para cada aluno
        treinos_db[i].append(Treino(exercicios[i],5,5))
        alunos_db[i].status = True
def consulta_aluno():  # Ajuda na listagem, seleção e erros
    limpar_tela()
    print(f'{"*"*40}\n Lista de alunos:\n{"*"*40}')
    for i in alunos_db:
        print(f"    {i.indice} - {i.nome}")
    escolha = input("    x - Sair \n\nOpção: ")
    if escolha == 'x': main()  # Sair
    elif escolha.isdecimal() and int(escolha) <= len(alunos_db)-1: return int(escolha)
    else:
        limpar_tela()
        print("Opção inválida!")
        return sair()
def listar_treinos(aluno_id):  # Verifica se o aluno possui treinos
    if len(treinos_db[aluno_id]) == 0: 
        limpar_tela()
        print("Nenhum treino cadastrado! \n")
        sair()
    # Lista todos os treinos do aluno
    for i in enumerate(treinos_db[aluno_id]):
        print(f"    {i[0]} -",i[1].nome)
    escolha = input("    x - Sair \n\nOpção: ")
    if escolha == 'x': main()
    elif escolha.isdecimal() and int(escolha) <= len(treinos_db)-1: return int(escolha)
    else:
        print("Opção inválida!")
        return sair()
## Rodar o programa
if __name__ == "__main__":  # Abrir na inicialização
    popular_db()
    while True: main()  # O loop não deixa o programa fechar
