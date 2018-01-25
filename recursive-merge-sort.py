def merge(left,right):
  res = []
  i,j = 0, 0
  while len(res) < (len(left) + len(right)):
    if left[i] <= right[j]:
      res.append(left[i])
      i += 1
    else:
      res.append(right[j])
      j += 1
    if i == len(left) or j == len(right):
      res.extend(left[i:] or right[j:])
      break
 
  return res

def merge_sort(arr):
  if len(arr) > 1:
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left,right)
  else:
    return arr

print("Enter array to be sorted")
l = list(map(int,input().split(" ")))
print("Sorted array")
print(merge_sort(l))
