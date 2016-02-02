import pickle
import pygame
from src.Obstacle import *
from src.ObstacleGroup import *
from src.Goal import *
from src.GoalGroup import *

class Scenario():

    def __init__(self,name):

        self.elements = {}
        self.elements['Name'] = name

    def get_element(self,key):

        if key not in self.elements:
            return None

        switcher = {
            'Name': self.get_name(),
            'BoardStep': self.get_board_step(),
            'LogicalWidth': self.get_logical_width(),
            'LogicalHeight': self.get_logical_height(),
            'Background': self.get_background(),
            'BorderColour': self.get_border_colour(),
            'BeeBotSprite': self.get_beebot_sprite(),
            'BeeBotStartPosition': self.get_beebot_start_position(),
            'BeeBotHeading': self.get_beebot_heading(),
            'ObstacleGroup': self.get_obstacle_group(),
            'ObstacleCount': self.get_obstacle_count(),
            'GoalGroup': self.get_goal_group(),
            'goal_count': self.get_goal_count(),
            'BeeBotFailSprite': self.get_beebot_fail_sprite(),
        }

        return switcher.get(key)

    def get_obstacle_count(self):
        return self.elements['ObstacleCount']

    def get_goal_count(self):
        return self.elements['goal_count']

    def set_beebot_fail_sprite(self,inputString):
        input = pygame.image.load(inputString)
        self.elements['BeeBotFailSprite'] = self.format_surface_for_pickle(input)

    def get_beebot_fail_sprite(self):
        return self.format_pickle_to_surface(self.elements['BeeBotFailSprite'])

    def add_goal(self,x,y,sprite=None):

        if 'GoalGroup' not in self.elements:
            self.elements['GoalGroup'] = {}
            self.elements['goal_count'] = 0

        if sprite != None:
            sprite = pygame.image.load(sprite)
            sprite = self.format_surface_for_pickle(sprite)

        self.elements['GoalGroup'][self.elements['goal_count']] = (sprite,x,y)
        self.elements['goal_count'] = self.elements['goal_count'] + 1

    def get_goal_group(self):
        goalGroup = GoalGroup()
        goalPtr = 0
        while goalPtr < self.elements['goal_count']:
            pickledGoal = self.elements['GoalGroup'][goalPtr]
            goalGroup.add(Goal(self.format_pickle_to_surface(pickledGoal[0]),pickledGoal[1],pickledGoal[2],self.elements['BoardStep']))
            goalPtr = goalPtr + 1
        return goalGroup

    def add_obstacle(self,x,y,sprite=None):

        if 'ObstacleGroup' not in self.elements:
            self.elements['ObstacleGroup'] = {}
            self.elements['ObstacleCount'] = 0

        if sprite != None:
            sprite = pygame.image.load(sprite)
            sprite = self.format_surface_for_pickle(sprite)
        self.elements['ObstacleGroup'][self.elements['ObstacleCount']] = (sprite,x,y)
        self.elements['ObstacleCount'] = self.elements['ObstacleCount'] + 1

    def get_obstacle_group(self):
        obstacleGroup = ObstacleGroup()
        obsPtr = 0
        while obsPtr < self.elements['ObstacleCount']:
            pickledObs = self.elements['ObstacleGroup'][obsPtr]
            obstacleGroup.add(Obstacle(self.format_pickle_to_surface(pickledObs[0]),pickledObs[1],pickledObs[2],self.elements['BoardStep']))
            obsPtr = obsPtr + 1
        return obstacleGroup

    def set_beebot_heading(self,input):
        self.elements['BeeBotHeading'] = input

    def get_beebot_heading(self):
        return self.elements['BeeBotHeading']

    def set_beebot_sprite(self,inputString):
        input = pygame.image.load(inputString)
        self.elements['BeeBotSprite'] = self.format_surface_for_pickle(input)

    def get_beebot_sprite(self):
        return self.format_pickle_to_surface(self.elements['BeeBotSprite'])

    def get_beebot_start_position(self):
        return self.elements['BeeBotStartPosition']

    def set_beebot_start_position(self,x,y):
        self.elements['BeeBotStartPosition'] = (x,y)

    def get_logical_height(self):
        return self.elements['LogicalHeight']

    def get_logical_width(self):
        return self.elements['LogicalWidth']

    def set_logical_height(self,input):
        self.elements['LogicalHeight'] = input

    def set_logical_width(self,input):
        self.elements['LogicalWidth'] = input

    def get_board_step(self):
        return self.elements['BoardStep']

    def set_board_step(self,input):
        self.elements['BoardStep'] = input

    def format_pickle_to_surface(self,input):
        if input == None:
            return None
        return pygame.image.fromstring(input['image'],input['size'],input['format'])

    def format_surface_for_pickle(self,input):
        if input == None:
            return None
        return {'image': pygame.image.tostring(input,"RGBA"), 'size': input.get_size(), 'format': "RGBA"}

    def set_background(self,inputString):
        input = pygame.image.load(inputString)
        self.elements['Background'] = self.format_surface_for_pickle(input)

    def get_background(self):
        return self.format_pickle_to_surface(self.elements['Background'])

    def set_border_colour(self,input):
        self.elements['BorderColour'] = input

    def get_border_colour(self):
        return self.elements['BorderColour']

    def get_name(self):
        return self.elements['Name']

    def write_to_file(self):
        pickle.dump( self, open( "./scenarios/"+ self.elements['Name'] +".scibot", "wb" ) )
