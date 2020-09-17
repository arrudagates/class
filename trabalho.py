import random
import string

#Tamanho definido da lista (constante).
tamanhoLista = 8

#Área de definição do classe (registro).
class Pessoa:  # Nome da classe (registro).
    nome = ''   # Atributos nome e matrícula.
    matricula = 0

class Lista:     # Nome da classe (registro).
    alunos = [Pessoa()]*tamanhoLista  # Vetor de alunos de tamanhoLista (constante).
    numeroElementos = 0                   # Número de elementos ocupados na lista.



#Módulo criaLista.
# Objetivo: Cria lista com nº de elementos informado pelo usuário.
# Entrada.: Nenhuma.
# Saída..: Lista criada.

def criaLista():
  # Inicializa a lista.
  lista = Lista()
  print("Beleza, você criou uma lista!")
  return lista


#Módulo imprimeLista.
# Objetivo: Imprime todos os elementos da lista em tela.
# Entrada.: Lista.
# Saída..: Em tela.

def imprimeLista(lista):
  print("[ ________ RELATÓRIO ________ ]")

  # Imprime elementos válidos da lista.
  for i in range(lista.numeroElementos):
    print("[{}] Nome: {}".format(i, lista.alunos[i].nome), end = "\t")
    print("Matricula: {}".format(lista.alunos[i].matricula))

  print("[{} elemento(s) ocupado(s) de {}]".format(lista.numeroElementos, tamanhoLista))


#Módulo entradaDados.
# Objetivo: Gera um novo elemento (registro) com os dados informados pelo usuário.
# Entrada.: Nenhuma.
# Saída..: Novo elemento (registro).

def entradaDados():
  aluno = Pessoa()
  aluno.nome = input("Informe o nome.....: ")
  aluno.matricula = int(input("Informe a matricula: "))

  return aluno


#Módulo incluiFimLista.
# Objetivo: Inclui um novo elemento ao final da lista válida (após o último elemento com dados).
# Entrada.: Lista.
# Saída..: Lista modificada com um novo elemento no final.

def incluiFimLista(lista): # append

  # Se lista não atingiu o tamanho máximo de elementos,
  if lista.numeroElementos != len(lista.alunos):
    # inclui um novo elemento ao final da lista válida.
    lista.alunos[lista.numeroElementos] = entradaDados()

    # Incrementa o número de elementos válidos da lista.
    lista.numeroElementos += 1
    print("Sucesso na inclusão... 👏!")
  else:
    # Caso contrário, informa:
    print("Lista lotadinha... desculpe!")

  return lista

def consultaElementLista(lista):
    index = int(input("Informe o index.....: "))
    print(lista.alunos[index].nome + ' ' + lista.alunos[index].matricula)

def incluiInicioLista(lista): # append

  # Se lista não atingiu o tamanho máximo de elementos,
  if lista.numeroElementos != len(lista.alunos):
    listabkp = lista.alunos
    lista.alunos = [Pessoa()]*tamanhoLista
    lista.alunos[0] = entradaDados()
    for i in range(lista.numeroElementos):
        lista.alunos[i+1] = listabkp[i]

    # Incrementa o número de elementos válidos da lista.
    lista.numeroElementos += 1

    print("Sucesso na inclusão... 👏!")
  else:
    # Caso contrário, informa:
    print("Lista lotadinha... desculpe!")

  return lista

def excluiElementoLista(lista):

    index = int(input("Informe o index.....: "))
    lista.alunos = lista.alunos[:index] + lista.alunos[index+1 :]
    lista.numeroElementos -= 1
    return lista


def alteraElementoLista(lista):
    index = int(input("Informe o index.....: "))
    lista.alunos[index] = entradaDados()

    return lista


def bubbleSort(lista):
    n = lista.numeroElementos

    for i in range(n-1):
        for j in range(0, n-i-1):
            if int(lista.alunos[j].matricula) > int(lista.alunos[j+1].matricula) :
                lista.alunos[j], lista.alunos[j+1] = lista.alunos[j+1], lista.alunos[j]
    return lista



def corrompeLista(lista):
    for i in range(lista.numeroElementos):
        lista.alunos[i].nome = ''.join(random.SystemRandom().choice(string.ascii_letters) for j in range(len(str(lista.alunos[i].nome))))
        lista.alunos[i].matricula = ''.join(random.SystemRandom().choice(string.digits) for j in range(len(str(lista.alunos[i].matricula))))
    return lista

def menu():
  while True:
    print("[ ____ SISTEMA ACADÊMICO ____ ]\n \
    1. Cria lista, cara\n \
    2. Bota no fim da lista, cara\n \
    3. Coloca no inicio da lista, cara\n \
    4. Tira elemento da lista, bro\n \
    5. Printa lista, meo\n \
    6. Vamo vê oq tem nesse lugar da lista, parça \n \
    7. Troca aquele elemento ali por esse aqui, mano\n \
    8. Organiza a lista por bolhinhas, velho\n \
    9. sjfbhKSbfHfbKDBffjd, maninho")

    # Valida entrada de dados para opção aceitar apenas o menu.
    while True:
      opcaoMenu = input("Opção: ")
      if opcaoMenu >= '1' and opcaoMenu <= '9':
        break
    print()

    if opcaoMenu == '1':
      lista = criaLista()
    elif opcaoMenu == '2':
      lista = incluiFimLista(lista)
    elif opcaoMenu == '3':
      lista = incluiInicioLista(lista)
    elif opcaoMenu == '4':
      lista = excluiElementoLista(lista)
    elif opcaoMenu == '5':
      imprimeLista(lista)
    elif opcaoMenu == '6':
      consultaElementLista(lista)
    elif opcaoMenu == '7':
      lista = alteraElementoLista(lista)
    elif opcaoMenu == '8':
      lista = bubbleSort(lista)
    elif opcaoMenu == '9':
      lista = corrompeLista(lista)

    else:
      print()
      print("[ ____ Ahhhh, que pena, você já vai... Volte sempre! ____ ]")
      break


#Início do programa.
menu()
