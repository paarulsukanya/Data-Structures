def linear_search(nums,item):
  """
  Function to find index of item in nums linearly.
  """
  for i in nums:
    if i == item:
      return nums.index(i)
  #item not found
  return -1
  
print("Enter elements in list")
nums = list(map(int,input().split(" ")))
print("Enter item to be found")
item = int(input())
print("Index of item in list: ", linear_search(nums,item))
