#iterative implementation of binary search
def binary_search(arr,item):
  """
  Returns the index of item in arr
  """
  start = 0
  end = len(arr) - 1
  while(start <= end):
    mid = (start + end) // 2
    if item == arr[mid]:
      return mid
    elif item <= arr[mid]:
      end = mid - 1
    else:
      start = mid + 1
  #if item is not found return -1
  return -1
  
print("Enter Array")
arr = list(map(int,input().split(" ")))
#binary_search works only on sorted lists
arr.sort()

print("Enter item whose index is to be found")
item = int(input())
print("Index of item: ",binary_search(arr,item))
