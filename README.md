# Graph isomorphism colourings problem

Group of 4 people , uni project 

## The Problem statement 
The graph isomorphism problem is the computational problem of determining whether two finite graphs are isomorphic.
It was solved using python. Even when two graphs are isomorphic( mapping of nodes and edges are preserved between 2 structures), it may not be immediately obvious. As the number of nodes increases it is important to keep effivciency in mind and develop a relatively time efficient solution. 

## Solution  
Here this problem was solved using python by colouring each edge and seeing if it matches. In such a way that no two touching edges have the same colour and in a way that the fewest number of colours as possible are availed of. 

## Desired Output
So if A is isomorphic to B. func(A≅B) -> true. 
So if A is NOT isomorphic to B. func(A≅B) -> false. 
![image](https://user-images.githubusercontent.com/44605305/231787426-202db02b-b305-4a27-8ece-0389b97f3474.png)


##  Algorithm Testing 

The algorithm was tested on numerous sample graphs for first of all getting the desired output and second, to be relatively efficienct on large graph sets. Feel free to test on sampe sets and further optimise!
