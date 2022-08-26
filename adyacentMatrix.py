import networkx as nx

# Pandas
import pandas as pd

# Mathplotlib
import matplotlib.pyplot as plt

#  
plt.rcParams['figure.figsize'] = (20.0, 10.0)

spain_flights = pd.read_csv("Grafo.csv")
spain_flights.head()
        
DG=nx.DiGraph()

DG.add_node(0)
DG.add_node(1)
DG.add_node(2)
DG.add_node(3)
DG.add_node(4)
DG.add_node(5)
DG.add_node(6)
DG.add_node(7)
DG.add_node(8)

for row in spain_flights.iterrows():
    DG.add_edge(row[1]["Origen"],
                row[1]["Destino"])

DG.nodes(data=True)
list(DG.nodes(data=True))
B=nx.adjacency_matrix(DG)
B1=B.todense()
B1=B1-1

#Set goal to 100
goal = 4
i = 0
for row in B1:
    if(row[0, goal] == 0):
        row[0, goal] = 100
    i += 1

print(B1)