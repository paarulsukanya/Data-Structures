def bfs(graph,start):
  """
  Returns all nodes of the graph visited using BFS
  """
  #keeps track of nodes to be visited
  queue = []
  #keeps track of nodes already visited
  explored = []
  queue.append(start)
  while queue:
    #remove first node from queue
    curr_node = queue.pop(0)
    #check if node is visited
    if curr_node not in explored:
      explored.append(curr_node)
      adjacent_nodes = graph[curr_node]
      #add adjacent nodes to queue
      for i in adjacent_nodes:
        queue.append(i)
  return explored
  
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'F'],
         'E': ['A', 'B','D'],
         'F': ['C', 'D'],
         'G': ['C']}
         
print(bfs(graph,'A'))
