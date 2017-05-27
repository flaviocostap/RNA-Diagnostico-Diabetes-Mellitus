from sklearn.neural_network import MLPRegressor
import numpy as np

mlp = MLPRegressor(verbose=True, max_iter=200) 
X = np.array([[0.,0.], [0.,1.],[1.,0.],[1.,1.]])
y = np.array([0.,1.,1.,0.])

mlp.fit(X,y)

print "Score: ", mlp.score(X, y)

m = mlp.predict(X)
for i in xrange(4):
    print X[i], ":", m[i]