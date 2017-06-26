##Arpan Patel#
#csc 321###

def dfs(adj,start,vertices_order=[]):
    #print(vertices_order)
    vertices_order += [start]
    #print(vertices_order)
    for i in adj[start]:
        #print(i)
        if i in vertices_order:
            return vertices_order
        if i not in vertices_order:
            #print(vertices_order)
            vertices_order = dfs(adj,i,vertices_order)
            #print("Vertices Order: ",vertices_order)
    return vertices_order

#[0, 1, 5, 6, 4, 2, 3]       
adjaceny_list ={0: [1,2,3],
         1: [5,6],
         2: [4],
         3: [2, 4],
         4: [1],
         5: [],
         6: [4]}
print ("Adjacency list shows the order of the visited vertices:" ,dfs(adjaceny_list,0))




