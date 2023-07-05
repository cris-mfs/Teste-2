import tkinter as tk
import random

class SimuladorFutebol(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Equipa")

        self.equipa = {"nome": "Minha Equipa", "jogadores": [], "saldo": 1000}

        tk.Label(self, text=self.equipa["nome"]).pack()
        tk.Label(self, text=f"Saldo: {self.equipa['saldo']}").pack()

        tk.Button(self, text="Simular Jogo", command=self.simular_jogo).pack()

    def simular_jogo(self):
        resultado = random.choice(['Vitória', 'Derrota', 'Empate'])
        tk.Label(self, text=f"Resultado do jogo: {resultado}").pack()

if __name__ == '__main__':
    app = SimuladorFutebol()
    app.mainloop()

# A implementar:
## Contador de pontos na liga com max 20 jogos. Extra: fazer tabela de classificação com mais 10 equipas com os pontos delas a ser random. - Rocha
## Janela para visualizar a formação escolhida e permite trocar a formação a cada jogo. - Rebelo
## Fazer menu gestão dos jogadores da equipa com estatiticas e botão para melhorar o skill do jogador utilizando o saldo da equipa - Cristiano