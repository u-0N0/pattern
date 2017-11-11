import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def init_data(filename):
    
    df = pd.read_csv(filename, header=None)
    df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']
    df = df.query("horsepower != '?'")
    df.index = range(len(df))
    df.loc[:,'horsepower'] = df.loc[:,'horsepower'].astype('float')

    x = np.array([np.ones(len(df)), df.weight, df.horsepower]).T
    t = np.array(df.mpg).T
    
    return x, t

def analyze(x, t):
    
    pinv_x = np.linalg.pinv(x)
    w = np.dot(pinv_x, t)

    return w

def main():

    x, t = init_data('auto-mpg.csv')
    w = analyze(x, t)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel('weight')
    ax.set_ylabel('horsepower')
    ax.set_zlabel('mpg')

    ax.scatter(x[:,1], x[:,2], t)

    step1 = (np.max(x[:,1])-np.min(x[:,1]))/20
    step2 = (np.max(x[:,2])-np.min(x[:,2]))/20
    x1 = np.arange(np.min(x[:,1]), np.max(x[:,1]), step1)
    x2 = np.arange(np.min(x[:,2]), np.max(x[:,2]), step2)
    X1, X2 = np.meshgrid(x1, x2)
    Y = w[0] + w[1]*X1 + w[2]*X2

    ax.plot_wireframe(X1, X2, Y)
    
    plt.show()

main()
