import graph
import graph_io
import os
import math


def Compare(array1, array2):
    clone = array2[:]
    while len(clone) > 0:
        for i in range (len(array1)):
            element = array1[i]
            if element in clone:
                clone.remove(element);
            else:
                return False;
    return True;

#currentvertex = vertex you want to check if it already exists
#similar = array of vertices with the same colordegree
def checkExists(currentVertex,similar):
    clone = similar[:]
    clone.remove(currentvertex)
    currentcolors = []

    #get array of colors of vertex you want to check if exists
    for l in range(len(currentVertex.neighbours)):
        currentcolors.append(currentVertex.neighbours[l].colornum)

    #get array of colors of an array of vertexes with same color degree
    for m in range(len(clone)):
        toCompare = clone[m]
        compareNeighbours = toCompare.neighbours
        comparecolors = [];
        for n in range(len(compareNeighbours)):
            comparecolors.append(compareNeighbours[n].colornum)
        checker = Compare(currentcolors, comparecolors)
        if checker == True:
            return m;
    return -1;


#open the graph, choose L[0][0] or L[0][1] depending on which graph you want to choose
with open("colorref_smallexample_2_49.grl") as f:
    L=graph_io.load_graph(f,read_list=True)
    graph_1 = L[0][0]
    graph_2 = L[0][1]

#give colors based on degree
for v in graph_1.vertices:
    v.colornum=v.degree;

for v in graph_2.vertices:
    v.colornum=v.degree;


#if len(graph_1.vertices == len(graph_2.vertices)):





maxcolor = 0;
#make maxcolor
for v in graph_1.vertices:
    if v.colornum > maxcolor:
        maxcolor = v.colornum;

#loop for max color
for i in range(maxcolor):
    #start at i=1
    color = i+1;
    similar = [];
    colors = [];

    #loop all vertices
    for v in graph_1.vertices:
        #check if vertex = current color
        if v.colornum == color:
            #if yes, add to similar array
            similar.append(v)


    #make arrays of neighbours of the 1st similar element
    neighbours = similar[0].neighbours;
    #get the colors of the neighbours of the 1st element
    for j in range(len(neighbours)):
        colors.append(neighbours[j].colornum)

    previous = [];
    #compare array:colors to similar[k].neighbours.colors
    for k in range(1,len(similar)):
        #make the variables based on the current vertex you want to compare to
        currentvertex = similar[k];
        previous.append(similar[k])
        currentNeighbours = currentvertex.neighbours;
        currentcolors = [];
        #get all colornums for the neighbours of current vertex
        for l in range(len(currentNeighbours)):
           currentcolors.append(currentNeighbours[l].colornum)
        print("current:",currentcolors)
        print("compare with:",colors)
        #comparison between colors and currentcolors
        if Compare(currentcolors,colors) == True:
            print("okay!")
        #give non similar values a new color
        else:
            existing = checkExists(currentvertex,previous)
            print(existing)
            if (existing == True):
                print("hello")







    #for j in range(len(similar)):
    #    for similar[j].neighbours



#write to dot file
with open("colorful2.dot", "w") as f:
    graph_io.write_dot(graph_1, f)


