class ObstacleGroup:
    def __init__(self):
        self.obstacles = {}
        self.obstacleCount = 0
        
    #def __init__(self,obstacles):
    #    self.obstacles = obstacles
    #    self.obstacleCount = len(a)
        
    def add(self,obstacle):
        self.obstacles[self.obstacleCount] = obstacle
        self.obstacleCount = self.obstacleCount + 1    