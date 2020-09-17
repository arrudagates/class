import random
import string

tamanhoLista = 4


class Pessoa:
    nome = ''

class Lista:
    alunos = [Pessoa()]*tamanhoLista
    numeroElementos = 0


def criaLista():

  lista = Lista()
  print("🧐 Beleza, você criou uma lista!")
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

def consultaElementLista(lista): #consulta o elemento chamado lista
    index = int(input("Informe o index.....: ")) #cria a variavel index e pede para o usuario informar o numero desta variavel
    if index < lista.numeroElementos:
        print(str(lista.alunos[index].nome) + ' ' + str(lista.alunos[index].matricula)) #imprime o nome e a matricula na posicao informada pelo index
    else:
        print('ops, esse index n tem nada')

def incluiInicioLista(lista):

  if lista.numeroElementos != len(lista.alunos): #Se o numero de elementos for diferente do numero total
    listabkp = lista.alunos #criada nova lista pra receber a lista antiga
    lista.alunos = [Pessoa()]*tamanhoLista
    lista.alunos[0] = entradaDados()
    for i in range(lista.numeroElementos):
        lista.alunos[i+1] = listabkp[i]


    lista.numeroElementos += 1 #conta +1 no numero de elementos

    print("Sucesso na inclusão... 👏!")
  else:

    print("Lista lotadinha... desculpe!")

  return lista

def excluiElementoLista(lista):

    index = int(input("Informe o index.....: "))
    if index < lista.numeroElementos: #se index existe na lista
        lista.alunos = lista.alunos[:index] + lista.alunos[index+1 :] #transforma a lista em 2 cortando antes e depois do index, juntando depois
        lista.numeroElementos -= 1 #tira 1
    else:
        print('ops, esse index n tem nada')
    return lista

def alteraElementoLista(lista):
    index = int(input("Informe o index.....: ")) #digitar a matricula a ser excluida
    if index < lista.numeroElementos:
        lista.alunos[index] = entradaDados() #pega o index novo e cola em cima do outro
    else:
        print('ops, esse index n tem nada')
    return lista


def bubbleSort(lista):

    for i in range(lista.numeroElementos-1): #itera por toda a lista
        for j in range(0, lista.numeroElementos-i-1): #itera de 0 até tamanho da lista - i - 1
            if int(lista.alunos[j].matricula) > int(lista.alunos[j+1].matricula): #se j for maior que o proximo elemento
                lista.alunos[j], lista.alunos[j+1] = lista.alunos[j+1], lista.alunos[j] #coloca o j depois do elemento que é maior que ele
    return lista



def corrompeLista(lista):
    for i in range(lista.numeroElementos):
        lista.alunos[i].nome = ''.join(random.SystemRandom().choice(string.ascii_letters) for j in range(len(str(lista.alunos[i].nome))))
        lista.alunos[i].matricula = ''.join(random.SystemRandom().choice(string.digits) for j in range(len(str(lista.alunos[i].matricula))))
    return lista


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
9. sjfbhKSbfHfbKDBffjd, maninho\n \
0. Vlw flw, buddy")


    while True:
      opcaoMenu = input("Opção: ")
      if opcaoMenu >= '0' and opcaoMenu <= '9':
        break
    print()

    if opcaoMenu >= '2' and opcaoMenu <= '9':
        try:
            lista
        except NameError:
            lista = criaLista()

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

    elif opcaoMenu == '0':
      print()
      print("\033[93m" + "[ ____ 🤬 Não Volte sempre! 🤬 ____ ]")
      break

menu()
