import tkinter as tk
import random
from tkinter import * # Para poder utilizar a linha de apagar a entrada de texto
import pandas as pd # para guardar os dados dos jogadores

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
janela.geometry("1210x610")

# Criação do canvas
canvas = tk.Canvas(janela, width=comprimento_campo, height=largura_campo, bg=cor_fundo_campo)
canvas.grid(row=0, column=0, columnspan=2, rowspan=20)

# Criação do seletor para alterar a formação tática do time 1
formacao_time1_selector = tk.StringVar(janela)
formacao_time1_selector.set("3-4-3")
formacao_time1_menu = tk.OptionMenu(janela, formacao_time1_selector, "3-4-3", "4-3-3", "4-4-2")
formacao_time1_menu.grid(row=48, column=2)

# Criação do botão para iniciar o jogo
jogar_button = tk.Button(janela, text="Jogar", command=iniciar_jogo)
jogar_button.grid(row=49, column=2)

# Chamada inicial para desenhar o campo de futebol
desenhar_campo()

#####################################################################
#                                                                   #
# ------------ Secção de Código para Gestão do Plantel ------------ #
#                                                                   #
#####################################################################

saldo = 0


## Conjunto de Widgets para adicionar jogador
nome_label = tk.Label(janela, text="Nome do Jogador")
nome_label.grid(row=0,column=2)
nome = tk.Entry(janela)
nome.grid(row=0,column=3)

idade_label = tk.Label(janela, text="Idade do Jogador")
idade_label.grid(row=2,column=2)
idade = tk.Entry(janela)
idade.grid(row=2,column=3)

posicao_label = tk.Label(janela, text="Posição do Jogador")
posicao_label.grid(row=4,column=2)
posicao = tk.Listbox(janela, height=4) # botão para posição de jogador
posicao.insert(1, "Atacante")
posicao.insert(2, "Médio")
posicao.insert(3, "Defesa")
posicao.insert(4, "Gaurda-Redes")
posicao.grid(row=4,column=3)

plantel_list = tk.Listbox(janela, width=20, height=15)
plantel_list.grid(row=4, column=3, rowspan=2)
scrollbar = Scrollbar(janela)
scrollbar.grid(row=4, column=4, rowspan=2, sticky="ns")
plantel_list.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = plantel_list.yview)

jogadores_dict = {
    "Nome Jogador":[],
    "Idade":[],
    "Posição":[],
    "Velocidade": [],
    "Força":[],
    "Resistência":[],
    "Drible":[],
    "Passe":[]
    }
jogadores_df = pd.DataFrame(jogadores_dict)

# Para adicionar um jogador ao plantel a partir dos inputs
def command_adicionar_dados_jogador():
    dados_jogador = [
        nome.get(), 
        idade.get(), 
        posicao.get(posicao.curselection()), 
        random.randint(1,10), 
        random.randint(1,10), 
        random.randint(1,10),
        random.randint(1,10),
        random.randint(1,10)
        ]
    jogadores_df.loc[len(jogadores_df)] = dados_jogador
    inserir_na_lista = f"{dados_jogador[0]}" # Insere o nome do jogador na lista com base no número do jogador na tabela de dados
    plantel_list.insert(END, inserir_na_lista) #Adicionar o nome do jogador à lista
    nome.delete(0, END)
    idade.delete(0, END)
    posicao.selection_clear(0, "end")
    return

botao_submeter = tk.Button(janela, text="Adicionar jogador", command=command_adicionar_dados_jogador)
botao_submeter.grid(row=4, column=2)

# Excerto para criar plantel aleatório
exemplos_primeiro_nome = ["David","Cristiano","João", "Pedro", "Alberto", "Inácio", "Mauro", "José", "Eusébio", "Ricardo", "Miguel"]
exemplos_apelido = ["Rebelo","Rocha","Silva", "Pereira", "Marques", "Santos", "Parreira", "Tavares", "Sousa"]
for i in range(11):
    dados_jogador = [ # os nomes não se podem repetir se não os searchs ficam todos baralhados... Tenho que conseguir extrair o indice unico de cada jogador
        random.choice(exemplos_primeiro_nome)+" "+random.choice(exemplos_apelido), 
        random.randint(18,34), 
        random.choice(["Atacante", "Médio", "Defesa", "Guarda-Redes"]),
        random.randint(1,10), 
        random.randint(1,10), 
        random.randint(1,10),
        random.randint(1,10),
        random.randint(1,10)
        ]
    jogadores_df.loc[len(jogadores_df)] = dados_jogador
    inserir_na_lista = f"{dados_jogador[0]}"
    plantel_list.insert(END, inserir_na_lista) #Adicionar o nome do jogador à lista

#----------------------------------#
#-- Menu de Treino dos jogadores --#
#----------------------------------#
    def detalhes_jogador():
        global saldo
        nome_jogador = plantel_list.get(plantel_list.curselection())
        detalhes_app = Toplevel(janela)
        detalhes_app.title("Estatísticas Jogador")
        detalhes_app.geometry("500x500")
        #print(jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador].get(key = "Idade"))
        label_nome_jogador = tk.Label(detalhes_app, text=f"Nome: {nome_jogador}")
        label_nome_jogador.pack()
        idade_jogador = jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador]["Idade"].values[0]
        label_idade = tk.Label(detalhes_app, text=f"Idade: {idade_jogador}")
        label_idade.pack()
        posicao_jogador = jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador]["Posição"].values[0]
        label_posicao = tk.Label(detalhes_app, text=f"Posição: {posicao_jogador}")
        label_posicao.pack()
        stat1_jogador = jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador]["Velocidade"].values[0]
        label_stat1 = tk.Label(detalhes_app, text=f"Velocidade: {stat1_jogador}")
        label_stat1.pack()
        stat2_jogador = jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador]["Força"].values[0]
        label_stat2 = tk.Label(detalhes_app, text=f"Força: {stat2_jogador}")
        label_stat2.pack()
        stat3_jogador = jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador]["Resistência"].values[0]
        label_stat3 = tk.Label(detalhes_app, text=f"Resistência: {stat3_jogador}")
        label_stat3.pack()
        stat4_jogador = jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador]["Drible"].values[0]
        label_stat4 = tk.Label(detalhes_app, text=f"Drible: {stat4_jogador}")
        label_stat4.pack()
        stat5_jogador = jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador]["Passe"].values[0]
        label_stat5 = tk.Label(detalhes_app, text=f"Passe: {stat5_jogador}")
        label_stat5.pack()

        #BOTÕES PARA TREINAR
        def command_treinar():
            old_value = jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador]["Velocidade"].values[0]
            print(old_value)
            new_value = old_value + 1
            print(new_value)
            teste = jogadores_df.xs("Velocidade")
            print(teste)
            return
        
        botao_treino1 = tk.Button(detalhes_app, text="Treino1", command=command_treinar)
        botao_treino1.pack()
        return
## botão para selecionar jogador e abrir menu de treino
botao_selecionar = tk.Button(janela, text="Detalhes", command=detalhes_jogador)
botao_selecionar.grid(row=5,column=2)

janela.mainloop()
