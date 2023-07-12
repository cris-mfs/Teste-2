import tkinter as tk
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.league = 4

class resultado_partida:
    def __init__(self, team1, team2, winner):
        self.team1 = team1
        self.team2 = team2
        self.winner = winner

class FootballSimulator:
    def __init__(self):
        self.teams = []
        self.current_team = None
        self.opponent_team = None
        self.match_results = []
        self.window = tk.Tk()
        self.create_gui()

    def create_gui(self):
        self.window.title("Football Simulator")

        # Create team name input
        self.team_name_label = tk.Label(self.window, text="Team Name:")
        self.team_name_label.pack()
        self.team_name_entry = tk.Entry(self.window)
        self.team_name_entry.pack()
        self.create_team_button = tk.Button(self.window, text="Create Team", command=self.create_team)
        self.create_team_button.pack()

        # Simulate game button
        self.simulate_game_button = tk.Button(self.window, text="Simulate Game", command=self.simulate_game)
        self.simulate_game_button.pack()

        # Result label
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        # Match history label
        self.match_history_label = tk.Label(self.window, text="Match History:\n")
        self.match_history_label.pack()

    def create_team(self):
        name = self.team_name_entry.get()
        if name:
            team = Team(name)
            self.teams.append(team)
            self.current_team = team
            self.team_name_entry.delete(0, tk.END)
            print("Team created:", name)

    def simulate_game(self):
        if not self.teams:
            print("No teams created yet.")
            return

        self.opponent_team = random.choice(self.teams)
        result = random.choice(["win", "draw", "loss"])
        if result == "win":
            self.current_team.wins += 1
            if self.current_team.wins == 6:
                self.current_team.league = 3
            elif self.current_team.wins == 13:
                self.current_team.league = 2
            elif self.current_team.wins == 21:
                self.current_team.league = 1

        match_result = resultado_partida(self.current_team.name, self.opponent_team.name, self.current_team.name)
        self.match_results.append(match_result)

        result_text = "Simulation result: {}\nTeam: {}\nOpponent: {}\nWins: {}\nLeague: {}".format(
            result, self.current_team.name, self.opponent_team.name, self.current_team.wins, self.current_team.league
        )
        self.result_label.config(text=result_text)

        self.update_match_history()

    def update_match_history(self):
        history_text = "Match History:\n"
        for result in self.match_results:
            history_text += "Team {}: {} vs. Team {}: {}\n".format(result.team1, result.team2, result.winner, "Won")

        self.match_history_label.config(text=history_text)

simulator = FootballSimulator()
simulator.window.mainloop()