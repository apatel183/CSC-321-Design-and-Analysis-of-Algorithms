###Arpan Patel##
##CSC 321##
from collections import defaultdict

class Stack:
     def __init__(self):
         self.container = []  
     def isEmpty(self):
         return self.size() == 0   

     def push(self, item):
         self.container.append(item)  

     def pop(self):
         return self.container.pop()  

     def size(self):
         return len(self.container)

def createGraph(graph):
    dictionary = defaultdict(list)
    for i in graph:
        dictionary[i[0]].append(i[1])
    return dictionary

def topological_sort(graph):
    visit = set()
    answer = Stack()
    #for d in graph:
    for i in list(graph):
        if i not in visit:
            dfs(graph, answer, visit, i)
    return answer

def dfs(graph, stack, visited, v):
    visited.add(v)
    for w in graph[v]:
        if w not in visited:
            dfs(graph, stack, visited, w)
    stack.push(v)
     
graphEdges =  [[38, 4], [50, 4], [38, 5], [50, 5], [3, 5], [3, 7], [4, 56], [5, 56], [50, 6], [6, 7], [6, 8], [7, 9], [7, 24], [8, 9], [8, 24], [9, 15], [24, 15]]

graph = createGraph(graphEdges)

stack = topological_sort(graph)

while(not stack.isEmpty()):
    print(stack.pop())
