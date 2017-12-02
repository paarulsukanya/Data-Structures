def insertion_sort(l):
  """
  Function which returns an array sorted using insertion sort algorithm.
  Time Complexity: O(n^2)
  """
  for i in range(len(l)):
    j = i
    while (j > 0 and l[j-1] > l[j]):
      temp = l[j-1]
      l[j-1] = l[j]
      l[j] = temp
      j = j - 1
  return l
  
l = list(map(int,input().split(" ")))

print(insertion_sort(l))
