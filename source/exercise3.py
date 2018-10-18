import networkx as nx
import dwave_networkx as dnx
import dimod

samplerSA = dimod.SimulatedAnnealingSampler()

G = nx.Graph()
G.add_edges_from([(1,2),(1,3),(2,3),(3,4),(3,5),(4,5),(4,6),(5,6),(6,7)])

s = 
