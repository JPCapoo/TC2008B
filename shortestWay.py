 #8/15/2022
# Networkx para grafos
import networkx as nx

# Pandas
import pandas as pd

# Mostrar imágenes
from IPython.display import HTML

# Mathplotlib
import matplotlib.pyplot as plt

rutas = pd.read_csv("Ejemplo.csv")
rutas.head()
  
  
DG=nx.DiGraph()
for row in rutas.iterrows():
    DG.add_edge(row[1]["Origen"],
                row[1]["Destino"],
                duration=row[1]["Costo"])
    nx.draw_circular(DG,
                 node_color="lightblue",
                 edge_color="gray",
                 font_size=24,
                 width=2, with_labels=True, node_size=3500,
)
list(nx.dijkstra_path(DG, source="0", target="2", weight="Costo"))  

def show_path(path):
    total_price = 0
   
    
    for i in range(len(path)-1):
        origin = path[i]
        destination = path[i+1]
      
        price = DG[origin][destination]["Costo"]
        
        total_price = total_price+price
        
        print("    %s -> %s\n    - Price: %s €" % (
            rutas.loc[origin]["name"],
            rutas.loc[destination]["name"],
            price)
        )
    
    print("\n     Total Duration: %s Total price: %s € \n" % (
            total_duration, total_price)
    )