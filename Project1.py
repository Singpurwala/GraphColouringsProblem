import graph
import graph_io
import os
import math

#open the graph, choose L[0][0] or L[0][1] depending on which graph you want to choose
with open("colorref_largeexample_6_960.grl") as f:
    L=graph_io.load_graph(f,read_list=True)
    start_graph_1 = L[0][0]
    start_graph_2 = L[0][1]

#write to dot file
with open("colorful2.dot", "w") as f:
    graph_io.write_dot(start_graph_1, f)








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
    clone.remove(currentVertex)
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



















def refine(graph_1):
    # give colors based on degree
    for v in graph_1.vertices:
        v.colornum = v.degree;
    maxcolor = 0;
    graphStart = graph_1;
    # make maxcolor
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

        if (len(similar)) > 0:
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
                #comparison between colors and currentcolors
                #if Compare(currentcolors,colors) == True:
                    #print(currentvertex.colornum)
                #give non similar values a new color
                else:
                    existing = checkExists(currentvertex,previous)
                    if (existing == -1):
                        maxcolor +=1;
                        currentvertex.colornum = maxcolor
                        #print(currentvertex.colornum)
                    else:
                        currentvertex.colornum = similar[existing+1].colornum
                        #print(similar[existing+1].colornum)

    return graph_1





refined = refine(start_graph_1)
superRefined = refine(refined)
print("start")
print(refined)
print(superRefined)
print("end")
