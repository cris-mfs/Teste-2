import tkinter as tk
import random
import subprocess
from random import choise

# Configurações do campo de futebol
comprimento_campo = 950
largura_campo = 600
cor_fundo_campo = "green"
cor_linhas = "white"

# Configurações dos jogadores
raio_jogador = 10
cor_time1 = "red"
cor_time2 = "blue"
posicoes_time1 = [(20, 300), (150, 100), (150, 250), (150, 350), (150, 500), (275, 100), (275, 250), (275, 350), (275, 500), (400, 200), (400, 400)]
posicoes_time2 = []

def desenhar_campo():
    # Criação do canvas
    canvas.delete("all")

    # Desenha as linhas de marcação do campo
    # Linhas laterais
    canvas.create_line(comprimento_campo / 2, 0, comprimento_campo / 2, largura_campo, fill=cor_linhas, width=2)
    canvas.create_line(0, 0, 0, largura_campo, fill=cor_linhas, width=2)
    canvas.create_line(comprimento_campo, 0, comprimento_campo, largura_campo, fill=cor_linhas, width=2)
    # Linhas de fundo
    canvas.create_line(0, 0, comprimento_campo, 0, fill=cor_linhas, width=2)
    canvas.create_line(0, largura_campo, comprimento_campo, largura_campo, fill=cor_linhas, width=2)
    # Linha central
    canvas.create_line(comprimento_campo / 2, 0, comprimento_campo / 2, largura_campo, fill=cor_linhas, width=2)
    # Círculos centrais
    canvas.create_oval(comprimento_campo / 2 - 50, largura_campo / 2 - 50, comprimento_campo / 2 + 50, largura_campo / 2 + 50, outline=cor_linhas, width=2)

    # Desenha os jogadores do time 1
    for posicao in posicoes_time1:
        x, y = posicao
        canvas.create_oval(x - raio_jogador, y - raio_jogador, x + raio_jogador, y + raio_jogador, fill=cor_time1)

    # Desenha os jogadores do time 2
    for posicao in posicoes_time2:
        x, y = posicao
        canvas.create_oval(x - raio_jogador, y - raio_jogador, x + raio_jogador, y + raio_jogador, fill=cor_time2)

def on_selecionar_formacao_time1(event):
        formacao_selecionada = formacao_time1_selector.get()
        if formacao_selecionada == "3-4-3":#OK posições
            posicoes_time1[:] = [(20, 300), (150, 150), (150, 300), (150, 450), (275, 100), (275, 250), (275, 350), (275, 500), (400, 150), (400, 300), (400, 450)]
        elif formacao_selecionada == "4-3-3":#OK posições
            posicoes_time1[:] = [(20, 300), (150, 100), (150, 250), (150, 350), (150, 500), (275, 150), (275, 300), (275, 450), (400, 150), (400, 300), (400, 450)]
        elif formacao_selecionada == "4-4-2":#OK posições
            posicoes_time1[:] = [(20, 300), (150, 100), (150, 250), (150, 350), (150, 500), (275, 100), (275, 250), (275, 350), (275, 500), (400, 200), (400, 400)]


def atualizar_formacao_time2():
    formacao_time2 = random.choice(["3-4-3", "4-3-3", "4-4-2"])
    if formacao_time2 == "3-4-3":#OK posições
        posicoes_time2[:] = [(880, 300), (750, 150), (750, 300), (750, 450), (625, 100), (625, 250), (625, 350), (625, 500), (500, 150), (500, 300), (500, 450)]
    elif formacao_time2 == "4-3-3":#OK posições
        posicoes_time2[:] = [(880, 300), (750, 100), (750, 250), (750, 350), (750, 500), (625, 150), (625, 300), (625, 450), (500, 150), (500, 300), (500, 450)]
    elif formacao_time2 == "4-4-2":#OK posições
        posicoes_time2[:] = [(880, 300), (750, 100), (750, 250), (750, 350), (750, 500), (625, 100), (625, 250), (625, 350), (625, 500), (500, 200), (500, 400)]

    desenhar_campo()

def iniciar_jogo():
    on_selecionar_formacao_time1(None)  # Chama a função para atualizar a formação do time1
    atualizar_formacao_time2()
# função para abrir o script do plantel


# Criação da janela
janela = tk.Tk()
janela.title("Campo de Futebol")
janela.geometry("1085x600")

# Criação do canvas
canvas = tk.Canvas(janela, width=comprimento_campo, height=largura_campo, bg=cor_fundo_campo)
canvas.grid(row=0, column=0, columnspan=2, rowspan=15)

# Criação do seletor para alterar a formação tática do time 1
formacao_time1_selector = tk.StringVar(janela)
formacao_time1_selector.set("3-4-3")
formacao_time1_menu = tk.OptionMenu(janela, formacao_time1_selector, "3-4-3", "4-3-3", "4-4-2")
formacao_time1_menu.grid(row=11, column=2)

# Criação do botão para iniciar o jogo
jogar_button = tk.Button(janela, text="Jogar", command=iniciar_jogo)
jogar_button.grid(row=12, column=2)

# Chamada inicial para desenhar o campo de futebol
desenhar_campo()

## Conjunto de Widgets para adicionar jogador
nome_label = tk.Label(janela, text="Nome do Jogador")
nome_label.grid(row=0,column=2)
nome = tk.Entry(janela)
nome.grid(row=1,column=2)

idade_label = tk.Label(janela, text="Idade do Jogador")
idade_label.grid(row=2,column=2)
idade = tk.Entry(janela)
idade.grid(row=3,column=2)

posicao_label = tk.Label(janela, text="Posição do Jogador")
posicao_label.grid(row=4,column=2)
posicao = tk.Listbox(janela, height=4) # botão para posição de jogador
posicao.insert(1, "Atacante")
posicao.insert(2, "Médio")
posicao.insert(3, "Defesa")
posicao.insert(4, "Gaurda-Redes")
posicao.grid(row=5,column=2)

#simulador de jogos
class simulador_futebol:
    def __init__(self,master):
        self.master = master
        self.master.title("simulador de futebol")
        self.pontos_equipa_usuario = 0
        self.pontos_equipa_adversaria = 0
#Janela para criar equipa
        self.label_equipa_usuario =tk.Label(master, text="Equipa do utilizador:")
        self.label_equipa_usuario.pack()

        self.entry_equipa_usuario = tk.Entry(master)
        self.entry_equipa_usuario.pack()
#Janela para criar equipa adversaria        
        self.label_equipa_adversaria = tk.Label(master, text="Equipa Adversária:")
        self.label_equipa_adversaria.pack()
        
        self.entry_equipa_adversaria = tk.Entry(master)
        self.entry_equipa_adversaria.pack()

        self.button_criar_equipas = tk.Button(master, text="Criar equipas", command=self.button_criar_equipas)
        self.button_criar_equipas.pack()

janela.mainloop()
