import tkinter as tk
import random
from tkinter import * # Para poder utilizar a linha de apagar a entrada de texto
from tkinter import messagebox
import pandas as pd # para guardar os dados dos jogadores
import unittest

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

# Criação da janela
janela = tk.Tk()
janela.title("Campo de Futebol")
janela.geometry("1400x800")

# Criação do canvas
canvas = tk.Canvas(janela, width=comprimento_campo, height=largura_campo, bg=cor_fundo_campo)
canvas.grid(row=0, column=0, columnspan=2, rowspan=50)

# Criação do seletor para alterar a formação tática do time 1
formacao_time1_selector = tk.StringVar(janela)
formacao_time1_selector.set("3-4-3")
formacao_time1_menu = tk.OptionMenu(janela, formacao_time1_selector, "3-4-3", "4-3-3", "4-4-2")
formacao_time1_menu.grid(row=12, column=2)

# Criação do botão para iniciar o jogo
formacao_label = tk.Label(janela, text="Formação Tática:")
formacao_label.grid(row=11, column=2)

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
                jogadores_df.at[id_jogador, Stat_a_treinar] = new_value
                # Atualizar os dados a mostrar
                dados = jogadores_df.filter(items=[id_jogador], axis=0)
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

#####################################################################
#                                                                   #
# ------- Secção de Código para Simular Jogos e Campeonato -------- #
#                                                                   #
#####################################################################



class SimuladorFutebol:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulador de Futebol")
        
        self.pontos_equipa_usuario = 0
        self.pontos_equipa_adversaria = 0
        self.historico_jogos = []
        
        self.label_equipa_usuario = tk.Label(master, text="Equipa do Utilizador:")
        self.label_equipa_usuario.grid(row=6,column=3)
        
        self.entry_equipa_usuario = tk.Entry(master)
        self.entry_equipa_usuario.grid(row=7, column=3)
        
        self.label_equipa_adversaria = tk.Label(master, text="Equipa Adversária:")
        self.label_equipa_adversaria.grid(row=8, column=3)
        
        self.entry_equipa_adversaria = tk.Entry(master)
        self.entry_equipa_adversaria.grid(row=9, column=3)
        
        self.button_criar_equipas = tk.Button(master, text="Criar Equipas", command=self.criar_equipas)
        self.button_criar_equipas.grid(row=10, column=3)
        
        self.button_simular_jogo = tk.Button(master, text="Simular Jogo", command=self.simular_jogo, state=tk.DISABLED)
        self.button_simular_jogo.grid(row=11, column=3)
        
        self.button_campeonato = tk.Button(master, text="Iniciar Campeonato", command=self.iniciar_campeonato, state=tk.DISABLED)
        self.button_campeonato.grid(row=12, column=3)
        
        self.button_reset = tk.Button(master, text="Reset", command=self.reset)
        self.button_reset.grid(row=13, column=3)
        
        self.label_historico = tk.Label(master, text="Histórico de Jogos:")
        self.label_historico.grid(row=14, column=3)
        
        self.textbox_historico = tk.Text(master, height=10, width=40)
        self.textbox_historico.grid(row=15, column=3)
        
    def criar_equipas(self):
        equipa_usuario = self.entry_equipa_usuario.get()
        equipa_adversaria = self.entry_equipa_adversaria.get()
        
        if equipa_usuario and equipa_adversaria:
            self.equipa_usuario = equipa_usuario
            self.equipa_adversaria = equipa_adversaria
            messagebox.showinfo("Sucesso", "Equipas criadas com sucesso!")
            self.button_simular_jogo.config(state=tk.NORMAL)
            self.button_campeonato.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Erro", "Preencha o nome das equipas!")
            
    def simular_jogo(self):
        resultado = random.choice(["vitória", "empate", "derrota"])
        on_selecionar_formacao_time1(None)  # Chama a função para atualizar a formação do time1
        atualizar_formacao_time2() 

        if resultado == "vitória":
            self.pontos_equipa_usuario += 3
            self.pontos_equipa_adversaria += 0
            vencedor = self.equipa_usuario
            perdedor = self.equipa_adversaria
        elif resultado == "empate":
            self.pontos_equipa_usuario += 1
            self.pontos_equipa_adversaria += 1
            vencedor = "Empate"
            perdedor = "Empate"
        else:
            self.pontos_equipa_usuario += 0
            self.pontos_equipa_adversaria += 3
            vencedor = self.equipa_adversaria
            perdedor = self.equipa_usuario
            
        resultado_jogo = f"{self.equipa_usuario} {resultado.upper()} {self.equipa_adversaria}"
        self.historico_jogos.append(resultado_jogo)
        
        self.textbox_historico.insert(tk.END, resultado_jogo + "\n")
        
        messagebox.showinfo("Resultado", resultado_jogo)
        
    def iniciar_campeonato(self):
        self.reset()
        
        for jogo in range(1, 16):
            self.simular_jogo()
        
        if self.pontos_equipa_usuario > self.pontos_equipa_adversaria:
            vencedor = self.equipa_usuario
        elif self.pontos_equipa_usuario < self.pontos_equipa_adversaria:
            vencedor = self.equipa_adversaria
        else:
            vencedor = "Empate"
            
        messagebox.showinfo("Campeonato", f"O vencedor do campeonato é: {vencedor}!")
        
    def reset(self):
        self.pontos_equipa_usuario = 0
        self.pontos_equipa_adversaria = 0
        self.entry_equipa_usuario.delete(0, tk.END)
        self.entry_equipa_adversaria.delete(0, tk.END)
        self.historico_jogos = []
        self.textbox_historico.delete(1.0, tk.END)
        
        self.button_simular_jogo.config(state=tk.DISABLED)
        self.button_campeonato.config(state=tk.DISABLED)
        

simulador = SimuladorFutebol(janela)

###################################
#                                 #
# ------- Teste Unitário -------- #
#                                 #
###################################

    
janela.mainloop()

class Testar_caracteristicas_jogador(unittest.TestCase):
    def teste_jogador_sem_características_vazias(self):
        # Verifica se a característica do jogador não está vazia
        self.assertFalse(jogadores_df.empty)
        # Verifica se algum jogador tem uma característica vazia
        for column in jogadores_df.columns:
            self.assertFalse((jogadores_df[column].str.len() == 0).any())

if __name__ == '__main__':
    unittest.main()