def collectStrings(obj, arr = []):
  for x in obj:
    if isinstance(obj[x], str):
      arr.append(obj[x])
    elif isinstance(obj[x], dict):
      collectStrings(obj[x], arr)
  return arr 


obj = {
    'stuff': "foo",
    'data': {
        'val': {
            'thing': {
                'info': "bar",
                'moreInfo': {
                    'evenMoreInfo': {
                        'weMadeIt': "baz"
                    }
                }
            }
        }
    }
}

print(collectStrings(obj))

# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# for item in a_dict.items():
#   print(item)


# print(a_dict.items())