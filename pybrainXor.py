from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.structure import LinearLayer
from pybrain.structure import SigmoidLayer
from pybrain.datasets import SupervisedDataSet 
import matplotlib.pyplot as plt
from Tkinter import *
import numpy as np
# b = raw_input('bias: (true/false): ')

n = buildNetwork(2,4,1, bias=True, hiddenclass=TanhLayer)
d = SupervisedDataSet(2,1)
# d.addSample([0, 0], [0])
# d.addSample([0, 1], [1])
# d.addSample([1, 0], [1])
# d.addSample([1, 1], [0])
X = np.array([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y = np.array([0., 1., 1., 0.])

for i in xrange(0,4):
	d.addSample(X[i,:], y[i])

tol_max = 1e-3
max_iter = 1000
trainer = BackpropTrainer(n, d, learningrate = 1e-3, momentum=0.9)
erroDpc = []

iter_t = 0
while max_iter>0:
	tol = trainer.train()
	erroDpc.append(tol)
	max_iter -= 1

	if tol<=tol_max:
		break
	iter_t += 1	

print n.activate([0,0])
print n.activate([0,1])
print n.activate([1,0])
print n.activate([1,1])

print iter_t 
plt.plot(erroDpc)
plt.xlabel('Geracao')
plt.ylabel('Erro')
plt.title('Decaimento do erro')
plt.show()