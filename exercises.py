#%%
# 01 - Escreva uma função em Python que recebe uma string e retorna uma lista contendo suas duas metades, utilizando slicing.
def dividir_string(string) :
    mid = (len(string) + 1) // 2
    return [string[:mid], string[mid:]]

string = input('Digite algo: ')
print(dividir_string(string))

#%%
# 02 - Escreva uma função que recebe duas strings e verifica se a primeira começa com o prefixo fornecido
# pela segunda.

def verifica_prefixo(str1, str2):
    if(str1[:3] == str2[:3]):
        print(f'A string {str1} tem o mesmo prefixo que {str2}')
    else :    
        print(f'A string {str1} não tem o mesmo prefixo que {str2}')
        
string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')

verifica_prefixo(string1, string2)

#%%
# 03 - Escreva uma função que converte uma string em uma lista, onde cada caractere da string se torna um elemento da lista.
def string_para_lista(string) :
    print(list(string))

string = input('Digite algo: ')
string_para_lista(string)

#%%
# 04 - Escreva uma função chamada substitui_str que substitui todas as ocorrências de uma substring por outra em uma string fornecida.
def substitui_str(str1, substr, str2) :
    return str1.replace(substr, str2)

str1 = input('Entre com a primeira string: ')
substr = input('Entre com o pedaço da string a ser substituida: ')
str2 = input('Entre com a segunda string: ')

new_string = substitui_str(str1, substr, str2)
print(new_string)

#%%
# 05 - Escreva uma função que verifica se uma string é composta apenas por dígitos numéricos.
def checar_numerico(string) :
    return string.isnumeric()

string = input('Digite algo: ')
numerico = checar_numerico(string)
print(numerico)

#%%
# 06 - Escreva uma função que recebe um número inteiro como entrada e retorna uma string contendo os dígitos do número na ordem inversa.
def reverte_numero(nro) :
    return str(nro)[::-1]
    
nro = int(input('Entre com um número inteiro: '))
numero_invertido = reverte_numero(nro)
print(numero_invertido)

#%%
# 07 - Escreva uma função que recebe uma string contendo números de 0 a 9 e substitui cada dígito pelo nome correspondente do número em português.
def substitui_digitos(string) :
    nomes_numeros = {
        '0': 'zero',
        '1': 'um',
        '2': 'dois',
        '3': 'três',
        '4': 'quatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'sete',
        '8': 'oito',
        '9': 'nove'
    }
    
    resultado = ''
    for char in str(string):
        if char in nomes_numeros:
            resultado = nomes_numeros[char]

    return resultado

try:
    while True:
        numero = int(input('Digite um número de 0-9: '))
        if(numero >= 0 and numero <= 9) :
            resultado = substitui_digitos(numero)
            print(resultado)
            break;
        else:
            print('Valor digitado não está no intervalo 0-9. Tente novamente')        
except ValueError:
    print('Valor digitado não é um número inteiro. Tente novamente')

#%%
# 08 - Escreva uma função que recebe uma lista de strings e remove todos os elementos duplicados, mantendo apenas a primeira ocorrência de cada elemento.
def remove_duplicados(lista):
    lista_filtrada = []
    for string in lista:
        if string not in lista_filtrada:
            lista_filtrada.append(string)
    return lista_filtrada

lista_strings = ['Python', 'Javascript', 'SQL', 'HTML', 'CSS', 'Python', 'HTML']
lista_filtrada = remove_duplicados(lista_strings)
print(lista_filtrada)

#%%
# 09 - Escreva uma função que recebe um número inteiro como entrada e retorna a soma dos dígitos desse número.
def soma_digitos(nro):
    soma = 0
    for char in str(nro):
        soma += int(char)
    return soma

while True:
    try:
        numero = int(input('Digite um nro inteiro: '))
        total = soma_digitos(numero)
        break
    except ValueError: 
        print('O valor digitado não é um número inteiro. Tente novamente')

# print(total)

#%%
# 10 - Escreva uma função que recebe duas strings como entrada e retorna uma lista contendo os caracteres comuns entre as duas strings, sem repetição.
def gerar_lista_caracteres_unicos(str1, str2):
    lista = []
    for char in str1:
        if char in str2 and char not in lista:
            lista.append(char)
    return lista

str1 = input('Digite a primeira string: ')
str2 = input('Digite a segunda string: ')
lista_filtrada = gerar_lista_caracteres_unicos(str1, str2)
print(lista_filtrada)

#%%
# 11 - Escreva uma função chamada inserir_palavra que receba uma lista de palavras e uma nova palavra. A função deve pedir ao usuário a posição desejada para inserir a nova palavra na lista. Se a lista tiver menos de três elementos, insira a nova palavra automaticamente no final da lista. No fim, retorne a lista atualizada.

def inserir_palavra(lista_palavras, nova_palavra) :
    if len(lista_palavras) < 3:
        lista_palavras.append(nova_palavra)
    else:
        posicao = int(input('Digite a posicao desejada para inserir a nova palavra na lista: '))
        lista_palavras.insert(posicao, nova_palavra)
    return lista_palavras

lista = ['Python', 'Javascript', 'HTML']
print(f'Lista: {lista}')

nova_palavra = input('Digite uma nova palavra a ser adicionada a lista: ')

lista_atualizada = inserir_palavra(lista, nova_palavra)
print(f'Lista atualizada: {lista_atualizada}')

#%%
# 12 - Escreva uma função chamada combinar_listas que receba duas listas de números e use o método extend para combiná-las em uma única lista. A função deve retornar essa lista combinada.
def combinar_listas(lista1, lista2):
    lista_combinada = []
    lista_combinada.extend(lista1)
    lista_combinada.extend(lista2)
    return lista_combinada

lista1 = ['Python', 'Django', 'Flask']
lista2 = ['Javascript', 'Next', 'React']

lista_combinada = combinar_listas(lista1, lista2)
print(lista_combinada)

#%%
# 13 - Escreva uma função chamada apagar_duplicatas que receba uma lista de palavras e remova todas as ocorrências de uma palavra duplicada, mantendo apenas a primeira ocorrência.
def apagar_duplicatas(lista) :
    lista_sem_duplicatas = []
    for item in lista:
        if item not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(item)
    return lista_sem_duplicatas

lista = ['Python', 'Next', 'React', 'React Native', 'Python']
lista_filtrada = apagar_duplicatas(lista)
print(lista_filtrada)

#%%
# 14 - Escreva uma função chamada organizar_compras que receba uma lista de itens de compras e permita ao usuário remover o último item da lista
# (simulando o cancelamento da última compra) usando a função pop. A função deve exibir a lista de compras atualizada após a remoção.
# OBS: Se a lista estiver vazia, a função deve informar que não há mais itens para remover.
def organizar_compras(items):
    if items:
        removido = items.pop()
        print(f'Produto "{removido}" removido com sucesso')
        print(f'Lista atualizada: {items}' if items else 'Lista vazia')
    else:
        print('Lista vazia')

lista_de_compras = ['Maça', 'Banana', 'Abacaxi']
organizar_compras(lista_de_compras)

#%%
# 15 - Escreva uma função chamada manusear_string que recebe uma string e faz as seguintes operações:
# Exibe a string original.
# Solicita ao usuário um índice de início e um índice de fim, e exibe a substring correspondente.
# Exemplo de uso: manipular_string("Python é incrível!")
def manusear_string(string):
    print(f'String original: {string}')
    while True:
        try:        
            indice_inicio = int(input('Digite o indice de inicio: '))
            indice_fim = int(input('Digite o indice de fim: '))

            if indice_inicio < 0 or indice_fim >= len(string) or indice_inicio > indice_fim:
                print('Índice inválidos. Tente novamente.')
                continue

            string_sliced = string[indice_inicio:indice_fim + 1]
            print(f'Substring: {string_sliced}')
            break

        except ValueError:
            print('Valor digitado não é um inteiro. Tente novamente.')

manusear_string('Python é incrível!')

#%%
# 16 - Escreva uma função administrar_lista_compras que recebe uma lista de compras e permite as seguintes operações:
# Digitar "fim" para encerrar.
# Digitar "retirar" seguido do nome do produto ou seu índice para retirar o item da lista.
# Digitar "acrescentar" seguido do índice e do nome do produto para acrescentar o item na lista na posição indicada.
# A função deve reorganizar a lista conforme as operações do usuário e exibi-la ao final.

def administrar_lista_compras(lista):
    print('Digite "fim" para encerrar.')
    print('Digite "retirar" para remover um item.')
    print('Digite "acrescentar" para adicionar um item.')

    while True:
        operacao = input('Digite a operação desejada: ').lower()

        if operacao == 'fim':
            print('Operação encerrada.')
            break

        elif operacao == 'retirar':
            print(f'Lista atual: {lista}')
            escolha = input('Digite o nome ou índice do produto a ser retirado: ')

            try:
                if escolha.isdigit():
                    indice = int(escolha)
                    produto_removido = lista.pop(indice)
                    print(f'Produto "{produto_removido}" removido com sucesso.')
                else:
                    lista.remove(escolha)
                    print(f'Produto "{escolha}" removido com sucesso.')
                
                print(f'Lista atualizada: {lista}')

            except (ValueError, IndexError):
                print('Produto não encontrado. Tente novamente.')

        elif operacao == 'acrescentar':
            print(f'Lista atual: {lista}')
            try:
                indice = int(input('Digite o índice onde o produto será inserido: '))
                nome_produto = input('Digite o nome do produto: ')
                lista.insert(indice, nome_produto)
                print(f'Produto "{nome_produto}" adicionado com sucesso na posição {indice}.')
                print(f'Lista atualizada: {lista}')
            except ValueError:
                print('Índice inválido. Tente novamente.')

        else:
            print('Operação inválida. Tente novamente.')

    print(f'Lista final de compras: {lista}')


# Lista inicial de compras
lista_de_compras = ['Banana', 'Maçã', 'Laranja']
administrar_lista_compras(lista_de_compras)
