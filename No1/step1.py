import numpy as np

class Variable:
	def __init__(self,data):
		self.data = data

data = np.array(1.0)
x = Variable(data)
print(x.data)
y = Variable(data)
y.data = np.array(2.0)
print(y.data)

