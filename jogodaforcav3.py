# Importando as bibliotecas que serão utiliadas
from os import system
import re
import unicodedata
import random

class JogoDaForca():
    
    # Criando as listas de palavras
    frutas = ["Abacaxi", "Banana", "Cereja", "Damasco", "Figo", "Goiaba", "Kiwi", "Laranja", "Maçã", "Melancia", "Melão", "Manga", "Pêssego", "Pera", "Uva", "Morango", "Abacate", "Ameixa", "Caju", "Jabuticaba"]
    paises = ["Brasil", "Estados Unidos", "Canadá", "México", "Reino Unido", "França", "Alemanha", "Itália", "Espanha", "Portugal", "Japão", "China", "Índia", "Austrália", "Nova Zelândia", "Argentina", "Colômbia", "Peru", "Chile", "Uruguai"]
    nomes = ["Ana", "Beatriz", "Carlos", "Débora", "Eduardo", "Fernanda", "Gabriel", "Helena", "Isabela", "João", "Karen", "Luis", "Maria", "Marcos", "Otávio", "Paula", "Rafael", "Sara", "Suli", "Thiago", "Vanessa"]
    paises_hard = [    "Uzbequistão",    "Quirguistão",    "Turcomenistão",    "Kazakhstan",    "Azerbaijão",    "Tajiquistão",    "Bielorrússia",    "Timor-Leste",    "São Cristóvão e Nevis",    "Santa Lúcia",    "São Vicente e Granadinas",    "Antígua e Barbuda",    "Guiné Equatorial",    "Ilhas Marshall",    "Kiribati",    "Tuvalu",    "Micronésia",    "Palau",    "Nauru",    "Vanuatu"]
    frutas_hard = ['Rambutão', 'Pitomba', 'Jenipapo', 'Lichia', 'Nêspera', 'Cupuaçu', 'Kiwano', 'Tamarindo', 'Jaca', 'Physalis', 'Maracujá', 'Carambola', 'Cajá', 'Jatobá', 'Graviola', 'Biribá', 'Sapodila', 'Atemoia', 'Ciruela', 'Acerola']
    nomes_hard = ['Gwendolyn', 'Xavier', 'Beatrix', 'Ezekiel', 'Aurelia', 'Leopold', 'Cressida', 'Thaddeus', 'Isadora', 'Percival', 'Seraphina', 'Augustus', 'Ophelia', 'Phineas', 'Cordelia', 'Lysander', 'Imogen', 'Caspian', 'Esmeralda', 'Atticus']

    # Criando o inicializador 
    def __init__(self):
        pass
    
    # Criando um módulo para o boneco do jogo da forca
    def forca(self, separador, x):
        pass  
    
    # Remove os acentos das letras maiúsculas e minúsculas.
    def remover_acentos(self, texto):
        texto = texto.lower()
        texto = unicodedata.normalize('NFD', texto)
        texto = re.sub(r'[\u0300-\u036f]', '', texto)
        return texto
    
    def opcao(self):
        pass

class DesenhoDaForca(JogoDaForca):
    
    def __init__(self):
        JogoDaForca.__init__(self)
    
    def forca(self, quantidade_de_letras, x):
        if x == 0:
            print("\t\t\t ______\n\t\t\t|      |\n\t\t\t|       \n\t\t\t|        \n\t\t\t|       \n\t\t\t|         \n\t\t\t|       \n\t\t\t|%s" %(quantidade_de_letras))
        if x == 1:
            print("\t\t\t ______\n\t\t\t|      |\n\t\t\t|      O\n\t\t\t|        \n\t\t\t|       \n\t\t\t|         \n\t\t\t|       \n\t\t\t|%s" %(quantidade_de_letras))
        if x == 2:
            print("\t\t\t ______\n\t\t\t|      |\n\t\t\t|      O\n\t\t\t|      |\n\t\t\t|      |\n\t\t\t|         \n\t\t\t|       \n\t\t\t|%s" %(quantidade_de_letras))
        if x == 3:
            print("\t\t\t ______\n\t\t\t|      |\n\t\t\t|      O\n\t\t\t|     \|\n\t\t\t|      |\n\t\t\t|         \n\t\t\t|       \n\t\t\t|%s" %(quantidade_de_letras))
        if x == 4:
            print("\t\t\t ______\n\t\t\t|      |\n\t\t\t|      O\n\t\t\t|     \|/\n\t\t\t|      |\n\t\t\t|         \n\t\t\t|       \n\t\t\t|%s" %(quantidade_de_letras))
        if x == 5:
            print("\t\t\t ______\n\t\t\t|      |\n\t\t\t|      O\n\t\t\t|     \|/\n\t\t\t|      |\n\t\t\t|     /   \n\t\t\t|       \n\t\t\t|%s" %(quantidade_de_letras))
        if x == 6:
            print("\t\t\t ______\n\t\t\t|      |\n\t\t\t|      O\n\t\t\t|     \|/\n\t\t\t|      |\n\t\t\t|     / \ \n\t\t\t|       \n\t\t\t|%s" %(quantidade_de_letras))

class CodigoDoJogo(JogoDaForca):
    def Codigo(self, palavra):

        def quantidade_de_letra(palavra):
            quantidade_de_letras = []
            for letra in palavra:
                if letra == ' ':
                    quantidade_de_letras.append(' ')
                else:
                    quantidade_de_letras.append('_')
            return quantidade_de_letras

        def string(palavra):
            return (' '.join(palavra)) 

        #contador_de_perdas = 0
        #contador_de_vitorias = 0
        erro = 0
        count = 0
        lista_de_letras_erradas = []
        lista_de_letras_certas = []
        quantidade_de_letras = quantidade_de_letra(palavra)
        DesenhoDaForca().forca(string(quantidade_de_letras),0)
        print("\n\t\tA palavra possui %d letras." %(len(quantidade_de_letras)))
              
        while count < len(palavra):
            letra = input("\n\t\tDigite '0' para voltar para as opções.\n\t\tEscolha uma letra: ")
            if letra == '0':
                break
            if letra not in lista_de_letras_erradas and letra not in lista_de_letras_certas:
                i = 0
                logica = False

                for letra_da_palavra in palavra:
                    letra_formatada = JogoDaForca().remover_acentos(letra_da_palavra)
                    if letra_formatada == letra:
                        quantidade_de_letras[i] = letra_da_palavra
                        logica = True
                        count += 1
                        system('cls')
                    i += 1

                if letra in quantidade_de_letras:
                    lista_de_letras_certas.append(letra)

                if logica == False:
                    erro += 1
                    system('cls')
                    lista_de_letras_erradas.append(letra)


                print('\n\t\tLista de palavras erradas: %s' %(lista_de_letras_erradas))
                print('\t\tLista de palavras certas: %s' %(lista_de_letras_certas))
                novas = string(quantidade_de_letras)
                DesenhoDaForca().forca(novas,erro)

                if erro == 6:
                    DesenhoDaForca().forca(novas,erro)
                    break

                #x+=1
            else:
                print("\n\t\tLetra já digitada. Tente novamente!")
        if logica == False:
            #contador_de_perdas += 1
            print("\n\t\tVocê Perdeu!")
            
        elif logica == True:
            #contador_de_vitorias += 1
            print("\n\t\tVocê Ganhou!")            
        #print("\n\t\tVitórias = %d\n\t\tDerrotas = %d." %(contador_de_vitorias, contador_de_derrotas))

def opcoes(lista):
    palavra_aleatoria = random.choice(lista)
    if palavra_aleatoria in lista_de_palavras_repetidas:
        print("\n\t\tFoi gerado uma palavra repetida. Tente novamente!")
        pass
    else:
        CodigoDoJogo().Codigo(palavra_aleatoria)
        lista_de_palavras_repetidas.append(palavra_aleatoria)
    print('\n\t\tPalavras que já foram utilizadas: ', lista_de_palavras_repetidas)

lista_de_palavras_repetidas = []

while True:
    try:
        print("\n\t\tEscolha o modo do jogo:\n\t\t1. Modo Fácil\n\t\t2. Modo Difícil\n\t\t0. Sair do Jogo")
        nivel = int(input("\n\t\tDigite o nível escolhido: "))
        if nivel == 0:
            print("\n\t\tObrigado por jogar!")
            break
        print("\n\t\tEscolha o tipo de palavras que você deseja adivinhar:\n\t\t1. Frutas\n\t\t2. Países\n\t\t3. Nomes\n\t\t0. Sair do Jogo")
        opcao = int(input("\n\t\tDigite a opção escolhida: "))

        if nivel == 1 and opcao == 1:
            system('cls')
            print("\n\t\tVocê escolheu o tipo Frutas no Modo Fácil.")
            opcoes(JogoDaForca.frutas)
        elif nivel == 1 and opcao == 2:
            system('cls')
            print("\n\t\tVocê escolheu o tipo Países no Modo Fácil.")
            opcoes(JogoDaForca.paises)
        elif nivel == 1 and opcao == 3:
            system('cls')
            print("\n\t\tVocê escolheu o tipo Nomes no Modo Fácil.")
            opcoes(JogoDaForca.nomes)
        elif nivel == 2 and opcao == 1:
            system('cls')
            print("\n\t\tVocê escolheu o tipo Frutas no Modo Difícil.")
            opcoes(JogoDaForca.frutas_hard)
        elif nivel == 2 and opcao == 2:
            system('cls')
            print("\n\t\tVocê escolheu o tipo Países no Modo Difícil.")
            opcoes(JogoDaForca.paises_hard)
        elif nivel == 2 and opcao == 3:
            system('cls')
            print("\n\t\tVocê escolheu o tipo Nomes no Modo Difícil.")
            opcoes(JogoDaForca.nomes_hard)
        elif nivel != 0 and opcao == 0:
            print("\n\t\tObrigado por jogar!")
            break
        else:
            print('\n\t\tOpção inválida! Tente novamente.')
    except:
        print("\n\t\tOpção inválida! Tente novamente.")