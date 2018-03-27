import random as r
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl


k = int(input("Enter number of clusters : ")) #Number of clusters
epochs = int(input("Enter number of epochs : "))
ipf = int(input("How would you like your points?\n1. Random gen\n2. CSV File \n3. Type in the points yourself\nTell me : "))
if ipf not in [1,2,3]:
    print("Invalid choice")
    exit()
points = []
if ipf is 1:
    for i in range(900):
        x = r.random()*100
        y = r.random()*100
        points.append([x, y])
elif ipf is 2:
    f_name = input("Enter file name : ")
    with open(f_name, 'r') as f:
        for line in f:
            line = line.strip()
            x, y = map(int, line.split(','))
            points.append([x, y])
elif ipf is 3:
    n = input("Enter number of points : ")
    for i in range(n):
        x = float(input("Enter x coordinate of point "+str(i)+" : "))
        y = float(input("Enter y coordinate of point " + str(i) + " : "))
        points.append([x, y])

if k > len(points):
    print("Too many clusters!")
    exit()
c = []
clusters = []
colors = pl.cm.jet(np.linspace(0,1,k))



def dist(p1,p2):
    return ((p1[0]- p2[0])**2 + (p1[1]-p2[1])**2)**0.5


def get_cluster(c, k, points):
    clusters = [[] for i in range(k)]
    for p in points :
        d = []
        for i in range(k):
            d.append(dist(p,c[i]))

        min_index = 0
        for i in range(k):
            if d[min_index] > d[i] :
                min_index = i
        clusters[min_index].append(p)
    return clusters


def cluster_mean(cluster):
    x,y = 0,0
    for a,b in cluster:
        x += a
        y += b
    x /= len(cluster)
    y /= len(cluster)
    return [x,y]

for i in range(k):
    choice = r.choice(points)
    while choice in c:
        choice = r.choice(points)
    c.append(r.choice(points))

clusters = get_cluster(c, k, points)
print("Start")
print(c)
for i in clusters:
    print(i)
print()

for i in range(epochs):
    for i in range(k):
        c[i] = cluster_mean(clusters[i])
    clusters = get_cluster(c, k, points)

print("Finish")
print(c)
for i in clusters:
    print(i)

for i in range(k):
    if clusters[i]:
        plt.scatter(*zip(*clusters[i]), color=colors[i])
plt.show()
