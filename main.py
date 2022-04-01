import os


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}Olá,{nome}, Prazer André Cardoso , tenho 29,solteiro, moro em são paulo, e-mail de contato andre.jr@hotmail.com.br telefone / whatsapp basta entrar em contato por email para solicitar.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, tenho Graduação em andamento no curso de Sistema da Informação, 4°semestre previsão prevista para agosto/2024, sou tambem formado em técnico de desenvolvimento de software no Itb Brasilio Flores de Azevedo localizado na cidade de barueri -sp. Tenho Realizado algumas certificações pela fundação bradesco, DIO , NIN {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome},desenvolvi alguns websites freelancer, recentemente peguei um freela de mobile para arrumar um bug e criar um layout melhor para agilidade dos funcionarios. Criei um projeto TCC no meu curso técnico de formação onde a aplicação era em mobile é um chat escolar(firebase), web e desktop (projeto escola , onde adicionava aluno, profe,máterias e nota e realiza relatório do que fosse pedido. usando banco de dados sqlserve), alguns projetos em python pela faculdade  e uns projetos pessoais que estou dando andamento. {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} , nesse caso o que me motiva é o avanço da técnologia e a vontade em que tenho de me ingressar na área e ter não só o conhecimento mais também a prática necessária, minha maior conquista foi ter lutado para conseguir ingressar na faculdade com todos impecilio que esta tendo mais continuo firme e forte em não desistir , pos quero me forma e se Deus quiser ter meu próprio negócio de densenvolvimento.{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o chatbot
    print('Bem-vindo , Conheça um pouco sobre André Cardoso')
    # pedir o nome
    nome = input('Digite seu nome: ')
    # pedir o e-mail
    email = input('Digite seu e-mail: ')
    while True:
        # Oferer o menu de opções
        resposta = input(
            f'Quais informações gostaria de saber?{os.linesep}[1] - Algumas informações pessoais?{os.linesep}[2] - Qual sua formação academica e alguns certificados?{os.linesep}[3] - Quais foram os jobs ou projetos desafiadores?{os.linesep}[4] - O que te motiva e qual é a sua maior conquista?{os.linesep}')
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()
