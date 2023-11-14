import pyautogui
import PySimpleGUI as psg
import time

def ia(x):
    perguntas = ['' ,'Computadores pessoais (PCs) já existem desde 1950. Verdadeiro ou falso?',
             'Que termo descreve os componentes físicos de um sistema de computador?',
             'No modelo de computação em grade, os recursos são agrupados para melhorar a eficiência. Verdadeiro ou falso?',
             'Software não funciona sem Hardware. Verdadeiro ou falso?',
             'As mudanças na computação afetaram muitas das nossas atividades diárias. Todas as atividades a seguir são exemplos dessa mudança? Sim ou não?',
             'A maioria dos mecanismos de pesquisa na Internet usa bancos de dados para armazenar dados. Verdadeiro ou falso?',
             'A Modelagem de Dados é a última etapa no processo de desenvolvimento de bancos de dados. Verdadeiro ou falso?',
             'Qual destas opções representa a sequência correta de etapas no Processo de Desenvolvimento de Bancos de Dados?',
             'Bancos de dados são usados na maioria dos países e pela maioria dos governos. A vida mudaria drasticamente se não tivéssemos mais acesso a bancos de dados. Verdadeiro ou falso?',
             'Considere a biblioteca da sua escola. Ela terá um banco de dados com detalhes sobre o empréstimo de livros aos alunos. Os detalhes do empréstimo de um livro a um dos alunos são considerados dados ou informações?',
             'Quais destas opções são exemplos de dados que se tornam informações?',
             'Como transformar "dados" em "informações"?',
             'O mercado para profissionais de TI ainda está crescendo e continuará assim no futuro, pois o mundo depende está cada vez mais de sistemas de computador. Verdadeiro ou falso?',
             'A demanda por profissionais de Tecnologia da Informação no mercado atual é cada vez maior. Verdadeiro ou falso?',
             'Depois que você aprender a escrever programas e construir sistemas, não precisará mais de entradas ou do envolvimento de usuários porque será perfeitamente capaz de fornecer os sistemas que as empresas precisam e desejam.',
             'O Modelo Físico é derivado do Modelo Conceitual. Verdadeiro ou falso?',
             'Os modelos de dados são desenhados para mostrar aos usuários os Dados reais que o novo sistema vai conter. Apenas Dados listados no Diagrama podem ser inseridos no Banco de Dados. Verdadeiro ou falso?',
             'Os atributos podem ter apenas um valor a qualquer momento para cada instância da entidade. Verdadeiro ou falso?',
             'As entidades normalmente são verbos. Verdadeiro ou falso?',
             'Um modelo de Entidade-Relacionamento é independente do hardware ou software usado para implementação. Verdadeiro ou falso?',
             'Como a modelagem de Entidade-Relacionamento é dependente no hardware ou software usado para implementação, você precisará alterar seu ERD caso decida mudar o Fornecedor de Hardware. Verdadeiro ou falso?',
             'Um Modelo Conceitual não está preocupado com a forma como o Modelo Físico será implementado. Verdadeiro ou falso?',
             'A modelagem de dados é realizada pelos seguintes motivos: (Escolha duas opções)',
             'Documentar requisitos de negócios ajuda os desenvolvedores a controlar o escopo do sistema e impede que os usuários aleguem que o novo sistema não atende às suas necessidades comerciais. Verdadeiro ou falso?',
             'O Modelo Físico é derivado do Modelo Conceitual. Verdadeiro ou falso?',
             'Quais destas afirmações sobre ERDs são verdadeiras? (Escolha duas opções)',
             'Um ERD bem-estruturado mostrará apenas algumas partes do modelo de dados finalizado. Você nunca deve tentar modelar o sistema inteiro em um único diagrama, por menor que seja o diagrama. Verdadeiro ou falso?',
             'Como a modelagem de Entidade-Relacionamento é dependente no hardware ou software usado para implementação, você precisará alterar seu ERD caso decida mudar o Fornecedor de Hardware. Verdadeiro ou falso?',
             'Qual é a finalidade de um Identificador Exclusivo?',
             'Os atributos podem ter apenas um valor a qualquer momento para cada instância da entidade. Verdadeiro ou falso?',
             'Todas as opções a seguir poderiam ser atributos de uma ENTITY chamada PERSON, exceto qual delas?',
             'Todas estas opções seriam instâncias da entidade PERSON, exceto qual delas?',
             'Nas afirmações a seguir, encontre dois bons exemplos de ENTITY: Instance. (Escolha duas opções)',
             'Um(a) _________ é uma informação específica que, de algum modo, descreve uma entidade. É uma propriedade da entidade e a quantifica, qualifica, classifica ou especifica.',
             'As entidades normalmente são verbos. Verdadeiro ou falso?',
             'Quais destas afirmações sobre atributos são verdadeiras?',
             'Existem muitos motivos para criar um modelo conceitual. Escolha três opções entre as alternativas abaixo.',
             'Um(a) _________ é uma informação específica que, de algum modo, descreve uma entidade. É uma propriedade da entidade e a quantifica, qualifica, classifica ou especifica.',
             'Identificadores Exclusivos...',
             'Quais destas afirmações sobre Entidades são verdadeiras?',
             'Quais destas entidades têm maior probabilidade de conter atributos válidos? (Escolha duas opções)',
             'O valor de um(a) _________ pode ser um número, uma string de caracteres, uma data, uma imagem, um som.',
             'A finalidade de um ERD é documentar o sistema proposto e facilitar o debate e a compreensão dos requisitos capturados pelo desenvolvedor. Verdadeiro ou falso?',
             'Quais destas alternativas podem ser encontradas em um ERD? (Escolha duas opções)',
             'Um ERD é um exemplo de Modelo Físico. Verdadeiro ou falso?',
             'Um ERD é um exemplo de Modelo Lógico. Verdadeiro ou falso?',
             'Todas estas opções seriam instâncias da entidade ANIMAL SPECIES, exceto qual delas?',
             'Qual dos itens a seguir é um exemplo de atributo volátil?',
             'Qual destas afirmações sobre ERDs é falsa?',
             #Novas Questões

             'Quais destas opções são exemplos de ENTITY: Instance? (Escolha duas opções)',
             'Os atributos podem ser obrigatórios ou opcionais. Verdadeiro ou falso?']

    respostas = ['', 'False',
             'Hardware',
             'True',
             'True',
             'Sim',
             'True',
             'False',
             'Análise, Design, Construção',
             'True',
             'Dados',
             'Opções A (Faixa etária -> Média de idade de todos os alunos na turma), B (Quantia de depósito bancário -> saldo total da conta) e D (Preço de um computador -> total de vendas de todos os computadores de uma empresa)',
             'Consultando-os ou acessando-os',
             'True',
             'True',
             'Falso. As necessidades da empresa podem e vão mudar. Por exemplo, podem surgir novos requisitos legais.',
             'True',
             'False',
             'True',
             'False',
             'True',
             'False',
             'True',
             'O ERD se torna um modelo para projetar o sistema real; Ela é útil em discussões e revisões.',
             'True',
             'True',
             'Uma informação específica deve ser encontrada apenas em um único lugar em um ERD; Não é recomendável modelar dados que possam ser derivados.',
             'False',
             'False',
             'Identificar uma instância exclusiva de uma entidade usando um ou mais atributos e/ou relacionamentos.',
             'True',
             'Natacha Hansen',
             'Male',
             'BOOK: Biography of Mahatma Gandhi; DAIRY PRODUCT: milk',
             'Atributo',
             'False',
             'Eles têm um tipo de dados, como número ou string de caracteres; Eles descrevem, qualificam, quantificam, classificam ou especificam uma entidade; Devem ter um único valor.',
             'Ele descreve com precisão o que um modelo físico vai conter; Ele captura as necessidades atuais e futuras; Ele modela necessidades funcionais e informativas.',
             'Atributo',
             'Diferenciam uma instância de uma entidade em relação a todas as outras instâncias dessa entidade.',
             '"Algo” importante para os negócios sobre o qual dados devem ser conhecidos; Normalmente são um nome; Representam um nome para um conjunto de itens semelhantes.',
             'Entity: Pet. Attributes: Name, Birthdate, Owner; Entity: Home. Attributes: Number of Bedrooms, Owner, Address, Date Built ',
             'Atributo',
             'True',
             'Atributos e Entidades',
             'False',
             'True',
             'Leaf',
             'Age',
             'Modele todas as informações que possam ser derivadas de outras informações já modeladas.',

             #Novas Respostas

             'ANIMAL: Dog; TRANSPORTATION METHOD: Car',
             'True']


#x = input()
    i = 0
    while(i<=1000):
        if(x == str(perguntas[i])):
            psg.popup(respostas[i])
            i = 1001
        i+=1
    return

click = False

psg.theme('topanga')

l1 = psg.Text('Questão:', key='-OUT-', font=('Arial Bold', 20), expand_x=True, justification='center')
t1 = psg.Input('', enable_events=True, key='-EMAIL-', font=('Arial Bold', 20), expand_x=True, justification='left')


# b1 = psg.Button('Ok', key='-OK-', font=('Arial Bold', 20))
b1 = psg.Button('Run', font=('Arial Bold', 20))
b2 = psg.Button('Exit', font=('Arial Bold', 20))
layout = [[l1], [t1], [b1, b2]]
window = psg.Window('Questões Oracle', layout, size=(750, 250))

while True:  # Event Loop
    event, values = window.Read()
    # print(event, values)
    if event in (None, 'Exit'):
        break
    elif event == 'Run':

        x = str(values['-EMAIL-'])
        ia(x)

        # b = str(values['-PASSWORD-'])

        # window.close()

# Layout end


while (click == True):
    pyautogui.click()
    time.sleep(2)
