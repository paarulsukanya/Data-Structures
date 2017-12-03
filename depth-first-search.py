def dfs(graph,start):
  """
  Returns all nodes of the graph visited using DFS.
  Iterative Approach.
  """
  #keeps track of nodes to be visited
  stack = []
  #keeps track of nodes already visited
  res = []
  stack.append(start)
  while stack:
    #remove last node from stack
    curr_node = stack.pop()
    #check if node is visited
    if curr_node not in res:
      res.append(curr_node)
      adj_nodes = graph[curr_node]
      #add adjacent nodes to stack
      for i in adj_nodes:
        stack.append(i)
  return res
         
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'F'],
         'E': ['A', 'B'],
         'F': ['C', 'D'],
         'G': ['C']}
print(dfs(graph,'A'))
