"author : Mehul Bafna"

from itertools import combinations
from collections import Counter
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import json
import math

class Polynomials:
    
    def __init__(self,graph):
        self.graph = graph
    
    # Function for computing neighbourhood of vertex subsets of the vertex set   
    def neighborhood(vertices,edges):
        M = []
        for vertex in vertices:
            L = []
            for edge in edges:
                if vertex in edge:
                    L.append(edge[0])
                    L.append(edge[1])
                    M.append((vertex,L))
            neighbors = []
                    
        for i in M:
            i[1].sort()
            neighbors.append((i[0],list(Counter(i[1]))))
        return dict(neighbors)
            
    #For computing proper subsets of a set
    def proper_subset(a,b):
        if a.issubset(b):
            if len(a)!=len(b):
                return True
            else:
                return False
        else:
            return False
        
        #For computing independence polynomial of null graph, empty graph and simple connected graph
    def ind_poly(self):
        
    
        vertices = []
        edges = []
        
        # For creating a list of vertices and edges
        for node,neighbors in self.graph.items():
            for i in range(0,len(neighbors)):
                if {node,neighbors[i]} not in edges and {neighbors[i],node} not in edges:
                    edges.append({node,neighbors[i]})       
            vertices.append(node) 
            
        # Sorting the vertex set in descending order   
        vertices.sort()
        vertices.reverse()
        
        if len(edges)==0:
            #For Null Graph
            if len(vertices)==1:
                if vertices == ['']:
                    print('\n Independent sets for the graph G is/are - ','\u03A6','\n')
                    print('1 is the Independence Polynomial for the graph G')
                    G = nx.Graph()
                    G.add_nodes_from(vertices)
                    G.add_edges_from(edges)
                    nx.draw(G,with_labels=True)
                    plt.title('G = (V,E)')
                    plt.show
                    return '\n Independence number \u03B1(G) is zero'
                #For empty graph with one vertex
                else:
                    G = nx.Graph()
                    G.add_nodes_from(vertices)
                    G.add_edges_from(edges)
                    nx.draw(G,with_labels=True)
                    plt.title('G = (V,E)')
                    plt.show
                    #For Empty Graph with one vertex
                    L = [0]*(len(vertices))
                    L.append(1)
                    L.reverse()
                    print('\nIndependent sets for the graph G are- ','\u03A6 and ',set(str(vertices[0])),'\n')
                    print('1+x is the Independence Polynomial for the graph G')
                    return '\n Independence number \u03B1(G) is 1'
            #For Empty Graphs with more than one vertex
            else:
                L = [0]*(len(vertices)+1)
                for i in range(0,len(vertices)+1):
                    L[i]=math.comb(len(vertices),i)
                Indep_sets = []
                for i in range(0,len(vertices)+1):
                    Indep_sets.append(list(combinations(vertices,i)))
                Indepe_sets = []
                for i in Indep_sets:
                    for j in i:
                        Indepe_sets.append(set(j))
                print('\n Independent sets for the graph G is/are - ',Indepe_sets,'\n')
                print(np.poly1d(L),' is the Independence Polynomial for the graph G')
                G = nx.Graph()
                G.add_nodes_from(vertices)
                G.add_edges_from(edges)
                nx.draw(G,with_labels=True)
                plt.title('G = (V,E)')
                plt.show
                return '\n Independence number \u03B1(G) is '+str(len(vertices))
        #For simple connected graphs
        else:
            # Creating a powerset of vertex set in form of nested list tuples
            power_set_list = []
            for i in range(0,len(vertices)+1):
                power_set_list.append(list(combinations(vertices,i)))
              
            # For fetching the tuples and storing in a list from the above nested list power_set_list
            power_set = []
            for i in power_set_list:
                for j in i:
                    power_set.append(set(j))
                    
            ind_set = []        
            for i in power_set[0:1+len(vertices)+int(len(vertices)*(len(vertices)-1)/2)]:
                if i not in edges:
                    ind_set.append(i)
            
            #Computation of independent sets along with computation of independence polynomial        
            ind = []
            ind.append(1)
            ind.append(len(vertices))
            ind.append(int(len(vertices)*(len(vertices)-1)/2)-len(edges))
            
            for i in range(3,len(vertices)):
                m = 0
                for Set in power_set[1+len(vertices)+int(len(vertices)*(len(vertices)-1)/2):len(power_set)]:
                    count = 0
                    for edge in edges:
                        if Polynomials.proper_subset(edge,Set)==False:
                            count+=1
                            continue
                        else:
                            count = 0
                            break
                    if count == len(edges):
                        if len(Set)==i:
                            ind_set.append(Set)
                            m+=1
                if m>0:
                    ind.append(m)  
            Ind = ind
            ind.reverse()
            
            
            print('\n Independent sets for the graph G is/are - ',ind_set,'\n')
            print(np.poly1d(ind),' is the Independence Polynomial for the graph G')
            
            #For drawing the original graph with vertex and edge set
        G = nx.Graph()
        G.add_nodes_from(vertices)
        G.add_edges_from(edges)
        nx.draw(G,with_labels=True)
        plt.title('G = (V,E)')
        plt.show
        
        #For computation of independence number
        
        for i in Ind:
            if i == 0:
                Ind.remove(i)
        
                
        return '\n Independence number \u03B1(G) is '+str(len(Ind)-1)
       
    def dom_poly(self):
    
        unsorted_edges = []
        vertices = []
        edges = []
        
        # For creating a list of vertices and ordered pair of edges
        for node,neighbors in self.graph.items():
            for i in range(0,len(neighbors)):
                if (node,neighbors[i]) not in unsorted_edges and (neighbors[i],node) not in unsorted_edges:
                    unsorted_edges.append((node,neighbors[i]))       
            vertices.append(node) 
            
        #  Updating edge set with sorted unordered pair of edges  
        for unsorted_edge in unsorted_edges:
            L = list(unsorted_edge)
            L.sort()
            edges.append(tuple(L))
            
        # Sorting the vertex set   
        vertices.sort()
        
        if len(edges)==0:
            if len(vertices)==1:
                #For Null Graph
                if vertices == ['']:
                    print('\n Dominating sets for the graph G is/are - ','\u03A6','\n')
                    print('Zero is the Domination Polynomial for the graph G')
                    '''G = nx.Graph()
                    G.add_nodes_from(vertices)
                    G.add_edges_from(edges)
                    nx.draw(G,with_labels=True)
                    plt.title('G = (V,E)')
                    plt.show'''
                    return '\n Domination number \u03B3(G) is zero'
                else:
                    #For Empty Graph with one vertex
                    L = [0]*(len(vertices))
                    L.append(1)
                    L.reverse()
                    print('\n Dominating sets for the graph G is/are - ',set(vertices),'\n')
                    print(np.poly1d(L),' is the Domination Polynomial for the graph G')
                    return '\n Domination number \u03B3(G) is '+str(len(vertices))
            #For Empty Graphs with more than one vertex
            else:
                L = [0]*(len(vertices))
                L.append(1)
                L.reverse()
                print('\n Dominating sets for the graph G is/are - ',set(vertices),'\n')
                print(np.poly1d(L),' is the Domination Polynomial for the graph G')
                return '\n Domination number \u03B3(G) is '+str(len(vertices)) 
            
            
        
        else:
            # Creating a powerset of vertex set in form of nested list tuples
            power_set_list = [] 
            for card_set in range(0,len(vertices)+1): 
                power_set_list.append(list(combinations(vertices,card_set)))
            
            # For fetching the tuples and storing in a list from the above nested list power_set_list
            power_set = []
            for Set_list in power_set_list:
                for Set in Set_list:
                    power_set.append(Set)
                
            
            neig_hood = Polynomials.neighborhood(vertices, edges) 
            
            N = []        
            for Set in power_set:
                L = []
                for vertex in Set:
                    L.append(neig_hood[vertex])
                N.append(L)
                
            R = []    
            for i in N:
                x = []
                for j in i:
                    x+=j
                R.append(list(Counter(x)))
            
            S = []        
            for i in range(0,len(power_set)):
                for j in range(0,len(R)):
                    if i==j:
                        S.append([power_set[i],R[j]])
            
            # For computing dominating sets
            T = []
            E = []
            for i in S:
                if len(i[1])==len(vertices):
                    T.append(len(i[0]))
                    E.append(i[0])
                    
            print('\n Dominating sets for the graph G is/are - ',E,'\n')
                    
            Counter(T).most_common()
            
            min_deg = sorted(Counter(T).items())[0][0]
            
            #For creating domination polynomial
            A = []
            for i in sorted(Counter(T).items()):
                A.append(i[1])
            
            A.reverse()
            C = [0]*(min_deg)
            C.append(1)
            C.reverse()
            B = np.poly1d(C)
            Z = np.poly1d(A)
            
            print(np.polymul(B,Z),' is the Domination Polynomial for the graph G')
            
            return '\n Domination number \u03B3(G) is '+str(min_deg)
        
        
#We pass input as dictionary in form of a string. Eg : {"a":["b"],"b":["c","a"],"c":["a"]}
if __name__=='__main__':
    dict_graph = input('Enter the neighborhood of all the graph vertices \n \n ')
    try:
        obj = Polynomials(json.loads(dict_graph))
        print(obj.dom_poly())
        print(obj.ind_poly())
    except:
        print("Wrong input")
