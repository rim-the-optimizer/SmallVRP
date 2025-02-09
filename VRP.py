!pip install vrpy
import numpy as np
import networkx as nx
from networkx import DiGraph
import vrpy as vrpy
from vrpy import VehicleRoutingProblem
import matplotlib.pyplot as plt

"""Problem aufbauen"""
G=DiGraph()
G.add_edge("Source", 1, cost=1)
G.add_edge("Source", 2, cost=2)
G.add_edge(1, "Sink", cost=0)
G.add_edge(2, 1, cost=1)
G.nodes[1]["demand"]=5
G.nodes[2]["demand"]=4
"""Alle Kanten, Knoten und Nachfrage aufgebaut"""

"""Berechnung"""
prob= VehicleRoutingProblem(G, load_capacity=10)
prob.solve()

"""Ergebnis der Berechnung"""
R=prob.best_routes
print(R)
print(prob.best_routes_load)
"""gewählte Knoten und Ladung ausgegeben"""

"""Umformen der Kantenliste in Knotenpäärchen"""
Routes=R[1]
Rou2=Routes.copy()
Rou2=Rou2[1:-1]
print(Rou2)
posi=[]
for i in Rou2:
    a=Routes.index(i)
    posi.append(a)
for j,l in zip(posi,Rou2):
    Routes.insert(j*2,l)
print(Routes)
Kanten=int(len(R[1])/2)
Routes=np.reshape(Routes,(Kanten,2))
Routes=Routes.tolist()
print( Routes)

"""Kantenliste Routes vorbereitet"""

"""Plotten des Graphes und des Ergebnisses"""
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=200)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=[("Source",2),(2,1),(1, "Sink")], edge_color='r', arrows=True)
plt.show()
