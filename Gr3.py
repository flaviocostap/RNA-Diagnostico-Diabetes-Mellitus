# -*- coding: utf-8 -*-

from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.structure import LinearLayer
from pybrain.structure import SigmoidLayer
from pybrain.datasets import SupervisedDataSet 
import matplotlib.pyplot as plt
from Tkinter import *
import numpy as np


n = buildNetwork(10,15,1, bias=True, hiddenclass=TanhLayer)
d = SupervisedDataSet(10,1)

X = np.random.randint(0, 2, (200, 10)).astype(np.float64)

def MSP(X):
	weight = np.array([2./10.5, 2./10.5, 2./10.5, 1./10.5, 1./10.5, 0.5/10.5, 0.5/10.5, 0.5/10.5, 0.5/10.5, 0.5/10.5])
	return np.dot(X, weight)

y = MSP(X)

for i in xrange(0,X.shape[0]):
	d.addSample(X[i,:], y[i])

tol_max = 1e-3
max_iter = 200
trainer = BackpropTrainer(n, d, learningrate = 1e-3, momentum=0.9)
erroDpc = []

iter_t = 0
while max_iter>0:
	tol = trainer.train()
	erroDpc.append(tol)
	max_iter -= 1
	print 'erro: ', tol
	if tol<=tol_max:
		break
	iter_t += 1	

print 'Responda com 1 para sim e 0 para não'
print iter_t 
q = np.zeros((1,10))
q[0,0] = int(raw_input('Você sente sede excessiva com frequência ?'))
q[0,1] = int(raw_input('Urina em grandes quantidades, cerca de 3,0 L por dia ?'))
q[0,2] = int(raw_input('Você tem reparado que está perdendo muito peso ultimamente ?'))
q[0,3] = int(raw_input('Você sente uma necessidade anormal de ingerir alimentos ?'))
q[0,4] = int(raw_input('Sua visão tem ficado turva ultimamente ?'))
q[0,5] = int(raw_input('Tem sentido tontura ultimamente ?'))
q[0,6] = int(raw_input('Tem se sentido muito cansaço ou fraqueza com frequência ?'))
q[0,7] = int(raw_input('Tem se sentido muitas dores de cabeça ?'))
q[0,8] = int(raw_input('Você fica doente com muita frequência ?'))
q[0,9] = int(raw_input('Você tem tido lesões nos membros inferiores que demoram a cicatrizar ?'))



print" Chance real", MSP(q)
print"predito", n.activate(q[0,:])
plt.plot(erroDpc)
plt.xlabel('Geracao')
plt.ylabel('Erro')
plt.title('Decaimento do erro')
plt.show()