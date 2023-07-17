import tkinter as tk
import random
from tkinter import * # Para poder utilizar a linha de apagar a entrada de texto
from tkinter import messagebox
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
janela.geometry("1210x602")

# Criação do canvas
canvas = tk.Canvas(janela, width=comprimento_campo, height=largura_campo, bg=cor_fundo_campo)
canvas.grid(row=0, column=0, columnspan=2, rowspan=15)

# Criação do seletor para alterar a formação tática do time 1
formacao_time1_selector = tk.StringVar(janela)
formacao_time1_selector.set("3-4-3")
formacao_time1_menu = tk.OptionMenu(janela, formacao_time1_selector, "3-4-3", "4-3-3", "4-4-2")
formacao_time1_menu.grid(row=11, column=2, columnspan=2)

# Criação do botão para iniciar o jogo
jogar_button = tk.Button(janela, text="Jogar", command=iniciar_jogo)
jogar_button.grid(row=12, column=2, columnspan=2)

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
idade_label.grid(row=1,column=2)
idade = tk.Entry(janela)
idade.grid(row=1,column=3)

posicao_label = tk.Label(janela, text="Posição do Jogador")
posicao_label.grid(row=2,column=2)
posicao = tk.Listbox(janela, height=4) # botão para posição de jogador
posicao.insert(1, "Atacante")
posicao.insert(2, "Médio")
posicao.insert(3, "Defesa")
posicao.insert(4, "Gaurda-Redes")
posicao.grid(row=2,column=3)

plantel_list = tk.Listbox(janela, width=20, height=10)
plantel_list.grid(row=4, column=3)
scrollbar = Scrollbar(janela)
scrollbar.grid(row=4, column=4, sticky="ns")
plantel_list.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = plantel_list.yview)
lista_plantel_label = tk.Label(janela, text="Lista Jogadores")
lista_plantel_label.grid(row=4, column=2)

jogadores_dict = {
    "Nome":[],
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
botao_submeter.grid(row=3, column=3)

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
        id_jogador = int(plantel_list.curselection()[0])
        dados = jogadores_df.filter(items=[id_jogador], axis=0)
        detalhes_app = Toplevel(janela)
        detalhes_app.title("Estatísticas Jogador")
        detalhes_app.geometry("300x200")
        dados = jogadores_df.filter(items=[id_jogador], axis=0)
        cabecalhos = dados.columns.tolist()
        valores = dados.values.flatten().tolist()
        texto1 = "\n".join([f"{cabecalho}" for cabecalho in cabecalhos])
        label = tk.Label(detalhes_app, text=texto1, justify='left', anchor='w')
        label.grid(row=0, column=0)
        texto2 = "\n".join([f"{valor}" for valor in valores])
        label = tk.Label(detalhes_app, text=texto2, justify='right', anchor='w')
        label.grid(row=0, column=1)

        #BOTÕES PARA TREINAR
        def command_treinar(Stat_a_treinar):
            linha_a_mudar = jogadores_df.filter(items=[id_jogador], axis=0)
            old_value = linha_a_mudar[Stat_a_treinar].values[0]
            new_value = old_value + 1
            if new_value < 11: # Limite de treino é até 10
                indice_jogador_a_treinar = jogadores_df[jogadores_df["Nome"]==nome_jogador].index[0]
                jogadores_df.at[indice_jogador_a_treinar, Stat_a_treinar] = new_value
                # Atualizar os dados a mostrar
                dados = jogadores_df[jogadores_df["Nome"]==nome_jogador]
                valores = dados.values.flatten().tolist()
                texto2 = "\n".join([f"{valor}" for valor in valores])
                label = tk.Label(detalhes_app, text=texto2, justify='right', anchor='w')
                label.grid(row=0, column=1)
            else:
                messagebox.showinfo("Erro", "Não é possível treinar porque o Stat do jogador está no máximo")
            return
        
        botao_treino_stat1 = tk.Button(detalhes_app, text="+ Velocidade", height=1, command=lambda i = "Velocidade": command_treinar(i))
        botao_treino_stat1.grid(row=1, column=0)
        botao_treino_stat2 = tk.Button(detalhes_app, text="+ Força", height=1, command=lambda i = "Força": command_treinar(i))
        botao_treino_stat2.grid(row=1, column=1)
        botao_treino_stat3 = tk.Button(detalhes_app, text="+ Resistência", height=1, command=lambda i = "Resistência": command_treinar(i))
        botao_treino_stat3.grid(row=1, column=2)
        botao_treino_stat4 = tk.Button(detalhes_app, text="+ Drible", height=1, command=lambda i = "Drible": command_treinar(i))
        botao_treino_stat4.grid(row=2, column=0)
        botao_treino_stat5 = tk.Button(detalhes_app, text="+ Passe", height=1, command=lambda i = "Passe": command_treinar(i))
        botao_treino_stat5.grid(row=2, column=1)
        return
## botão para selecionar jogador e abrir menu de treino
botao_selecionar = tk.Button(janela, text="Ver Detalhes", command=detalhes_jogador)
botao_selecionar.grid(row=5,column=3)

janela.mainloop()
