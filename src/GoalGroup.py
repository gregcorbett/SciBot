class GoalGroup:
    def __init__(self):
        self.goals = {}
        self.goalCount = 0
        self.goalPtr = 0
        
    def add(self,goal):
        self.goals[self.goalCount] = goal
        self.goalCount = self.goalCount + 1
        
    def display(self,screen):
        if self.goalPtr < self.goalCount:
            self.goals[self.goalPtr].display(screen)