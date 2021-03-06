#
# This class implements union-find operations on disjoint sets.
# The constructor creates individual sets for the values 0..count-1.
#
# The other methods work the way you expect.
class UFset:

    def __init__(self, count):
        self.lst = []
        for i in range(0, count):
            self.lst.append(i)

    def findset(self, element):
        name = element
        while self.lst[name] != name:
            name = self.lst[name]

        return name

    def union(self, element1, element2):
        root1 = self.findset(element1)
        root2 = self.findset(element2)
        self.lst[root2] = root1

#
# This class implements an edge object, where an edge has two endpoint
# vertices, v and w (both integers), and a weight.
#
class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __repr__(self):
        return "Edge("+repr(self.v)+","+repr(self.w)+","+repr(self.weight)+")"

    def __str__(self):
        return "("+repr(self.v)+","+repr(self.w)+","+repr(self.weight)+")"

# Your task is to implement this method by adapting the
# pseudocode for Kruskal's algorithm found in the textbook.
# Note that, unlike the pseudocode, your method must return
# the list of edges in the MST.
def kruskal_mst(edge_list, n):
    # *** Your code goes here. *** #
    tree = []
    edge_list.sort(key = lambda i : i.weight)
    Uf_set = UFset(n)
    count = 0
    i = 0
    while(count < n-1):
        if (Uf_set.findset(edge_list[i].v) != Uf_set.findset(edge_list[i].w)):
            edges_hold_t = Edge(edge_list[i].v, edge_list[i].w, edge_list[i].weight)
            tree.append(edges_hold_t)
            count = count + 1
            Uf_set.union(edge_list[i].v, edge_list[i].w)
        i=i+1
    return tree

#
# The main program builds two graphs and computes a minimal-weight
# spanning tree for each.  Your task is to fill in the code for the
# kruskal_mst method above.
#
print("-- Graph 1 --")
edge_list = [Edge(0, 4, 1), Edge(0, 1, 3), Edge(1, 4, 4), Edge(4, 2, 6), Edge(4, 3, 7), Edge(2, 3, 2), Edge(1, 2, 5)]
print("Edge list")
print(edge_list)
tree_edge_list = kruskal_mst(edge_list, 5)
tree_weight = 0
print("Tree edge list")
print(tree_edge_list)
for edge in tree_edge_list:
    tree_weight += edge.weight
print("Tree weight:", tree_weight) # This should print a weight of 11.
print()

print("-- Graph 2 --")
edge_list = [Edge(0, 1, 4), Edge(0, 7, 8), Edge(1, 2, 8), Edge(1, 7, 11), Edge(2, 3, 7), Edge(2, 5, 4), Edge(3, 4, 9), Edge(3, 5, 14), Edge(5, 4, 10), Edge(6, 5, 2), Edge(7, 6, 1), Edge(7, 8, 7), Edge(8, 2, 2), Edge(8, 6, 6)] 
print("Edge list")
print(edge_list)
tree_edge_list = kruskal_mst(edge_list, 9)
tree_weight = 0
print("Tree edge list")
print(tree_edge_list)
for edge in tree_edge_list:
    tree_weight += edge.weight
print("Tree weight:", tree_weight) # This should print a weight of 37.

