class Agent:
    def __init__(self, number, actions):
        self.number = number
        self.actions = actions

class Player(Agent):
    def __init__(self, number, actions, payoff, state, history, gamma, epsilon, alpha):
        super().__init__(number, actions)
        self.payoff = payoff
        self.state = state
        self.history = history
        self.gamma = gamma
        self.epsilon = epsilon
        self.alpha = alpha
        
        payoff_diff = [[] for alt_action in range(len(actions))]
        for old_action in range(len(actions)):
            payoff_diff[old_action] = [[] for alt_action in range(len(actions))]
        
        self.payoff_diff = payoff_diff

    def regret(self, old_action, alt_action):
        # payoff_diffs[player, old_action, alt_action] is an array of the difference
        # in utilities player would have gotten in the past by playing alt_action
        # wherever they actually played old_action
        return max(0, sum(self.payoff_diff[old_action][alt_action])/len(self.history))

    def replace_at_index(self, tup, index, val):
        return tup[:index] + (val,) + tup[index + 1:]

    def update_payoff_diffs(self, action_tuple):
        # payoff_diffs[player, old_action, alt_action] is an array of the difference
        # in utilities player would have gotten in the past by playing alt_action
        # wherever they actually played old_action
        old_action = action_tuple[self.number]
        old_payoff = self.payoff[action_tuple]
        for alt_action in range(len(self.actions)):
            alt_action_tuple = self.replace_at_index(action_tuple, self.number, alt_action)
            alt_payoff = self.payoff[alt_action_tuple]
            self.payoff_diff[old_action][alt_action].append(alt_payoff- old_payoff)

    def prob_next_action(self, last_action):
        regret_array = [self.regret(last_action, alt_action) for alt_action in self.actions]
        #assert regret_array[last_action] == 0, "your regret isn't zero when it should obviously be"
        normalisation_const = 2 * len(self.actions) * np.amax(self.payoff)
        probs_array = [regret / normalisation_const for regret in regret_array]
        prob_last_action = 1 - sum(probs_array)
        probs_array[last_action] = prob_last_action
        return probs_array

    def updateState(self):
        self.update_payoff_diffs(self.history[-1])
        old_action = self.history[-1][self.number]
        current_regret_array = [self.regret(old_action, alt_action) for alt_action in self.actions]
        regret_matrix = [[self.regret(old_action, alt_action) for alt_action in self.actions] for old_action in self.actions]
        max_R = np.amax(regret_matrix)
           
        if self.state == 'asyn':
            if epsilon**(max_R) > random.random():
                self.state = 'syn'
            else:
                self.state = 'asyn'
        else:
            if epsilon**(gamma) > random.random():
                self.state = 'syn'
            else:
                if  max_R <= self.alpha:
                    self.state = 'syn'
                else:
                    self.state = 'asyn'
                    
    def updatehistory(self, profile):
        self.history.append(profile)
        
    def play(self):
        prob_matrix = np.zeros((len(self.actions), len(self.actions)))
        old_action = self.history[-1][self.number]
        prob_matrix[old_action] = self.prob_next_action(old_action)
        
        for alt_action in self.actions:
            if alt_action != old_action:
                prob_matrix[alt_action] = self.prob_next_action(alt_action)

        mc = qe.MarkovChain(prob_matrix)
        mc.stationary_distributions
        next_action = np.random.choice(self.actions, p = mc.stationary_distributions[0])
        return next_action
