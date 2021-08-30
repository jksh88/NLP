def sumZero_refactor(arr, p1 = 0):
  p2 = len(arr) -1
  while p1 < p2:
    if arr[p1] + arr[p2] == 0:
      return [arr[p1], arr[p2]]
    elif arr[p1] + arr[p2] < 0:
      p1 += 1
    else:
      p2 -= 1
  
  # return sumZero_refactor(arr, p1, p2)







print(sumZero_refactor([-3, -2, -1, 0, 1, 2, 3]))
print(sumZero_refactor([-2, 0, 1, 3]))
print(sumZero_refactor([1, 2, 3]))
print(sumZero_refactor([-8, -7, -5, -2, 0, 1, 2, 3, 4, 5, 6]))