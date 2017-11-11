import random
import matplotlib.pyplot as plt
import numpy as np

def main():

    #initialize dataset
    dataset = []
    features = init_data(dataset) 

    #plot each cluster and center
    fig = plt.figure()
    colors = ['r', 'b', 'g', 'c', 'y']
    for k in range(2, 6):
        clusters, centers = k_means(k, features) #k-means clustering
        ax = fig.add_subplot(2, 2, k-1)
        ax.set_xlabel('petal length')
        ax.set_ylabel('petal width')
        ax.set_title('k = {}'.format(k))
        for k_ in range(k): 
            labels = np.array(clusters[k_])
            center = np.array(centers[k_])
            ax.scatter(labels[:, 0], labels[:, 2], c = colors[k_])
            ax.scatter(center[0], center[2], c = 'white', s = 60)

    #coordinate, show, and save the figure
    fig.tight_layout() 
    plt.show()
    fig.savefig('sepallength-petallength.png')
       
def init_data(dataset):

    f = open('iris.dat', 'r')
    for line in f:
        dataset.append(line.strip().split(",")[:-1])
    f.close

    for data in dataset:
        for i in range(4):
            data[i] = float(data[i])

    return dataset
    
def k_means(k, features):

    #select the initial centroids of k clusters at random
    centers = []
    centers.append(random.sample(features, k)) 

    diff = 1
    
    clusters = []
    while(diff > 0.001):
        
        clusters.append([])
        for i in range(k):
            clusters[-1].append([])

        #x is an element of cluster-k,
        #where k is the argmin of the distance between x and a centroid.
        for x in features:
            k_ = argmin(x, centers[-1], k)
            clusters[-1][k_].append(x)

        #update the centroids
        update_centers(features, clusters[-1], centers, k)

        #use for the convergence test
        diff = assess(centers[-1], centers[-2])
        
    return [clusters[-1], centers[-1]]

def argmin(x, cc, k):
    
    d_list = []
    for k_ in range(k):
        d_list.append([dist(x, cc[k_]), k_])

    d_list = sorted(d_list, key=lambda x: x[0])
    k_ = d_list[0][1]
        
    return k_
    
def update_centers(features, clusters, centers, k):

    centers.append([])
    
    for k_ in range(k):
        nc = np.array([0., 0., 0., 0.])
        for x in clusters[k_]:
            x_ = np.array(x)
            nc += x_
        nc /= len(clusters[k_])
        centers[-1].append(nc.tolist())
        
def assess(cc, pc):

    diff = 0
    for k_ in range(len(cc)):
        diff += dist(cc[k_], pc[k_])

    return diff

def dist(x1, x2):
    
    d = 0
    for i in range(4):
        d += (x1[i]-x2[i])**2
    return d
    
main()
