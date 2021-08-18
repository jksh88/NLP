def capFirst(arr, result = [], i = 0):
  if i < len(arr):
    result.append(arr[i][0].upper() + arr[i][1:])
    i += 1
    capFirst(arr, result, i)
  return result
  




print(capFirst(['car','taco','banana']))