# Objetivo:  Fazer menu gestão dos jogadores da equipa com estatiticas e botão para melhorar o skill do jogador utilizando o saldo da equipa

import tkinter as tk
from tkinter import * # Para poder utilizar a linha de apagar a entrada de texto
from tkinter import messagebox
import random
import pandas as pd
#from detalhes import detalhes_jogador


""" app_plantel = tk.Tk()
app_plantel.title("Gestão Plantel")
app_plantel.geometry("200x400") """

app_add_jogador = tk.Tk()
app_add_jogador.title("Adicionar jogador")
app_add_jogador.geometry("400x350")
nome_label = tk.Label(app_add_jogador, text="Nome do Jogador")
nome_label.grid(row=0,column=0)
nome = tk.Entry(app_add_jogador)
nome.grid(row=0,column=1)
idade_label = tk.Label(app_add_jogador, text="Idade do Jogador")
idade_label.grid(row=1,column=0)
idade = tk.Entry(app_add_jogador)
idade.grid(row=1,column=1)
posicao_label = tk.Label(app_add_jogador, text="Posição do Jogador")
posicao_label.grid(row=3,column=0)
posicao = tk.Listbox(app_add_jogador, height=4) # botão para posição de jogador
posicao.insert(1, "Atacante")
posicao.insert(2, "Médio")
posicao.insert(3, "Defesa")
posicao.insert(4, "Gaurda-Redes")
posicao.grid(row=3,column=1)

saldo = 0
jogadores_dict = {
    "Nome Jogador":[],
    "Idade":[],
    "Posição":[],
    "Stat1": [],
    "Stat2":[],
    "Stat3":[],
    "Stat4":[],
    "Stat5":[]
    }
jogadores_df = pd.DataFrame(jogadores_dict)

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
    plantel_list.insert(END, nome.get())
    nome.delete(0, END)
    idade.delete(0, END)
    posicao.selection_clear(0, "end")
    return

def detalhes_jogador():
    global saldo
    nome_jogador = plantel_list.get(plantel_list.curselection())
    detalhes_app = Toplevel(app_add_jogador)
    detalhes_app.title("Estatísticas Jogador")
    detalhes_app.geometry("500x500")
    print(jogadores_df[jogadores_df["Nome Jogador"]==nome_jogador])
    nome_jogador = tk.Label(detalhes_app, text=f"Nome: {nome_jogador}")
    nome_jogador.pack()

    return

botao_submeter = tk.Button(app_add_jogador, text="Adicionar jogador", command=command_adicionar_dados_jogador)
botao_submeter.grid(row=0, column=2)

# visualizar plantel com transição para menu de treino onde mostrar versao expandida e botao de treino
plantel_list = tk.Listbox(app_add_jogador, width=20, height=10)
plantel_list.grid(row=5, column=1)
## botão para selecionar jogador e abrir menu de treino
botao_selecionar = tk.Button(app_add_jogador, text="Detalhes", command=detalhes_jogador)
#botao_selecionar = tk.Button(app_add_jogador, text="Detalhes")

botao_selecionar.grid(row=5,column=2)


#Visualiar estaticaticas de jogador e melhorar certas estatsticas com base no saldo. Incluir botão para remover jogador do plantel
## em progresso


app_add_jogador.mainloop()

# gerar plantel automaticamente!