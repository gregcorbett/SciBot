import pickle

class Scenario:
	def __init__(self,name):
		self.name = name
		self.background = None
		
	def setBackground(self,input):
		self.background = input
		
	def writeToFile(self):
		pickle.dump( self, open( "./scenarios/"+ self.name +".scibot", "wb" ) )