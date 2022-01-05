class Game:
    def __init__(self, history, epsilon):
        self.players = []
        self.history = history
        self.epsilon = epsilon
        self.distribution = {}
        self.iterations = 0
        
    def add_player(self, player):
        self.players.append(player)
    
    def update_empirical_distribution(self):
        if self.history[-1] in self.distribution:
            self.distribution[self.history[-1]] = self.distribution[self.history[-1]] + 1 
        else:
            self.distribution[self.history[-1]] = 1

    def runGame(self):
        payoffs = [self.players[k].payoff for k in range(len(self.players))]
        self.iterations = int((2*np.amax(payoffs))/(self.epsilon**2))
        print('iterations', self.iterations)
        for t in tqdm(range(self.iterations)):
            self.update_empirical_distribution()
            
            profiles = list(self.distribution.keys())
            #print('profiles ', profiles)
            probabilities  = np.multiply(list(self.distribution.values()), 1/(t+1))
            #print('probabilities ', probabilities)
            recommendation = np.random.choice(len(profiles), p = probabilities)
            #print('recommendation ', recommendation)            
            for i in range(len(self.players)):
                player = self.players[i]
                player.update_payoff_diffs(self.history[-1])

            next_actions = []
                
            for i in range(len(self.players)):
                player = self.players[i]
                next_action = player.play()
                
                #next_action = profiles[recommendation][player.number]
                next_actions.append(next_action)
            self.history.append(tuple(next_actions))
            #print('Actions ', tuple(next_actions))

    def getResults(self):
        p = []
        distribution = {}
        n, m = np.shape(self.players[0].payoff)
        for i in range(n):
            for j in range(m):
                distribution[(i,j)] = 0
        for i in tqdm(range(0, self.iterations)):
            profile = self.history[i]
            distribution[profile] = distribution[profile] + 1
            p.append(np.multiply(list(distribution.values()), 1/(i+1)))
        p = np.array(p)
        x = [r for r in range(0, self.iterations)]

        fig = plt.figure(figsize=(13, 6))
        ax = fig.add_subplot(111)

        ax.set(ylim=(-0.1, 1.1))

        for k in range(len(list(distribution.values()))):
            ax.plot(x, p[:,k])

        print('###########################################################################')
        print('##### Correlated epsilon-equilibrium probability distribution reached #####')
        print('###########################################################################')
        probas = np.multiply(list(distribution.values()), 1/(self.iterations))
        profiles = list(distribution.keys())
        print(tabulate([[profiles[k], probas[k]] for k in range(len(distribution))], headers=['Profiles', 'Probabilities']))
    
        ax.legend()        
        plt.xlabel("Iterations")
        plt.ylabel("Probabilities of action profiles")
