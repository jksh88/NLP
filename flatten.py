def flatten(lst, result = []):
  for x in lst:
    if type(x) == list:
      flatten(x, result)
    else:
      result.append(x)
  return result

# print(flatten([1, 2, 3, [4, 5] ]))
# print(flatten([1, [2, [3, 4], [[5]]]]))
# print(flatten([[1],[2],[3]]))
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))