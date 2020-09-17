import random
import string
# import pickle

tamanhoLista = 8


class Pessoa:
    nome = ''

class Lista:
    alunos = [Pessoa()]*tamanhoLista
    numeroElementos = 0


def criaLista():

  lista = Lista()
  print("Beleza, você criou uma lista!")
  return lista



def imprimeLista(lista):
  print("[ ________ RELATÓRIO ________ ]")

  for i in range(lista.numeroElementos):
    print("[{}] Nome: {}".format(i, lista.alunos[i].nome), end = "\t")
    print("Matricula: {}".format(lista.alunos[i].matricula))

  print("[{} elemento(s) ocupado(s) de {}]".format(lista.numeroElementos, tamanhoLista))


def entradaDados():
  aluno = Pessoa()
  aluno.nome = input("Informe o nome.....: ")
  aluno.matricula = int(input("Informe a matricula: "))

  return aluno


def incluiFimLista(lista):


  if lista.numeroElementos != len(lista.alunos):

    lista.alunos[lista.numeroElementos] = entradaDados()


    lista.numeroElementos += 1
    print("Sucesso na inclusão... 👏!")
  else:

    print("Lista lotadinha... desculpe!")

  return lista

def consultaElementLista(lista):
    index = int(input("Informe o index.....: "))
    print(lista.alunos[index].nome + ' ' + lista.alunos[index].matricula)

def incluiInicioLista(lista):


  if lista.numeroElementos != len(lista.alunos):
    listabkp = lista.alunos
    lista.alunos = [Pessoa()]*tamanhoLista
    lista.alunos[0] = entradaDados()
    for i in range(lista.numeroElementos):
        lista.alunos[i+1] = listabkp[i]


    lista.numeroElementos += 1

    print("Sucesso na inclusão... 👏!")
  else:

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

# def save(lista):
#     with open('lista.dictionary', 'wb') as listaFile:
#         pickle.dump(lista, listaFile)


def menu():
  while True:
    print("\033[93m" + "[ ____ SISTEMA 🤑 ACADÊMICO ____ ]\n \
1. Cria lista, cara\n \
2. Bota no fim da lista, cara\n \
3. Coloca no inicio da lista, cara\n \
4. Tira elemento da lista, bro\n \
5. Printa lista, meo\n \
6. Vamo vê oq tem nesse lugar da lista, parça \n \
7. Troca aquele elemento ali por esse aqui, mano\n \
8. Organiza a lista por bolhinhas, velho\n \
9. sjfbhKSbfHfbKDBffjd, maninho")


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
    # elif opcaoMenu == '10':
    #   save(lista.alunos)

    else:
      print()
      print("\033[93m" + "[ ____ Ahhhh, que pena, você já vai... Volte sempre! ____ ]")
      break

menu()
