def capitalizeWords (arr, result = [], i = 0):
  if i < len(arr):
    result.append(arr[i].upper())
    i += 1
    capitalizeWords(arr, result, i)
  return result

words = ["this", "is", "my", "life"]

print(capitalizeWords(words))