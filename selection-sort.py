#Implementation of selection sort
def selection_sort(arr):
  """
  Returns array sorted using selection sort algorithm.
  """
  for i in range(len(arr)):
    min = i
    #find min element in array from i+1 index
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min]:
        min = j
    #swap min element with element at index i
    arr[min],arr[i] = arr[i], arr[min]
  return arr
  
print("Enter List")
arr = list(map(int,input().split(" ")))
print("Sorted List: ", selection_sort(arr))
