import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices (greater than 3): "))

if n > 3:
   
    G = nx.complete_graph(n)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True,
            node_color='lightgreen',
            node_size=800,
            edge_color='black')

    plt.title(f"Complete Graph with {n} Vertices")
    plt.show()
else:
    print("Number of vertices must be greater than 3.")
