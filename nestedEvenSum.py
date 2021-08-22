def nestedEvenSum(obj, sum = 0):
  for x in obj:
    if isinstance(obj[x], (int, float)) == True and obj[x] % 2 == 0:
      sum += obj[x]
    if isinstance(obj[x], dict) == True:
      sum += nestedEvenSum(obj[x])
  return sum


obj1 = {
  'outer': 2,
  'obj': {
    'inner': 4,
    'otherObj': {
      'superInner': 4,
      'notANumber': True,
      'alsoNotANumber': 'yup',
    },
  },
};

obj2 = {
  'a': 2,
  'b': { 'b': 8, 'bb': { 'b': 3, 'bb': { 'b': 2 } } },
  'c': { 'c': { 'c': 2 }, 'cc': 'ball', 'ccc': 5 },
  'd': 1,
  'e': { 'e': { 'e': 2 }, 'ee': 'car' },
};

print(nestedEvenSum(obj1))
print(nestedEvenSum(obj2))