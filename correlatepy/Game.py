class Game:
    def __init__(self, iterations, history, gamma, epsilon, alpha):
        self.players = []
        self.iterations = iterations
        self.history = history
        self.gamma = gamma
        self.epsilon = epsilon
        self.alpha = alpha
        self.distribution = {}
        
    def add_player(self, player):
        self.players.append(player)
    
    def update_empirical_distribution(self):
        if self.history[-1] in self.distribution:
            self.distribution[self.history[-1]] = self.distribution[self.history[-1]] + 1 
        else:
            self.distribution[self.history[-1]] = 1

#    def runGame(self):
