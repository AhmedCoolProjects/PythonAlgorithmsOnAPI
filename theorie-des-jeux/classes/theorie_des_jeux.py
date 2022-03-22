class TheorieDesJeux():
    def __init__(self,my_input,my_input_proba,my_alpha):
        self.my_input = my_input
        self.my_input_proba = my_input_proba
        self.my_alpha = my_alpha
        self.nb_etats = len(my_input[list(my_input.keys())[0]])
    def getKeys(self):
        return list(self.my_input.keys())
    def vnm(self):
        final_result = {}
        # return a list of utilities for each action
        for my_key in self.getKeys():
            final_result[my_key] = 0
            for i in range(self.nb_etats):
                final_result[my_key] += self.my_input_proba[i] * self.my_input[my_key][i]
        return {"details":final_result,"answer":max(final_result, key = final_result.get)}
    def laplace(self):
        final_result = {}
        for my_key in self.getKeys():
            final_result[my_key] = sum(self.my_input[my_key])/self.nb_etats
        return {"details":final_result,"answer":max(final_result, key = final_result.get)}
    def maximax(self):
        final_result = {}
        for my_key in self.getKeys():
            final_result[my_key] = max(self.my_input[my_key])
        return {"details":final_result,"answer":max(final_result, key = final_result.get)}
    def waldMaxmin(self):
        final_result = {}
        for my_key in self.getKeys():
            final_result[my_key] = min(self.my_input[my_key])
        return {"details":final_result,"answer":max(final_result, key = final_result.get)}
    def hurwicz(self):
        final_result = {}
        for my_key in self.getKeys():
            final_result[my_key] = self.my_alpha * min(self.my_input[my_key]) + (1 - self.my_alpha) * max(self.my_input[my_key])
        return {"details":final_result,"answer":max(final_result, key = final_result.get)}
    def getRegretMatrix(self):
        my_regret_matrix = self.my_input.copy()
        for i in range(self.nb_etats):
            max_action = max([self.my_input[my_key][i] for my_key in self.getKeys()])
            for my_key in self.getKeys():
                my_regret_matrix[my_key][i] = max_action - self.my_input[my_key][i]
        return my_regret_matrix
    def savageRegretMinimax(self):
        my_regret_matrix = self.getRegretMatrix()
        final_result = {}
        for my_key in self.getKeys():
            final_result[my_key] = max(my_regret_matrix[my_key])
        return {"details":final_result,"answer":min(final_result, key = final_result.get)}
