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

app = Tk()
app.title("Grupo 03 - Diabetes Mellitus")
app.geometry("810x800+200+200")

labelText = StringVar()
labelText.set("---- Configrações da RNA ----")
label = Label(app, textvariable=labelText, height=4)
label.pack()

Biaslabel = StringVar()
Biaslabel.set("Seleção de Bias:")
labelB = Label(app, textvariable=Biaslabel, height=4)
labelB.place(x = 20, y = 40)

b = True
print b

def checkBiasTrue():
    if(BiasTrue.get()):
       BiasFalse.set(0)
       b = True
       print b

def checkBiasFalse():
    if(BiasFalse.get()):
       BiasTrue.set(0)
       b = False
       print b

BiasTrue=IntVar()
checkbox_tb = Checkbutton(app, text='Com Bias', variable=BiasTrue, command=checkBiasTrue)
BiasFalse=IntVar()
checkbox_fb = Checkbutton(app, text='Sem Bias', variable=BiasFalse, command=checkBiasFalse)
checkbox_tb.place(x = 20, y = 80)
checkbox_fb.place(x = 20, y = 100)

Functionlabel = StringVar()
Functionlabel.set("Seleção de Função:")
labelF = Label(app, textvariable=Functionlabel, height=4)
labelF.place(x = 140, y = 40)

f=TanhLayer
print f

def checkFunctionTahn():
    if(Tahn.get()):
       Sigmoid.set(0)
       Linear.set(0)
       f=TanhLayer
       print f

def checkFunctionSig():
    if(Sigmoid.get()):
       Tahn.set(0)
       Linear.set(0)
       f=SigmoidLayer
       print f

def checkFunctionLin():
    if(Linear.get()):
       Sigmoid.set(0)
       Tahn.set(0)
       f=LinearLayer
       print f

Tahn=IntVar()
checkbox_tahn = Checkbutton(app, text='Tangente hiperbólica', variable=Tahn, command=checkFunctionTahn)
Sigmoid=IntVar()
checkbox_sig = Checkbutton(app, text='Sigmoide', variable=Sigmoid, command=checkFunctionSig)
Linear=IntVar()
checkbox_lin = Checkbutton(app, text='Linear', variable=Linear, command=checkFunctionLin)

checkbox_tahn.place(x = 140, y = 80)
checkbox_sig.place(x = 140, y = 100)  
checkbox_lin.place(x = 140, y = 120)

# ------- Variáveis de entrada
InterL=0

def getInterLayer():
  InterL=InterLayer.get()
  print InterL

LayerL = StringVar()
LayerL.set("Camadas Intermediárias:")
labelL = Label(app, textvariable=LayerL, height=4)
labelL.place(x = 320, y = 40)

InterLayer=IntVar()
InterLayerSelect=Entry(app, textvariable=InterLayer)
InterLayerSelect.place(x = 320, y = 80)

# --------
LRate=0 

def getLearnRate():
  LRate=LearnR.get()
  print LRate

LearnRate = StringVar()
LearnRate.set("Taxa de aprendizado:")
labelLR = Label(app, textvariable=LearnRate, height=4)
labelLR.place(x = 480, y = 40)

LearnR=DoubleVar()
LearnEntrySelect=Entry(app, textvariable=LearnR)
LearnEntrySelect.place(x = 480, y = 80)

# --------
beta=0 

def getMomentum():
  beta=Momentum.get()
  print beta

MomentumLayer = StringVar()
MomentumLayer.set("Momento:")
labelLR = Label(app, textvariable=MomentumLayer, height=4)
labelLR.place(x = 640, y = 40)

Momentum=DoubleVar()
MomentumEntry=Entry(app, textvariable=Momentum)
MomentumEntry.place(x = 640, y = 80)

# --------
Iter=0

def getMaxIter():
  Iter=IterMax.get()
  print Iter

IterLayer = StringVar()
IterLayer.set("Épocas:")
labelIL = Label(app, textvariable=IterLayer)
labelIL.place(x = 320, y = 120)

IterMax=DoubleVar()
ImaxEntry=Entry(app, textvariable=IterMax)
ImaxEntry.place(x = 320, y = 140)

# --------
erro=0

def getErro():
  erro=Tol.get()
  print erro

TolLayer = StringVar()
TolLayer.set("Erro:")
labelIL = Label(app, textvariable=TolLayer)
labelIL.place(x = 480, y = 120)

Tol=DoubleVar()
TolEntry=Entry(app, textvariable=Tol)
TolEntry.place(x = 480, y = 140)

n = buildNetwork(10,InterL,1, bias=b, hiddenclass=f)
d = SupervisedDataSet(10,1)
trainer = BackpropTrainer(n, d, learningrate = LRate, momentum=beta)
# --------------------------------------------------------------
# Perguntas

labelText = StringVar()
labelText.set("---- Questionário ----")
label = Label(app, textvariable=labelText, height=4)
label.place(x = 400, y = 200, anchor=CENTER)

Q1 = StringVar()
Q1.set("Você sente sede excessiva com frequência ?")
label1 = Label(app, textvariable=Q1, height=4)
label1.place(x = 20, y = 220)

def checkQ1t():
    if(Q1t.get()):
       Q1f.set(0)

def checkQ1f():
    if(Q1f.get()):
       Q1t.set(0)

Q1t=IntVar()
checkbox_Q1t = Checkbutton(app, text='Sim', variable=Q1t, command=checkQ1t)
Q1f=IntVar()
checkbox_Q1f = Checkbutton(app, text='Não', variable=Q1f, command=checkQ1f)
checkbox_Q1t.place(x = 20, y = 260)
checkbox_Q1f.place(x = 20, y = 280)

# -------

Q2 = StringVar()
Q2.set("Urina em grandes quantidades, cerca de 3,0 L por dia ?")
label1 = Label(app, textvariable=Q2, height=4)
label1.place(x = 20, y = 300)

def checkQ2t():
    if(Q2t.get()):
       Q2f.set(0)

def checkQ2f():
    if(Q2f.get()):
       Q2t.set(0)

Q2t=IntVar()
checkbox_Q2t = Checkbutton(app, text='Sim', variable=Q2t, command=checkQ2t)
Q2f=IntVar()
checkbox_Q2f = Checkbutton(app, text='Não', variable=Q2f, command=checkQ2f)
checkbox_Q2t.place(x = 20, y = 340)
checkbox_Q2f.place(x = 20, y = 360)

#--------

Q3 = StringVar()
Q3.set("Você sente uma necessidade anormal de ingerir alimentos ?")
label1 = Label(app, textvariable=Q3, height=4)
label1.place(x = 20, y = 380)

def checkQ3t():
    if(Q3t.get()):
       Q3f.set(0)

def checkQ3f():
    if(Q3f.get()):
       Q3t.set(0)

Q3t=IntVar()
checkbox_Q3t = Checkbutton(app, text='Sim', variable=Q3t, command=checkQ3t)
Q3f=IntVar()
checkbox_Q3f = Checkbutton(app, text='Não', variable=Q3f, command=checkQ3f)
checkbox_Q3t.place(x = 20, y = 420)
checkbox_Q3f.place(x = 20, y = 440)

#--------

Q4 = StringVar()
Q4.set("Você tem reparado que está perdendo muito peso ultimamente ?")
label1 = Label(app, textvariable=Q4, height=4)
label1.place(x = 20, y = 460)

def checkQ4t():
    if(Q4t.get()):
       Q4f.set(0)

def checkQ4f():
    if(Q4f.get()):
       Q4t.set(0)

Q4t=IntVar()
checkbox_Q4t = Checkbutton(app, text='Sim', variable=Q4t, command=checkQ4t)
Q4f=IntVar()
checkbox_Q4f = Checkbutton(app, text='Não', variable=Q4f, command=checkQ4f)
checkbox_Q4t.place(x = 20, y = 500)
checkbox_Q4f.place(x = 20, y = 520)

#--------

Q5 = StringVar()
Q5.set("Sua visão tem ficado turva ultimamente ?")
label1 = Label(app, textvariable=Q5, height=4)
label1.place(x = 20, y = 540)

def checkQ5t():
    if(Q5t.get()):
       Q5f.set(0)

def checkQ5f():
    if(Q5f.get()):
       Q5t.set(0)

Q5t=IntVar()
checkbox_Q5t = Checkbutton(app, text='Sim', variable=Q5t, command=checkQ5t)
Q5f=IntVar()
checkbox_Q5f = Checkbutton(app, text='Não', variable=Q5f, command=checkQ5f)
checkbox_Q5t.place(x = 20, y = 580)
checkbox_Q5f.place(x = 20, y = 600)


#--------

Q6 = StringVar()
Q6.set("Tem sentido tontura ultimamente ?")
label1 = Label(app, textvariable=Q6, height=4)
label1.place(x = 400, y = 220)

def checkQ6t():
    if(Q6t.get()):
       Q6f.set(0)

def checkQ6f():
    if(Q6f.get()):
       Q6t.set(0)

Q6t=IntVar()
checkbox_Q6t = Checkbutton(app, text='Sim', variable=Q6t, command=checkQ6t)
Q6f=IntVar()
checkbox_Q6f = Checkbutton(app, text='Não', variable=Q6f, command=checkQ6f)
checkbox_Q6t.place(x = 400, y = 260)
checkbox_Q6f.place(x = 400, y = 280)

#--------

Q7 = StringVar()
Q7.set("Tem se sentido muito cansaço ou fraqueza com frequência ?")
label1 = Label(app, textvariable=Q7, height=4)
label1.place(x = 400, y = 300)

def checkQ7t():
    if(Q7t.get()):
       Q7f.set(0)

def checkQ7f():
    if(Q7f.get()):
       Q7t.set(0)

Q7t=IntVar()
checkbox_Q7t = Checkbutton(app, text='Sim', variable=Q7t, command=checkQ7t)
Q7f=IntVar()
checkbox_Q7f = Checkbutton(app, text='Não', variable=Q7f, command=checkQ7f)
checkbox_Q7t.place(x = 400, y = 340)
checkbox_Q7f.place(x = 400, y = 360)

#--------

Q8 = StringVar()
Q8.set("Tem se sentido muitas dores de cabeça ?")
label1 = Label(app, textvariable=Q8, height=4)
label1.place(x = 400, y = 380)

def checkQ8t():
    if(Q8t.get()):
       Q8f.set(0)

def checkQ8f():
    if(Q8f.get()):
       Q8t.set(0)

Q8t=IntVar()
checkbox_Q8t = Checkbutton(app, text='Sim', variable=Q8t, command=checkQ8t)
Q8f=IntVar()
checkbox_Q8f = Checkbutton(app, text='Não', variable=Q8f, command=checkQ8f)
checkbox_Q8t.place(x = 400, y = 420)
checkbox_Q8f.place(x = 400, y = 440)

#--------

Q9 = StringVar()
Q9.set("Você fica doente com muita frequência ?")
label1 = Label(app, textvariable=Q9, height=4)
label1.place(x = 400, y = 460)

def checkQ9t():
    if(Q9t.get()):
       Q9f.set(0)

def checkQ9f():
    if(Q9f.get()):
       Q9t.set(0)

Q9t=IntVar()
checkbox_Q9t = Checkbutton(app, text='Sim', variable=Q9t, command=checkQ9t)
Q9f=IntVar()
checkbox_Q9f = Checkbutton(app, text='Não', variable=Q9f, command=checkQ9f)
checkbox_Q9t.place(x = 400, y = 500)
checkbox_Q9f.place(x = 400, y = 520)

#--------

Q10 = StringVar()
Q10.set("Você tem tido lesões nos membros inferiores que demoram a cicatrizar ?")
label1 = Label(app, textvariable=Q10, height=4)
label1.place(x = 400, y = 540)

def checkQ10t():
    if(Q10t.get()):
       Q10f.set(0)

def checkQ10f():
    if(Q10f.get()):
       Q10t.set(0)

Q10t=IntVar()
checkbox_Q10t = Checkbutton(app, text='Sim', variable=Q10t, command=checkQ10t)
Q10f=IntVar()
checkbox_Q10f = Checkbutton(app, text='Não', variable=Q10f, command=checkQ10f)
checkbox_Q10t.place(x = 400, y = 580)
checkbox_Q10f.place(x = 400, y = 600)

#-------------------------------------------------

Treinar = Button(app, text="Começar Treinamento", command=getErro)
Treinar.place(x = 400, y = 680, anchor=CENTER)

app.mainloop()
